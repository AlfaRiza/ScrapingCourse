from bs4 import BeautifulSoup
import requests
import time

print('Masukkan skill yang tidak ingin dicari')
unfamiliar_skill = input('>')
print(f'Hasil tanpa {unfamiliar_skill}')


def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for i, job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').text
        if 'few' in date:
            name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.find('h2').find('a')['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{i}.txt', 'w') as f:
                    f.write(f'Company Name : {name.strip()} \n')
                    f.write(f'Skill : {skills.strip()} \n')
                    f.write(f'More Info : {more_info} \n')
                print(f'File saved: {i}')

if __name__ == '__main__':
    while True:
        find_job()
        wait_time = 10
        print(f'Waiting {wait_time} minutes. . .')
        time.sleep(wait_time * 60)
