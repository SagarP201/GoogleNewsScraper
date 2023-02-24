from setuptools import setup, find_packages                                                      

setup (
    name='Google News Scraper',
    version='0.1.0',
    description='A refreshed pygooglenews with article text scraping',
    author='Sagar Patel',
    author_email='sagar@ncri.io',
    packages=find_packages(),
    install_requires=[
        'feedparser',
        'bs4',
        'python-dateutil',
        'requests'
    ],
)
