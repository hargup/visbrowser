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

### `click(page, text)`

Clicks on an element that contains the specified text.

- `page`: The Playwright page object.
- `text`: The text content of the element to click.

### `double_click(page, text)`

Double-clicks on an element that contains the specified text.

- `page`: The Playwright page object.
- `text`: The text content of the element to double-click.

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

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README file based on your specific library and add more sections as needed, such as installation instructions, more detailed usage examples, and any additional information that would be helpful for users of your library.
