from O_tps.core import *
from O_tps.localuseragent import *


async def porter(phone, client, out):
    name = "porter"
    domain = "porter.in"
    frequent_rate_limit = False

    data = {
        "phone": phone,
        "referrer_string": "",
        "brand": "porter"
    }

    try:
        response = await client.post(
            "https://porter.in/restservice/send_app_link_sms",
            json=data
        )

        if "true" in response.text:
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
            "error": True})
