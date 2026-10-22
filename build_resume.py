# 이력서 4개 언어(ko/en/ja/zh) HTML 생성 — 웹에서도 보고 A4로 인쇄·PDF도 되게. 개인정보(전화·생년월일·학번) 없음, 회사 일은 추상적으로만.
import html, pathlib

OUT = pathlib.Path(__file__).parent
SITE = {"ko": "index.html", "en": "en.html", "ja": "ja.html", "zh": "zh.html"}
FILE = {"ko": "resume.html", "en": "resume.en.html", "ja": "resume.ja.html", "zh": "resume.zh.html"}

L = {
"ko": dict(
  title="강도현 이력서", name="강도현", name_en="Dohyun Kang", role="직접 개발하고 경험하며 PM의 길을 걷고 있습니다",
  now="Allie Research Inc. · Junior PM · AI/AX", back="포트폴리오", print="PDF로 저장·인쇄",
  sec=dict(sum="요약", exp="경력", proj="프로젝트", edu="학력", award="수상", lic="자격·병역", act="교육·활동", skill="기술"),
  summary="제품·마케팅 기획과 팀 간 조율을 하면서, AI를 활용한 개발도 직접 합니다. 학부 시절 임베디드·차량 통신(C/C++, CAN)에서 시작해 팀장 3회, 수상 4건을 거쳤고, 기획에서 멈추지 않고 직접 만들어 확인하는 PM을 지향합니다.",
  stats=[("3.93 / 4.5","총 학점 (전공 4.05)"),("4건","공모전·학술 수상"),("7회","리더 경험"),("2026.08~","현재 재직")],
  exp=[
   ("Allie Research Inc.","Junior PM · AI/AX","2026.08 – 현재",["기획 — 제품 기획 · 마케팅 기획 · 팀 간 업무 조율","개발 — 메신저 앱 개발 · AI 모델 파인튜닝 · 사내 시스템 자동화"]),
   ("Telechips 아카데미","C/C++ · 저수준 시스템 과정","2026.02 – 2026.05",["C/C++, 시스템 아키텍처, 리눅스 커널 구조, 디바이스 드라이버, 하드웨어 포팅","임베디드 OS 솔루션·미니게임(Allegro) 개발, 디스어셈블리 분석으로 최적화","부트캠프 반장 · 격주 스터디(코드 리뷰·저수준 프로그래밍) 운영"]),
   ("Techways","현장실습 · 시험 자동화","2024.08 – 2025.02",["장비 제어·실시간 그래프·자동 시퀀스 도구 개발 (C#, LabVIEW)","CAN/UDS 진단의 긴 메시지 수신을 흐름 제어·큐 기록으로 개선","현장실습 수기공모전 최우수상"]),
   ("한국알프스 (Korea Alps)","R&D 센터 인턴 · 차량 검증","2024.01 – 2024.02",["CAN/CAN FD 환경에서 차량 스위치 제품 검증 (CANoe, CANalyzer, VT System)","신호 동작·검증 기준 분석, 이슈 관리"]),
   ("고주파 안테나 설계 연구실","학부연구생 · 인천대학교","2022.09 – 2023.12",["농촌진흥청·안동대 산학협력 양봉 IoT 개발 참여","CST 안테나 설계, 28 GHz 전파 측정 (VNA·스펙트럼 분석기)"]),
  ],
  proj=[
   ("빌라 주차 관리 앱","2024.04 – 10 · 팀장(4인)","번호판 인식과 출차 시간 예측으로 빌라 이중 주차 불편을 줄임. 요구사항·화면 설계·ERD 작성, YOLOv8·EasyOCR로 차량·번호판 인식, Django 웹으로 칸별 현황과 예상 출차 시간 제공. 공모전 뒤 혼자 React로 새로 만들고 가우시안 프로세스 예측·Docker·GitHub Actions 배포까지 정리.","ACK 2024 논문 우수상 · 한이음 공모전 입선","Python · Django · React · YOLOv8 · EasyOCR · Docker"),
   ("통신 기능 안전모","2023.05 – 07 · 4인","넘어짐·유해 가스를 감지해 LoRa로 관리자에게 알림. 지그 설계, 센서 회로 납땜, Arduino 펌웨어와 PyQt5 관제 프로그램 작성(최대 6명 동시 모니터링).","산학 캡스톤디자인 은상","Arduino · C/C++ · LoRa · PyQt5"),
   ("양봉 IoT","2022.09 – 2023.12 · 산학협력","농촌진흥청·안동대와 벌통 온습도·가스·무게를 원격 확인. ESP32 펌웨어(ESP-NOW·딥슬립)와 PHP·MySQL 웹 개발, 벌통 3곳 실시간 모니터링.","","ESP32 · PHP · MySQL · CST"),
   ("계측·진단 자동화 도구","2024.08 – 2025.02 · Techways","손으로 하나씩 하던 장비 조작과 진단 확인을 도구로 자동화(전원 → 부하 → 진단 → 기록).","현장실습 수기공모전 최우수상","C# · LabVIEW · CAN/UDS"),
  ],
  edu=[("인천대학교 정보통신공학과 (공학사)","2019.03 – 2025.02","총 학점 3.93 / 4.5 · 전공 4.05 / 4.5")],
  award=[("현장교육실습 수기공모전 최우수상","인천대학교","2025.02"),("ACK 2024 논문 우수상 — Smart Parking System for Villas with Small Parking Spaces","한국정보처리학회 ICT 멘토링 학술대회","2024.11"),("한이음 ICT 멘토링 공모전 입선","한국정보산업연합회","2024.12"),("산학 캡스톤디자인 은상 — 통신 기능 안전모","인천대학교","2023.07")],
  lic=[("정보처리기사","한국산업인력공단","2025.07"),("TOEIC Speaking IM3","","2024.09"),("1종 보통 운전면허","","2022.08"),("육군 만기전역 (병장 · 분대장)","","2020.02 – 2021.08")],
  act=[("차량용 CAN/CAN-FD · Ethernet 교육","성균관대 미래형자동차 사업단","2024.06"),("디지털 3D 프린팅 · 기업가정신 교육","인천대학교","2023"),("프로그래밍 학술 동아리 NULL — 2023 회장, 후배 C/C++ 멘토링","","2019 – 2024"),("대학 풋살 동아리 Chaba — 회장","","2023 – 2024")],
  skill=[("편해요","TypeScript · Python"),("어느 정도","C/C++ · C# · React · Django · MySQL · Docker"),("써 봤어요","LabVIEW · Arduino · PyQt · PHP · AWS EC2")],
),
"en": dict(
  title="Dohyun Kang — Resume", name="Dohyun Kang", name_en="강도현", role="Learning the PM path by building and experiencing things myself",
  now="Allie Research Inc. · Junior PM · AI/AX", back="Portfolio", print="Save / print as PDF",
  sec=dict(sum="Summary", exp="Experience", proj="Projects", edu="Education", award="Awards", lic="Licenses & Service", act="Training & Activities", skill="Skills"),
  summary="I plan products and marketing and coordinate across teams, and I also build with AI myself. Starting from embedded systems and vehicle communication (C/C++, CAN) in university, I led three teams and won four awards. I aim to be a PM who doesn’t stop at planning — I build it and check it myself.",
  stats=[("3.93 / 4.5","GPA (major 4.05)"),("4","Contest & academic awards"),("7","Leadership roles"),("2026.08–","Current role")],
  exp=[
   ("Allie Research Inc.","Junior PM · AI/AX","Aug 2026 – Present",["Planning — product planning · marketing planning · cross-team coordination","Development — messenger app development · AI model fine-tuning · internal system automation"]),
   ("Telechips Academy","C/C++ · Low-level systems program","Feb 2026 – May 2026",["C/C++, system architecture, Linux kernel internals, device drivers, hardware porting","Embedded OS solution and mini-game (Allegro); optimization through disassembly analysis","Bootcamp class representative · ran a biweekly study (code review, low-level programming)"]),
   ("Techways","Work-study · Test automation","Aug 2024 – Feb 2025",["Built equipment control, real-time graph and auto-sequence tools (C#, LabVIEW)","Improved long-message reception in CAN/UDS diagnostics with flow control and queue logging","Grand Prize, Work-study Essay Contest"]),
   ("Korea Alps","R&D Center intern · Vehicle verification","Jan 2024 – Feb 2024",["Verified vehicle switch products in CAN/CAN FD (CANoe, CANalyzer, VT System)","Analyzed signal behavior and verification criteria; issue tracking"]),
   ("High-frequency Antenna Design Lab","Undergraduate researcher · Incheon National University","Sep 2022 – Dec 2023",["Joined a beekeeping IoT industry-academia project with RDA and Andong National University","CST antenna design; 28 GHz measurements (VNA, spectrum analyzer)"]),
  ],
  proj=[
   ("Villa Parking Management App","Apr – Oct 2024 · Team leader (4)","Reduced double-parking inconvenience with plate recognition and exit-time prediction. Wrote requirements, screen design and ERD; YOLOv8 + EasyOCR for vehicles and plates; Django web showing per-slot status and expected exit time. After the contest, rebuilt it alone in React with Gaussian-process prediction, Docker and GitHub Actions deployment.","ACK 2024 Excellence Paper Award · Hanium ICT Mentoring Contest Selected","Python · Django · React · YOLOv8 · EasyOCR · Docker"),
   ("Safety Helmet with Communication","May – Jul 2023 · Team of 4","Detects falls and harmful gas and alerts managers over LoRa. Designed the jig, soldered the sensor circuit, wrote Arduino firmware and a PyQt5 monitor (up to 6 workers at once).","Industry-Academia Capstone Design — Silver","Arduino · C/C++ · LoRa · PyQt5"),
   ("Beekeeping IoT","Sep 2022 – Dec 2023 · Industry-academia","Remote view of hive temperature, humidity, gas and weight with RDA and Andong National University. ESP32 firmware (ESP-NOW, deep sleep) and PHP·MySQL web; real-time monitoring of 3 hives.","","ESP32 · PHP · MySQL · CST"),
   ("Measurement & Diagnostics Automation","Aug 2024 – Feb 2025 · Techways","Automated manual equipment handling and diagnostic checks (power → load → diagnosis → logging).","Grand Prize, Work-study Essay Contest","C# · LabVIEW · CAN/UDS"),
  ],
  edu=[("B.Eng., Information & Telecommunication Engineering — Incheon National University","Mar 2019 – Feb 2025","GPA 3.93 / 4.5 · Major 4.05 / 4.5")],
  award=[("Grand Prize, Work-study Essay Contest","Incheon National University","Feb 2025"),("Excellence Paper Award, ACK 2024 — Smart Parking System for Villas with Small Parking Spaces","KIPS ICT Mentoring Conference","Nov 2024"),("Hanium ICT Mentoring Contest — Selected","KAIT","Dec 2024"),("Industry-Academia Capstone Design Silver — Safety Helmet with Communication","Incheon National University","Jul 2023")],
  lic=[("Engineer Information Processing","HRD Korea","Jul 2025"),("TOEIC Speaking IM3","","Sep 2024"),("Class 1 Driver’s License","","Aug 2022"),("Army, honorable discharge (Sergeant · squad leader)","","Feb 2020 – Aug 2021")],
  act=[("Automotive CAN/CAN-FD · Ethernet training","Sungkyunkwan Univ. Future Automotive Program","Jun 2024"),("Digital 3D printing · Entrepreneurship training","Incheon National University","2023"),("Programming club NULL — 2023 president, C/C++ mentoring","","2019 – 2024"),("University futsal club Chaba — president","","2023 – 2024")],
  skill=[("Comfortable","TypeScript · Python"),("Working knowledge","C/C++ · C# · React · Django · MySQL · Docker"),("Have used","LabVIEW · Arduino · PyQt · PHP · AWS EC2")],
),
"ja": dict(
  title="カン・ドヒョン 履歴書", name="カン・ドヒョン", name_en="Dohyun Kang", role="自ら開発し経験しながら、PMの道を歩んでいます",
  now="Allie Research Inc. · Junior PM · AI/AX", back="ポートフォリオ", print="PDF保存・印刷",
  sec=dict(sum="要約", exp="職歴", proj="プロジェクト", edu="学歴", award="受賞", lic="資格・兵役", act="研修・活動", skill="スキル"),
  summary="製品・マーケティングの企画とチーム間の調整を行いながら、AIを活用した開発も自分で行います。学部時代は組込み・車載通信(C/C++、CAN)から始め、チームリーダー3回、受賞4件を経験しました。企画で終わらず、自分で作って確かめるPMを目指しています。",
  stats=[("3.93 / 4.5","GPA(専攻 4.05)"),("4件","コンテスト・学術受賞"),("7回","リーダー経験"),("2026.08~","現職")],
  exp=[
   ("Allie Research Inc.","Junior PM · AI/AX","2026.08 – 現在",["企画 — 製品企画 · マーケティング企画 · チーム間調整","開発 — メッセンジャーアプリ開発 · AIモデルのファインチューニング · 社内システム自動化"]),
   ("Telechips アカデミー","C/C++ · 低レベルシステム課程","2026.02 – 2026.05",["C/C++、システムアーキテクチャ、Linuxカーネル構造、デバイスドライバ、ハードウェア移植","組込みOSソリューション・ミニゲーム(Allegro)開発、逆アセンブル分析で最適化","ブートキャンプ班長 · 隔週勉強会(コードレビュー・低レベルプログラミング)運営"]),
   ("Techways","現場実習 · 試験自動化","2024.08 – 2025.02",["機器制御・リアルタイムグラフ・自動シーケンスツール開発(C#、LabVIEW)","CAN/UDS診断の長いメッセージ受信をフロー制御・キュー記録で改善","現場実習手記コンテスト 最優秀賞"]),
   ("韓国アルプス (Korea Alps)","R&Dセンター インターン · 車両検証","2024.01 – 2024.02",["CAN/CAN FD環境で車載スイッチ製品を検証(CANoe、CANalyzer、VT System)","信号動作・検証基準の分析、課題管理"]),
   ("高周波アンテナ設計研究室","学部研究生 · 仁川大学","2022.09 – 2023.12",["農村振興庁・安東大学との産学協力 養蜂IoT開発に参加","CSTアンテナ設計、28 GHz電波測定(VNA・スペクトラムアナライザ)"]),
  ],
  proj=[
   ("ヴィラ駐車管理アプリ","2024.04 – 10 · チームリーダー(4名)","ナンバー認識と出庫時間予測で、ヴィラの二重駐車の不便を軽減。要件・画面設計・ERDを作成し、YOLOv8・EasyOCRで車両とナンバーを認識、Django Webで区画別状況と予想出庫時間を提供。コンテスト後に一人でReactで再構築し、ガウス過程予測・Docker・GitHub Actionsで配備まで整備。","ACK 2024 論文優秀賞 · ハニウム公募展 入選","Python · Django · React · YOLOv8 · EasyOCR · Docker"),
   ("通信機能付き安全帽","2023.05 – 07 · 4名","転倒と有害ガスを検知し、LoRaで管理者に通知。治具設計、センサ回路のはんだ付け、ArduinoファームウェアとPyQt5 管制プログラムを作成(最大6名同時監視)。","産学キャップストーンデザイン 銀賞","Arduino · C/C++ · LoRa · PyQt5"),
   ("養蜂IoT","2022.09 – 2023.12 · 産学協力","農村振興庁・安東大学と巣箱の温湿度・ガス・重量を遠隔確認。ESP32ファームウェア(ESP-NOW・ディープスリープ)とPHP·MySQL Webを開発、巣箱3か所をリアルタイム監視。","","ESP32 · PHP · MySQL · CST"),
   ("計測・診断自動化ツール","2024.08 – 2025.02 · Techways","手作業だった機器操作と診断確認をツールで自動化(電源 → 負荷 → 診断 → 記録)。","現場実習手記コンテスト 最優秀賞","C# · LabVIEW · CAN/UDS"),
  ],
  edu=[("仁川大学 情報通信工学科(工学士)","2019.03 – 2025.02","GPA 3.93 / 4.5 · 専攻 4.05 / 4.5")],
  award=[("現場教育実習 手記コンテスト 最優秀賞","仁川大学","2025.02"),("ACK 2024 論文優秀賞 — Smart Parking System for Villas with Small Parking Spaces","韓国情報処理学会 ICTメンタリング学術大会","2024.11"),("ハニウムICTメンタリング公募展 入選","韓国情報産業連合会","2024.12"),("産学キャップストーンデザイン 銀賞 — 通信機能付き安全帽","仁川大学","2023.07")],
  lic=[("情報処理技師","韓国産業人力公団","2025.07"),("TOEIC Speaking IM3","","2024.09"),("普通自動車運転免許(1種)","","2022.08"),("陸軍 満期除隊(兵長 · 分隊長)","","2020.02 – 2021.08")],
  act=[("車載CAN/CAN-FD · Ethernet 研修","成均館大学 未来型自動車事業団","2024.06"),("デジタル3Dプリンティング · 起業家精神教育","仁川大学","2023"),("プログラミングサークル NULL — 2023年会長、後輩へC/C++指導","","2019 – 2024"),("大学フットサルサークル Chaba — 会長","","2023 – 2024")],
  skill=[("得意","TypeScript · Python"),("ある程度","C/C++ · C# · React · Django · MySQL · Docker"),("使った経験","LabVIEW · Arduino · PyQt · PHP · AWS EC2")],
),
"zh": dict(
  title="姜道贤 简历", name="姜道贤", name_en="Dohyun Kang", role="亲自开发、亲身体验，走在PM之路上",
  now="Allie Research Inc. · Junior PM · AI/AX", back="作品集", print="保存/打印为PDF",
  sec=dict(sum="概要", exp="经历", proj="项目", edu="学历", award="获奖", lic="资格·兵役", act="培训·活动", skill="技能"),
  summary="我负责产品与营销策划及跨团队协调，同时也亲自用AI进行开发。大学期间从嵌入式与车载通信(C/C++、CAN)起步，担任过3次组长，获得4项奖项。我希望做一名不止于策划、亲手做出来并验证的PM。",
  stats=[("3.93 / 4.5","总绩点(专业 4.05)"),("4项","竞赛·学术获奖"),("7次","领导经历"),("2026.08~","现任职")],
  exp=[
   ("Allie Research Inc.","Junior PM · AI/AX","2026.08 – 至今",["策划 — 产品策划 · 营销策划 · 跨团队协调","开发 — 即时通讯应用开发 · AI模型微调 · 内部系统自动化"]),
   ("Telechips 学院","C/C++ · 底层系统课程","2026.02 – 2026.05",["C/C++、系统架构、Linux内核结构、设备驱动、硬件移植","嵌入式OS方案与小游戏(Allegro)开发，通过反汇编分析优化","训练营班长 · 运营双周学习会(代码评审·底层编程)"]),
   ("Techways","实习 · 测试自动化","2024.08 – 2025.02",["开发设备控制、实时图表、自动序列工具(C#、LabVIEW)","用流控与队列记录改善CAN/UDS诊断中的长消息接收","现场实习征文比赛 最优秀奖"]),
   ("韩国阿尔卑斯 (Korea Alps)","R&D中心实习 · 车辆验证","2024.01 – 2024.02",["在CAN/CAN FD环境验证车载开关产品(CANoe、CANalyzer、VT System)","分析信号行为与验证标准，管理问题"]),
   ("高频天线设计实验室","本科研究生 · 仁川大学","2022.09 – 2023.12",["参与农村振兴厅·安东大学产学合作养蜂IoT开发","CST天线设计，28 GHz电波测量(VNA·频谱分析仪)"]),
  ],
  proj=[
   ("别墅停车管理应用","2024.04 – 10 · 组长(4人)","通过车牌识别与出车时间预测，减轻别墅双排停车的不便。编写需求·界面设计·ERD，用YOLOv8·EasyOCR识别车辆与车牌，Django网站提供车位状态与预计出车时间。比赛后独立用React重做，并完成高斯过程预测、Docker、GitHub Actions部署。","ACK 2024 论文优秀奖 · Hanium竞赛入选","Python · Django · React · YOLOv8 · EasyOCR · Docker"),
   ("通信功能安全帽","2023.05 – 07 · 4人","检测跌倒与有害气体，通过LoRa通知管理员。设计夹具、焊接传感器电路，编写Arduino固件与PyQt5监控程序(最多同时监控6人)。","产学Capstone设计 银奖","Arduino · C/C++ · LoRa · PyQt5"),
   ("养蜂IoT","2022.09 – 2023.12 · 产学合作","与农村振兴厅·安东大学远程查看蜂箱温湿度、气体、重量。开发ESP32固件(ESP-NOW·深度睡眠)与PHP·MySQL网站，实时监控3个蜂箱。","","ESP32 · PHP · MySQL · CST"),
   ("测量·诊断自动化工具","2024.08 – 2025.02 · Techways","将手动设备操作与诊断确认自动化(电源 → 负载 → 诊断 → 记录)。","现场实习征文比赛 最优秀奖","C# · LabVIEW · CAN/UDS"),
  ],
  edu=[("仁川大学 信息通信工程系(工学学士)","2019.03 – 2025.02","总绩点 3.93 / 4.5 · 专业 4.05 / 4.5")],
  award=[("现场教育实习征文比赛 最优秀奖","仁川大学","2025.02"),("ACK 2024 论文优秀奖 — Smart Parking System for Villas with Small Parking Spaces","韩国信息处理学会 ICT导师学术大会","2024.11"),("Hanium ICT导师竞赛 入选","韩国信息产业联合会","2024.12"),("产学Capstone设计 银奖 — 通信功能安全帽","仁川大学","2023.07")],
  lic=[("信息处理工程师","韩国产业人力公团","2025.07"),("TOEIC Speaking IM3","","2024.09"),("1种普通驾驶执照","","2022.08"),("陆军 服役期满退伍(上士 · 班长)","","2020.02 – 2021.08")],
  act=[("车载CAN/CAN-FD · Ethernet 培训","成均馆大学 未来汽车事业团","2024.06"),("数字3D打印 · 创业精神教育","仁川大学","2023"),("编程社团 NULL — 2023年会长，指导学弟C/C++","","2019 – 2024"),("大学足球社团 Chaba — 会长","","2023 – 2024")],
  skill=[("熟练","TypeScript · Python"),("较熟悉","C/C++ · C# · React · Django · MySQL · Docker"),("用过","LabVIEW · Arduino · PyQt · PHP · AWS EC2")],
),
}

