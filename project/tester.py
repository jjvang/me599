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


def query_job_zip_recruiter(job_title, location):
    if type(job_title) != str:
        raise ValueError('Please input persons name with a string variable')
    job_title = job_title.replace(" ", "+")
    location = location.replace(" ", "+")
    # Query = ?type=search&cn=william+smart
    # query_url = 'https://www.indeed.com/jobs?q=' + job_title + '&l='
    query_url = 'https://www.ziprecruiter.com/candidate/search?search=' + job_title + '&location=' + location
    return query_url


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
    # print(soup.prettify())
    # container = soup.find_all('div', {'class': 'records'})
    # jobs = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
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
        href.append(base_query + hrefs["href"])

    return (job_list, href, company_list, location_list)


if __name__ == '__main__':
    # query = query_job2('robotics intern')
    # need to add a parameter where it has a bad query
    # looks like div tag with class "bad query"
    # grab the li tag
    # print(query)
    # job_query = input('Please enter the type of job you want to search: ')
    # location = input('Please enter the location you want to work at: ')
    # soup_zip = http_connect_zip_recruiter('robotics', 'california')
    # super_list_zip = "\n\n" + "-----------------------------JOBS FROM ZIP-RECRUITER:----------------------------------" + "\n"
    # # # print('-----------------------------JOBS FROM INDEED:----------------------------------')
    # for iter3 in range(len(soup_zip[0])):
    #     job2 = 'Job Description: {}'.format(soup_zip[0][iter3])
    #     # company = 'Company: {}'.format(soup[1][iter])
    #     href2 = soup_zip[1][iter3]
    #     company_list2 = 'Company Name: {}'.format(soup_zip[2][iter3])
    #     location_list2 = 'Location: {}'.format(soup_zip[3][iter3])
    #     super_list_zip = super_list_zip + job2 + '\n' + company_list2 + '\n' + location_list2 + '\n' + href2 + '\n\n'
    #     # print('Job Description: {}'.format(soup[0][iter]))
    #     # print('Company: {}'.format(soup[1][iter]))
    #     # print('\n')
    # print(super_list_zip)
    a = ['hello', 'comobo']
    if 'comobo' in a:
        print('yes')
    else:
        print('no')
