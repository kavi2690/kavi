class RolesPage:
    def __init__(self, page):
        self.page = page
        
    def create_Roles(self):
        # create event 
        self.page.set_default_timeout(6000)
        
        self.page.get_by_text("Create").click()
        
        self.page.wait_for_timeout(4000)
        
        # fill role name
        self.page.fill('input[name="name"]', "Office Staff")

        # select permissions
        self.page.locator('select[name="permission[]"]').select_option(["1","2"])

        # wait
        self.page.wait_for_timeout(3000)
    
        self.page.get_by_text("Save").click()
        
        self.page.wait_for_timeout(4000)
        
        # # scroll down 
        self.page.evaluate("window.scrollTo(0, -5000)")
        
        # click edit button
        self.page.locator("a.edit").first.click()

        self.page.wait_for_timeout(3000)

# clear and update role name
        self.page.fill('#editModal input[name="name"]', "Office Staff")
        self.page.wait_for_timeout(3000)
# update permissions
        self.page.locator('select[name="permission[]"]').select_option(["2","3"])
        self.page.wait_for_timeout(3000)
# click update
        self.page.get_by_text("Submit").click()
    
        self.page.wait_for_timeout(3000)
        
        # view 
        
        self.page.locator("//a[@data-id='2']").first.click()

    # wait for modal
        self.page.wait_for_selector(".modal.show", timeout=5000)

        # close modal
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()