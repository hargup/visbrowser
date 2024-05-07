# VisBrowser: Visual Browsing Adapter for Playwright Python

VisBrowser is a visual browsing adapter for Playwright Python that enables navigation and interaction with web pages based on visual information rather than CSS selectors. It provides a high-level API for performing actions like clicking, typing, and waiting for elements using visual cues such as text and images. With VisBrowser, you can automate web browsing tasks by leveraging the visual layout and content of the page, making your scripts more resilient to changes in the underlying HTML structure. Particularly useful for website which doesn't give a proper dom, like fuller website, or websites using HTML canvas.

## Installation

To install the Visual Browser Adapter, use pip:

```
pip install git+https://github.com/hargup/visbrowser.git
```

## Quick Start

```
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
```

## API Reference

### `click_image(page, image_path, confidence=0.8)`

Clicks on an image on the page that matches the specified image file.

- `page`: The Playwright page object.
- `image_path`: The path to the image file to search for on the page.
- `confidence` (optional): The minimum confidence level (between 0 and 1) for a match to be considered valid. Defaults to 0.8.

### `wait_for_image(page, image_path, timeout=10.0, confidence=0.6)`

Waits for an image to appear on the page that matches the specified image file.

- `page`: The Playwright page object.
- `image_path`: The path to the image file to wait for on the page.
- `timeout` (optional): The maximum time to wait in seconds. Defaults to 10.0 seconds.
- `confidence` (optional): The minimum confidence level (between 0 and 1) for a match to be considered valid. Defaults to 0.6.

Returns `True` if the image is found within the specified timeout, otherwise returns `False`.

### `click(page, text)`

Clicks on an element that contains the specified text.

- `page`: The Playwright page object.
- `text`: The text content of the element to click.

### `hover(page, text)`

Hovers over an element that contains the specified text.

- `page`: The Playwright page object.
- `text`: The text content of the element to hover over.

### `type(page, text)`

Types the specified text into the focused input element.

- `page`: The Playwright page object.
- `text`: The text to type.

### `wait_for_text(page, text, timeout=None)`

Waits for the specified text to appear on the page.

- `page`: The Playwright page object.
- `text`: The text to wait for.
- `timeout` (optional): The maximum time to wait in milliseconds. Defaults to `None`, which means it will wait indefinitely.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.


## License

The code is licensed under GPLv3.

## Automation Consulting and dual licensing

If you are looking to build automation scripts for your company, say a script to periodically download data from a website, or automatically tweet a certain thing at a schedule or something else. Please contact me at harsh AT felvin DOT com, send me a quick video of you doing the task value and we'll get back to you with a quote, typical price being $300 per script.