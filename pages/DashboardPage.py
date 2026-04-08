class DashboardPage:

    def __init__(self, page):
        self.page = page

    def open_master(self):
        self.page.get_by_text("Master").click()
        self.page.wait_for_timeout(3000)

    def open_country(self):
        self.page.get_by_text("Country").click()
        self.page.wait_for_timeout(3000)

    def open_state(self):
        self.page.get_by_text("State").click()
        self.page.wait_for_timeout(3000)
    
    def open_state(self):
        self.page.locator("a[href*='states']").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)
        
    def open_city(self):
         self.page.goto("https://hywebdemo.com/medora/admin/cities")
         self.page.wait_for_timeout(3000)
         
    def open_EventType(self):
        self.page.get_by_text("Event Type").click()
        self.page.wait_for_timeout(3000)
        
    def open_BlogCategory(self):
        self.page.get_by_text("Blog Category").click()
        self.page.wait_for_timeout(3000)
        
    def open_BlogTag(self):
        # self.page.get_by_text("Blog Tag").click()
        self.page.goto("https://hywebdemo.com/medora/admin/blog-tags")
        self.page.set_default_timeout(60000)
        
    def open_EventDomain(self):
        self.page.get_by_text("Event Domain").click()
        self.page.wait_for_timeout(3000)
        
    def open_Institution(self):
        self.page.get_by_text("Institution").click()
        self.page.wait_for_timeout(3000)
        
    def open_Highlights(self):
        self.page.get_by_text("Highlights").click()
        self.page.wait_for_timeout(3000) 
        
    def open_EventGroup (self):
        self.page.get_by_text("Event Group").click()
        self.page.wait_for_timeout(3000)
        
    def open_Roles (self):
        self.page.get_by_text("Roles").click()
        self.page.wait_for_timeout(3000)
        
    def open_AgeGroup(self):
        self.page.goto("https://hywebdemo.com/medora/admin/age-groups")
        self.page.set_default_timeout(60000)
        # self.page.get_by_text("Age Group").click()
        # self.page.wait_for_timeout(3000)
       
          
        
        