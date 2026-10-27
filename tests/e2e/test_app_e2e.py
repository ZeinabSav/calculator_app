import subprocess
import time
from playwright.sync_api import sync_playwright

def test_add_endpoint():
    # Start FastAPI server
    server = subprocess.Popen(
        ["uvicorn", "app.api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Give server time to start
    time.sleep(3)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("http://127.0.0.1:8000/add?a=5&b=3")
        response = page.content()

        assert "8" in response  # 5 + 3 = 8

        browser.close()

    # Stop server
    server.terminate()


