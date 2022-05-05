# %%
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

#Create DataFrame from HTML table (read_html)
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#Assign columns to the DataFrame
df.columns=['Description', 'Mars', 'Earth']
# Make Description the Index
df.set_index('Description', inplace=True)
df


df.to_html()

#browser.quit()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
html = browser.html
hemi_soup = soup(html, 'html.parser')

# titles = hemi_soup.find_all('h3')
# for title in titles: 
#     print(title.text.strip())

# link_image = hemi_soup.select("div.description a")[0].get('href')
# browser.visit(f'https://marshemispheres.com/{link_image}')
# html = browser.html
# img_soup = soup(html, 'html.parser')
# img_url = img_soup.select_one("div.downloads ul li a").get('href')
# img_url

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemispheres = {}
    link_image = hemi_soup.select("div.description a")[i].get('href')
    browser.visit(f'https://marshemispheres.com/{link_image}')
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_url = img_soup.select_one("div.downloads ul li a").get('href')
    img_title = img_soup.select_one("h2.title").get_text()
    # Add extracts to the results dict
    hemispheres = {
        'img_url': f'https://marshemispheres.com/{img_url}',
        'title': img_title}
    
    # Append results dict to hemisphere image urls list
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    
hemisphere_image_urls

browser.quit()
