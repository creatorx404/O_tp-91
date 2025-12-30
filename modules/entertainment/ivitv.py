# Module: ivitv
# URL: https://api.ivi.ru/mobileapi/user/register/phone/v6/
# Method: POST

from O_tps.core import *
from O_tps.localuseragent import *


async def ivitv(phone, client, out):
    name = "ivitv"
    domain = "ivitv"
    frequent_rate_limit = False

    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }

    data = {
        'phone': f'92{phone[-10:]}',
        'device': 'Windows+v.43+Chrome+v.7453451',
        'app_version': '870',
    }

    try:
        response = await client.post(
            'https://api.ivi.ru/mobileapi/user/register/phone/v6/',
            headers=headers,
            data=data,
        )

        # Success identifier: 'true'
        if 'true' in response.text.lower():
            out.append({
                "name": name,
                "domain": domain,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "sent": True,
                "error": False
            })
            return None

        elif response.status_code == 429 or 'rate' in response.text.lower() or 'limit' in response.text.lower() or 'wait' in response.text.lower():
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