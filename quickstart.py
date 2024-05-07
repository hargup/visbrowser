from playwright.sync_api import sync_playwright

def click(page, text):
    # Find an element containing the specified text and click on it
    element = page.locator(f"text={text}").first
    if element.count() == 0:
        print(f"No element found with text '{text}'")
        return False
    element.click()
    print(f"Clicked on element with text '{text}'")
    return True

def main():
    # Initialize Playwright and start a browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://paulgraham.com/index.html")
        text_to_click = "How to Start Google"
        success = click(page, text_to_click)
        
        if not success:
            print("Failed to click on the element.")
        
        page.wait_for_timeout(3000)
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()
