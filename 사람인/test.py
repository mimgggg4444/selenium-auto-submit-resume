from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL 리스트
url_list = [
    'https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx=44036382',
    'https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx=44038074',

]

driver = webdriver.Chrome()  # 크롬 드라이버 초기화

for url in url_list:
    print(f"접속 중인 URL: {url}")
    driver.get(url)  # 각 URL 접속

    try:
        # 입사지원 버튼 대기 및 클릭
        apply_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "프레임으로 전환할 버튼 셀렉터"))
        )
        apply_button.click()
        print("입사지원 버튼 클릭 완료")

        # 프레임 전환
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "입사지원 버튼이 있는 프레임 셀렉터"))
        )
        print("프레임 전환 완료")

        # 프레임 내 입사지원 버튼 대기 및 클릭  
        inner_apply_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "프레임 내 입사지원 버튼 셀렉터"))
        )
        inner_apply_button.click()
        print("프레임 내 입사지원 버튼 클릭 완료")

        # 원래 프레임으로 복귀
        driver.switch_to.default_content()
        print("원래 프레임으로 복귀 완료")

        print(f"{url} - 입사지원 완료")

    except Exception as e:
        print(f"{url} - 입사지원 중 오류 발생: {str(e)}")

driver.quit()  # 드라이버 종료
