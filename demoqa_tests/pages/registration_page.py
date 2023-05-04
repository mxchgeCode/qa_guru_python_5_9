from selene import browser, have, command
from demoqa_tests import resource

class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even
        self.submiting_form = browser.element('#example-modal-sizes-title-lg')
        self.state = browser.element('#state')
    def open(self):
        browser.open('/automation-practice-form')
    def fill_first_name(self, value):
        browser.element('[id = firstName]').type(value)
    def fill_second_name(self, value):
        browser.element('[id = lastName]').type(value)
    def fill_user_email(self, value):
        browser.element('[id = userEmail]').type(value)
    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()
    def fill_mobile(self, value):
        browser.element('[id = userNumber]').type(value)
    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--00{day}:not(.react-datepicker__day--outside-mounth)').click()
    def fill_subjects(self, subject1, subject2, subject3):
        browser.element('#subjectsInput').type(subject1).press_enter()
        browser.element('#subjectsInput').type(subject2).press_enter()
        browser.element('#subjectsInput').type(subject3).press_enter()

    def fill_hobbie(self, value1, value2):
        browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(value1)).click()
        browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(value2)).click()
    def upload_picture(self,name):
        browser.element('#uploadPicture').type(resource.path(name))
    def fill_address(self,value):
        browser.element('[id = currentAddress]').type(value)
    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
    def submit(self):
        browser.element('#submit').perform(command.js.click)
    def submiting_form_check(self,message):
        self.submiting_form.should(have.text(f'{message}'))
