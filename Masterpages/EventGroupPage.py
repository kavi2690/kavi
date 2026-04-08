class EventGroupPage:
    def __init__(self, page):
        self.page = page
        
    def create_EventGroup(self):
        # create eventgroup 
        self.page.set_default_timeout(6000)
        
        self.page.get_by_text("Create").click()
        
        self.page.wait_for_timeout(4000)
        
        self.page.fill("input[name='title']", "Educational Activities")
        
        self.page.wait_for_timeout(4000)
        
        self.page.fill("textarea[name='description']", "Activities that focus on learning, knowledge development, and academic excellence such as seminars, quizzes, workshops, and competitions")
        
        self.page.get_by_text("Save").click()
        
        self.page.wait_for_timeout(4000)
        
        # # scroll down 
        self.page.evaluate("window.scrollTo(0, -5000)")
        
        self.page.locator('a.edit[data-id="6"]').click()
        self.page.wait_for_timeout(4000)
        
        self.page.locator('#editModal input[id="edit_title"]').clear()
        self.page.wait_for_timeout(3000)
        
        self.page.locator('#editModal input[id="edit_title"]').fill("Smart Scholars")
        self.page.wait_for_timeout(3000)
        
        self.page.fill("#editModal textarea[id='edit_description']", "Smart Scholars is a group of motivated and talented students who are passionate about learning and academic excellence. The group focuses on developing knowledge, creativity, and critical thinking skills through & various educational activities, competitions, and school events. Members of Smart Scholars support each other, work as a team, and strive to achieve their goals with dedication and discipline. This group encourages curiosity, innovation, and leadership while promoting a positive learning environment where every student can grow, share ideas, and reach their full potential")
        
        self.page.get_by_text("Update").click()
        self.page.wait_for_timeout(3000)
        
        # view 
        
        self.page.locator("//a[@data-id='6']").first.click()

    # wait for modal
        self.page.wait_for_selector(".modal.show", timeout=5000)

        # close modal
        self.page.locator(".modal.show button[data-bs-dismiss='modal']").click()
        
    # inactive country
   
        # self.page.evaluate("window.scrollTo(0, 9000)")
        self.page.locator("//button[@onclick='showStatusModal(4, 1)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)

    # active country
   
        
        self.page.locator("//button[@onclick='showStatusModal(4, 0)']").click()
        self.page.wait_for_timeout(6000)
        self.page.get_by_text("Yes").click()
        self.page.wait_for_timeout(6000)
        
        # active status 
        self.page.select_option("//select[@name='status']", label='Active')
        self.page.wait_for_timeout(6000)
        
        self.page.fill("//input[@name='search']",("Educational Activities"))
        self.page.wait_for_timeout(6000)
        
         # click filter
    
        self.page.get_by_text("Filter").click()
        self.page.wait_for_timeout(6000)

    # click reset
    
        self.page.get_by_text("Reset").click()
        self.page.wait_for_timeout(6000)