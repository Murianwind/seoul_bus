# Seoul Bus Sensor(서울버스)

Seoul Bus Sensor for Home Assistant 입니다.<br>
본 컴포넌트는 [miumida님의 원본 소스](https://github.com/miumida/seoul_bus)를 기반으로 기능 개선 및 UI 설정을 추가한 버전입니다.

- 서울버스 도착정보를 알려줍니다.
- 지정한 정류장에 도착예정인 버스를 확인할 수 있습니다.
- **UI 설정 지원**: 모든 설정을 HA 통합 구성요소 UI에서 진행합니다. (YAML 설정을 지원하지 않습니다.)
- **엔티티 자동 관리**: 설정된 노선에 따라 센서를 자동으로 생성하고 삭제합니다.
- **활성화 스위치**: API 호출을 수동으로 제어할 수 있는 스위치가 제공됩니다. (기존의 자동 시간 설정 대체)

## Version history
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
- HA 설치 경로 아래 `custom_components` 폴더에 `seoul_bus` 패키지 전체를 넣어줍니다.<br>
  `<config directory>/custom_components/seoul_bus/` 내부의 모든 파일 (`__init__.py`, `config_flow.py`, `const.py`, `manifest.json`, `sensor.py`, `switch.py`, `button.py` 등)<br>
- Home Assistant를 재시작합니다.<br>

<br>

## Usage
### 통합구성요소 추가 (UI)
1. Home Assistant 설정 -> 기기 및 서비스 -> 통합구성요소 추가를 누릅니다.
2. `Seoul Bus`를 검색하여 선택합니다.
3. 발급받은 API 키와 정류소 번호(ARS-ID)를 입력합니다.

### 기본 설정값 (UI 진입 시 입력)

|옵션|값|
|--|--|
|api_key| (필수) 서울버스 API KEY |
|station_id| (필수) 정류장 고유번호 (ARS-ID) |

<br>

### API KEY 발급
공공데이터포털에서 **정류소정보조회 서비스**(<https://www.data.go.kr/data/15000303/openapi.do>)를 신청하여 인증키(개인 서비스키)를 발급받습니다.

<br>

### 옵션 설정값 (통합구성요소 구성 후 '옵션' 메뉴에서 수정 가능)

|옵션|값|
|--|--|
|name| (옵션) 표시될 정류장 이름 |
|include_buses| (옵션) 특정 버스만 필터링하여 보고 싶을 경우, 버스 노선 ID 입력 |

<br>

### 정류장 고유번호(station_id) 값 확인
- station_id는 5자리 숫자로 된 정류장 고유번호(ARS-ID)입니다.
- 서울 버스도착정보 - 버스노선 사이트(<http://bus.go.kr/searchResult6.jsp>) 또는 네이버/카카오 지도 등에서 정류장을 조회하여 
http://googleusercontent.com/immersive_entry_chip/0
