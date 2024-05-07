# VisBrowser: Visual Browsing Adapter for Playwright Python

The Visual Browser Adapter is a Python library that provides a high-level and intuitive API for interacting with web pages using Playwright. It simplifies common tasks like clicking, typing, and waiting for elements, making it easier to automate web browsing and testing.

## Installation

To install the Visual Browser Adapter, use pip:

```
pip install visbrowser
```

## Usage

Here's a basic example of how to use the Visual Browser Adapter:

```python
import visbrowser as vb

# Perform actions on the page
vb.click(page, "Enter mobile number")
vb.type(page, "9999988888")
vb.wait_for_text(page, "Enter MPIN", timeout=5000)
vb.click(page, "Enter MPIN")
vb.type(page, "2020")
vb.wait_for_text(page, "Login", timeout=5000)
vb.click(page, "Login")
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
