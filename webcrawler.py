import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import requests
# from flask import Flask, jsonify, request

# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "service on"
def checkhyperlink(url):

    chrome_options = webdriver.ChromeOptions()

    chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
    CHROMEDRIVERLOC = "D:\\UBUNTU SERVER SKRIPSI\chromedriver.exe"

    WINDOW_SIZE = "1920,1080" 
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE) 
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument('--ignore-certificate-errors')
 
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERLOC, options=chrome_options)


    # driver = webdriver.Chrome(executable_path=r'D:\UBUNTU SERVER SKRIPSI\chromedriver.exe')
    string = url
    driver.get(string)

    ### split url into domain by / ###

    list_string = string.split("/")

    if 'www' in list_string[2]:
        domain = list_string[2].split(".")
        domain = str(domain[1]) + "." + str(domain[2])
    else:
        domain = list_string[2]


    internal_count = 0
    external_count = 0
    nullhyperlink_count = 0
    internal_redirect_count = 0
    external_redirect_count = 0
    internal_error_count = 0
    external_error_count = 0
    F1 = 0
    F2 = 0
    F3 = 0
    F4 = 0
    F5 = 0
    F6 = 0 
    F7 = 0
    F8 = 0
    F9 = 0
    F10 = 0
    F11 = 0
    F12 = 0

    ### koefisien F1-F12 ###
    ko1 = -0.017236
    ko2 = 23.231230
    ko3 = 2.327730
    ko4 = 1.914151
    ko5 = 20.263021
    ko6 = 2.515211
    ko7 = 0.149838
    ko8 = 0.826801
    ko9 = 2.089872
    ko10 = 0.222953
    ko11 = 5.445638
    ko12 = 2.910151
    kointercept = -3.714364
    e = 2.718281

    links_body = driver.find_elements(By.TAG_NAME, 'a')
    links_head = driver.find_elements(By.TAG_NAME, 'link')
    links_img = driver.find_elements(By.TAG_NAME, 'img')
    links_script = driver.find_elements(By.TAG_NAME, 'script')
    forms = driver.find_elements(By.TAG_NAME, 'form')

    # F1 and F2 (total hyperlink and no hyperlink feature)
    total_link = len(links_body) + len(links_head) + len(links_img)
    
    print("total link = " + str(total_link))

    F1 = total_link
    if F1 > 0 :
        F2 = 0
    elif F1 == 0:
        F2 = 1
    
    # F3 and F4 (internal and external hyperlink feature)
    for link in links_body:
    
        try:
            if re.findall(domain, str(link.get_attribute("href"))):
                internal_count += 1
            else:
                external_count += 1
        except:
            continue

    for link in links_img:
    
        check_img = link.get_attribute("src")
        try:
            if re.findall(domain, check_img):
                internal_count += 1
            else:
                external_count += 1
        except:
            continue
    
    print("internal hyperlink = " + str(internal_count))
    print("external hyperlink = " + str(external_count))

    if total_link == 0:
        ratio_internal = 0
        ratio_external = 0
    else :
        ratio_internal = internal_count / total_link
        ratio_external = external_count / total_link

    if ratio_internal < 0.5 : 
        F3 = 1
    else :
        F3 = 0

    if ratio_external > 0.5 :
        F4 = 1
    else :
        F4 = 0
    
    # F5 (null hyperlink feature)
    for link in links_body:
        try :
            if str(link.get_attribute("href")) == "":
                nullhyperlink_count += 1
                continue
            if str(link.get_attribute("href")).endswith('#'):
                nullhyperlink_count += 1
                continue
            if re.findall('#', link.get_attribute("href")):
                nullhyperlink_count += 1
                continue
            if re.findall("javascript:void", str(link.get_attribute("href"))) or re.findall("javascript: void", str(link.get_attribute("href"))):
                nullhyperlink_count += 1
                continue
        except:
                continue
    
    print("null hyperlink = " + str(nullhyperlink_count))
    
    if total_link == 0:
        ratio_null = 0
    else :
        ratio_null = nullhyperlink_count / total_link
    
    if ratio_null > 0.34 :
        F5 = 1
    else :
        F5 = 0

    # F6 (internal / external CSS feature)
    csschecker = ".css"

    for css in links_head:
        if re.findall(csschecker, str(css.get_attribute("href"))):
            if re.findall(domain, str(css.get_attribute("href"))):
                F6 = 0
            else:
                F6 = 1
                break

    # F7 and F8 (internal and external redirection)
    for link in links_body:
        try:
            if re.findall(domain, str(link.get_attribute("href"))):
                redirect = requests.get(link.get_attribute("href"))
                if redirect.status_code == 301 or redirect.status_code == 302:
                    internal_redirect_count += 1
                    continue
            else:
                redirect = requests.get(link.get_attribute("href"))
                if redirect.status_code == 301 or redirect.status_code == 302:
                    external_redirect_count += 1
                    continue
        except:
            continue
    
    for link in links_img:
        try:
            if re.findall(domain, str(link.get_attribute("src"))):
                redirect = requests.get(link.get_attribute("src"))
                if redirect.status_code == 301 or redirect.status_code == 302:
                    internal_redirect_count += 1
                    continue
            else:
                redirect = requests.get(link.get_attribute("src"))
                if redirect.status_code == 301 or redirect.status_code == 302:
                    external_redirect_count += 1
                    continue
        except:
            continue

    if internal_count > 0:
        F7 = internal_redirect_count / internal_count
    elif internal_count == 0 :
        F7 = 0

    if external_count > 0:
        F8 = external_redirect_count / external_count
    elif external_count == 0 :
        F8 = 0
    
    # F9 and F10 (internal and external error)
    for link in links_body:
        try:
            if re.findall(domain, str(link.get_attribute("href"))):
                error = requests.get(link.get_attribute("href"))
                if error.status_code == 403 or error.status_code == 404:
                    internal_error_count += 1
                    continue
            else:
                error = requests.get(link.get_attribute("href"))
                if error.status_code == 403 or error.status_code == 404:
                    external_error_count += 1
                    continue
        except:
            continue

    for link in links_img:
        try:
            if re.findall(domain, str(link.get_attribute("src"))):
                error = requests.get(link.get_attribute("src"))
                if error.status_code == 403 or error.status_code == 404:
                    internal_error_count += 1
                    continue
            else:
                error = requests.get(link.get_attribute("src"))
                if error.status_code == 403 or error.status_code == 404:
                    external_error_count += 1
                    continue
        except:
            continue

    if internal_count > 0:
        F9 = internal_error_count / internal_count
    elif internal_count == 0 :
        F9 = 0

    if external_count > 0:
        F10 = external_error_count / external_count
    elif external_count == 0 :
        F10 = 0

    # F11 (login form link feature)
    for form in forms:
        check_form = form.get_attribute("action")
        print(check_form)
        if check_form == "":
            F11 = 1
            break
        if check_form.endswith('#'):
            F11 = 1
            break
        if re.findall("#", check_form):
            F11 = 1
            break
        if re.findall("javascript:void", check_form) or re.findall("javascript: void", check_form):
            F11 = 1
            break
        if check_form.endswith('.php'):
            F11 = 1
            break
        if re.findall(domain, check_form):
            F11 = 0
        else:
            F11 = 1
    
    # F12 (internal / external favicon feature)
    faviconchecker = ".ico"

    for favicon in links_head:
        if re.findall(faviconchecker, str(favicon.get_attribute("href"))):
            if re.findall(domain, str(favicon.get_attribute("href"))):
                F12 = 0
            else:
                F12 = 1
                break
        else:
            F12 = 0


    print("F1 =" + str(F1))
    print("F2 =" + str(F2))
    print("F3 =" + str(F3))
    print("F4 =" + str(F4))
    print("F5 =" + str(F5))
    print("F6 =" + str(F6))
    print("F7 =" + str(F7))
    print("F8 =" + str(F8))
    print("F9 =" + str(F9))
    print("F10 =" + str(F10))
    print("F11 =" + str(F11))
    print("F12 =" + str(F12))


    #classifier using logistic regression


    classifier = kointercept+(ko1*F1)+(ko2*F2)+(ko3*F3)+(ko4*F4)+(ko5*F5)+(ko6*F6)+(ko7*F7)+(ko8*F8)+(ko9*F9)+(ko10*F10)+(ko11*F11)+(ko12*F12) 

    probability = 1 / (1 + (e ** -(classifier)))

    print("Probability = " + str(probability))

    if probability < 0.5:
        return "no phishing"
    else:
        return "phishing"

    # driver.quit()
