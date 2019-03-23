#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys
import pdb
import smtplib, ssl


def get_str_between_strs(string, begin_s, end_s):
    """
    given:
        string = '<li class="dept">Undergraduate Pathway</li>',
        begin_s = '"dept">'
        end_s = '>'
    
    returns:
        'Undergraduate Pathway'
    """
    # keep text between last occurence of begin_s and the end of string
    # print(string)
    second_half = string.split(begin_s)[-1]
    # keep text before end_s and after begin_s
    return second_half.split(end_s)[0]


def get_info(firstname, lastname):
    if len(sys.argv) < 2:
        print('usage: ./directory.py first_name [optional: last_name]')
        exit(1)
    str_search = '+'.join(sys.argv[1:])
    c = []  # noting if only part of name provided
    page = requests.get("http://directory.oregonstate.edu/?type=search&cn=" + str_search)

    # print("http://directory.oregonstate.edu/?type=search&cn="+str_search)
    soup = BeautifulSoup(page.text, 'html.parser')
    Student_names_info = soup.find(id='records')
    # print(Student_name_info)
    h3 = Student_names_info.find_all('h3')
    if len(h3) == 0:
        flag = 0
    else:
        flag = 1
    if flag == 1:
        name_list = []
        all_Students = []
        for i in h3:
            # print(i)
            each_Student = {}
            each_name = i.find_all('a')[0].contents[0]
            each_url = i.find_all('a', href=True)
            each_name_url = each_url[0]['href']
            name_string = ''
            for j in each_name:
                name_string = name_string + j
                # print("name:", name_string)
                name_list.append(name_string)
            each_name_page = requests.get('http://directory.oregonstate.edu/' + each_name_url)
            each_name_soup = BeautifulSoup(each_name_page.text, 'html.parser')
            each_name_info = each_name_soup.find(class_='record')
            each_name_title = each_name_info.find_all('b')
            each_name_title_info = each_name_info.find_all('dd')
            # print(each_name_soup.get_text())
            for k in range(len(each_name_title)):
                b = each_name_title[k].get_text()
                dd = each_name_title_info[k].get_text()
                each_Student[b] = dd
            # print(b)
            all_Students.append(each_Student)
        # print("in here")

        return all_Students

    # except:
    if flag == 0:
        Student = {}
        Student_name_info = soup.find(class_='record')
        bs = Student_name_info.find_all('b')
        dds = Student_name_info.find_all('dd')
        # print(bs)

        # an object (eg. student['Full Name'] = 'John Smith')
        for i in range(len(bs)):
            b = bs[i].get_text()
            dd = dds[i].get_text()
            Student[b] = dd

        return Student


def student_detail(firstname, lastname):
    Student = get_info(firstname, lastname)
    if type(Student) is list:  # multiple students
        for i in range(len(Student)):
            print_infos(Student[i])
    else:
        print_infos(Student)

    # Student_info={}
    # # print(Student)


def print_infos(Student):
    for header in Student:
        if 'Full Name' in header:
            print(header, ':', Student[header])
        elif 'Title' in header:
            print(header, ':', Student[header])
        elif 'Department' in header:
            print(header, ':', Student[header])
        elif 'Phone' in header:
            print(header, ':', Student[header])


student_detail(sys.argv[1], sys.argv[2])

# #[0][0].contents[0]
# #input directory.py Jane Kim
#
# #Name: Kim, Jane
# #Title:
# #Department :
# #Phone :

# no hits, many hits, no catagory
