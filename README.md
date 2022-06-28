# Shortmyurl Project
### How to build and run your solution
Copy .env.example as .env  and update configuration accordingly
```bash
cp .env.example .env
```
Install required packages using requirements.txt
```bash
pip install -r requirements.txt
```
Run migrations
```bash
python .\manage.py makemigrations
python .\manage.py migrate 
```
Run local server
```bash
python .\manage.py runserver
```
Access application using local server
```bash
http://localhost:8000/
```
### Reasoning behind design and any trade-offs
####Used md5 hash function and converted to hex digits to get unique slug. This can be improved to reduced length of the slug.
####Validations to take input from end users can be improved.

### Explanation of what could be done with more time
#### Improve hash function to reduce length of the short url
#### Add required test cases
#### Introduce service as API so can be integrated with different platforms
#### Introduce caching to reduce db calls incase frequent access for short url
#### Different users should have different short url for same link. To improve user experience

### Deploy this to Elastic Beanstalk on AWS Cloud
#### Update .platform scripts according to AWS account you are using
#### Create elastic beanstalk with platform Python 3.8 running on 64bit Amazon Linux 2/3.3.9
#### To initialize project - Run using CLI - Command ***eb init***
#### Do required configuration (add aws secret keys)
#### To deploy - Run using CLI - Command ***eb deploy***
#### Check deployment status - Run using CLI - Command ***eb status***