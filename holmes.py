import requests

print("""

    ##     ##  #######  ##       ##     ## ########  ######  
    ##     ## ##     ## ##       ###   ### ##       ##    ## 
    ##     ## ##     ## ##       #### #### ##       ##       
    ######### ##     ## ##       ## ### ## ######    ######  
    ##     ## ##     ## ##       ##     ## ##             ## 
    ##     ## ##     ## ##       ##     ## ##       ##    ## 
    ##     ##  #######  ######## ##     ## ########  ######

""")

username = input("[?] Enter username: ").strip()
print("[*] Enumerating usernames...")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

# Check github 

github_url = f"https://github.com/{username}" 
github_response = requests.get(github_url, headers=headers)

if github_response.status_code == 200: 
    print(f"[+] Github: {github_url}")

# Check reddit 

reddit_url = f"https://www.reddit.com/user/{username}"
reddit_response = requests.get(reddit_url, headers=headers)

if "Sorry, nobody on Reddit goes by that name." not in reddit_response.text: 
    print(f"[+] Reddit: {reddit_url}")

# Check youtube 

youtube_url = f"https://www.youtube.com/@{username}"
youtube_response = requests.get(youtube_url, headers=headers)

if youtube_response.status_code == 200: 
    print(f"[+] Youtube: {youtube_url}")

# Check instagram

instagram_url = f"https://www.instagram.com/{username}"
instagram_response = requests.get(instagram_url, headers=headers, allow_redirects=True)

if "PolarisErrorRoot" not in instagram_response.text:
    print(f"[+] Instagram: {instagram_url}")

# Check facebook

facebook_url = f"https://www.facebook.com/{username}"
facebook_response = requests.get(facebook_url, headers=headers)

if "This content isn't available at the moment" not in facebook_response.text:
    print(f"[+] Facebook: {facebook_url}")

# Check twitch

twitch_url = f"https://www.twitch.tv/{username}"
twitch_response = requests.get(twitch_url, headers=headers, allow_redirects=True)

if f"{username}" in twitch_response.text:
    print(f"[+] Twitch: {twitch_url}")

# Check pinterest

pinterest_url = f"https://www.pinterest.com/{username}"
pinterest_response = requests.get(pinterest_url, headers=headers)

if f'"username":"{username}"' in pinterest_response.text:
    print(f"[+] Pinterest: {pinterest_url}")

# Check pastebin

pastebin_url = f"https://pastebin.com/u/{username}"
pastebin_response = requests.get(pastebin_url, headers=headers)

if "#404" not in pastebin_response.text:
    print(f"[+] Pastebin: {pastebin_url}")

# Check medium

medium_url = f"https://medium.com/@{username}"
medium_response = requests.get(medium_url, headers=headers)

if "PAGE NOT FOUND" not in medium_response.text:
    print(f"[+] Medium {medium_url}")

# Check replit 

replit_url = f"https://replit.com/@{username}"
replit_response = requests.get(replit_url, headers=headers)

if f"@{username}" in replit_response.text: 
    print(f"[+] Replit: {replit_url}")


# Check gitlab

gitlab_url = f"https://gitlab.com/{username}"
gitlab_response = requests.get(gitlab_url, headers=headers)

if f"@{username}" in gitlab_response.text:
    print(f"[+] Gitlab: {gitlab_url}")

# Check tiktok 

tiktok_url = f"https://www.tiktok.com/@{username}"
tiktok_response = requests.get(tiktok_url, headers=headers)

if "userInfo" in tiktok_response.text:
   print(f"[+] Tiktok: {tiktok_url}")