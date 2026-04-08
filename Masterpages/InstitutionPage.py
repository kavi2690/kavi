class InstitutionPage:
    def __init__(self, page):
        self.page = page
        
    def create_Institution(self):
        self.page.set_default_timeout(6000)
        
        self.page.evaluate("window.scrollTo(0, -5000)")
        
        self.page.wait_for_timeout(4000)
        
        self.page.evaluate("window.scrollTo(0, 5000)")
        
        self.page.wait_for_timeout(4000)
        
        self.page.get_by_text("Create").click()
        
        self.page.wait_for_timeout(4000)
        
        self.page.fill("input[name='name']", "Fun Friday")
        
        self.page.wait_for_timeout(4000)
        
        self.page.locator("#createForm select[name='type']").select_option(label="School")
        
        self.page.wait_for_timeout(3000)
        
        # self.page.get_by_text("Save")
        # self.page.wait_for_timeout(3000)

        self.page.locator("text=Save").click()
        
        # edit
        self.page.wait_for_timeout(3000)
        # self.page.evaluate("window.scrollTo(0, -5000)")
        
        self.page.locator('a.edit[data-id="1"]').click()
        self.page.wait_for_timeout(4000)
        
        self.page.locator('#editModal input[id="edit_name"]').clear()
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_name"]').fill("Sunrise Public School")
        self.page.wait_for_timeout(3000)
        
        # change dropdown value
        self.page.locator('#editModal select[id="edit_type"]').select_option(label="School")

        self.page.wait_for_timeout(3000)

        # click update button
        self.page.get_by_text("Update").click()
        
        self.page.wait_for_timeout(3000)
        
        # view 
        
        self.page.locator("//a[@data-id='5']").first.click()

    # wait for modal
        self.page.wait_for_selector(".modal.show", timeout=5000)

        # close modal
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        
    # inactive country
   
        # self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//button[@onclick='showStatusModal(2, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # active country
   
        
        self.page.locator("//button[@onclick='showStatusModal(2, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)
        
        # active status 
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        
        self.page.locator("select[name='type']:visible").select_option(label="College")
        self.page.wait_for_timeout(6000)
        
        
        self.page.fill("//input[@name='search']",("Global Engineering College"))
        self.page.wait_for_timeout(6000)
        
         # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)
        
        
        
        