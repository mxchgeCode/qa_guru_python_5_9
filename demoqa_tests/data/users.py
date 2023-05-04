import dataclasses
from datetime import datetime, date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    accounting = 'Accounting'
    arts = 'Arts'
    biology = 'Biology'
    english = 'English'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    commerce = 'Commerce'
    maths = 'Maths'
    physics = 'Physics'
    economics = 'Economics'
    social_studies = 'Social Studies'



class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    genders: List[Gender]
    phone_number: int
    date_of_birth: date
    # birth_year: str
    # birth_month: str
    # birth_day: str
    subjects: List[Subject]
    hobbies: List[Hobby]
    upload_filename: str
    current_address: str
    state: str
    city: str