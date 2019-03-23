#!/usr/bin/env python3

# Project - Find me a job - Web scraping
# Johnny Vang - ME 499/599
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from string import digits
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt
import time


# Indeed Query
def query_job_indeed(job_title, location):
    if type(job_title) != str:
        raise ValueError('Please input persons name with a string variable')
    job_title = job_title.replace(" ", "+")
    location = location.replace(" ", "+")
    # Query = ?type=search&cn=william+smart
    query_url = 'https://www.indeed.com/jobs?q=' + job_title + '&l=' + location
    return query_url


# Disney Query
def query_job_disney(job_title):
    if type(job_title) != str:
        raise ValueError('Please input persons name with a string variable')
    job_title = job_title.replace(" ", "%20")
    # Query = ?type=search&cn=william+smart
    # query_url = 'https://www.indeed.com/jobs?q=' + job_title + '&l='
    query_url = 'https://jobs.disneycareers.com/search-jobs?k=' + job_title
    return query_url


# ZipRecruiter Query
def query_job_zip_recruiter(job_title, location):
    if type(job_title) != str:
        raise ValueError('Please input persons name with a string variable')
    job_title = job_title.replace(" ", "+")
    location = location.replace(" ", "+")
    # Query = ?type=search&cn=william+smart
    # query_url = 'https://www.indeed.com/jobs?q=' + job_title + '&l='
    query_url = 'https://www.ziprecruiter.com/candidate/search?search=' + job_title + '&location=' + location
    return query_url


# FETCH HTTP FOR INDEED
def http_connect_indeed(job_title, location):
    query = query_job_indeed(job_title, location)
    base_query = 'https://www.indeed.com'
    print(query)
    # urlopen connects and download data from the URL
    url = urlopen(query)
    # url.read() read the data, we must store it into a variable
    html = url.read()
    # html parsing, stores everything into different variables
    soup = BeautifulSoup(html, 'html.parser')
    job_list = []
    company_list = []
    location_list = []
    href_list = []
    # This grabs all the job descriptions
    for jobs in soup.find_all('div', {'class': 'jobsearch-SerpJobCard'}):
        # print(jobs.a["title"])
        job_list.append(jobs.a["title"])
    # This grabs all the company names
    for company in soup.find_all('span', {'class': 'company'}):
        # print(locations.get_text())
        good = company.get_text().split()
        better = ""
        for words in good:
            better = better + words + " "
        company_list.append(better)
    # This grabs all the href, but they do not work
    for jobs in soup.find_all('div', {'class': 'jobsearch-SerpJobCard'}):
        href_list.append(base_query + jobs.a["href"])

    for locations in soup.find_all('div', {'class': 'jobsearch-SerpJobCard'}):
        # print(jobs.a["title"])
        # print(locations.div.get_text())
        # words = filter(lambda x: x.isalpha(), locations.div.get_text().replace("reviews", "/"))
        words = locations.div.get_text().replace("reviews", "-- Location:")
        new_words = re.sub("\d+", " ", words).split()
        # print(len(new_words))
        combo = "Company Name: "
        for i in new_words:
            combo = combo + '{}'.format(i) + " "
        location_list.append(combo)
    return (job_list, company_list, location_list, href_list)


# FETCH HTTP FOR DISNEY
def http_connect_disney(job_title):
    query = query_job_disney(job_title)
    print(query)
    base_query = 'https://jobs.disneycareers.com'
    # urlopen connects and download data from the URL
    url = urlopen(query)
    # url.read() read the data, we must store it into a variable
    html = url.read()
    # html parsing, stores everything into different variables
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    job_list = []
    company_list = []
    location_list = []
    href = []
    i = 1
    for jobs in soup.find_all('tr'):
        if i == 1:
            i = i + 1
            continue
        href.append(base_query + jobs.a["href"])
        job_list.append(jobs.h2.get_text())
    for companys in soup.find_all('span', {'class': 'job-brand'}):
        company_list.append(companys.get_text())
    for locations in soup.find_all('span', {'class': 'job-location'}):
        location_list.append(locations.get_text())
    # combo = tuple(job_list, href, company_list, location_list)
    return (job_list, href, company_list, location_list)


# ZIP RECRUITER GIVES ME A ---HTTP Error 403: Forbidden
def http_connect_zip_recruiter(job_title, location):
    query = query_job_zip_recruiter(job_title, location)
    print(query)
    base_query = 'https://www.ziprecruiter.com'
    # urlopen connects and download data from the URL
    # HTTP Error 403: Forbidden
    # fix error - https://stackoverflow.com/questions/13055208/httperror-http-error-403-forbidden
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(query, headers=hdr)
    url = urlopen(req)
    # url.read() read the data, we must store it into a variable
    html = url.read()
    # html parsing, stores everything into different variables
    soup = BeautifulSoup(html, 'html.parser')
    job_list = []
    company_list = []
    location_list = []
    href = []
    for jobs in soup.find_all('span', {'class': 'just_job_title'}):
        job_list.append(jobs.get_text())
    for companies in soup.find_all('a', {'class': 't_org_link name'}):
        company_list.append(companies.get_text())
    for locations in soup.find_all('a', {'class': 't_location_link location'}):
        location_list.append(locations.get_text())
    for hrefs in soup.find_all('a', {'class': 'job_link t_job_link'}):
        href.append(hrefs["href"])
    return (job_list, href, company_list, location_list)


