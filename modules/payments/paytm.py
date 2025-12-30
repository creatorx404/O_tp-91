from O_tps.core import *
from O_tps.localuseragent import *


async def paytm(phone, client, out):
    name = "paytm"
    domain = "commonfront.paytm.com"
    frequent_rate_limit = False

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
    }

    data = {
        'phone': phone,
        'guid': "2952fa812660c58dc160ca6c9894221d",
    }

    response = await client.post(
        'https://commonfront.paytm.com/v4/api/sendsms',
        headers=headers,
        data=data,
    )

    try:
        response_data = response.json()
        if "202" in str(response_data).lower() or response_data.get("success") == True or response_data.get("msg") == "success":
            out.append({
                "name": name,
                "domain": domain,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "sent": True,
                "error": False
            })
            return None

        elif "rate" in str(response_data).lower() or "limit" in str(response_data).lower() or "wait" in str(response_data).lower():
            out.append({
                "name": name,
                "domain": domain,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": True,
                "sent": False,
                "error": False
            })
            return None

        else:
            out.append({
                "name": name,
                "domain": domain,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "sent": False,
                "error": False
            })
            print(f"Error: Unexpected response from {name}: {response_data}")
            return None

    except Exception:
        out.append({
            "name": name,
            "domain": domain,
            "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False,
            "sent": False,
            "error": True
        })
        return None
