import time
# import pytesseract
from PIL import Image
from playwright.sync_api import Page, expect, sync_playwright
import io
from autocorrect import Speller
import easyocr

spell = Speller(only_replacements=True)
reader = easyocr.Reader(['en'])

def extract_text_and_bbox(image):
    results = reader.readtext(image)
    text_bbox_list = []
    for res in results:
        bbox = res[0]
        x = min(bbox[0][0], bbox[1][0], bbox[2][0], bbox[3][0])
        y = min(bbox[0][1], bbox[1][1], bbox[2][1], bbox[3][1])
        width = max(bbox[0][0], bbox[1][0], bbox[2][0], bbox[3][0]) - x
        height = max(bbox[0][1], bbox[1][1], bbox[2][1], bbox[3][1]) - y
        text_bbox_list.append((spell(res[1]), [x, y, width, height]))
    return text_bbox_list

def wait_for_text(page: Page, text: str, timeout: int = 10000):
    start_time = time.time()
    while True:
        screenshot = page.screenshot()
        image = Image.open(screenshot)
        text_bbox_list = extract_text_and_bbox(image)
        for extracted_text, _ in text_bbox_list:
            if text in extracted_text:
                return True
        if timeout and time.time() - start_time > timeout:
            return False
        time.sleep(1)


def click(page: Page, text: str):
    screenshot = page.screenshot()
    image = Image.open(io.BytesIO(screenshot))
    text_bbox_list = extract_text_and_bbox(image)
    for extracted_text, bbox in text_bbox_list:
        if text.lower() in extracted_text.lower():
            center_x = bbox[0] + (bbox[2] // 2)
            center_y = bbox[1] + (bbox[3] // 2)
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