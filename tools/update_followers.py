"""Fetch live data from the Facebook page and save it for the site.
Runs every 6 hours from GitHub Actions (.github/workflows/update-facebook-followers.yml).

Writes:
  assets/data/stats.json    – follower count
  assets/data/reviews.json  – customer reviews / recommendations

Needs two repository secrets:
  FB_PAGE_ID     – the page id or username (skylineupvcwindow)
  FB_PAGE_TOKEN  – a Page access token (never expires if made from a long-lived user token).
                   For reviews the token needs the pages_read_user_content permission.

If Facebook fails or a permission is missing, the old files are kept as they are.
"""
import json, os, sys, urllib.request, urllib.parse, urllib.error, datetime, pathlib

API = "https://graph.facebook.com/v21.0/"
DATA = pathlib.Path(__file__).resolve().parent.parent / "assets" / "data"
page = os.environ.get("FB_PAGE_ID", "").strip()
token = os.environ.get("FB_PAGE_TOKEN", "").strip()


def get(path, params):
    url = API + path + "?" + urllib.parse.urlencode(dict(params, access_token=token))
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try:
            msg = json.load(e).get("error", {}).get("message", "")
        except Exception:
            msg = ""
        raise RuntimeError(f"HTTP {e.code} {msg}")


def save(name, obj):
    path = DATA / name
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    new = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    strip = lambda s: {k: v for k, v in json.loads(s).items() if k != "updated"} if s else None
    if old and strip(old) == strip(new):
        print(f"{name}: no change")
        return
    path.write_text(new, encoding="utf-8")
    print(f"{name}: updated")


def followers():
    data = get(urllib.parse.quote(page), {"fields": "followers_count,fan_count"})
    count = data.get("followers_count") or data.get("fan_count")
    if not isinstance(count, int) or count <= 0:
        raise RuntimeError(f"no follower count in response: {data}")
    save("stats.json", {"facebook_followers": count, "updated": datetime.date.today().isoformat(),
                        "source": "facebook-graph-api"})


def reviews():
    fields = "created_time,recommendation_type,review_text,rating,reviewer{name}"
    try:
        res = get(urllib.parse.quote(page) + "/ratings", {"fields": fields, "limit": 100})
    except RuntimeError:  # reviewer names need extra access on some pages – retry without them
        res = get(urllib.parse.quote(page) + "/ratings", {"fields": fields.replace(",reviewer{name}", ""), "limit": 100})
    items = []
    while True:
        for r in res.get("data", []):
            text = (r.get("review_text") or "").strip()
            if not text:
                continue
            rec = r.get("recommendation_type")
            items.append({
                "name": ((r.get("reviewer") or {}).get("name") or "").strip(),
                "text": text,
                "date": (r.get("created_time") or "")[:10],
                "recommends": rec != "negative",
                "rating": r.get("rating"),
            })
        nxt = res.get("paging", {}).get("next")
        if not nxt or len(items) >= 500:
            break
        with urllib.request.urlopen(nxt, timeout=30) as r:
            res = json.load(r)
    # merge: keep the reviews already on the site (they carry profile links), add only new ones on top
    path = DATA / "reviews.json"
    cur = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    have = cur.get("items", [])
    norm = lambda s: "".join(str(s).split())[:40]
    known = {norm(x.get("text", "")): x for x in have}
    fresh = []
    for it in items:
        old = known.get(norm(it["text"]))
        if old:
            if not old.get("date") and it["date"]:
                old["date"] = it["date"]
            if not old.get("name") and it["name"]:
                old["name"] = it["name"]
        else:
            fresh.append(it)
    fresh.sort(key=lambda x: x["date"], reverse=True)
    out = dict(cur, updated=datetime.date.today().isoformat(), items=fresh + have)
    out["total_on_facebook"] = max(len(out["items"]), cur.get("total_on_facebook", 0))
    save("reviews.json", out)


if not page or not token:
    print("FB_PAGE_ID / FB_PAGE_TOKEN secrets are not set - skipping (site keeps the last saved data).")
    sys.exit(0)

for job in (followers, reviews):
    try:
        job()
    except Exception as e:  # one failing part never blocks the other
        print(f"{job.__name__}: Facebook API error - kept old data:", e)
