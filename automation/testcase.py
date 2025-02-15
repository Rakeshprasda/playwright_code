from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser= p.chromium.launch(headless=False,)
    page=browser.new_page()
    page.goto("https://demo.automationtesting.in/")
    page.wait_for_timeout(3000)
    print(page.title())
    page.wait_for_selector('#email').fill("rakp.gmail.com")
    page.wait_for_timeout(3000)
    next=page.locator("#enterimg")
    next.click()
    page.wait_for_timeout(3000)
    title = page.title()
    if title=="Register":
        page.wait_for_selector('input[placeholder="First Name"]').fill("rakesh")
        page.wait_for_selector('input[placeholder="Last Name"]').fill("prasad")
        page.wait_for_timeout(3000)
        page.locator("//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").type("rakesh is sdet")
        page.wait_for_timeout(3000)
        #page.query_selector("select#Skills").select_option(label="C++")        #we can give location and option seperatly
        #page.select_option("select#Skills",label="Corel Word Perfect")      #pass location and option in same
        #page.select_option("select#Skills", index=4)                    #based on index value

        ######## get the option name by index and select #######
        options = page.locator("select#Skills > option")
        option_to_select = options.nth(2).get_attribute("value")  # Get the value of the 3rd option
        print(option_to_select)
        page.select_option("select#Skills", value=option_to_select)
        page.wait_for_timeout(3000)
    else:
        print("not this page")