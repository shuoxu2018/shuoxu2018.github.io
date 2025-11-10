# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os

# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)




from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

# Read Google Scholar ID from environment variable
GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
if not GOOGLE_SCHOLAR_ID:
    raise ValueError("Environment variable GOOGLE_SCHOLAR_ID is not set")

# Try to use free proxies to reduce CAPTCHA/blocks on CI.
# Newer 'free-proxy' versions can be incompatible with scholarly==1.5.1,
# so we guard this call and continue without proxy if it fails.
pg = ProxyGenerator()
try:
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
except TypeError as e:
    print(f"[WARN] FreeProxies() failed due to library mismatch: {e}")
    print("[INFO] Continuing without proxy (may hit CAPTCHA).")

# Fetch author information with retries (exponential backoff)
author = None
for attempt in range(5):
    try:
        # Get the author object by Scholar ID
        author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
        # Fill core sections first; publications are handled separately below
        scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        break
    except Exception as e:
        print(f"[scholarly] attempt {attempt+1}/5 failed: {e}")
        time.sleep(3 * (2 ** attempt))

if author is None:
    raise RuntimeError(
        "Failed to fetch author information after multiple attempts. "
        "Verify your Scholar ID or enable a more stable proxy (e.g., Tor)."
    )

# Try to fill publications; skip gracefully if it fails to avoid breaking the run
pub_map = {}
try:
    scholarly.fill(author, sections=['publications'])
    # Convert publications list into a dict keyed by 'author_pub_id'
    pub_map = {v['author_pub_id']: v for v in author.get('publications', [])}
except Exception as e:
    print(f"[scholarly] publications fill skipped due to: {e}")

# Augment and persist results (same structure as your original logic)
name = author.get('name')
author['updated'] = str(datetime.now())
author['publications'] = pub_map  # empty dict if publications failed

print(json.dumps(author, indent=2))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

# Create the Shields.io citation badge data
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)



# from scholarly import scholarly, ProxyGenerator
# import jsonpickle
# import json
# from datetime import datetime
# import os
# import time

# # Read Google Scholar ID from environment variable
# GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
# if not GOOGLE_SCHOLAR_ID:
#     raise ValueError("Environment variable GOOGLE_SCHOLAR_ID is not set")

# # Try to use free proxies to avoid Google Scholar blocking (skip silently if it fails)
# pg = ProxyGenerator()
# if pg.FreeProxies():
#     scholarly.use_proxy(pg)

# # --- Fetch author information (minimal change: added retry loop) ---
# author = None
# for attempt in range(5):
#     try:
#         # Fetch author data by ID
#         author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
#         # Fill basic info and indices first; publications handled separately below
#         scholarly.fill(author, sections=['basics', 'indices', 'counts'])
#         break
#     except Exception as e:
#         print(f"[scholarly] attempt {attempt+1}/5 failed: {e}")
#         time.sleep(3 * (2 ** attempt))

# if author is None:
#     raise RuntimeError(
#         "Failed to fetch author information after multiple attempts. "
#         "Please verify your Scholar ID or enable a more stable proxy (e.g., Tor)."
#     )

# # --- Try filling publications; skip gracefully if it fails ---
# pub_map = {}
# try:
#     scholarly.fill(author, sections=['publications'])
#     # Convert publication list to a dictionary keyed by author_pub_id
#     pub_map = {v['author_pub_id']: v for v in author.get('publications', [])}
# except Exception as e:
#     print(f"[scholarly] publications fill skipped due to: {e}")

# # --- Save results (identical to your original logic) ---
# name = author.get('name')
# author['updated'] = str(datetime.now())
# author['publications'] = pub_map  # Use empty dict if publications failed

# print(json.dumps(author, indent=2))

# os.makedirs('results', exist_ok=True)
# with open('results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# # Create the Shields.io citation badge data
# shieldio_data = {
#     "schemaVersion": 1,
#     "label": "citations",
#     "message": f"{author.get('citedby', 0)}",
# }
# with open('results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)
