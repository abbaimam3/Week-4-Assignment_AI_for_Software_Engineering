import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ==========================================
# Part 2, Task 2: Automated Testing with AI
# ==========================================

def setup_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment to run headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_login(driver, username, password, test_name):
    print(f"Running Test: {test_name}...")
    driver.get("https://www.saucedemo.com/")
    
    # Locate elements
    user_field = driver.find_element(By.ID, "user-name")
    pass_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    # Perform actions
    user_field.send_keys(username)
    pass_field.send_keys(password)
    login_btn.click()
    time.sleep(1) # Wait for page load/animation
    
    # Check results
    screenshot_name = f"screenshot_{test_name}.png"
    driver.save_screenshot(screenshot_name)
    
    current_url = driver.current_url
    if "inventory.html" in current_url:
        print(f"  -> SUCCESS: Logged in successfully. Screenshot saved to {screenshot_name}")
        return True
    else:
        # Check for error message
        try:
            error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
            print(f"  -> FAILED LOGIN (Expected for invalid): {error_msg}")
            print(f"  -> Screenshot saved to {screenshot_name}")
        except:
            print(f"  -> UNKNOWN STATE. Screenshot saved to {screenshot_name}")
        return False

def main():
    driver = setup_driver()
    try:
        # Test Case 1: Valid Credentials
        test_login(driver, "standard_user", "secret_sauce", "valid_login")
        
        print("-" * 30)
        
        # Test Case 2: Invalid Credentials
        test_login(driver, "locked_out_user", "secret_sauce", "invalid_login")
        
    finally:
        driver.quit()
        print("\nTests Completed.")

if __name__ == "__main__":
    main()

# ==========================================
# Summary: AI vs Manual Testing
# ==========================================
"""
How AI improves test coverage compared to manual testing:

1.  **Speed & Scale:** AI-driven tools (like Selenium with AI plugins or Testim) can execute thousands of test cases in minutes across multiple browsers/devices simultaneously, which is impossible manually.
2.  **Self-Healing:** Traditional scripts break when UI selectors (IDs/Classes) change. AI tools use visual locators and machine learning to identify elements even if attributes change, reducing maintenance.
3.  **Visual Regression:** AI can detect subtle pixel-level changes in the UI that a human tester might miss, ensuring the visual integrity of the application.
4.  **Edge Case Generation:** Generative AI can automatically suggest and generate edge case data (e.g., SQL injection strings, boundary values) to improve test coverage beyond the "happy path."
"""
