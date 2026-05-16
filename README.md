# Seoul Bus Sensor(서울버스)

![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.4][version-shield]

Seoul Bus Sensor for Home Assistant 입니다.<br>
- 서울버스 도착정보를 알려줍니다.
- 지정한 정류장에 도착예정인 버스를 확인할 수 있습니다.
- 정류장, 버스, 그리고 API. 모두 세가지 센서로 구성됩니다. API 센서는 옵션입니다.


<br>

## Installation
### Manual
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/seoul_bus/__init__.py`<br>
  `<config directory>/custom_components/seoul_bus/manifest.json`<br>
  `<config directory>/custom_components/seoul_bus/sensor.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>

<br>

```
<br><br>
### 기본 설정값

|옵션|값|
|--|--|
|platform| (필수) seoul_bus |
|api_key| (필수) 서울버스 API KEY |
|api_issued_date| (옵션) API 발급일자. |
|view_type | (옵션) 버스센서 상태에 출력타입 |
|stations| (필수) 센서로 등록할 버스정류장 목록 |

<br>

### API KEY 발급
공공데이터포털에서 정류소정보조회 서비스(<https://www.data.go.kr/data/15000303/openapi.do>)를 발급신청하여 인증키를 발급받습니다.

<br>

### station별 설정값

|옵션|값|
|--|--|
|station_id| (필수) 정류장 고유번호 |
|name| (옵션) 정류장 이름 |
|include_buses| (옵션) 특정 버스만 보고 싶을 경우, 설정 |
|exclude_buses| (옵션) 특정 버스만 빼고 보고 싶을 경우, 설정 |

<br>

### 정류장 고유번호(station_id) 값 확인
- station_id는 정류장 고유번호입니다.
- 서울 버스도착정보 - 버스노선 사이트(<http://bus.go.kr/searchResult6.jsp>)에 접속하여 정류장을 조회하여 ```정류소번호```를 확인합니다.

![screenshot_3](https://github.com/miumida/seoul_bus/blob/master/image/Screenshot_3.png?raw=true)<br>
<br>

### view_type 설정값

|옵션|값|
|--|--|
|S| (디폴트) 버스 센서 state를 초로 표시 |
|M| 버스 센서 state를 00분00초 표시 |
|A| 버스 센서 state를 API msg로 표시 ( 00분00초후[0번째전] )|

<br>

### include_buses/exclude_buses 버스id(노선id)설정값
- include_buses/exclude_buses의 버스id(노선id)를 입력하여 설정한다.
- 서울특별시 버스노선 기본정보 항목정보(<http://data.seoul.go.kr/dataList/OA-15262/F/1/datasetView.do>)에서 버스노스id를 확인하여 입력한다.

<br>

## 참고사이트
[1]서울 버스도착정보 - 버스노선 사이트(<http://bus.go.kr/searchResult6.jsp>)<br>
[2]서울특별시 버스노선 기본정보 항목정보(<http://data.seoul.go.kr/dataList/OA-15262/F/1/datasetView.do>)

[version-shield]: https://img.shields.io/badge/version-v1.4.1-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
