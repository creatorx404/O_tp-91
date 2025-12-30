from O_tps.core import *
from O_tps.localuseragent import *
import httpx 
import re
import uuid
import random
import trio 

async def mobikwik(phone, client, out):
    name = "mobikwik"
    domain = "mobikwik.com"
    
    res = {
        "name": name, "domain": domain, "frequent_rate_limit": False,
        "rateLimit": False, "sent": False, "error": False
    }

    try:
        clean_phone = re.sub(r'\D', '', str(phone))[-10:]

        # 1. Identity Selection
        # Logic check: ensures ua is treated as a dict of strings
        random_id = random.choice(list(ua.keys()))
        selected_ua = str(ua[random_id])
        
        # If your 'ua' dict only contains words like 'chrome', use a fallback string
        if len(selected_ua) < 10:
            selected_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

        # 2. Use a standard AsyncClient (Trio compatible)
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as s:
            
            # STEP 1: INITIAL HANDSHAKE
            init_headers = {
                "User-Agent": selected_ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
            await s.get("https://www.mobikwik.com/login", headers=init_headers)
            
            await trio.sleep(random.uniform(1.0, 2.0))

            # STEP 2: TRIGGER OTP
            api_headers = {
                "User-Agent": selected_ua,
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Origin": "https://www.mobikwik.com",
                "Referer": "https://www.mobikwik.com/login",
                "X-MClient": "0",
                "X-Request-Id": str(uuid.uuid4())
            }

            url = 'https://webapi.mobikwik.com/p/user/login/generate/otp'
            payload = {
                "cell": clean_phone,
                "deviceId": str(uuid.uuid4()),
                "isIos": False,
                "version": "1"
            }

            response = await s.post(url, json=payload, headers=api_headers)

            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "SUCCESS" or data.get("statuscode") == "0":
                    res["sent"] = True
                else:
                    res["error"] = True
            else:
                res["error"] = True

    except Exception as e:
        # THIS WILL PRINT THE ACTUAL ERROR IN YOUR TERMINAL
        print(f"\n[DEBUG ERROR]: {e}\n") 
        res["error"] = True
    finally:
        out.append(res)
