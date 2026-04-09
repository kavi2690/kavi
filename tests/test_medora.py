from typing import Self

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

from EducationPages.EducationTypesPage import EducationTypesPage
from EducationPages.StagesCategoriesPage import StagesCategoriesPage
from EducationPages.SubStagesLevelPage import SubStagesLevelPage
from EducationPages.DepartmentsPage import DepartmentsPage


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
    
    educationtypes = EducationTypesPage(page)
    stagescategories = StagesCategoriesPage(page)
    substageslevel = SubStagesLevelPage(page)
    departments = DepartmentsPage(page)
    login.open(BASE_URL)

    login.check_logo()

    login.print_page_details()

    login.enter_email(EMAIL)

    login.click_submit()

    login.enter_otp(OTP)

    login.click_submit()

    # dashboard.open_master()
    
    dashboard.open_EducationManagement()
    page.wait_for_timeout(2000)
    
    
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

# education 
    # dashboard.open_EducationTypes()
    # page.wait_for_timeout(2000)
    # educationtypes.create_EducationTypes()
    
    
# stagesCategories
    
    # dashboard.open_StagesCategoriesPage()

    # stagescategories.create_StagesCategories()
    
# Substageslevel 
    
    
    # dashboard.open_SubStagesLevel()
    
    # substageslevel.create_SubStagesLevel()
   
# departments

    dashboard.open_Departments()
    
    departments.create_Departments()