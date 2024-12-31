"""
The Census Data API provides a fast and simple way to access its data. To query the ACS 5-year data, a request should be made to https://api.census.gov/data/2020/acs/acs5 specifying the 
Preview: Docs Loading link description
variables
 to fetch and the geographic level you want. For example, an API call requesting the total population count of commuters (B08303_001E) at the state level would look like this: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*.

Visit this URL in a new tab on your browser to see how the data is returned. A graphic of the API response is also included in the workspace.

The part of the URL after ? contains the query parameters, each parameter is separated by &.

The get parameter specifies a comma-separated list of variables we want to fetch
NAME is the name of the geographic level
B08303_001E is the number of commuters
The for parameter specifies the geographic level
we are requesting state-level data
and we want all states, as indicated by the *.
Looking through the data, you may have also noticed an extra column of data at the end. This is automatically generated and is the code for geographic level of the data. In this case, the last column contains the 2-digit FIPS state code.

A final note about requesting variables is that you can choose to request an entire variable group as well. For example, since we are looking at commute time, if we wanted to request all variables in the Time to Work B08303 group at the state-level, the API query would be:

https://api.census.gov/data/2020/acs/acs5?get=NAME,group(B08303)&for=state:*.

Note the differences with our original query:

https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*

Requesting by variable group will return all the variables in that group, annotations and 
Preview: Docs Loading link description
errors
 included, no matter how many there are.

API Call 1

Using the browser in another tab on your web browser, make an API call to request state-level data containing:

The NAME variable,
The total number of commuters, and
The count for commuters who travel less than 5 minutes.
Find the appropriate variables to request in the B08303 variable group documentation.

API Call 2

This time, make an API call to request state-level data containing:

The NAME variable,
The total commuters count, and
The count for commuters who travel 90 or more minutes.
API Call 1 (Click to Toggle Correct Answers)
Your query should look like this: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_002E&for=state:*

API Call 2
Your query should look like this: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=state:*
"""