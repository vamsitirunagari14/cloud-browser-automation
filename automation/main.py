import json
from pathlib import Path
from playwright.sync_api import sync_playwright


def main():

    # Read profile summary from JSON
    config_path = Path("config/profile.json")

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    new_summary = config["profile_summary"]

    # Open demo webpage
    demo_file = Path("demo/index.html").resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(demo_file)

        # Fill summary
        page.locator("#summary").fill(new_summary)

        # Save summary
        page.locator("#save").click()

        # Verify saved content
        saved_summary = page.evaluate(
            "() => localStorage.getItem('profileSummary')"
        )

        assert saved_summary == new_summary

        print("SUCCESS: Configuration loaded!")
        print("SUCCESS: Summary entered!")
        print("SUCCESS: Summary saved and verified!")

        browser.close()


if __name__ == "__main__":
    main()
