from datetime import date
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling_submitting():
    student = User(
        first_name='Michael',
        last_name='Kors',
        email='Michael@Kors.com',
        genders=Gender.male.value,
        phone_number=8667095677,
        date_of_birth=date(1959, 8, 9),
        subjects=[Subject.chemistry.value, Subject.maths.value, Subject.physics.value],
        hobbies=[Hobby.sports.value, Hobby.reading.value],
        upload_filename='solution.png',
        current_address='Rodriguez side, LA 93111',
        state='Uttar Pradesh',
        city='Agra',
    )

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_have_registered(student)
