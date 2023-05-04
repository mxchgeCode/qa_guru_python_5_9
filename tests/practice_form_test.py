from selene import have
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import Subject, Hobby

def test_successful_input_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Michael')
    registration_page.fill_second_name('Kors')
    registration_page.fill_user_email('Michael@Kors.com')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile('8667095677')
    registration_page.fill_date_of_birth('9', 'August', '1959')
    registration_page.fill_subjects(Subject.chemistry.value, Subject.maths.value, Subject.physics.value )
    registration_page.fill_hobbie(Hobby.sports.value, Hobby.reading.value)
    registration_page.upload_picture('solution.png')
    registration_page.fill_address("Rodriguez side, LA 93111")
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')

    registration_page.submit()

    # THEN
    registration_page.submiting_form_check('Thanks for submitting the form')
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Michael Kors',
            'Michael@Kors.com',
            'Male',
            '8667095677',
            '09 August,1959',
            'Chemistry, Maths, Physics',
            'Sports, Reading',
            'solution.png',
            'Rodriguez side, LA 93111',
            'Uttar Pradesh Agra'
        )
    )
