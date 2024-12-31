"""
Exploring Census variables
3 min
Imagine you are curious about the average commute time to work in the U.S. and want to compare it across different regions. Whenever you develop a new research question you want to investigate, the very first thing you’ll need to do is collect the data!

commute

In this lesson, we will explore an example of acquiring secondary data using an API and converting between different data formats. At the end, we will also look at how to simulate our own dataset.

To answer our question about commute time to work, we will be using Census data, specifically the American Community Survey (ACS) 5-year estimates. There is a group of 
Preview: Docs Loading link description
variables
, B08303, that breaks down the population counts by travel time to work. The full table of variables is accessible through the Census Data API and a graphic showing the first portion of the table is available in the workspace. Take a look to see what variables are available. Notice how for each measure, there is the actual estimate itself (variable with suffix E), optional notes for the estimate (variable with suffix EA), the margin of error for the estimate (variable with suffix M), and optional notes for the margin of error (variable with suffix MA).

With larger data repositories like Census data, there are often other sites that arise that help document information about the data, often in a more user-friendly manner. For example, check out the B08303 variable group documentation provided by Social Explorer.

Move on to the next section when you are ready to start requesting some data!
"""