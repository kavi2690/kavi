class LoginPage:

    def __init__(self, page):
        self.page = page

        self.logo = "img"
        self.page.wait_for_timeout(3000)
        self.email = "//input[@type='email']"
        self.page.wait_for_timeout(3000)
        self.submit = "//button[@type='submit']"
        self.page.wait_for_timeout(3000)
        self.otp_inputs = "input[maxlength='1']"
        self.page.wait_for_timeout(3000)


    def open(self, url):
        self.page.wait_for_timeout(3000)
        self.page.goto(url)

    def check_logo(self):
        self.page.wait_for_timeout(3000)
        logo = self.page.locator(self.logo).first

        if logo.is_visible():
            print("Login page logo is visible")

        print("Logo src:", logo.get_attribute("src"))

        logo.screenshot(path="logo.png")

    def print_page_details(self):

        print("page title:", self.page.title())
        print("page url:", self.page.url)

    def enter_email(self, email):
        self.page.wait_for_timeout(3000)
        self.page.fill(self.email, email)

    def click_submit(self):
        self.page.wait_for_timeout(3000)
        self.page.locator(self.submit).click()

    def enter_otp(self, otp):
        self.page.wait_for_timeout(3000)
        self.page.wait_for_selector(self.otp_inputs)

        inputs = self.page.locator(self.otp_inputs)

        for i in range(6):
            inputs.nth(i).fill(otp[i])