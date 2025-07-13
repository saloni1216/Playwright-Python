from playwright.sync_api import sync_playwright
import time

def check_speed(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        start = time.time()
        try:
            page.goto(url, wait_until="load")
            end = time.time()
            load_time = round(end - start, 2)
            if load_time < 3:
                result = f"{url} loaded in {load_time}s - Fast"
            else:
                result = f"{url} loaded in {load_time}s - Slow"
        except:
            result = f"{url} - Failed to load"
        browser.close()
        return result

while True:
    user_input = input("Enter website URL (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting.")
        break
    if not user_input.startswith("http"):
        user_input = "https://" + user_input
    result = check_speed(user_input)
    print(result)
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")
    print("Result added to report.txt\n")
