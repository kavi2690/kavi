class StatePage:

    def __init__(self, page):
        self.page = page

    def create_state(self):
        self.page.wait_for_timeout(3000)
        # self.page.get_by_text("Create").click()
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator("#createModal select[name='country_id']").select_option(label="United Kingdom")
        # self.page.wait_for_timeout(6000)
        
        # self.page.fill("input[name='name']", "Scotland")
        # self.page.wait_for_timeout(3000)
        
        # self.page.fill("input[name='code']", "SCT")
        # self.page.wait_for_timeout(3000)

        # self.page.get_by_text("Save").click()
        
        # self.page.wait_for_timeout(3000)
        
        # self.page.evaluate("window.scrollTo(0, 9000)")
    
        # self.page.wait_for_timeout(3000)
    
        # self.page.evaluate("window.scrollTo(0, -9000)")
        # Click next button 
        # self.page.locator("a[aria-label='Next »']").click()
    
        # self.page.evaluate("window.scrollTo(0, 9000)")
    
        # self.page.wait_for_timeout(3000)

    # Click Previous button
        # self.page.get_by_label("Previous").click()
    
        # self.page.evaluate("window.scrollTo(0, -7000)")
    
        # self.page.wait_for_timeout(6000)
        
        # self.page.evaluate("window.scrollTo(0, 9000)")
        # self.page.click("//a[@aria-label='Next »']")
    
        
        
    # Edit state 
    
        self.page.wait_for_timeout(8000)
        
        self.page.locator('a.edit[data-id="1"]').click()
        
        self.page.wait_for_timeout(3000)
        
        self.page.wait_for_selector("select[id='edit_country_id']", timeout=10000)

        self.page.locator("select[id='edit_country_id']").select_option(value="")
        self.page.wait_for_timeout(3000)
        self.page.select_option("select[id='edit_country_id']", label="Brazil")
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_name"]').clear()
        self.page.wait_for_timeout(3000)
        self.page.locator('#editModal input[id="edit_name"]').fill("Acre")
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_code"]').clear()
        self.page.wait_for_timeout(3000)
        self.page.locator('#editModal input[id="edit_code"]').fill("AC")
        self.page.wait_for_timeout(3000)
        
        # self.page.get_by_text("Update").click()
        self.page.locator("#editModal button:has-text('Update')").click()
        
        self.page.wait_for_timeout(3000)
        
        # previous
        # self.page.get_by_label("Previous").click()
        # self.page.wait_for_timeout(6000)
    # view country
    
        # self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//a[@data-id='1']").first.click()
        self.page.wait_for_timeout(6000)
    #     self.page.locator("//a[@data-id='31']").first.click()
        
        
    # # close view modal
    
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        self.page.wait_for_timeout(6000)
    
    # inactive country
   
        self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//button[@onclick='showStatusModal(30, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # active country
   
        
        self.page.locator("//button[@onclick='showStatusModal(30, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # status dropdown filter
    
        self.page.evaluate("window.scrollTo(0, -9000)")
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        self.page.locator("select[name='country_id']:visible").select_option(label="Brazil")
        self.page.wait_for_timeout(6000)
        self.page.fill("//input[@name='search']",("United Kingdom"))
        self.page.wait_for_timeout(6000)
        

    # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)

    # search country
    
        self.page.fill("//input[@name='search']", "Brazil")
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Reset").click()
        