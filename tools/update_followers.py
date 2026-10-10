"""Fetch the real Facebook follower count and write assets/data/stats.json.
Runs daily from GitHub Actions. Needs two repository secrets:
  FB_PAGE_ID     – the page id or username (skylineupvcwindow)
  FB_PAGE_TOKEN  – a Page access token (never expires if made from a long-lived user token)
"""
import json, os, sys, urllib.request, urllib.parse, datetime, pathlib

page = os.environ.get("FB_PAGE_ID", "").strip()
token = os.environ.get("FB_PAGE_TOKEN", "").strip()
out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "data" / "stats.json"

if not page or not token:
    print("FB_PAGE_ID / FB_PAGE_TOKEN secrets are not set - skipping (site keeps the last saved number).")
    sys.exit(0)

url = f"https://graph.facebook.com/v21.0/{urllib.parse.quote(page)}?" + urllib.parse.urlencode(
    {"fields": "followers_count,fan_count", "access_token": token})
try:
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.load(r)
except Exception as e:  # keep the old number if Facebook fails
    print("Facebook API error:", e)
    sys.exit(0)

count = data.get("followers_count") or data.get("fan_count")
if not isinstance(count, int) or count <= 0:
    print("No follower count in response:", data)
    sys.exit(0)

old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
if old.get("facebook_followers") == count:
    print("No change:", count)
    sys.exit(0)

out.write_text(json.dumps({"facebook_followers": count,
                           "updated": datetime.date.today().isoformat(),
                           "source": "facebook-graph-api"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Updated followers:", count)
