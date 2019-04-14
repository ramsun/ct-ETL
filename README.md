# ct-ETL
---

## Purpose: 
Perform ETL process on location data from clinicaltrials.gov and bmsstudyconnect.com to compare locations available on each site.  This project aims to scrape location data from a given trial url and store the data in a MongoDB database.   

## Data Sources:
- Clinicaltrials.gov (XML)
- bmsstudyconnect.com (HTML)

## Data Scraped:
- Status (recruiting or not)
- Location (city and zip-code)
- Trial ID (research tag)

## Tools Used
- Jupyter Notebook (Python IDE)
- BeautifulSoup (HTML parser)
- PyMongo (MongoDB ORM)
- chromedriver.exe (Driver for asynchronous parsing)
- Selenium (Allows for asynchronous parsing control in Python)

## Database Considerations:
We considered a  is useful for warehousing data sets that will be growing over time.  A nested json structure will be easier to work with as we continue to collect location data for different research tags from different websites.

The database collections are named as the website name the data was scraped from.  The final output of the databases as shown from mongo Shell are shown bellow:
### ClinicalTrials.gov and BMS Study Connect mongo Shell output:
![Database Ouput](readme_assets/collection.png)

## Transformation Process for each website:
### BMS Study connect:


### ClinicalTrials.gov:
1. Using requests and beautiful soup we pulled data using ct.gov URL by nctID.
2. Appended site name, recruiting status, city, and zip to dictionary Loaded records into a json.
3. Using a for loop records were inserted row by row into MongoDB.

#### Code snippet for extraction process:
Bellow is a code snippet of the function used to extract from ClinicalTrials.gov:
'''python
Input: Research id used for querying from clinicaltrials.gov
Ouput: Returns a dictionary of lists of cleaned XML site data
Purpose: Function takes a nctid string as input and ouputs cleaned XML data. The nctid is querried in the website using the request.get(URL) method. This queried xml is loaded into a soup object, which is then used to parse the xml into the "data" dictionary list object.
def clinicalTrialsGov(nctid):
    
    # Initialize dictionary list
    data = defaultdict(list)
    
    # Load XML into soup object
    soup = BeautifulSoup(requests.get("https://clinicaltrials.gov/ct2/show/"\
                                    + nctid + "?displayxml=true").text, "xml")
    
    # Create list of tags that will be scraped from the "soup" object
    subset = ['name','status','city', 'zip']
    
    # Find all subset tags in the soup object
    for tag in soup.find_all(subset):
        # Transform the found location data and put into the "data" object
        data['ct{}'.format(tag.name.capitalize())].append(tag.get_text(strip=True))
    
    # Return the "data" object
    return data

Create a dictionary of scraped data for the NCT01592370 tag
data = clinicalTrialsGov('NCT01592370')
'''



 




