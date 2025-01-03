"""
Intro to Data Acquisition
Exploring and defining the methods of obtaining data

Introduction
“It is a capital mistake to theorize before one has data.” - Sherlock Holmes 

(Fictional) detectives like Sherlock Holmes and real life data scientists have a lot in common: they both need to find data! Where a detective goes looking for clues, a data scientist goes looking for datasets. But where do all of those datasets come from?

Data acquisition (also called data mining) is the process of gathering data. Ideally, we have a question in mind before we collect the data, but not always. Sometimes data is gathered before we know what to do with it. When that happens, it is important to take a step back and define what questions can be answered with the available data.

In addition, some things to consider when acquiring data are:

What data is needed to achieve the goal?
How much data is needed?
Where and how can this data be found?
What legal and privacy concerns should be considered?
The role of data collection
Imagine for a moment that you are collecting data about books. You decided to record the title, author, and number of pages of all the books in your local library. You decided not to include language, subtitles, editors, or publishers.

If you want to publish this data to make it available to others, you would need to document how you measured your variables (i.e., were appendices included in the page count?) and the parameters for collection (i.e., your local library). This is your methodology.

How the data was collected (the methodology) directly affects the questions we can ask and what generalizations we can make. This article introduces the broad types of data available, the file formats that they can come in, and where to find datasets. But even once you find (or make) a dataset, the most important part about it is the documentation that comes with it!

Data sources
Data can be acquired from many different sources. Broadly, they can be categorized into primary data and secondary data.

Primary data is data collected by the individual or organization who will be doing the analysis. Examples include:

Experiments (e.g., wet lab experiments like gene sequencing)
Observations (e.g., surveys, sensors, in situ collection)
Simulations (e.g., theoretical models like climate models)
Scraping or compiling (e.g., webscraping, text mining)
Secondary data is data collected by someone else and is typically published for public use. Most data you will use falls into this category. Examples include:

Any primary data that was collected by someone else
Institutionalized data banks (e.g., census, gene sequences)
As you can imagine, collecting your own primary data can be time consuming. However, the closer you are to the data, the better you understand it and its nuances. On the other hand, secondary data is much easier to find. Even with secondary data, understanding how the data was created is essential in order to correctly utilize and analyze it. This includes reading any available data methodology or README files.

Cleaned vs. raw data
There is another subcategory of secondary data that can be called “pre-cleaned” data. These are datasets published by institutions like Kaggle that are already cleaned, filtered, and ready to use.

While pre-cleaned data is undoubtedly easier to use, you lose some of the flexibility and control that working with unaltered, “raw” data offers. For example, if a cleaned dataset discarded certain fields or rows during the data processing step, there is no way of getting the information back. Nevertheless, pre-cleaned datasets are still popular, and that can be perfectly fine depending on the end goal.

Data file formats
Data can come in a variety of different file formats, depending on the type of data. Being able to open and convert between these file types opens a whole world of data that is otherwise inaccessible. Examples of file formats include:

Tabular (e.g., .csv, .tsv, .xlsx)
Non-tabular (e.g., .txt, .rtf, .xml)
Image (e.g., .png, .jpg, .tif)
Agnostic (e.g., .dat)
Further, some file formats are proprietary and can only be opened by software developed by a particular company. Opening these in another program requires converting to a universal format (this has to do with how the characters are encoded). Proprietary formats include Excel or MS Access files that are designed to be opened by Microsoft Office applications, as opposed to more generic types like .csv files. There are also other file formats that store metadata, such as SPSS and STATA files that contain information on data labels.

It is best practice to store data in a way that is most easily accessible for everyone. Generally, this means storing data in a non-proprietary and openly documented format, using standard character encodings (utf-8), and keeping data files uncompressed, if space allows. There are various methods, including online tools, that can be used to convert between formats if necessary.

Where to get data
Primary data
Conducting research and experiments is typically out of the scope for Data Scientists, but surveys and simulations are common methods for acquiring primary data. Webscraping is also a special case of primary data collection by extracting or copying data directly from a website. To learn more, check out our full course on webscraping and this article demonstrating how to webscrape MLB stats using Python.

Secondary data
Secondary data can be obtained from many different websites. Some of the most popular repositories include:

GitHub
Kaggle
KDnuggets
UCI Machine Learning Repository
US Government’s Open Data
Five Thirty Eight
Amazon Web Services
BuzzFeed
Data is Plural
Harvard HCI
Each repository or individual dataset has its own terms of use and method for downloading. Be sure to read the description on the website you are using for how to access the data.

Secondary data can sometimes be obtained via an application programming interface (API). APIs are built around the HTTP request/response cycle. A client (you) sends a request for data to a website’s server through an API call. Then, the server searches its database and responds either with the data, or an error stating that the request cannot be fulfilled.

Diagram of client-server communication and request-response cycle

What about big data?
With advancements in digital technology, data can be collected and shared easier than ever. The result is the era of big data. The number of records and variables present in big data is often too large to manage locally, giving it its name. However, big data is outside the scope of this article.

Conclusion
Working with data can be an exciting process. As tempting as it may be to jump straight into the analysis, it is important to take a step back and first consider how the data was acquired, as that is often an integral part of the data itself and what conclusions can be drawn from it. It will de
"""