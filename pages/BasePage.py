from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait(self, ms: int = 3000):
        self.page.wait_for_timeout(ms)

    def scroll_down(self, px: int = 3000):
        self.page.evaluate(f"window.scrollTo(0, {px})")
        self.wait(9000)

    def scroll_up(self, px: int = 3000):
        self.page.evaluate(f"window.scrollTo(0, -{px})")
        self.wait(9000)
