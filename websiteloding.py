from playwright.sync_api import sync_playwright  # For browser automation
import time  # To measure page load time

# Function to check how fast a website loads
def check_speed(url):
    with sync_playwright() as p:
        # Open Chromium browser (headless=False means browser will be visible)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
         # Start timing before loading the page

        start = time.time() 
        try:
            # Load the page and wait until it's fully loaded
            page.goto(url, wait_until="load")
            end = time.time()  
             # Calculate load time
            load_time = round(end - start, 2) 
            # Classify speed
            if load_time < 3:
                result = f"{url} loaded in {load_time}s - Fast"
            else:
                result = f"{url} loaded in {load_time}s - Slow"

        except:
            # In case of any error while loading
            result = f"{url} - Failed to load"

        browser.close()  
        return result  

# === MAIN PROGRAM ===
while True:
    # Ask user for website URL
    user_input = input("Enter website URL (or 'q' to quit): ")

    # Exit loop if user types 'q'
    if user_input.lower() == 'q':
        print("Exiting.")
        break

    # Add https:// if user didn't type it
    if not user_input.startswith("http"):
        user_input = "https://" + user_input

    # Run the speed check
    result = check_speed(user_input)
    print(result)

    # Save result to a file (append mode)
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")

    print("Result added to report.txt\n")
