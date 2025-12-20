
from O_tps.localuseragent import *
from O_tps.core import *
import aiohttp
import json

async def textile(phone, client, out):
    name = "textile"
    domain = "textileinfomedia.com"
    frequent_rate_limit = False

    url = 'https://www.textileinfomedia.com/include-modal/ajax-send-login-with-otp.php'
    
    # Using aiohttp.FormData for multipart/form-data
    data = aiohttp.FormData()
    data.add_field('tk_s', '1def68c22bf82a9ff5b7d70fbb2c8c02e4b61cac') 
    data.add_field('buyer_cmobile', phone[-10:])
    data.add_field('usercntrycode', '91')
    data.add_field('user_selected_country', '1')

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.textileinfomedia.com/login-otp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    }

    try:
        async with client.post(url, headers=headers, data=data, timeout=10) as response:
            text = await response.text()
            
            res = {
                "name": name,
                "domain": domain,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "sent": False,
                "error": False
            }

            if response.status == 200:
                try:
                    resp_data = json.loads(text)
                    # Response: {"lg_valid":"TRUE","u_type":0}
                    if resp_data.get("lg_valid") == "TRUE":
                        res["sent"] = True
                    else:
                        res["error"] = True
                except:
                    res["error"] = True
            else:
                res["error"] = True

            out.append(res)

    except Exception:
        out.append({
            "name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False, "sent": False, "error": True
        })
