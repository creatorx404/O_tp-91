#!/usr/bin/env python3
import sys
import asyncio
from playwright.async_api import async_playwright

async def zomato_otp(phone):
    try:
        async with async_playwright() as p:
            # Use Firefox instead of Chromium
            browser = await p.firefox.launch(headless=True)
            
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
                viewport={'width': 1920, 'height': 1080},
            )
            
            page = await context.new_page()
            
            await page.goto('https://www.zomato.com/', timeout=30000)
            await page.wait_for_timeout(3000)
            
            # Click login
            try:
                await page.click('text=Log in', timeout=5000)
                await page.wait_for_timeout(2000)
            except:
                pass
            
            # Fill phone
            try:
                await page.fill('input[type="tel"]', phone, timeout=10000)
                await page.wait_for_timeout(500)
                await page.click('button:has-text("Send")', timeout=5000)
                await page.wait_for_timeout(4000)
                
                content = await page.content()
                await browser.close()
                
                if 'otp' in content.lower() or 'verify' in content.lower():
                    return "SUCCESS"
                return "FAILED"
            except Exception as e:
                await browser.close()
                return f"ERROR:{e}"
    except Exception as e:
        return f"ERROR:{e}"

async def airtel_otp(phone):
    try:
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            )
            page = await context.new_page()
            
            await page.goto('https://www.airtel.in/manage-account/login', timeout=30000)
            await page.wait_for_timeout(3000)
            
            try:
                await page.fill('input[type="tel"]', phone, timeout=10000)
                await page.click('button:has-text("OTP"), button:has-text("Continue")', timeout=5000)
                await page.wait_for_timeout(5000)
                
                content = await page.content()
                await browser.close()
                
                if 'otp' in content.lower() or 'verify' in content.lower():
                    return "SUCCESS"
                return "FAILED"
            except Exception as e:
                await browser.close()
                return f"ERROR:{e}"
    except Exception as e:
        return f"ERROR:{e}"

async def main():
    if len(sys.argv) < 3:
        print("ERROR:Usage")
        sys.exit(1)
    
    site = sys.argv[1].lower()
    phone = sys.argv[2][-10:]
    
    if site == "zomato":
        result = await zomato_otp(phone)
    elif site == "airtel":
        result = await airtel_otp(phone)
    else:
        result = "ERROR:Unknown"
    
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
