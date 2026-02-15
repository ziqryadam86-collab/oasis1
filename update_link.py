import requests
import re
import os

def get_latest_m3u8():
    page_url = "https://www.kds.tw/tv/malaysia-tv-channels-online/oasis/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.kds.tw/"
    }
    
    try:
        response = requests.get(page_url, headers=headers, timeout=15)
        # Mencari link m3u8 menggunakan Regex
        match = re.search(r'url["\']\s*:\s*["\'](http.*?\.m3u8.*?)["\']', response.text)
        if match:
            link = match.group(1).replace('\\/', '/')
            return link
    except Exception as e:
        print(f"Ralat: {e}")
    return None

new_link = get_latest_m3u8()

if new_link:
    # Format kandungan fail M3U
    m3u_content = f"""#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=1920x1080
{new_link}"""
    
    # Simpan ke fail playlist.m3u
    with open("playlist.m3u", "w") as f:
        f.write(m3u_content)
    print("Playlist dikemaskini!")
else:
    print("Gagal mendapatkan link baru.")
  
