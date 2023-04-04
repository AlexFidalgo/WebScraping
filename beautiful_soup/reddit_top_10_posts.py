import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/worldnews/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('div', {'class': '_1oQyIsiPHYt6nx7VOmd1sz'})

for i, post in enumerate(posts[:10]):
    title = post.find('h3', {'class': '_eYtD2XCVieq6emjKBH3m'}).text
    link = 'https://www.reddit.com' + post.find('a', {'class': 'SQnoC3ObvgnGjWt90zD9Z'}).get('href')
    upvotes = post.find('div', {'class': '_1rZYMD_4xY3gRcSS3p8ODO'}).text
    print(f"{i+1}. {title} ({upvotes})\n{link}\n")
    
    