CSS = """
:root{--bg:#ECEEF2;--paper:#fff;--ink:#1A1D23;--sub:#4A5260;--faint:#7F8794;--line:#DADEE5;--accent:#2F47C6;--soft:#E4E8F8}
@media (prefers-color-scheme:dark){:root{--bg:#24272E;--paper:#2D3139;--ink:#F2F4F7;--sub:#C3C9D2;--faint:#8F97A3;--line:#3B4049;--accent:#A3B4FF;--soft:#343C5C}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 -apple-system,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo","Noto Sans JP","Noto Sans SC",system-ui,sans-serif;word-break:keep-all}
a{color:inherit;text-decoration:none}
.bar{max-width:880px;margin:0 auto;padding:14px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar a,.bar button{font:inherit;font-size:13px;font-weight:600;border:0;background:var(--paper);color:var(--sub);padding:7px 14px;border-radius:999px;cursor:pointer;box-shadow:0 1px 2px rgba(0,0,0,.08)}
.bar .sp{flex:1}
.bar a[aria-current]{background:var(--ink);color:var(--bg)}
.page{max-width:880px;margin:0 auto 60px;background:var(--paper);padding:44px 48px;border-radius:14px;box-shadow:0 14px 34px -18px rgba(26,29,35,.3)}
header.h{display:flex;justify-content:space-between;gap:20px;align-items:flex-end;border-bottom:3px solid var(--accent);padding-bottom:16px}
h1{margin:0;font-size:32px;letter-spacing:-.02em;line-height:1.2}
h1 small{font-size:16px;color:var(--faint);font-weight:500;margin-left:8px}
.role{margin:6px 0 0;color:var(--sub)}
.now{margin:4px 0 0;font-size:13px;color:var(--accent);font-weight:700}
.ct{text-align:right;font-size:13px;color:var(--sub);line-height:1.8}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:18px 0 4px}
.stats div{background:var(--soft);border-radius:10px;padding:10px 12px}
.stats b{display:block;font-size:19px;color:var(--accent);line-height:1.3}
.stats span{font-size:12px;color:var(--sub)}
h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:26px 0 10px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.sum{margin:0}
.it{display:grid;grid-template-columns:1fr auto;gap:2px 16px;padding:9px 0;border-bottom:1px dashed var(--line)}
.it:last-child{border-bottom:0}
.it h3{margin:0;font-size:15px}
.it h3 em{font-style:normal;font-weight:500;color:var(--sub);font-size:13.5px;margin-left:6px}
.when{font-size:13px;color:var(--faint);text-align:right;white-space:nowrap}
.it ul{grid-column:1/-1;margin:4px 0 0;padding-left:18px;color:var(--sub);font-size:14px}
.it p{grid-column:1/-1;margin:4px 0 0;color:var(--sub);font-size:14px}
.tag{display:inline-block;justify-self:start;margin-top:5px;font-size:12px;font-weight:700;color:var(--accent);background:var(--soft);padding:2px 9px;border-radius:999px}
.stack{display:block;font-size:12px;color:var(--faint);margin-top:4px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:0 32px}
.row{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px dashed var(--line);font-size:14px}
.row small{display:block;color:var(--faint);font-size:12.5px}
.row .d{color:var(--faint);font-size:13px;white-space:nowrap}
.sk{display:grid;grid-template-columns:110px 1fr;gap:4px 12px;font-size:14px}
.sk b{color:var(--sub)}
@media (max-width:700px){.page{padding:26px 20px;border-radius:0}.stats{grid-template-columns:1fr 1fr}.two{grid-template-columns:1fr}header.h{display:block}.ct{text-align:left;margin-top:10px}}
@media print{@page{size:A4;margin:12mm}body{background:#fff;font-size:11px}.bar{display:none}.page{box-shadow:none;border-radius:0;padding:0;max-width:none;margin:0}h1{font-size:26px}.it,.row{break-inside:avoid}h2{break-after:avoid;margin-top:16px}.stats b{font-size:15px}.it ul,.it p{font-size:11px}.tag{border:1px solid var(--accent)}}
"""

