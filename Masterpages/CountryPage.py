class CountryPage:

    def __init__(self, page):
        self.page = page

    def create_country(self):
        
        self.page.evaluate("window.scrollTo(0, 9000)")
    
        self.page.wait_for_timeout(9000)
    
        self.page.evaluate("window.scrollTo(0, -9000)")
    

        self.page.get_by_text("Create").click()
        self.page.wait_for_timeout(3000)

        self.page.locator('input[placeholder="Enter country name"]').first.fill("Zimbave")
        self.page.wait_for_timeout(3000)

        self.page.locator(
            'input[placeholder="Enter country code (e.g., IND)"]'
        ).first.fill("ZIM")

        self.page.wait_for_timeout(3000)
        self.page.get_by_text("Save").click()
        self.page.wait_for_timeout(3000)

    
        # edit
        self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.wait_for_timeout(8000)
        self.page.locator('a.edit[data-id="6"]').click()
        self.page.wait_for_timeout(8000)

        self.page.locator('#editModal input[name="name"]').clear()
        self.page.wait_for_timeout(6000)

        self.page.locator('#editModal input[name="code"]').clear()
        self.page.wait_for_timeout(6000)

        self.page.locator('#editModal input[name="name"]').fill("United Kingdom")
        self.page.wait_for_timeout(6000)

        self.page.locator('#editModal input[name="code"]').fill("GBR")
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Update").click()
        self.page.wait_for_timeout(6000)

    # view country
    
        self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//a[@data-id='6']").first.click()
        self.page.wait_for_timeout(6000)
        
    # close view modal
    
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        self.page.wait_for_timeout(6000)
    # inactive country
   
        self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//button[@onclick='showStatusModal(9, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # active country
   
        
        self.page.locator("//button[@onclick='showStatusModal(9, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # status dropdown filter
    
        self.page.evaluate("window.scrollTo(0, -9000)")
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        

    # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)

    # search country
    
        self.page.fill("//input[@name='search']", "Singapore")
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Reset").click()
        
        