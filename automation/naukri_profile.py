from playwright.sync_api import sync_playwright

PROFILE_URL = "https://www.naukri.com/mnjuser/profile?action=modalOpen"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Opening Naukri profile...")

        page.goto(
            PROFILE_URL,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        print("Page title:", page.title())
        print("Current URL:", page.url)

        if "login" in page.url.lower():
            print("Authentication required.")
        else:
            print("Naukri page loaded. Inspecting profile fields...")

            fields = page.locator("input, textarea").all()

            for field in fields:
                print({
                    "placeholder": field.get_attribute("placeholder"),
                    "type": field.get_attribute("type"),
                    "id": field.get_attribute("id")
                })

        browser.close()


if __name__ == "__main__":
    main()
