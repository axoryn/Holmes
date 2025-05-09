# 🕵️ Holmes

*A simple OSINT tool for enumerating usernames across multiple popular social media platforms.*

---

## Features

- Checks username existence across 10+ platforms (GitHub, Reddit, Instagram, etc.)
- Simple, clean Python code 
- Easy to modify and extend

---

## Installation 

Installing with `wget` 

```
wget https://raw.githubusercontent.com/axoryn/Holmes/refs/heads/main/holmes.py
```

## Requirements 

- Python 3.6+
- Requests library installed

## Dependencies 
```Requests``` can be installed by: 

- Directly with pip3: ```pip3 install requests```\
- For Arch: ```sudo pacman -S python-requests```\
- For Debian/Ubuntu: ```sudo apt install python```

## Usage

Just enter a username and your good to go! 
```
$ python3 holmes.py

    ##     ##  #######  ##       ##     ## ########  ######  
    ##     ## ##     ## ##       ###   ### ##       ##    ## 
    ##     ## ##     ## ##       #### #### ##       ##       
    ######### ##     ## ##       ## ### ## ######    ######  
    ##     ## ##     ## ##       ##     ## ##             ## 
    ##     ## ##     ## ##       ##     ## ##       ##    ## 
    ##     ##  #######  ######## ##     ## ########  ######

[?] Enter username: john_doe12
[*] Enumerating usernames...
[+] GitHub: https://github.com/john_doe12
[+] Reddit: https://www.reddit.com/user/john_doe12
[+] Instagram: https://www.instagram.com/john_doe12
...
```

## Ethical considerations

This tool is meant to be used for educational purposes only. The developer is not responsible for the misuse of this tool. 

