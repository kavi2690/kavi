class CityPage:
    def __init__(self, page):
        self.page = page

    def create_city(self):

        # Click Create
        
        # self.page.get_by_text("Create").click()
           
        # # Wait for country dropdown
        # self.page.wait_for_timeout(4000)
        # self.page.wait_for_selector("#country_id")

        # # Select country
        # self.page.wait_for_timeout(4000)
        # self.page.select_option("#country_id", label="India")

        # # Wait until state options are loaded
        # self.page.wait_for_function(
        #     "document.querySelector('#state_id').options.length > 1"
        # )

        # # Select state
        # self.page.wait_for_timeout(4000)
        # self.page.select_option("#state_id", label="Tamil Nadu")

        # # Fill city name
        # self.page.wait_for_timeout(4000)
        # self.page.fill("input[name='name']", "pollachi")

        # # Fill city code
        # self.page.wait_for_timeout(4000)
        # self.page.fill("input[name='code']", "PO")

        # # Click Save
        # self.page.wait_for_timeout(4000)
        # self.page.get_by_text("Save").click()
        
        # scroll down 
        self.page.evaluate("window.scrollTo(0, 9000)")
        
        self.page.wait_for_timeout(4000)
        
        # edit 
        self.page.locator('a.edit[data-id="8"]').click()
        self.page.wait_for_timeout(4000)
        
        self.page.wait_for_selector("select[id='edit_country_id']", timeout=10000)

        self.page.locator("select[id='edit_country_id']").select_option(value="")
        self.page.wait_for_timeout(3000)
        
        self.page.select_option("select[id='edit_country_id']", label="India")
        self.page.wait_for_timeout(3000)
        
        self.page.wait_for_selector("select[id='edit_state_id']", timeout=10000)

        self.page.locator("select[id='edit_state_id']").select_option(value="")
        self.page.wait_for_timeout(3000)
        
        self.page.select_option("select[id='edit_state_id']", label="Tamil Nadu")
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_name"]').clear()
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_name"]').fill("Udumalapet")
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_code"]').clear()
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_code"]').fill("UDU")
        self.page.wait_for_timeout(3000)
        
        # self.page.get_by_text("Update").click()
        self.page.locator("#editModal button:has-text('Update')").click()
        
        self.page.wait_for_timeout(3000)
        
        # view city 
        self.page.locator("//a[@data-id='8']").first.click()
        self.page.wait_for_timeout(4000)
        
        # # close view modal
    
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
        
        self.page.locator("select[name='country_id']:visible").select_option(label="India")
        self.page.wait_for_timeout(6000)
        
        self.page.locator("select[name='state_id']:visible").select_option(label="Tamil Nadu")
        self.page.wait_for_timeout(6000)
        
        self.page.fill("//input[@name='search']",("Palani"))
        self.page.wait_for_timeout(6000)
        

    # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)
        
        
        
        