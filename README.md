# Quiz3_Practice

## Instructions

### 1. Create a GitHub Repository
1. Log in to your GitHub account.
2. Create a new **private repository** named `Live_Quiz_Python_Project`.
3. Invite me (`delveccj`) as a collaborator to your repository.

### 2. Clone Your Repository Locally
1. Open your terminal and clone the repository.
2. Navigate to the cloned directory:
   ```bash
   cd Live_Quiz_Python_Project
   ```

### 3. Add Python Script for Extracting URLs
1. Download or copy the following Python script (`url_extractor.py`), which extracts all URLs from an HTML document:
   ```python
   # url_extractor.py
   from bs4 import BeautifulSoup

   def extract_urls_from_html(file_path):
       urls = []
       with open(file_path, 'r') as file:
           content = file.read()
           soup = BeautifulSoup(content, 'html.parser')
           for link in soup.find_all('a'):
               urls.append(link.get('href'))
       return urls

   if __name__ == "__main__":
       html_file = "example.html"
       urls = extract_urls_from_html(html_file)
       print(urls)
   ```
2. Save the script in your local repository directory as `url_extractor.py`.

### 4. Create a Sample HTML File
1. Create a sample HTML file called `example.html` in the same directory:
   ```html
   <!-- example.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Sample Page</title>
   </head>
   <body>
       <a href="">Example</a>
       <a href="">GitHub</a>
       <a href="">Python</a>
   </body>
   </html>
   ```

### 5. Create a Unit Test for the Script
1. Create a Python test script `test_url_extractor.py`:
   ```python
   import unittest
   from url_extractor import extract_urls_from_html

   class TestURLExtractor(unittest.TestCase):
       def test_extract_urls(self):
           test_file = "example.html"
           expected_urls = [
               "https://example.com",
               "https://github.com",
               "https://www.python.org"
           ]
           self.assertEqual(extract_urls_from_html(test_file), expected_urls)

   if __name__ == '__main__':
       unittest.main()
   ```

2. Ensure that the test checks if the URLs extracted from the `example.html` file match the expected URLs.
3. HINT - It will fail the first time you run the test - you will need to first add the libary it uses and second 

### 6. Create a `requirements.txt` File
1. Install **BeautifulSoup**:
   ```bash
   pip install beautifulsoup4
   ```
2. Create a `requirements.txt` file to capture dependencies:
   ```bash
   pip freeze > requirements.txt
   ```
3. Make sure the `requirements.txt` includes `beautifulsoup4`.

### 7. Add, Commit, and Push Your Changes
1. Add all the files to Git:
   ```bash
   git add .
   ```
2. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Added URL extractor script and test case"
   ```
3. Push your changes to GitHub:
   ```bash
   git push origin main
   ```

---

## GitHub Workflow for Testing

### 8. Add a GitHub Actions Workflow
1. Create a directory `.github/workflows` in the root of your repository:
   ```bash
   mkdir -p .github/workflows
   ```
2. Create a file called `workflow.yml` inside `.github/workflows` with the following content:
   ```yaml
   name: URL Extractor Workflow

   on:
     push:
       branches:
         - main  # Trigger workflow when code is pushed to the main branch

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
       # Step 1: Checkout the repository
       - name: Checkout code
         uses: actions/checkout@v2

       # Step 2: Set up Python 3.x
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.x'

       # Step 3: Install dependencies
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt

       # Step 4: Run the unit tests
       - name: Run unit tests
         run: |
           python -m unittest discover

       # Step 5: Check for specific commit comment
       - name: Check for specific commit comment
         run: |
           git log -1 --pretty=%B | grep "Live quiz complete"
         continue-on-error: false
   ```

### 9. Push the Workflow File
1. Add the workflow file:
   ```bash
   git add .github/workflows/workflow.yml
   ```
2. Commit the workflow file:
   ```bash
   git commit -m "Added GitHub Actions workflow"
   ```
3. Push the workflow to GitHub:
   ```bash
   git push origin main
   ```

---

## Submission Instructions
1. Ensure the repository contains:
   - `url_extractor.py`
   - `test_url_extractor.py`
   - `example.html`
   - `requirements.txt`
   - GitHub Actions workflow in `.github/workflows/workflow.yml`
2. Ensure all tests pass in the GitHub Actions workflow.
3. Make sure your last commit message includes the text `"Live quiz complete"`.
4. Once done, ensure all changes are pushed to the repository, and notify me (via GitHub or email) that your quiz is complete.

---

Good luck! 🎉
```
