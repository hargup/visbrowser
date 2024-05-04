import time
import pytesseract
from PIL import Image
from playwright.sync_api import Page, expect, sync_playwright
import io


def extract_text_and_bbox(image):
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    text_bbox_list = []
    for i in range(len(data['text'])):
        if data['text'][i].strip():
            bbox = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            text_bbox_list.append((data['text'][i], bbox))
    return text_bbox_list


def wait_for_text(page: Page, text: str, timeout: int = None):
    start_time = time.time()
    while True:
        screenshot_bytes = page.screenshot()
        image = Image.open(io.BytesIO(screenshot_bytes))
        text_bbox_list = extract_text_and_bbox(image)
        for extracted_text, _ in text_bbox_list:
            if text in extracted_text:
                return True
        if timeout and time.time() - start_time > timeout:
            return False
        time.sleep(1)

def click(page: Page, text: str):
    screenshot = page.screenshot()
    image = Image.open(screenshot)
    text_bbox_list = extract_text_and_bbox(image)
    for extracted_text, bbox in text_bbox_list:
        if text in extracted_text:
            center_x = bbox[0] + bbox[2] // 2
            center_y = bbox[1] + bbox[3] // 2
            page.mouse.click(center_x, center_y)
            return
    raise ValueError(f"Text '{text}' not found on the page.")

def hover(page: Page, text: str):
    screenshot = page.screenshot()
    image = Image.open(screenshot)
    text_bbox_list = extract_text_and_bbox(image)
    for extracted_text, bbox in text_bbox_list:
        if text in extracted_text:
            center_x = bbox[0] + bbox[2] // 2
            center_y = bbox[1] + bbox[3] // 2
            page.mouse.move(center_x, center_y)
            return
    raise ValueError(f"Text '{text}' not found on the page.")