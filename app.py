from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("kay-kay-t")

password_box = browser.find_element_by_id("password")
password_box.send_keys("ertfegh")
password_box.submit()

# to verify we logged in correctly
assert "kay-kay-t" in browser.page_source

profile_link = browser.find_elements_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "kay-kay-t" in link_label

browser.quit()
