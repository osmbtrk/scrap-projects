from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import re
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.facebook.com/AtheistRepublic/')

pre_scroll_height = driver.execute_script('return document.body.scrollHeight;')
run_time, max_run_time = 0, 5
while True:
    iteration_start = time.time()
    # Scroll webpage, the 100 allows for a more 'aggressive' scroll
    driver.execute_script('window.scrollTo(0, 100*document.body.scrollHeight);')

    post_scroll_height = driver.execute_script('return document.body.scrollHeight;')

    scrolled = post_scroll_height != pre_scroll_height
    timed_out = run_time >= max_run_time

    if scrolled:
        run_time = 0
        pre_scroll_height = post_scroll_height
    elif not scrolled and not timed_out:
        run_time += time.time() - iteration_start
    elif not scrolled and timed_out:
        break

# closing the driver is