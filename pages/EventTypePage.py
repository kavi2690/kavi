class EventTypePage:
    def __init__(self, page):
        self.page = page
        
    def create_EventType(self):
        
        # create event 
        self.page.wait_for_timeout(3000)
        
        self.page.get_by_text("Create").click()
        
        self.page.wait_for_timeout(4000)
        
        self.page.fill("input[name='name']", "Seminar")
        
        self.page.wait_for_timeout(4000)
        
        self.page.get_by_text("Save").click()
        
        self.page.wait_for_timeout(4000)
        
        # # scroll down 
        # self.page.evaluate("window.scrollTo(0, 9000)")
        
        # self.page.locator('a.edit[data-id="1"]').click()
        # self.page.wait_for_timeout(4000)
        
        # self.page.locator('#editModal input[id="edit_name"]').clear()
        # self.page.wait_for_timeout(3000)
        
        # self.page.locator('#editModal input[id="edit_name"]').fill("Networking Event")
        # self.page.wait_for_timeout(3000)
        
        # self.page.get_by_text("Update").click()
        # self.page.wait_for_timeout(3000)
        
        # view 
        
    #    self.page.locator("//a[@data-id='6']").first.click()

    # wait for modal
        self.page.wait_for_selector(".modal.show", timeout=5000)

        # close modal
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        
    # inactive country
   
        # self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//button[@onclick='showStatusModal(6, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # active country
   
        
        self.page.locator("//button[@onclick='showStatusModal(6, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)
        
        # active status 
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        
        self.page.fill("//input[@name='search']",("Competition"))
        self.page.wait_for_timeout(6000)
        
         # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)
        