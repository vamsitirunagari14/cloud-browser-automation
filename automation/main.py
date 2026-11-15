from pathlib import Path
from playwright.sync_api import sync_playwright

NEW_SUMMARY = """
Java Backend Developer with 3 years of experience in developing scalable
applications using Java, Spring Boot, and Microservices. Skilled in building
REST APIs, implementing backend business logic, integrating services, and
optimizing database interactions using SQL, Hibernate, and Spring Data JPA.
Experienced in developing secure applications using Spring Security and JWT.
Strong understanding of backend architecture, problem-solving, and Agile
development practices.
""".strip()


def main():
    demo_file = Path("demo/index.html").resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open our demo webpage
        page.goto(demo_file)

        # Enter the summary
        page.locator("#summary").fill(NEW_SUMMARY)

        # Click Save
        page.locator("#save").click()

        # Verify the result
        status = page.locator("#status").inner_text()
        saved_summary = page.evaluate(
            "() => localStorage.getItem('profileSummary')"
        )

        assert status == "Summary saved successfully!"
        assert saved_summary == NEW_SUMMARY

        print("SUCCESS: Summary entered and saved!")
        print("Verification passed!")

        browser.close()


if __name__ == "__main__":
    main()
