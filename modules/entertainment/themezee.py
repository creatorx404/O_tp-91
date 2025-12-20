# Module: themezee
# URL: https://themezee.com/wp-admin/admin-ajax.php?action=mc4wp-form
# Method: POST

from O_tps.core import *
from O_tps.localuseragent import *


async def themezee(phone, client, out):
    name = "themezee"
    domain = "themezee"
    frequent_rate_limit = False

    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }

    data = {
        'EMAIL': phone,
        'AGREE': '1',
        '_mc4wp_honeypot': '',
        '_mc4wp_timestamp': '1614865641',
        '_mc4wp_form_id': '184963',
        '_mc4wp_form_element_id': 'mc4wp-form-1',
    }

    try:
        response = await client.post(
            'https://themezee.com/wp-admin/admin-ajax.php?action=mc4wp-form',
            headers=headers,
            data=data,
        )

        # Success identifier: 'mc4wp-success'
        if 'mc4wp-success' in response.text.lower():
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