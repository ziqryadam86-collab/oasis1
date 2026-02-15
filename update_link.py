import requests
import re

def get_latest_link():
    # URL asal untuk dapatkan link
    url = "https://www.kds.tw/tv/malaysia-tv-channels-online/oasis/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.kds.tw/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # Cari link .m3u8 dalam kod HTML
        match = re.search(r'url["\']\s*:\s*["\'](http.*?\.m3u8.*?)["\']', response.text)
        if match:
            # Bersihkan link daripada karakter escape (seperti \/)
            full_link = match.group(1).replace('\\/', '/')
            return full_link
    except Exception as e:
        print(f"Ralat semasa mencari link: {e}")
    return None

# Jalankan fungsi
m3u8_link = get_latest_link()

if m3u8_link:
    # Kita simpan dalam format M3U supaya player video lebih senang baca
    # Tapi nama fail tetap index.m3u8 seperti yang awak nak
    content = f"#EXTM3U\n#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=1920x1080\n{m3u8_link}"
    
    with open("index.m3u8", "w") as f:
        f.write(content)
    print("Berjaya! Fail index.m3u8 telah dikemaskini.")
else:
    print("Gagal mencari link m3u8.")
    
