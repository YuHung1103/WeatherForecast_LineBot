import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def week():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%Y%m%d%H")
    firstMinuteDigit = currentDateAndTime.strftime("%M")[0]

    url = "https://www.cwa.gov.tw/V8/C/W/County/MOD/Week/63_Week_m.html?T="+currentTime+"-"+firstMinuteDigit

    response = requests.get(url)

    result = []

    # 确保请求成功
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        panel_elements = soup.select('.panel.panel-default')

        for panel_element in panel_elements:
            # .panel-title 裡的內容
            panel_title_element = panel_element.select_one('.panel-title')
            # .panel-body 裡的內容
            panel_body_element = panel_element.select_one('.panel-body')

            # 提取星期和日期的文本内容
            date_element = panel_title_element.select_one('.date')
            day_text = date_element.select_one('.daily').get_text(strip=True)
            date_value = date_element.find_all('span')[-1].get_text(strip=True)

            # 提取天氣描述的文本内容
            weather_description_elements = panel_body_element.select('ol li')[1:]
            weather_descriptions = [element.get_text(strip=True) for element in weather_description_elements]

            # 提取早、晚溫度的文本内容
            day_temp = panel_title_element.select_one('.Day span.tem-C.is-active').get_text(strip=True)
            night_temp = panel_title_element.select_one('.Night span.tem-C.is-active').get_text(strip=True)

            # 提取體感溫度的文本内容
            temperature_element = panel_body_element.select_one('ul li span.tem-C.is-active').get_text(strip=True)

            # 提取紫外線等級的文本内容
            uvi_element = panel_body_element.select_one('ul li span.sr-only').get_text(strip=True)

            # 提取天氣狀況的照片
            day_img = panel_title_element.select_one('.Day img')
            night_img = panel_title_element.select_one('.Night img')

            # day_img_url = "https://www.cwa.gov.tw"+day_img['src']
            # night_img_url = "https://www.cwa.gov.tw"+night_img['src']

            result.append([date_value+" "+day_text+" 早", day_temp, weather_descriptions[0], temperature_element, uvi_element])
            result.append([date_value+" "+day_text+" 晚", night_temp, weather_descriptions[1], temperature_element, uvi_element])
    
        return result
    else:
        print(f"請求失敗，狀態碼: {response.status_code}")

def today():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%Y%m%d%H")
    firstMinuteDigit = currentDateAndTime.strftime("%M")[0]
    # JS 的檔案
    url = "https://www.cwa.gov.tw/Data/js/TableData_36hr_County_C.js?T="+currentTime+"-"+firstMinuteDigit+"&_=1704348200352"

    response = requests.get(url)
    data = response.text

    # 提取TableData_36hr字符串
    start_index = data.find('var TableData_36hr = {')
    end_index = data.find('};', start_index) + 1
    table_data_str = data[start_index:end_index]

    # 去掉多餘的註釋
    table_data_str = table_data_str.replace('// Updated:', '')

    # 要移除的部分
    prefix_to_remove = "var TableData_36hr = "

    # 使用字符串切片移除前缀
    single_string = table_data_str[len(prefix_to_remove):]

    # 把字串中的單引號都改成雙引號
    result_string = single_string.replace("'", '"')

    # 轉成字典
    dic = json.loads(result_string)

    # 取得該城市的資料
    city_data = dic.get('63')

    # 取得溫度
    low_temp = city_data[0].get('Temp').get('C').get('L')
    high_temp = city_data[0].get('Temp').get('C').get('H')
    temp = low_temp+" - "+high_temp

    # 取得降雨機率
    pop = city_data[0].get('PoP')+"%"

    # 取得天氣狀況
    wx = city_data[0].get('Wx')

    # 取得天氣狀況的icon編碼
    wxi = city_data[0].get("Wx_Icon")

    # 取得氣溫狀況
    ci = city_data[0].get('CI')

    img = ""
    current_time = currentDateAndTime.time()
    # 判斷當前時間是否介於04:00到16:00之間
    current_time = datetime.now().time()
    start_time = datetime.strptime("04:00", "%H:%M").time()
    end_time = datetime.strptime("16:00", "%H:%M").time()
    print("current_time:"+str(current_time))
    print("start_time:"+str(start_time))
    print("end_time:"+str(end_time))

    if start_time <= current_time <= end_time:
        # img = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/"+wxi+".svg"
        img = "https://attach.setn.com/newsimages/2022/12/02/3945459-PH.jpg"
    else:
        # img = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/night/"+wxi+".svg"
        img = "https://wegotoexperiencelife.com/wp-content/uploads/2020/05/image1-6.jpeg"

    return [img, temp, pop, wx, ci]

def city(area):
    match area:
        case "基隆市":
            return "10017"
        case "臺北市":
            return "63"
        case "新北市":
            return "65"
        case "桃園市":
            return "68"
        case "新竹市":
            return "10018"
        case "新竹縣":
            return "10004"
        case "苗栗縣":
            return "10005"
        case "臺中市":
            return "66"
        case "彰化縣":
            return "10007"
        case "南投縣":
            return "10008"
        case "雲林縣":
            return "10009"
        case "嘉義市":
            return "10020"
        case "嘉義縣":
            return "10010"
        case "臺南市":
            return "67"
        case "高雄市":
            return "64"
        case "屏東縣":
            return "10013"
        case "宜蘭縣":
            return "10002"
        case "花蓮縣":
            return "10015"
        case "臺東縣":
            return "10014"
        case "澎湖縣":
            return "10016"
        case "金門縣":
            return "09020"
        case "連江縣":
            return "09007"