# Audible Insights: Scraping Bestselling Audiobook Data with Python and Selenium

This project is a Python-based web scraper that automates the extraction of audiobook data from Audible's Bestsellers page using **Selenium**. The script scrapes audiobook titles, authors, and runtimes from multiple pages of bestsellers and saves the data into a CSV file for easy analysis and use.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [XPath Usage](#xpath-usage)
- [Example Output](#example-output)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## Features

- **Automated Web Scraping**: Automatically navigates through Audible's bestseller pages to extract data.
- **Pagination Handling**: Effectively scrapes data from multiple pages without manual intervention.
- **Data Extraction**: Extracts audiobook title, author, and runtime for each bestseller.
- **CSV Export**: Outputs the scraped data into a structured CSV file, making it easy for further analysis or integration with other applications.
- **Selenium Integration**: Uses Selenium to control and interact with a Chrome browser for scraping.

## Technologies Used

- **Python**: The core programming language used for writing the script.
- **Selenium**: A browser automation tool that allows for interaction with dynamic web content.
- **Pandas**: A Python library used for data manipulation and exporting the scraped data into a CSV file.
- **ChromeDriver**: A tool to interface with Google Chrome, required for Selenium.

## Prerequisites

Before running this script, make sure you have the following installed:

- **Python 3.6+**: Ensure you have Python installed on your system.
- **Selenium**: Selenium is required to automate the web browser.
- **ChromeDriver**: Required to automate Google Chrome via Selenium. Make sure to download the correct version of ChromeDriver compatible with your version of Chrome.

### Installing Required Python Libraries

To install the required Python libraries, use the following command:

```bash
pip install selenium pandas
```

### ChromeDriver Setup

Download the appropriate version of **ChromeDriver** from [here](https://sites.google.com/a/chromium.org/chromedriver/). After downloading, place the ChromeDriver executable in a directory and update the path to the executable in the script.

## Installation

1. **Clone the Repository**:

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/audible-bestsellers-scraper.git
   cd audible-bestsellers-scraper
   ```

2. **Modify ChromeDriver Path**:

   Update the `path` variable in the script to point to the location of your downloaded ChromeDriver:

   ```python
   path = "/path/to/your/chromedriver"
   ```

## Usage

1. Once you have set up the project and updated the ChromeDriver path, you can run the script with the following command:

   ```bash
   python WebScrapingWithSelenium_audible.py
   ```

2. The script will open Chrome, navigate to the Audible Bestsellers page, and begin scraping the titles, authors, and runtime of the audiobooks. It will navigate through multiple pages of the bestseller list.

3. After the scraping process is complete, the data will be saved into a CSV file named `books_bestsellers.csv` in the project directory.

## How It Works

1. **Web Browser Automation**: The script opens Google Chrome using Selenium, maximizes the window, and navigates to Audible's Bestsellers page.
   
2. **XPath for Element Selection**: XPath is used extensively in the script to locate specific HTML elements on the Audible webpage. In this case, XPath is used to:
   - Extract **titles** of audiobooks from an `h3` element that contains the class `bc-pub-break-word`.
   - Capture **authors** by targeting list items (`li`) with the class `authorLabel`.
   - Retrieve **runtime** information from the class `runtimeLabel`.
   
   For example:
   ```python
   title = product.find_element_by_xpath('.//h3[contains(@class, "bc-pub-break-word")]').text
   author = product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text
   runtime = product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text
   ```

   This ensures that the script precisely identifies the audiobook data within each product container on the page.

3. **Scraping Loop**: The script identifies the total number of pages in the bestseller list and scrapes each page. For each audiobook, it captures:
   - **Title**
   - **Author**
   - **Runtime**

4. **Pagination Handling**: The script handles pagination by clicking the "Next" button after scraping the data from each page until it reaches the last page.

5. **Data Export**: After scraping all pages, the data is compiled into a Pandas DataFrame and saved as `books_bestsellers.csv`.

### XPath Usage

XPath, or XML Path Language, is used to locate specific elements in a web page's HTML structure. In this project, XPath expressions help extract detailed information from Audible's bestseller page by pinpointing the exact elements containing the title, author, and runtime of audiobooks. The following XPath selectors are employed:

- **Title**: The XPath selector targets the `h3` element containing the title, which is identified by the class `bc-pub-break-word`:
  ```python
  .//h3[contains(@class, "bc-pub-break-word")]
  ```

- **Author**: The author information is extracted from list items with the class `authorLabel`:
  ```python
  .//li[contains(@class, "authorLabel")]
  ```

- **Runtime**: The runtime is pulled from elements that use the class `runtimeLabel`:
  ```python
  .//li[contains(@class, "runtimeLabel")]
  ```

These XPath expressions allow the script to reliably navigate through the web page's structure and accurately extract the desired data.

## Example Output

After running the script, you will get a CSV file with the following structure:

| title                             | authors            | runtime  |
| ---------------------------------- | ------------------ | -------- |
| The Subtle Art of Not Giving a F*ck| Mark Manson        | 5 hrs 57 mins |
| Atomic Habits                      | James Clear        | 8 hrs 55 mins |
| Becoming                           | Michelle Obama     | 19 hrs 3 mins |

## Customization

- **Headless Mode**: You can run the browser in headless mode (i.e., without a visible GUI) by setting the following line to `True` in the script:
  
   ```python
   options.headless = True
   ```

- **Change Scraped Fields**: You can adjust the XPath selectors in the script to scrape additional information such as ratings or prices by modifying the following sections:
  
   ```python
   titles.append(product.find_element_by_xpath('.//h3').text)
   ```

## Troubleshooting

- **Browser Fails to Open**: Make sure that the `path` variable is correctly set to the location of your ChromeDriver and that your ChromeDriver version matches your Chrome browser version.
- **Empty Data**: If no data is being scraped, Audible may have updated their webpage. Check the XPath selectors to ensure they are still valid.

## Future Enhancements

- **Error Handling**: Add robust error handling for better resilience in the face of network or browser issues.
- **Data Validation**: Implement checks to ensure that the scraped data is valid and non-duplicative.
- **Dockerization**: Create a Dockerfile to containerize the project for easier deployment.
- **Additional Data Fields**: Scrape more detailed information such as audiobook ratings, release dates, or pricing.
