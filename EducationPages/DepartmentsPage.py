class DepartmentsPage:

    def __init__(self, page):
        self.page = page

    def create_Departments(self):
        
        self.page.wait_for_timeout(2000)   
        
        self.page.get_by_text("Create").click()