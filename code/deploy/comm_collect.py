'''
프로그램 실행코드는 ctrl + f 후 ## or 프로그램 실행 코드 검색

저장된 comment폴더의 파일들을 시각화 하기 위해선
visualize 파일을 실행시켜 주세요.

# 필수 라이브러리 설치 체크
def checker_module()

# 필수 저장 폴더 생성 유무 체크
def checker_required_folder()

# 영상 정보 수집(웹 드라이버 객체)
def info_collect(driver)

# 스크롤을 밑까지 내리는 함수 (웹 드라이버 객체)
def scroll_down(driver)

# 대댓글을 여는 함수(웹 드라이버 객체)
def open_reply(driver)

# 문자열을 형태소 분석하여 리스트 형식으로 반환
def mrphl_anlys(arr)

# 형태소 분석 리스트의 데이터를 중복체크후 dict 형태로 변경
def data_prfct(arr)

# dict의 값을 csv로 저장(댓글 딕셔너리 형태, 영상정보 딕셔너리 형태, 반복회차)
def save_data(comment_dict, video_info, index)

# xpath 체크 함수 element의 유무를 확인한여 유 : True ,무 : False 값을 반환
def check_exists_by_xpath(xpath):

# 댓글 수집(웹 드라이버, 인덱스, 검색 키워드)
def get_comment(driver, index, keyword):
'''

print('-------------------------------------------------------------------')
print('\t Team 임대(Rental)\n')
print('\t 프로그램명 : comm_collect\n')
print('\t 수집된 데이터 저장 위치')
print('\t  - 댓글 및 영상 수집 데이터는 comment 폴더에 저장됩니다.')
print('\t  - 영상정보 수집 데이터는 nocomment 폴더에 저장됩니다.\n')
print('\t 시각화를 위해 visualize.exe 를 실행시켜 주세요.\n')
print('\t 유튜브 댓글 수집 프로그램을 시작합니다.')
print('-------------------------------------------------------------------\n')
# %%

# 필수 라이브러리 설치 체크


