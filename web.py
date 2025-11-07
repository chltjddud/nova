import requests
from bs4 import BeautifulSoup

def simple_crawler(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('title').get_text() if soup.find('title') else 'No Title Found'
    print(f"Page Title: {title}") # 결과 1: 페이지 제목 출력

    links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):
            links.add(href)
    
    print("\n--- Extracted Links ---")
    for link in sorted(list(links))[:10]:
        print(link) # 결과 2: 추출된 링크 목록 출력

if __name__ == "__main__":
    target_url = "https://www.naver.com" 
    simple_crawler(target_url)
