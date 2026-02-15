import requests
import re

def get_link():
    url = "https://www.kds.tw/tv/malaysia-tv-channels-online/oasis/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.kds.tw/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # Cari link m3u8 guna regex
        match = re.search(r'url["\']\s*:\s*["\'](http.*?\.m3u8.*?)["\']', response.text)
        if match:
            return match.group(1).replace('\\/', '/')
    except:
        return None
    return None

link = get_link()

if link:
    # Buat format playlist M3U
    m3u_text = f"#EXTM3U\n#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=1920x1080\n{link}"
    with open("index.m3u8", "w") as f:
        f.write(m3u_text)
    print("Berjaya update link!")
else:
    print("Gagal dapatkan link.")
    