def checker_module():
    import sys
    import subprocess

    print('-------------------------------------------------------------------')
    try:
        # 없는 라이브러리 import시 에러 발생
        print('selenium 라이브러리 설치 여부를 체크합니다.')
        import selenium
        print('selenium 라이브러리가 존재합니다.\n')
    except:
        print('selenium 라이브러리가 존재하지 않습니다.')
        print("selenium 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'selenium'])
        print("selenium 라이브러리 설치를 완료하였습니다.\n")

    try:
        print('webdriver_manager 라이브러리 설치 여부를 체크합니다.')
        import webdriver_manager
        print('webdriver_manager 라이브러리가 존재합니다.\n')
    except:
        print('webdriver_manager 라이브러리가 존재하지 않습니다.')
        print("webdriver_manager 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'webdriver-manager'])
        print("webdriver_manager 라이브러리 설치를 완료하였습니다.\n")

    try:
        print('pandas 라이브러리 설치 여부를 체크합니다.')
        import pandas
        print('pandas 라이브러리가 존재합니다.\n')
    except:
        print('pandas 라이브러리가 존재하지 않습니다.')
        print("pandas 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pandas'])
        print("pandas 라이브러리 설치를 완료하였습니다.\n")

    try:
        print('bs4 라이브러리 설치 여부를 체크합니다.')
        import bs4
        print('bs4 라이브러리가 존재합니다.\n')
    except:
        print('bs4 라이브러리가 존재하지 않습니다.')
        print("bs4 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'bs4'])
        print("bs4 라이브러리 설치를 완료하였습니다.\n")

    try:
        print('konlpy 라이브러리 설치 여부를 체크합니다.')
        import konlpy
        print('konlpy 라이브러리가 존재합니다.\n')
    except:
        print('konlpy 라이브러리가 존재하지 않습니다.')
        print("konlpy 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'konlpy'])
        print("konlpy 라이브러리 설치를 완료하였습니다.")
    print('-------------------------------------------------------------------\n')

    return True


# 필수 저장 폴더 생성 유무 체크
def checker_required_folder():
    import os
    print('폴더 생셩 여부를 체크합니다.\n')

    # comment폴더 유무 확인후 생성
    if not os.path.exists('./comment'):
        print('comment 폴더 생성')
        os.mkdir('./comment')

    # nocomment폴더 유무 확인후 생성
    if not os.path.exists('./nocomment'):
        print('nocomment 폴더 생성')
        os.mkdir('./nocomment')

    # img폴더 유무 확인후 생성
    if not os.path.exists('./img'):
        print('img 폴더 생성')
        os.mkdir('./img')


# 영상 정보 수집(웹 드라이버 객체)
def info_collect(driver):
    # 영상 정보 수집 (현재 날짜 밑 시간, 영상 이름, 채널명, 조회수, 게시일)
    import time
    from selenium.webdriver.common.by import By

    # 수집 날짜                       년.월.일
    collection_date = time.strftime('%Y.%m.%d')

    # 영상 이름
    viedo_name = driver.find_element(
        By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string').text

    # 채널명
    channel_name = driver.find_element(
        By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a').text

    # 조회수
    views = driver.find_element(
        By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/div/yt-formatted-string/span[1]').text.split(' ')[1]

    # 게시일
    opening_date = driver.find_element(
        By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/div/yt-formatted-string/span[3]').text

    # 수집 된 영상 정보
    video_info = {'수집 날짜': collection_date, '영상 이름': viedo_name,
                  '채널 이름': channel_name, '조회수': views, '게시일': opening_date}

    return video_info


# 스크롤을 밑까지 내리는 함수 (웹 드라이버 객체)
def scroll_down(driver):
    import time

    # 화면 크기 조정(유튜브 댓글 수집 안정성 증가)
    driver.set_window_size(800, 1100)

    # scrollHeight = 화면 바깥으로 삐져나간 부분까지 포함한 전체 길이
    # 0부터 전체길이(맨 아래)까지 스크롤한다.
    driver.execute_script(
        "window.scrollTo(0, document.documentElement.scrollHeight)")
    time.sleep(1.5)

    # 스크롤 이전 높이
    last_height = driver.execute_script(
        "return document.documentElement.scrollHeight")

    while True:
        # 스크롤의 y좌표를 가장아래(scrollHeight)까지 내림
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.5)

        # 스크롤 후 높이 구하기
        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight")
        # 끝까지 스크롤 한 뒤 멈추기
        if new_height == last_height:
            break
        last_height = new_height

        time.sleep(1.5)


# 대댓글을 여는 함수(웹 드라이버 객체)
def open_reply(driver):
    import time
    from selenium.webdriver.common.by import By

    # class='more-button'인 element들을 배열에 저장
    replies = driver.find_elements(By.CLASS_NAME, "more-button")

    # 로딩이 완료될 때까지 10초간 대기, 로딩이 완료되면 바로 다음 코드 실행
    driver.implicitly_wait(10)

    for reply in replies:
        # 순차적으로 나타나는 replies배열의 요소를 클릭
        driver.execute_script("arguments[0].click();", reply)
        time.sleep(1.5)


# 형태소 분석(댓글배열)
# 문자열을 형태소 분석하여 리스트 형식으로 반환
def mrphl_anlys(arr):
    from konlpy.tag import Okt
    import re

    # 한국어 형태소 분석
    okt = Okt()

    # 분석된 글자들을 리스트형태로 저장하는 변수
    mrphl_list = []

    for text in arr:
        temp_comment = text.text

        temp_comment = temp_comment.replace('\n', ' ')
        temp_comment = temp_comment.replace('\r', ' ')
        temp_comment = temp_comment.replace(
            '\t', ' ').split(" ")  # 문자열을 각 단어 별로 분리

        # filter함수를 이용하여 '@', 'https'를 포함한 단어 제거
        temp_comment = list(filter(lambda n: n.find('@') != 0, temp_comment))
        temp_comment = list(
            filter(lambda n: n.find('https') != 0, temp_comment))

        # re.sub() 정규표현식을 통해 문자열을 치환하는 함수
        # 한글, 숫자, 영어, 일본어, 한자를 제외한 댓글 정리
        temp_comment = list(map(lambda n: re.sub(
            r"[^\uAC00-\uD7A30-9a-zA-Zぁ-ゔァ-ヴー々〆〤一-龥]", "", n).replace(u'\xa0', u''), temp_comment))

        # 1차원 배열을 문자열로 정렬
        temp_comment = " ".join(temp_comment)
        # okt객체를 이용한 형태소 분석
        temp_comment = okt.morphs(temp_comment, stem=True)
        # '' 빈 요소 값 제거
        temp_comment = list(filter(None, temp_comment))

        mrphl_list.append(temp_comment)

    # 2차원 배열을 1차원 배열로 변환
    mrphl_list = sum(mrphl_list, [])

    # 글자 수가 한글자인 요소를 필터링
    mrphl_list = list(filter(lambda n: len(n) != 1, mrphl_list))

    return mrphl_list


# 형태소 분석 리스트의 데이터를 중복체크후 dict 형태로 변경
def data_prfct(arr):

    # 중복된 단어들을 합쳐서 {key:value}형태로 저장하는 변수 ex) {'안녕':3, '인사':2}
    comment_dict = {}

    for key in arr:
        # dict에 key 값이 없을시 value 값을 1로 생성
        if key not in comment_dict:
            comment_dict[key] = 1
        # 있을시 value 값 1 증감
        else:
            comment_dict[key] = comment_dict[key]+1

    # 빈도 수가 높은 순으로 정렬
    sorted_1 = sorted(comment_dict.items(),
                      key=lambda item: item[1], reverse=True)
    comment_dict = dict(sorted_1)

    return comment_dict


# dict의 값을 csv로 저장(댓글 딕셔너리 형태, 영상정보 딕셔너리 형태, 반복회차)
def save_data(comment_dict, video_info, index):
    import pandas as pd
    import os

    # 댓글이 있을경우
    if (len(comment_dict) != 0):
        # 경로를 comment폴더로 지정
        filename = os.getcwd()+'/comment/'
        print('형태소 분석 결과\n', comment_dict, '\n')
    else:
        # 경로를 nocomment폴더로 지정
        filename = os.getcwd()+'/nocomment/'
    filename += video_info['수집 날짜'] + '_' + \
        video_info['검색어'] + '_' + str(index)
    # 영상 정보 딕셔너리화
    pd_data = {"수집 날짜": [video_info['수집 날짜']], "제목": [video_info['영상 이름']], "채널": [
        video_info['채널 이름']], "조회수": [video_info['조회수']], "게시일": [video_info["게시일"]]}

    # 댓글 딕셔너리 값을 업데이트 해줌
    pd_data.update(comment_dict)
    # 데이터 프레임 생성
    youtube_pd = pd.DataFrame(pd_data)
    # csv파일의 행,열 반전
    youtube_pd = youtube_pd.transpose()
    # filename으로 csv파일 생성
    youtube_pd.to_csv(filename + '.csv', encoding="utf-8-sig")
    print(f'파일이 저장되었습니다.\n경로 : {filename}.csv\n')


# xpath 체크 함수 element의 유무를 확인한여 유 : True ,무 : False 값을 반환
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


# 댓글 수집(웹 드라이버, 인덱스, 검색 키워드)
def get_comment(driver, index, keyword, count):
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup
    import time

    time.sleep(1)

    # index번째 영상의 xpath값 저장
    # 영상 선택 방식 변경 - 23.03.10
    time.sleep(1)
    driver.execute_script(
        f"document.querySelectorAll('ytd-video-renderer')[{index}].querySelector('a#thumbnail').click()")
    driver.implicitly_wait(10)

    # url에 shorts가 포함 될 경우 False 반환
    cur_url = driver.current_url
    time.sleep(1)
    is_shorts = cur_url.find('shorts') == -1

    if is_shorts:
        # 영상 일시정지
        video_xtml = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video'
        driver.find_element(
            By.XPATH, video_xtml).click()
        time.sleep(1)

        # 페이지 높이의 1/3 값을 가져와서 저장
        half_height = driver.execute_script(
            "return document.documentElement.scrollHeight")/3

        time.sleep(1)
        driver.execute_script(
            f"window.scrollTo(0, {half_height})")

        # element의 유무 체크
        is_element_Ok = check_exists_by_xpath(
            '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/h2/yt-formatted-string/span[1]')

        time.sleep(1)
        if is_element_Ok:
            print('\n영상정보 수집을 시작합니다.\n')

            # 영상 설명 더보기 클릭
            driver.find_element(
                By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]').click()
            time.sleep(1)

            video_info = info_collect(driver)  # 영상 정보를 json형태로 리턴 받음

            video_info['검색어'] = keyword      # 영상 정보에 '검색어':keyword 추가

            # data_prfct 함수로 부터 반환된 dict 값을 저장하는 변수
            comment_dict = {}

            for key, value in video_info.items():
                print(key + " : " + value)

            # index 3이하의 영상만 댓글 수집
            if index <= 3+count:
                print("스크롤 시작 : " + time.strftime('%H:%M:%S'))
                scroll_down(driver)

                print("대댓글 열기 시작 : " + time.strftime('%H:%M:%S'))
                open_reply(driver)

                print("댓글 수집 시작 : " + time.strftime('%H:%M:%S'))

                # html source 불러와서 저장
                html_source = driver.page_source
                # bs4를 이용한 html parsing
                soup = BeautifulSoup(html_source, 'html.parser')
                # 댓글의 text 수집
                comment_list = soup.select("yt-formatted-string#content-text")
                # if(len(comment_list)==0):

                # 댓글의 형태소 분석
                item = mrphl_anlys(comment_list)

                # 리스트를 딕셔너리 형태로 변환
                comment_dict = data_prfct(item)

            # 영상정보를 csv로 저장
            save_data(comment_dict, video_info, index-count)
        else:
            print('댓글이 없는 영상은 기능을 지원하지 않습니다.\n다음 영상을 선택합니다.\n')
    else:
        print('유튜브 쇼츠에서는 기능을 지원하지 않습니다.\n다음 영상을 선택합니다.\n')

    # 이전 페이지로 되돌아가기
    driver.back()
    driver.implicitly_wait(10)

    # 영상 선택을 위해 전체화면으로 변경
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 쇼츠 혹은 댓글이 없는 영상의 경우 False 값이 하나라도 있으면 False 값을 저장
    is_checker = is_shorts and is_element_Ok

    return not (is_checker)


# 프로그램 실행 코드
try:
    # 라이브러리 설치 여부 체크
    if (checker_module()):
        # 웹사이트 크롤링을 위해 사용하는 라이브러리
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import NoSuchElementException

        # 크롬 드라이버를 설정하기 위해 사용
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver import ChromeOptions

        # 크롬 드라이버를 크롬 브라우저 버전에 맞게 자동으로 다운로드하는 라이브러리
        from webdriver_manager.chrome import ChromeDriverManager

        # 크롤링시 강제적으로 대기할 떄 사용
        import time

    # 필수 폴더 생성 여부 체크
    checker_required_folder()

    # 접속 url
    keyword_url = 'https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR&hl=ko'
    youtube_url = "https://youtube.com/"

    print('\n크롬 드라이버 연결을 시작합니다.\n')

    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # 크롬 드라이버 매니저 연결
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    # 윈도우 전체화면으로 실행
    driver.maximize_window()
    print('\n크롬 드라이버 연결을 완료 하였습니다.\n')

    # 구글 데일리 인기 검색어 1위 키워드 수집
    driver.get(keyword_url)
    driver.implicitly_wait(10)
    keyword = driver.find_element(
        By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/ng-include/div/div/div/div/md-list[1]/feed-item/ng-include/div/div/div[1]/div[2]/div[1]/div/span/a').text

    # 유튜브 접속
    driver.get(youtube_url)
    driver.implicitly_wait(10)
    time.sleep(0.5)

    # 키워드 입력하여 검색
    search = driver.find_element(By.NAME, "search_query")
    search.send_keys(keyword)
    time.sleep(0.5)
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    # 10개의 영상 정보를 수집
    i = 1
    end_index = 10
    count = 0
    while (i <= end_index):
        if get_comment(driver, i, keyword, count):
            # 영상을 건너뛴경우 1증가
            end_index += 1
            count += 1
        i += 1

    print('-------------------------------------------------------------------')
    print('\t Team 임대(Rental)\n')
    print('\t 프로그램명 : comm_collect\n')
    print('\t 수집된 데이터 저장 위치')
    print('\t  - 댓글 및 영상 수집 데이터는 comment 폴더에 저장되어있습니다.')
    print('\t  - 영상정보 수집 데이터는 nocomment 폴더에 저장되어있습니다.\n')
    print('\t 시각화를 위해 visualize.exe 를 실행시켜 주세요.')
    print('-------------------------------------------------------------------\n')

    # 드라이브 완전 종료
    driver.quit()
    input('Enter 입력시 프로그램이 종료됩니다...')
    print('\n유튜브 댓글 수집 프로그램을 종료합니다.')

except Exception as e:
    print(e)
