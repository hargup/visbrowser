import time
# import pytesseract
from PIL import Image
from playwright.sync_api import Page, expect, sync_playwright
import io
# from autocorrect import Speller
import easyocr
import diskcache
import hashlib

# spell = Speller(only_replacements=True)
reader = easyocr.Reader(['en'])


cache = diskcache.Cache('screenshot_cache')

def hash_image(image_bytes):
    return hashlib.md5(image_bytes).hexdigest()

def extract_text_and_bbox(image_bytes):
    image_hash = hash_image(image_bytes)
    if image_hash in cache:
        # print("Cache hit, using pre-stored results")
        return cache[image_hash]
    else:
        pass
        # print("Didn't found cache")

    results = reader.readtext(image_bytes)
    text_bbox_list = []
    for res in results:
        bbox = res[0]
        x = min(bbox[0][0], bbox[1][0], bbox[2][0], bbox[3][0])
        y = min(bbox[0][1], bbox[1][1], bbox[2][1], bbox[3][1])
        width = max(bbox[0][0], bbox[1][0], bbox[2][0], bbox[3][0]) - x
        height = max(bbox[0][1], bbox[1][1], bbox[2][1], bbox[3][1]) - y
        text_bbox_list.append((res[1], [x, y, width, height]))

    cache[image_hash] = text_bbox_list
    return text_bbox_list

def wait_for_text(page: Page, text: str, timeout: int = 10):
    start_time = time.time()
    while True:
        screenshot_bytes = page.screenshot()
        text_bbox_list = extract_text_and_bbox(screenshot_bytes)
        # print(text_bbox_list)
        for extracted_text, _ in text_bbox_list:
            if text.lower() in extracted_text.lower():
                return True
        if timeout and time.time() - start_time > timeout:
            raise TimeoutError(f"Text '{text}' not found on the page within the specified timeout.")
        time.sleep(1)

def type(page, text):
    page.keyboard.type(text)

def click(page: Page, text: str):
    screenshot_bytes = page.screenshot()
    text_bbox_list = extract_text_and_bbox(screenshot_bytes)
    for extracted_text, bbox in text_bbox_list:
        if text.lower() in extracted_text.lower():
            center_x = int(bbox[0] + (bbox[2] // 2))
            center_y = int(bbox[1] + (bbox[3] // 2))
            # print(f'clicking {center_x}, {center_y}')
            page.mouse.click(center_x, center_y)
            return
    raise ValueError(f"Text '{text}' not found on the page.")

def hover(page: Page, text: str):
    screenshot_bytes = page.screenshot()
    text_bbox_list = extract_text_and_bbox(screenshot_bytes)
    for extracted_text, bbox in text_bbox_list:
        if text.lower() in extracted_text.lower():
            center_x = bbox[0] + bbox[2] // 2
            center_y = bbox[1] + bbox[3] // 2
            page.mouse.move(center_x, center_y)
            return
    raise ValueError(f"Text '{text}' not found on the page.")