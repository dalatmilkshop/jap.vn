import requests
import os
from urllib.parse import urlparse, quote
from bs4 import BeautifulSoup

# Cấu hình
DOMAIN = "jap.vn"
START_YEAR = 2012
END_YEAR = 2015
SAVE_DIR = "docs/wayback"

CDX_API = f"http://web.archive.org/cdx/search/cdx?url={DOMAIN}/*&from={START_YEAR}&to={END_YEAR}&output=json&fl=timestamp,original&collapse=urlkey"
WAYBACK_URL = "http://web.archive.org/web/{timestamp}id_/{original}"

os.makedirs(SAVE_DIR, exist_ok=True)

def get_snapshots():
    resp = requests.get(CDX_API)
    data = resp.json()
    # Bỏ header
    return data[1:]

def fetch_and_save(snapshot):
    timestamp, original = snapshot
    url = WAYBACK_URL.format(timestamp=timestamp, original=quote(original, safe=':/?&='))
    print(f"Tải {url}")
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        # Loại bỏ khung Wayback
        for el in soup.select("#wm-ipp, script, style"): el.decompose()
        # Lưu file
        parsed = urlparse(original)
        fname = parsed.path.strip("/").replace("/", "_") or "index"
        fname = fname + ".html"
        with open(os.path.join(SAVE_DIR, fname), "w", encoding="utf-8") as f:
            f.write(f"<!-- Bản lưu trữ từ Wayback Machine: {url} -->\n")
            f.write(str(soup))
    except Exception as e:
        print(f"Lỗi với {url}: {e}")

def main():
    snapshots = get_snapshots()
    print(f"Tìm thấy {len(snapshots)} snapshot.")
    for snap in snapshots:
        fetch_and_save(snap)

if __name__ == "__main__":
    main()
