from xml.dom.minidom import Element
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import json
import time
from collections import defaultdict


word_collection = set({'product',
'products',
'pipeline',
'drugs',
'drugs',
'our-drugs',
'medicine'
'medicines',
'our-medicine',
'our-medicines',
'pharmaceuticals',
'clinical trials',
'clinical trial',   
'clinical-trial',
'clinical-trials',
'chemistry',
'biology',
'small molecule',
'small-molecule',
'small-molecules',
'small-molecules',
'biologics',
'biosimilar',
'biosimilars',
'drug-product',
'drug-products',
'discovery',
'drug-discovery',
'drug_discovery',
'drug-development',
'drug_development',
'product-development',
'product_development',
'science',
'sciences',
'our-science',
'scientific-discovery',
'scientific discovery',
'research-and-discovery',
'research-and-development',
'research and development',
'r&d',
'research',
'clinical-research',
'clinical research',
'clinical-science',
'clinical-sciences',
'oncology',
'immunology',
'virology',
'neuroscience',
'neurology',
'immno',
'onco',
'eye-care',
'eye care',
'derm',
'medical-aesthetics',
'dermal',
'analgesic',
'analgesics'
'genetics',
'genomics',
'genome',
'proteome',
'biomarker',
'biomarkers',
'degradomer',
'degradomers',
'gastroenterology',
'cardiovascular',
'cardiology',
'antibody',
'antibodies',
'ADC',
'antibody-drug-conjugate',
'conjugate-drug',
'conjugate-drugs',
'bispecific-drugs',
'therapeutics',
'therapies', 
'partnerships',
'partner',
'collaborations', 
'about',
'case',
'case-studies',
'news'})

driver = webdriver.Chrome((ChromeDriverManager().install()))


# categories = driver.find_element(By.XPATH,value ='//*[@id="container-c987c4bac5"]/div[3]/div/div/div/div[2]/div/div[1]/ul')
# print(categories.text)
def get_body(driver):
    element = driver.find_element(By.XPATH, "/html/body")
    time.sleep(5)
    # content = re.sub('\n', ' ', element.text)
    # string = content.encode("utf-8")
    # print(element.text)
    content = element.text
    content = re.sub('\n', ' ', content)
    print(content)

    return content

crawlingSites = [
['novatis','https://www.novartis.com/'], 
['eli lilly','https://www.lilly.com/'],
['janssen','https://www.janssen.com/'],
['amgen', 'https://www.amgen.com/'], 
['pfizer','https://www.pfizer.com/'],
['gsk','https://www.gsk.com'], 
['biogen','https://www.biogen.com'],
['abbvie', 'https://www.abbvie.com/'],
['jazz Pharmaceuticals', 'https://www.jazzpharma.com/'],
['prothena','https://www.prothena.com/'],
['roivant','https://www.roivant.com/'],
['polaris QB','https://www.polarisqb.com/'],
['Max BioPharma', 'https://www.maxbiopharma.com/'],
['Lex Pharma','https://www.lexpharma.com/'],
['Asceneuron','https://www.asceneuron.com'],
['Denali Therapeutics','https://www.denalitherapeutics.com'],
['Acimmune','https://www.acimmune.com'],
['Ribontx','https://www.ribontx.com']]

crawlingSite = [
['novartis','https://www.novartis.com/about/products']
]


# define depth of crawling to be 2 so only limited number of site are being crawled.
# iteration = 2
# for sourceSite in crawlingSites:
#     websitesList = [(None, sourceSite)]
#     # visited sets to keep track of visited sites
#     visited = set()
#     # traverse 2 links
#     for i in range(iteration):
#         newList = []
#         for parent, website in websitesList:
#             print('parent: ', parent, 'site: ', website)
#             driver.get(website)
#             linksIterator = driver.find_elements(By.TAG_NAME, value = 'a')
#             # create json data instance
#             data = {}
#             data['parent'] = parent
#             data['url'] = website
#             data['body'] = get_body(driver)
#             json_data = json.dumps(data)
#             file = open('abbvieSite', 'a')
#             file.write(json_data)
#             file.close()

#             for link in linksIterator:
#                 extractLink = str(link.get_attribute('href'))
#                 # make sure the new site is the child of the previous link and hasn't been visited yet
#                 if extractLink.startswith(sourceSite) and extractLink not in visited:
#                     newList.append((website, extractLink))
#                     visited.add(extractLink)
#         websitesList = newList
        
#     # print(websitesList)
#     print('-----------------------')

# loop through each site
store = defaultdict(int)
website_list = set()
for name, sourceSite in crawlingSite:
    start_time = time.time()
    # driver = webdriver.Chrome((ChromeDriverManager().install()))
    driver.get(sourceSite)
    linksIterator = driver.find_elements(By.TAG_NAME, value = 'a')
    # create json data instance
    data = {}
    data['body'] = get_body(driver)
    file = open('./contents/' + name + '.txt', 'a')
    file.write(data['body'])
    file.close()
    # print(name, ' execution time: ', time.time() - start_time)
    # num = 0

    

    for link in linksIterator:
        extractLink = str(link.get_attribute('href'))
        if extractLink in website_list: continue
        if extractLink and extractLink[-1] == '/':
            extractLink = extractLink[:-1]
        # print(extractLink.split('/')[-1])
        # print(re.split('[-/]', extractLink))
        search = False
        for word in re.split('[-/]', extractLink):
            if word in word_collection and extractLink not in website_list:
                print(extractLink)
                website_list.add(extractLink)
                break
        
    

        
    # print(websitesList)
    # driver.close()
    # print('-----------------------')
    sorted(store.items(), key=lambda x: x[1], reverse=True)
print(website_list)

