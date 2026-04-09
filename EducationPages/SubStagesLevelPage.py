class SubStagesLevelPage:

    def __init__(self, page):
        self.page = page

    def create_SubStagesLevel(self):
        self.page.wait_for_timeout(4000)
        
    #     self.page.get_by_text("Create").click()
        
    #     self.page.locator("#createModal select[name='level_id']").select_option(label="School")
    #     self.page.wait_for_timeout(6000)
        
    #     self.page.locator("#createModal select[name='sub_level_id']").select_option(label="Matriculation")
    #     self.page.wait_for_timeout(6000)
        
    #     self.page.fill("input[name='label_name']", "High School")
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.fill("input[name='name']", "SSLC")
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.get_by_text("Save").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #     # Scroll down and up 
    #     self.page.evaluate("window.scrollTo(0, 10000)")
    
    #     self.page.wait_for_timeout(3000)
    
    #     # self.page.evaluate("window.scrollTo(0, -10000)")
        
    #     # edit
        
    #     # pagenation next button 
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.locator("a[aria-label='Next »']").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.evaluate("window.scrollTo(0, 9000)")
    
    #     self.page.wait_for_timeout(3000)
    
    #     self.page.locator('a.edit[data-id="29"]').click()
        
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.wait_for_selector("select[id='edit_level_id']", timeout=10000)

    #     self.page.locator("select[id='edit_level_id']").select_option(value="")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.select_option("select[id='edit_level_id']", label="School")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.wait_for_selector("select[id='edit_sub_level_id']", timeout=10000)

    #     self.page.locator("select[id='edit_sub_level_id']").select_option(value="")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.select_option("select[id='edit_sub_level_id']", label="State Board")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator('#editModal input[id="edit_label_name"]').clear()
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator('#editModal input[id="edit_label_name"]').fill("7th Standard")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator('#editModal input[id="edit_name"]').clear()
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator('#editModal input[id="edit_name"]').fill("Class 7")
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.get_by_text("Update").click()
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator("a[aria-label='Next »']").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.evaluate("window.scrollTo(0, 9000)")
    
    #     self.page.wait_for_timeout(3000)
        
    #     self.page.locator("a[aria-label='Next »']").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #      # view 
        
    #     self.page.locator("//a[@data-id='78']").first.click()
    #     self.page.wait_for_timeout(4000)
    # # wait for modal
    #     self.page.wait_for_selector(".modal.show", timeout=5000)

    #     # close modal
    #     self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.evaluate("window.scrollTo(0, 9000)")
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.get_by_role("link", name="3").click()
        
    #     self.page.evaluate("window.scrollTo(0, 9000)")
        
    #     self.page.wait_for_timeout(4000)
        
    #     self.page.get_by_role("link", name="1").click()
        
    #     self.page.wait_for_timeout(4000)
        
    #       # active and inactive filter 
    #     self.page.locator("//button[@onclick='showStatusModal(96, 1)']").click()
    #     self.page.wait_for_timeout(6000)
    #     self.page.get_by_text("Yes").click()
    #     self.page.wait_for_timeout(6000)
        
    #     self.page.locator("//button[@onclick='showStatusModal(96, 0)']").click()
    #     self.page.wait_for_timeout(6000)
    #     self.page.get_by_text("Yes").click()
    #     self.page.wait_for_timeout(6000)
        
         # status dropdown filter
    
        
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        
        self.page.locator("select[name='level_id']:visible").select_option(label="School")
        self.page.wait_for_timeout(6000)
        
        self.page.locator("select[name='sub_level_id']:visible").select_option(label="Matriculation")
        self.page.wait_for_timeout(6000)
        
        self.page.fill("//input[@name='search']",("Class 8"))
        self.page.wait_for_timeout(6000)
        
        # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)

    # search country
    
        self.page.fill("//input[@name='search']", "Class 10")
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)
        
        self.page.get_by_text("Reset").click()