from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.CountryPage import CountryPage
from pages.StatePage import StatePage
from pages.CityPage import CityPage
from pages.EventTypePage import EventTypePage
from pages.BlogCategoryPage import BlogCategoryPage
from pages.BlogTagPage import BlogTagPage
from pages.EventDomainPage import EventDomainPage
from pages.InstitutionPage import InstitutionPage
from pages.HighlightsPage import HighlightsPage
from pages.EventGroupPage import EventGroupPage
from pages.RolesPage import RolesPage


from config import BASE_URL, EMAIL, OTP


def test_medora_flow(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    country = CountryPage(page)
    state = StatePage(page)
    city = CityPage(page)
    eventtype = EventTypePage(page)
    blogcategory = BlogCategoryPage(page)
    blogtag = BlogTagPage(page)
    eventdomain = EventDomainPage(page)
    institution = InstitutionPage(page)
    highlights = HighlightsPage(page)
    eventgroup = EventGroupPage(page)
    roles = RolesPage(page)
    login.open(BASE_URL)

    login.check_logo()

    login.print_page_details()

    login.enter_email(EMAIL)

    login.click_submit()

    login.enter_otp(OTP)

    login.click_submit()

    dashboard.open_master()

    # dashboard.open_country()

    # country.create_country()

    # dashboard.open_state()

    # state.create_state()

    # dashboard.open_city()

    # city.create_city()
    
    # dashboard.open_EventType()
    
    # eventtype.create_EventType()
    
    # dashboard.open_BlogCategory()

    # blogcategory.create_BlogCategory()
    
    # BlogTag
    # dashboard.open_BlogTag()
    # blogtag.create_BlogTag()
    
    # Event Domain
    # dashboard.open_EventDomain()
    # eventdomain.create_EventDomain()
    
    # Institution
    dashboard.open_Institution()
    institution.create_Institution()
    
    # Highlights
    dashboard.open_Highlights()
    highlights.create_Highlights()

    # Event Group
    dashboard.open_EventGroup()
    eventgroup.create_EventGroup()

    # Roles
    dashboard.open_Roles()
    roles.create_Roles()
    
    
