import requests
from bs4 import BeautifulSoup

base_url = "https://kr.ufc.com/athletes/all/active"
page = 0

def get_athlete_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 선수 상세 페이지에서 특정 div의 데이터를 추출합니다.
    details_div = soup.select_one("#block-mainpagecontent > div > div > div > div.l-container.stats-record-wrap > div > div > div.c-carousel--multiple__content.carousel__multiple-items.stats-records-inner-wrap")
    
    if details_div:
        # div 내의 모든 텍스트를 추출합니다.
        details = details_div.get_text(separator=' | ', strip=True)
        return details
    else:
        return "상세 정보를 찾을 수 없습니다."

while True:
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    athletes = soup.select('div.c-listing-athlete-flipcard__back')
    
    if not athletes:
        print(f"페이지 {page}에서 선수를 찾을 수 없습니다. 크롤링을 종료합니다.")
        break
    
    print(f"--- 페이지 {page} ---")
    for athlete in athletes:
        link = athlete.select_one('div.c-listing-athlete-flipcard__action > a')
        if link and 'href' in link.attrs:
            athlete_url = "https://kr.ufc.com" + link['href']
            print(f"선수 URL: {athlete_url}")
            details = get_athlete_details(athlete_url)
            print(f"선수 상세 정보: {details}")
            print("-" * 50)
        else:
            print("선수 링크를 찾을 수 없습니다.")
    
    page += 1

# 타격
    # document.querySelector("#block-mainpagecontent > div > div > div > div.l-container.stats-record-wrap > div > div > div.c-carousel--multiple__content.carousel__multiple-items.stats-records-inner-wrap > div:nth-child(4) > div > div:nth-child(1) > div.c-stat-compare__group.c-stat-compare__group-1 > div.c-stat-compare__number")
# 방어
    # document.querySelector("#block-mainpagecontent > div > div > div > div.l-container.stats-record-wrap > div > div > div.c-carousel--multiple__content.carousel__multiple-items.stats-records-inner-wrap > div:nth-child(4) > div > div:nth-child(1) > div.c-stat-compare__group.c-stat-compare__group-2 > div.c-stat-compare__number")
# 명중률
    # document.querySelector("#block-mainpagecontent > div > div > div > div.l-container.stats-record-wrap > div > div > div.c-carousel--multiple__content.carousel__multiple-items.stats-records-inner-wrap > div:nth-child(2) > div > div.overlap-athlete-content.overlap-athlete-content--horizontal > div.c-overlap__chart > div > svg > text")