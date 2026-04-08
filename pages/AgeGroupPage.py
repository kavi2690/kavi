class AgeGroupPage:
    def __init__(self, page):
        self.page = page

    def create_AgeGroup(self):
        
        # self.page.set_default_timeout(6000)
        
        # self.page.get_by_text("Create").click()
        
        # self.page.wait_for_timeout(4000)
        
        # self.page.fill("input[name='name']", "Women")
        
        # self.page.wait_for_timeout(4000)
        
        # self.page.fill("input[name='from_age']", '8')
        
        # self.page.wait_for_timeout(4000)
        
        # self.page.fill("input[name='to_age']", '20')
        
        # self.page.get_by_text("Save").click()
        
        # self.page.wait_for_timeout(4000)
        
        # # edit 
        # self.page.evaluate("window.scrollTo(0, 3000)")
        
        # self.page.locator('a.edit[data-id="3"]').click()
        # self.page.wait_for_timeout(4000)
        
        # self.page.locator('#editModal input[id="edit_name"]').clear()
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_name"]').fill("Boy")
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_from_age"]').clear()
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_from_age"]').fill("18")
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_to_age"]').clear()
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_to_age"]').fill("25")
        # self.page.wait_for_timeout(3000)
        
        # self.page.get_by_text("Update").click()
        # self.page.wait_for_timeout(3000)
        
         # view 
        
        self.page.locator("//a[@data-id='3']").first.click()

    # wait for modal
        self.page.wait_for_selector(".modal.show", timeout=10000)

        # close modal
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        
        # Inactive
        
        self.page.locator("//button[@onclick='showStatusModal(3, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)
        
        # Active
        self.page.locator("//button[@onclick='showStatusModal(3, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)
        
        
         # active status 
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        
        self.page.fill("//input[@name='search']",("Boy"))
        self.page.wait_for_timeout(6000)
        
         # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)
        