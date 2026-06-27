from playwright.sync_api import sync_playwright
import re
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page(user_agent="Mozilla/5.0 Chrome/120")
        page.goto("https://taoiptv.com/#", timeout=40000, wait_until="networkidle")
        page.wait_for_timeout(5000)
        page.click("span:has-text(\"获取Token\")")
        page.wait_for_timeout(3000)
        html = page.content()
        browser.close()
        match = re.search(r"token=([a-zA-Z0-9]{16})", html)
        if not match:
            raise Exception("未匹配到16位Token")
        token = match.group(1)
        with open("token.txt", "w", encoding="utf-8") as f:
            f.write(token)
        print(f"TOKEN={token}")
if __name__ == "__main__":
    run()
