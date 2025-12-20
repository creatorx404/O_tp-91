from O_tps.core import *
from O_tps.localuseragent import *


async def kfc(phone, client, out):
    name = "kfc"
    domain = "kfc.co.in"
    frequent_rate_limit = False

    headers = {
        "User-Agent": random.choice(ua["browsers"]["chrome"]),
        "Referer": "https://online.kfc.co.in/login",
        "__RequestVerificationToken": "-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8",
        "Content-Type": "application/json"
    }

    data = {
        "AuthorizedFor": "3",
        "phoneNumber": phone,
        "Resend": "false"
    }

    try:
        response = await client.post(
            "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin",
            headers=headers,
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
            "error": True
        })
