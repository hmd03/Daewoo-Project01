'''
프로그램 실행코드는 ctrl + f 후 ## or 프로그램 실행 코드 검색 

# 필수 라이브러리 설치 체크
def checker_module()
'''
# %%

print('-------------------------------------------------------------------')
print('\t Team 임대(Rental)\n')
print('\t 프로그램명 : visualize\n')
print('\t 수집된 데이터 저장 위치')
print('\t  - 시각화된 이미지는 img 폴더에 저장됩니다.\n')
print('\t 시각화 프로그램을 시작합니다.')
print('-------------------------------------------------------------------\n')

# 필수 라이브러리 설치 체크
def checker_module():
    import sys
    import subprocess

    print('-------------------------------------------------------------------')
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
        print('wordcloud 라이브러리 설치 여부를 체크합니다.')
        import wordcloud
        print('wordcloud 라이브러리가 존재합니다.\n')
    except:
        print('wordcloud 라이브러리가 존재하지 않습니다.')
        print("wordcloud 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'wordcloud-1.8.1-cp311-cp311-win_amd64.whl'])
        print("wordcloud 라이브러리 설치를 완료하였습니다.\n")

    try:
        print('matplotlib 라이브러리 설치 여부를 체크합니다.')
        import matplotlib
        print('matplotlib 라이브러리가 존재합니다.\n')
    except:
        print('matplotlib 라이브러리가 존재하지 않습니다.')
        print("matplotlib 라이브러리를 설치합니다.")
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', '--upgrade', 'matplotlib'])
        print("matplotlib 라이브러리 설치를 완료하였습니다.\n")

    print('-------------------------------------------------------------------\n')

    return True


# 프로그램 실행 코드
try:
    # 라이브러리 설치 여부 체크
    if (checker_module()):
        # 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 라이브러리
        import os
        # 쉽고 직관적인 분류된 데이터로 작업할 수 있도록 데이터 구조를 제공 하는 라이브러리
        import pandas as pd
        # 정제된 데이터를 시각화 하기 위한 라이브러리
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud

        import time

    # comment 폴더의 유무 체크
    if os.path.isdir(os.getcwd()+'\comment'):
        path = os.getcwd()+'\comment'  # 파일 위치를 담고있는 변수
    else:
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        print(' comment폴더가 존재하지 않습니다.')
        print(' comm_collect 프로그램을 먼저 실행시켜주세요.')
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        time.sleep(3)
        exit()

    # img폴더 유무 확인후 생성
    if not os.path.exists('.\img'):
        os.mkdir('.\img')

    # .csv 파일 만 추출하여 리스트에 저장
    file_names = [file for file in os.listdir(path) if file.endswith('.csv')]

    if (len(file_names) == 0):
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        print(' comment폴더에 csv파일이 없습니다.')
        print(' comm_collect 프로그램을 먼저 실행시켜주세요.')
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        time.sleep(3)
        exit()

    print('파일 리스트 목록\n', *file_names, '\n')

    for name in file_names:
        print(f'{name} 파일 wordcloud 시작')
        # 데이터 프레임 생성
        df = pd.read_csv(path + '\\' + name,
                         names=['word', 'count'], skiprows=[1, 2, 3, 4, 5])

        # 생성된 데이터 프레임을 딕셔너리 형태로 변환
        wc = df.set_index("word").to_dict()["count"]

        wordCloud = WordCloud(
            font_path="malgun",  # 폰트 지정
            width=400,  # 워드 클라우드의 너비 지정
            height=400,  # 워드클라우드의 높이 지정
            max_font_size=100,  # 가장 빈도수가 높은 단어의 폰트 사이즈 지정
            background_color='white'  # 배경색 지정
        ).generate_from_frequencies(wc)  # 워드 클라우드 빈도수 지정

        plt.figure()  # figure 생성
        plt.imshow(wordCloud)  # 터미널에 이미지 보여주기
        plt.axis('off')  # axis 끄기

        save_name = name.rstrip('.csv') + '.png'
        # 이미지 저장 경로 및 파일 이름 설정
        print(f'{save_name}로 img 폴더에 저장\n')

        save_file = os.path.join(os.getcwd()+'\img', save_name)
        plt.savefig(save_file)  # img 폴더에 이미지 저장
        time.sleep(0.3)

    time.sleep(1)
    print('-------------------------------------------------------------------')
    print('\t Team 임대(Rental)\n')
    print('\t 프로그램명 : visualize\n')
    print('\t 수집된 데이터 저장 위치')
    print('\t  - 시각화한 이미지는 img 폴더에 저장되어있습니다.\n')
    print('-------------------------------------------------------------------\n')

    input('Enter 입력시 프로그램이 종료됩니다...')
    print('\n시각화 프로그램을 종료합니다.')

except Exception as e:
    print(e)
