# Mission to Mars

# Overview

The challenge was to create a webpage that can scrape, or collect, information for a variety of websites and make a summary page. 

# Process
Use BeautifulSoup, Splinter, and Pandas to scrape five different webpages related to Mars, and display the results on a webpage using MongoDB and Flask.

1. Scraping the Mars Data
 - Using Jupyter Notebook to test the code
 - Conncected to https://redplanetscience.com 
 - Pulled the first, or most recent news article
 - Also collected the summary paragraph

2. Scraping the Featured Mars Images
 - Connected to the website https://spaceimages-mars.com
 - Selected the featured image
 - Naviated to the URL for the image and downloaded the image

3. Scraping the Mars Facts
 - Using the website https://galaxyfacts-mars.com
 - Made a dataFrame in Pandas with the columns and descrption of facts about Mars

4. Scraping the Mars Hemispheres
 - Using the website https://marshemispheres.com
 - Selected the 4 images of the hemispheres of mars along with their titles. 
 - Navigated to the secondary pages on the website to the get full resolution image of each

5. Connecting images and information
 - Using Mongo databases, the stored information were collected into a database
 - Using Flask,  made routes to connect the scraped data
 - Using Bootstrap made the website customized. 

<img width="783" alt="MissiontoMars" src="https://user-images.githubusercontent.com/98054953/167322400-afe82050-d261-4d17-9e19-18024a211a4e.png">

# Summary

The customized website provides the requested information.  It includes a "Scrape New Data" button which allows the user to update the website with the click of a button. 

