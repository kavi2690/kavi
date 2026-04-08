from Masterpages.LoginPage import LoginPage
from Masterpages.DashboardPage import DashboardPage
from Masterpages.CountryPage import CountryPage
from Masterpages.StatePage import StatePage
from Masterpages.CityPage import CityPage
from Masterpages.EventTypePage import EventTypePage
from Masterpages.BlogCategoryPage import BlogCategoryPage
from Masterpages.BlogTagPage import BlogTagPage
from Masterpages.EventDomainPage import EventDomainPage
from Masterpages.InstitutionPage import InstitutionPage
from Masterpages.HighlightsPage import HighlightsPage
from Masterpages.EventGroupPage import EventGroupPage

from Masterpages.AgeGroupPage import AgeGroupPage
from Masterpages.RolesPage import RolesPage


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
    agegroup = AgeGroupPage(page)
    login.open(BASE_URL)

    login.check_logo()

    login.print_page_details()

    login.enter_email(EMAIL)

    login.click_submit()

    login.enter_otp(OTP)

    login.click_submit()

    dashboard.open_master()
    
    dashboard.open_EducationManagement()
    

#     dashboard.open_country()

#     country.create_country()

#     dashboard.open_state()

#     state.create_state()

#     dashboard.open_city()

#     city.create_city()
    
#     dashboard.open_EventType()
    
#     eventtype.create_EventType()
    
#     dashboard.open_BlogCategory()

#     blogcategory.create_BlogCategory()
    
#     # BlogTag
#     dashboard.open_BlogTag()
#     blogtag.create_BlogTag()
    
#     # Event Domain
#     dashboard.open_EventDomain()
#     eventdomain.create_EventDomain()
    
#     # Institution
#     dashboard.open_Institution()
#     institution.create_Institution()
    
#     # Highlights
#     dashboard.open_Highlights()
#     highlights.create_Highlights()

#     # Event Group
#     dashboard.open_EventGroup()
#     eventgroup.create_EventGroup()
      
#     # Agegroup
    # dashboard.open_AgeGroup()
    # agegroup.create_AgeGroup()
    
#     # # Roles
#     dashboard.open_Roles()
#     roles.create_Roles()


    
   
