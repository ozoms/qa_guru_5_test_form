from selene.support.shared import browser
from selene import be, have
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Снимок.png')

def test_filling_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(1920, 1080)
    browser.element('#firstName').type('Sasha')
    browser.element('#lastName').type('Slod')
    browser.element('#userEmail').type('ooo@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(8467538276)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1980"]').click()
    browser.element('.react-datepicker__month-select>[value="1"]').click()
    browser.element('.react-datepicker__day--022').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('Walking street, 1')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Sasha'
                                               and 'Slod' and 'ooo@gmail.com'
                                               and 'Male' and '8467538276'
                                               and '02 February,1980' and 'Arts'
                                               and 'Sports' and 'Music'
                                               and 'Снимок.png' and 'Walking street, 1'
                                               and 'NCR' and 'Noida'))