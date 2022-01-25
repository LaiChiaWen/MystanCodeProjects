"""
File: extension.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        items = soup.find_all('td')     # List(str)
        items_1 = items[1:len(items)-2]
        lst = []
        l_b = []
        l_g = []
        for item in items_1:
            lst.append(item.string)
        for i in range(len(lst)):
            if i % 5 == 2:
                new_lst = lst[i].replace(',', '')
                l_b.append(int(new_lst))
            if i % 5 == 4:
                new_lst = lst[i].replace(',', '')
                l_g.append(int(new_lst))
        total_boy = sum(l_b)
        total_girl = sum(l_g)

        print("Male Number: " + str(total_boy))
        print("Female Number: " + str(total_girl))


if __name__ == '__main__':
    main()
