import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_form_submission(times):
    service = Service("D:\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjzYV0T625DOK_feaYDhzv1YNYq8lw6XZqEwVN3o16xA_c8g/viewform"
    
    for _ in range(times):
        driver.get(form_url)
        time.sleep(2)
        
        try:
            select_age_and_education(driver, wait)
            handle_dependent_questions(driver, wait)
            fill_remaining_questions(driver, wait)
            ensure_questions_answered(driver, [4, 10, 15, 24])
            
            submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
            submit_button.click()
            
            # Random delay between submissions (30 sec to 10 min)
            delay = random.randint(30, 200)
            time.sleep(delay)
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            continue

    driver.quit()

def select_age_and_education(driver, wait):
    age_options = [
        ('Under 18', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label'),
        ('18-24', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label'),
        ('25-34', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label'),
    ]

    education_mapping = {
        'Under 18': ['College','High school'],
        '18-24': ['College', 'Undergraduate'],
        '25-34': ['Postgraduate'],
    }

    selected_age = random.choice(age_options)
    age_element = wait.until(EC.element_to_be_clickable((By.XPATH, selected_age[1])))
    age_element.click()
    time.sleep(1)
    
    valid_educations = education_mapping[selected_age[0]]
    education_xpaths = {
        'High school': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label',
        'College': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label',
        'Undergraduate': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label',
        'Postgraduate': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label',
    }
    
    selected_education = random.choice(valid_educations)
    education_element = wait.until(EC.element_to_be_clickable((By.XPATH, education_xpaths[selected_education])))
    education_element.click()
    time.sleep(1)

def handle_dependent_questions(driver, wait):
    heard_about_cp = random.choice(['Yes', 'No'])
    heard_about_cp_xpath = {
        'Yes':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label',
        'No': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label'
    }
    
    heard_element = wait.until(EC.element_to_be_clickable((By.XPATH, heard_about_cp_xpath[heard_about_cp])))
    heard_element.click()
    time.sleep(1)

    if heard_about_cp == 'No':
        participation_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label'
    else:
        participation_xpath = random.choice([
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]/label'
        ])
        
    participation_element = wait.until(EC.element_to_be_clickable((By.XPATH, participation_xpath)))
    participation_element.click()
    time.sleep(1)

def fill_remaining_questions(driver, wait):
    questions_xpaths = {
        4: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
        ],
        5: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[6]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[7]/label/div/div[2]/div/span',
        ],
        6: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        ],
        7: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span',
        ],
        8: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        ],
        9: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        ],
        10: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        ],
        11: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        ],
        12: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        ],
        13: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
        ],
        14: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
        ],
        15: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span', 
        ],
        16: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        ],
        17: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        ],
        18: [
            
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        ],
        19: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        ],
        20: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        ],
        21: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span',
        ],
        22: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        ],
        23: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        ],
        24: [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div',
        ],
    }

    for question in [5, 7, 13, 14, 16, 19, 20, 21, 22, 23]:
        try:
            xpaths = questions_xpaths[question]
            select_multiple_options(driver, wait, xpaths)
        except Exception as e:
            print(f"Error on question {question}: {str(e)}")
            continue

    for question, xpaths in questions_xpaths.items():
        try:
            if question not in [5, 7, 13, 14, 16, 19, 20, 21, 22, 23]:
                if question == 24:
                    if random.random() < 0.7:
                        fill_random_field(driver, wait, xpaths)
                else:
                    fill_random_field(driver, wait, xpaths)
        except Exception as e:
            print(f"Error on question {question}: {str(e)}")
            continue

def select_multiple_options(driver, wait, xpaths):
    num_options = random.randint(2, len(xpaths))
    selected_options = random.sample(xpaths, num_options)
    for xpath in selected_options:
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            time.sleep(0.5)
        except:
            continue

def fill_random_field(driver, wait, xpaths):
    for _ in range(2):
        try:
            xpath = random.choice(xpaths)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            time.sleep(0.5)
        except:
            continue

def ensure_questions_answered(driver, questions):
    for question in questions:
        try:
            question_div = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]'
            selected = driver.find_elements(By.XPATH, f"{question_div}//div[contains(@class, 'isChecked')]")
            
            if not selected:
                options = driver.find_elements(By.XPATH, f"{question_div}//div[contains(@role, 'radio')]")
                if options:
                    random.choice(options).click()
                    time.sleep(0.5)
        except:
            continue
print(" ")
print("Each form will be submitted randomly between 30 seconds to 10 minutes after the previous one.")
print(" ")
if __name__ == "__main__":
    times_to_run = int(input("How many times do you want to run the form submission? : "))
    run_form_submission(times_to_run)