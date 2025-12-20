from O_tps.core import *
from O_tps.localuseragent import *


async def dream11(phone, client, out):
    name = "dream11"
    domain = "dream11.com"
    frequent_rate_limit = False

    headers = {
        "User-Agent": random.choice(ua["browsers"]["chrome"]),
        "Referer": "https://www.dream11.com/",
        "Origin": "https://www.dream11.com",
        "Content-Type": "application/json"
    }

    data = {
        "siteId": "1",
        "mobileNum": phone,
        "appType": "androidfull"
    }

    try:
        response = await client.post(
            "https://api.dream11.com/sendsmslink",
            headers=headers,
            json=data
        )

        if response.status_code == 200 and "true" in response.text:
            out.append({
                "name": name,
                "domain": domain,
                "rateLimit": False,
                "sent": True,
                "error": False
            })
        else:
            out.append({
                "name": name,
                "domain": domain,
                "rateLimit": False,
                "sent": False,
                "error": False
            })
    except Exception as e:
        print(f"Error in module {name}: {e}")
        out.append({
            "name": name,
            "domain": domain,
            "rateLimit": False,
            "sent": False,
            "error": True
        })