if __name__ == '__main__':
    job_query = input('Please enter the type of job you want to search: ')
    location = input('Please enter the location you want to work at: ')
    rolling_list = []
    # ------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------  INDEED QUERY     ------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    soup_indeed = http_connect_indeed(job_query, location)
    super_list_indeed = "\n\n" + "-----------------------------JOBS FROM INDEED:----------------------------------" + "\n"
    # print('-----------------------------JOBS FROM INDEED:----------------------------------')
    for iter in range(len(soup_indeed[0])):
        job = 'Job Description: {}'.format(soup_indeed[0][iter])
        if job in rolling_list:
            continue
        rolling_list.append(job)
        # company = 'Company: {}'.format(soup[1][iter])
        company_location = soup_indeed[2][iter]
        href = soup_indeed[3][iter]
        super_list_indeed = super_list_indeed + job + '\n' + company_location + '\n' + href + '\n\n'
        # print('Job Description: {}'.format(soup[0][iter]))
        # print('Company: {}'.format(soup[1][iter]))
        # print('\n')
    print(super_list_indeed)
    if super_list_indeed == "\n\n" + "-----------------------------JOBS FROM INDEED:----------------------------------" + "\n":
        raise ValueError('No Jobs found, please try again')
    # ------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------  DISNEY QUERY     ------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    soup_disney = http_connect_disney(job_query)
    super_list_disney = "\n\n" + "-----------------------------JOBS FROM DISNEY:----------------------------------" + "\n"
    for iter2 in range(len(soup_disney[0])):
        job2 = 'Job Description: {}'.format(soup_disney[0][iter2])
        if job2 in rolling_list:
            continue
        rolling_list.append(job2)
        # company = 'Company: {}'.format(soup[1][iter])
        href = soup_disney[1][iter2]
        company_list = 'Company Name: {}'.format(soup_disney[2][iter2])
        location_list = 'Location: {}'.format(soup_disney[3][iter2])
        super_list_disney = super_list_disney + job2 + '\n' + company_list + '\n' + location_list + '\n' + href + '\n\n'
        # print('Job Description: {}'.format(soup[0][iter]))
        # print('Company: {}'.format(soup[1][iter]))
        # print('\n')
    print(super_list_disney)
    if super_list_indeed == "\n\n" + "-----------------------------JOBS FROM DISNEY:----------------------------------" + "\n":
        print('NO JOBS FOUND FROM DISNEY')
    # ------------------------------------------------------------------------------------------------------------------
    # -------------------------------------   ZIP-RECRUITER QUERY     --------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    soup_zip = http_connect_zip_recruiter(job_query, location)
    super_list_zip = "\n\n" + "-----------------------------JOBS FROM ZIP-RECRUITER:----------------------------------" + "\n"
    # # print('-----------------------------JOBS FROM INDEED:----------------------------------')
    for iter3 in range(len(soup_zip[0])):
        job3 = 'Job Description: {}'.format(soup_zip[0][iter3])
        if job3 in rolling_list:
            continue
        rolling_list.append(job3)
        # company = 'Company: {}'.format(soup[1][iter])
        href2 = soup_zip[1][iter3]
        company_list2 = 'Company Name: {}'.format(soup_zip[2][iter3])
        location_list2 = 'Location: {}'.format(soup_zip[3][iter3])
        super_list_zip = super_list_zip + job3 + '\n' + company_list2 + '\n' + location_list2 + '\n' + href2 + '\n\n'
        # print('Job Description: {}'.format(soup[0][iter]))
        # print('Company: {}'.format(soup[1][iter]))
        # print('\n')
    print(super_list_zip)
    if super_list_zip == "\n\n" + "-----------------------------JOBS FROM ZIP-RECRUITER:----------------------------------" + "\n":
        print('NO JOBS FOUND FROM ZIP RECRUITER')
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------EMAIL MYSELF------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    sender_email = "joniwoni92@gmail.com"
    receiver_email = "joniwoni92@gmail.com"
    password = input("To receive an email, please type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Job List Via Python"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Here are your jobs!
    """ + super_list_indeed \
           + super_list_disney \
           + super_list_zip

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
            server.quit()
    except:
        raise ValueError('Invalid Password. Please try again.')
    # ------------------------------------------------------------------------------------------------------------------

    # try:
    #     send_time = dt.datetime(2019, 3, 22, 5, 0, 0)  # set your sending time in UTC
    #     time.sleep(send_time.timestamp() - time.time())
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #         server.login(sender_email, password)
    #         server.sendmail(
    #             sender_email, receiver_email, message.as_string()
    #         )
    #         server.quit()
    # except:
    #     raise ValueError('Invalid Password. Please try again.')
    #
    # first_email_time = dt.datetime(2018, 8, 26, 3, 0, 0)  # set your sending time in UTC
    # interval = dt.timedelta(minutes=2 * 60)  # set the interval for sending the email
    #
    # send_time = first_email_time
    # while True:
    #     send_email_at(send_time)
    #     send_time = send_time + interval
    #
    # while the list was not equal to new one, it would be fine.....keeep running in background