def e(s): return html.escape(s, quote=False)

def build(lg):
    d = L[lg]; s = d["sec"]
    cur = ' aria-current="page"'
    langnav = "".join('<a href="%s"%s>%s</a>' % (FILE[k], cur if k==lg else "", n) for k, n in [("ko","KO"),("en","EN"),("ja","JA"),("zh","中文")])
    exp = "".join(f'<div class="it"><h3>{e(a)}<em>{e(b)}</em></h3><span class="when">{e(c)}</span><ul>{"".join(f"<li>{e(x)}</li>" for x in ls)}</ul></div>' for a,b,c,ls in d["exp"])
    proj = "".join(f'<div class="it"><h3>{e(a)}<em>{e(b)}</em></h3><span></span><p>{e(c)}</p>' + (f'<span class="tag">🏆 {e(t)}</span>' if t else '') + f'<span class="stack">{e(st)}</span></div>' for a,b,c,t,st in d["proj"])
    def rows(items): return "".join(f'<div class="row"><div>{e(a)}' + (f'<small>{e(b)}</small>' if b else '') + f'</div><span class="d">{e(c)}</span></div>' for a,b,c in items)
    edu = "".join(f'<div class="row"><div>{e(a)}<small>{e(c)}</small></div><span class="d">{e(b)}</span></div>' for a,b,c in d["edu"])
    stats = "".join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a,b in d["stats"])
    skill = "".join(f'<b>{e(a)}</b><span>{e(b)}</span>' for a,b in d["skill"])
    return f"""<!doctype html>
<html lang="{lg}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d["title"])}</title>
<meta name="description" content="{e(d["role"])}">
<style>{CSS}</style>
</head>
<body>
<div class="bar"><a href="{SITE[lg]}">← {e(d["back"])}</a><span class="sp"></span>{langnav}<button type="button" onclick="window.print()">{e(d["print"])}</button></div>
<main class="page">
<header class="h"><div><h1>{e(d["name"])}<small>{e(d["name_en"])}</small></h1><p class="role">{e(d["role"])}</p><p class="now">{e(d["now"])}</p></div>
<div class="ct">kid708502@gmail.com<br>gulpo1@naver.com<br>dohyunkang.github.io<br>github.com/DohyunKang</div></header>
<div class="stats">{stats}</div>
<h2>{s["sum"]}</h2><p class="sum">{e(d["summary"])}</p>
<h2>{s["exp"]}</h2>{exp}
<h2>{s["proj"]}</h2>{proj}
<h2>{s["edu"]}</h2>{edu}
<h2>{s["award"]}</h2>{rows(d["award"])}
<div class="two"><div><h2>{s["lic"]}</h2>{rows(d["lic"])}</div><div><h2>{s["act"]}</h2>{rows(d["act"])}</div></div>
<h2>{s["skill"]}</h2><div class="sk">{skill}</div>
</main>
</body>
</html>
"""

for lg in L:
    (OUT / FILE[lg]).write_text(build(lg), encoding="utf-8")
    print("wrote", FILE[lg])
