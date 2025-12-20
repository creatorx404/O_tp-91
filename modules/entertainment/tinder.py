from O_tps.core import *
from O_tps.localuseragent import *

async def tinder(phone, client, out):
    name = "tinder"
    domain = "api.gotinder.com"
    frequent_rate_limit = False

    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
        'Origin': 'https://tinder.com',
        'Referer': 'https://tinder.com'
    }

    data = {
        'phone_number': phone,  # Use the complete number passed from the core.py
    }

    try:
        response = await client.post(
            'https://api.gotinder.com/v2/auth/sms/send',
            headers=headers,
            json=data
        )

        try:
            response_data = response.json()
            if response_data.get("status") == "success":
                out.append({"name": name, "domain": domain, "rateLimit": False, "sent": True, "error": False})
            else:
                out.append({"name": name, "domain": domain, "rateLimit": False, "sent": False, "error": False})
        except Exception as e:
            print(f"Error parsing response: {e}")
            out.append({"name": name, "domain": domain, "rateLimit": False, "sent": False, "error": True})

    except Exception as e:
        print(f"Error in module {name}: {e}")
        out.append({"name": name, "domain": domain, "rateLimit": False, "sent": False, "error": True})
