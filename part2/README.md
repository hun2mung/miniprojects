# 미니프로젝트 Part2
기간 - 2023.05.02 ~ 2023.05.16

## WPF 학습
- SCADA 시뮬레이션(SmartHome시스템)
  - C# WPF
  - MahApps.Metro (MetrUI 디자인 라이브러리)
  - Bogus (더미데이터 생성 라이브러리)
  - Newtonsoft.json
  - M2Mqtt(통신 라이브러리)
  - DB 데이터바인딩(MySQL)
  - LiveCharts
  - OxyChart

- SmartHome 시스템 문제점
  - 메모리 남아있는 문제 => 해결
  - 시간이 소요되면 UI 스레드 느려짐 : TextBox에 텍스트 과도로 인함 => 텍스트 줄여 해결!
  - LiveCharts는 대용량 데이터 차트는 무리(LiveChart v.2.0)
  - 대용량 데이터 차는 OxyPlot를 사용

온습도 더미데이터 시뮬레이터, 스마트홈 모니터링 앱

<img src = "https://raw.githubusercontent.com/hun2mung/miniprojects/main/part2/images/SmartHomeMonitoring.gif" width="800">

