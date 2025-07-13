# Website Load Speed Tester

A simple and beginner-friendly Python project using [Playwright](https://playwright.dev/python/) to measure how fast a website loads, open the website in a browser, and save results to a text file.

## Features

✅ Takes user input (website URL)  
✅ Automatically opens the website in a browser  
✅ Measures total load time  
✅ Categorizes the result: `Fast` or `Slow`  
✅ Appends result to a `report.txt` file (doesn't overwrite previous tests)  
✅ Built with `Playwright` and pure `Python` (no AI required)

##  Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/website-load-speed-tester.git
cd website-load-speed-tester
```

### 2. Install Python Dependencies

```bash
pip install playwright
playwright install
```

## ▶️ How to Run

```bash
python page_speed_checker.py
```

Follow the prompt:

```text
Enter website URL (or 'q' to quit): google.com
https://google.com loaded in 1.32s - Fast
Result added to report.txt
```

## 📂 Project Structure

```
📦website-load-speed-tester/
├── page_speed_checker.py     # Main script
├── report.txt                # Output log file
├── README.md                 # GitHub README file
```

## 📄 Sample Output (`report.txt`)

```
https://google.com loaded in 1.32s - Fast
https://example.com loaded in 3.41s - Slow
https://invalid-url.test - Failed to load
```

## 📑 Documentation

You can find full documentation in the included Word file:

📄 Website_Load_Speed_Tester_Documentation.docx

## 🙋‍♀️ Author

👩‍💻 **Saloni Singh**  
🎓 Passionate about software development, testing, and real-world Python projects.

## ⭐ Give it a Star!

If you find this project helpful, please ⭐ star the repo and share it with others!

