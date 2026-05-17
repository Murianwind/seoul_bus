# Seoul Bus Sensor(서울버스)

Seoul Bus Sensor for Home Assistant 입니다.<br>
본 컴포넌트는 [miumida님의 원본 소스](https://github.com/miumida/seoul_bus)를 기반으로 기능 개선 및 UI 설정을 추가한 버전입니다.

- 서울버스 도착정보를 알려줍니다.
- 지정한 정류장에 도착예정인 버스를 확인할 수 있습니다.
- **UI 설정 지원**: 모든 설정을 HA 통합 구성요소 UI에서 진행합니다.
- **엔티티 자동 관리**: 설정된 노선에 따라 센서를 자동으로 생성하고 삭제합니다.
- **활성화 스위치**: API 호출을 수동으로 제어할 수 있는 스위치가 제공됩니다. (기존의 자동 시간 설정 대체)

<br>
# Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0    | 2020.01.15  | First version  |
| v1.1    | 2020.01.16  | Exception 처리 추가. API 오류코드/메세지 표시  |
| v1.2    | 2020.01.20  | xml2dict 문제점 보완. 정류장센서 update_time 구간만 상태반영  |
| v1.3    | 2020.04.21  | 정류장/버스센서 update_time 구간 상태반영 수정.  |
| v1.4    | 2020.04.21  | 버스센서 속성명 변경  |
| v1.4.1  | 2021.10.24  | manifest.json add version info  |
| v2.0.0  | 2024.05.16  | Config Flow(UI 설정) 도입, 시간 설정 제거 및 활성화 스위치 추가 |
| v2.3.4  | 2024.05.17  | 새로고침 버튼 추가, 엔티티 ID 최적화 및 불필요 엔티티 자동 삭제 로직 개선 |

<br>

## Credits
Special thanks to **miumida** for the original [seoul_bus](https://github.com/miumida/seoul_bus) component. This version is a functional fork focused on UI integration and dynamic API control.

## Installation
### Manual
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/seoul_bus/__init__.py`<br>
  `<config directory>/custom_components/seoul_bus/manifest.json`<br>
  `<config directory>/custom_components/seoul_bus/sensor.py`<br>
- Home-Assistant 를 재시작합니다<br>

<br>

## Usage
### 통합구성요소 추가 (UI)
1. Home Assistant 설정 -> 기기 및 서비스 -> 통합구성요소 추가를 누릅니다.
2. `Seoul Bus`를 검색하여 선택합니다.
3. 발급받은 API 키와 정류소 번호(ARS-ID)를 입력합니다.

### 기본 설정값

|옵션|값|
|--|--|
|api_key| (필수) 서울버스 API KEY |
|station_id| (필수) 정류장 고유번호 |

<br>

### API KEY 발급
공공데이터포털에서 정류소정보조회 서비스(<https://www.data.go.kr/data/15000303/openapi.do>)를 발급신청하여 인증키를 발급받습니다.

<br>

### station별 설정값

|옵션|값|
|--|--|
|name| (옵션) 정류장 이름 |
|include_buses| (옵션) 특정 버스만 보고 싶을 경우, 설정 |

<br>

### 정류장 고유번호(station_id) 값 확인
- station_id는 정류장 고유번호입니다.
- 서울 버스도착정보 - 버스노선 사이트(<http://bus.go.kr/searchResult6.jsp>)에 접속하여 정류장을 조회하여 ```정류소번호```를 확인합니다.

<br>

### include_buses/exclude_buses 버스id(노선id)설정값
- include_buses/exclude_buses의 버스id(노선id)를 입력하여 설정한다.
- 서울특별시 버스노선 기본정보 항목정보(<http://data.seoul.go.kr/dataList/OA-15262/F/1/datasetView.do>)에서 버스노스id를 확인하여 입력한다.

<br>

## 참고사이트
[1]서울 버스도착정보 - 버스노선 사이트(<http://bus.go.kr/searchResult6.jsp>)<br>
[2]서울특별시 버스노선 기본정보 항목정보(<http://data.seoul.go.kr/dataList/OA-15262/F/1/datasetView.do>)

[version-shield]: https://img.shields.io/badge/version-v2.3.4-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
