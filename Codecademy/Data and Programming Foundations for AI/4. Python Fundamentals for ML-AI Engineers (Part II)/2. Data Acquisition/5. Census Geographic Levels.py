"""
The Census website documents all the supported geographic levels with examples. As we’ve seen, using * specifies all data at that geographic level. For example, to request state-level data for all states, the API call would be: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*. You can review the output of this call by viewing the screenshot in the workspace

We can also request specific geographic regions, like states, by specifying them in a comma-separated format. For example, to request data from California and Utah, we specify their 2-digit FIPS state code (California is 06 and Utah is 49): https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:06,49.

The for parameter can also be used in conjunction with in to specify data within a certain geographic area, such as all unified school districts within specific states: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=school%20district%20(unified):*&in=state:06,49.

If you visit this URL in your browser, you can see that the NAME variable is the geographic level. The returned data will also contain additional columns at the end depending on the requested geographic level. In this case, there are 2 new columns added, identifying the 2-digit FIPS state code and 5-digit school district code for each row of data.

Instructions
Using the browser, make an API call to request state-level data containing the `NAME` variable, the total commuters count, and the count for commuters who travel 90 or more minutes for only the state of New York. (Click to Toggle Correct Answers)
Use the 2-digit FIPS state code to request data for a particular state.

Your query should look like this: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=state:36.

Make an API call to request the same 3 variables for all counties within the state of New York.
Use the for parameter in conjunction with in to request specific geographic regions.

Your query should look like this: https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36.
"""