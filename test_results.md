(venv) mvhoang@Nitro-AN515-57:~/Desktop/day4/Lab4-AI-Agent-LangGraph$ python agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: xin chào, tôi muốn đi du lịch nhưng chưa biết đi đâu

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn muốn đi du lịch. Việt Nam có rất nhiều điểm đến hấp dẫn. Bạn có thể thích khám phá các thành phố lớn như Hà Nội, Hồ Chí Minh, hoặc tận hưởng vẻ đẹp thiên nhiên ở Đà Nẵng, Nha Trang, Phú Quốc.

Bạn đã có ý tưởng nào về điểm đến chưa, hoặc có ngân sách cụ thể nào không? Ngoài ra, có bao nhiêu người sẽ đi cùng bạn và bạn dự định đi trong khoảng thời gian nào? Hãy cho mình biết để mình có thể tư vấn tốt hơn nhé!

Bạn: quit
(venv) mvhoang@Nitro-AN515-57:~/Desktop/day4/Lab4-AI-Agent-LangGraph$ python agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: tìm cho tôi chuyến bay từ hà nội đến đà nẵng

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Chuyến bay từ Hà Nội đến Đà Nẵng hiện có các lựa chọn như sau:

- **Vietnam Airlines (economy)**: 06:00 -> 07:20 | **Giá**: 1.450.000đ
- **Vietnam Airlines (business)**: 14:00 -> 15:20 | **Giá**: 2.800.000đ
- **VietJet Air (economy)**: 08:30 -> 09:50 | **Giá**: 890.000đ
- **Bamboo Airways (economy)**: 11:00 -> 12:20 | **Giá**: 1.200.000đ

Bạn dự định đi vào thời gian nào và có bao nhiêu người đi cùng? Mình có thể giúp bạn tìm khách sạn hoặc các hoạt động thú vị tại Đà Nẵng!

Bạn: quit

(venv) mvhoang@Nitro-AN515-57:~/Desktop/day4/Lab4-AI-Agent-LangGraph$ python agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: tôi ở hà nội, muốn đi phú quốc 2 đêm, ngân sách 7 triệu, tư vắn cho tôi

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 3500000})
Trả lời trực tiếp

TravelBuddy: Chuyến bay:
- Bạn có nhiều lựa chọn chuyến bay từ Hà Nội đến Phú Quốc:
  - Vietnam Airlines (economy): 07:00 -> 09:15 | Giá: 2.100.000đ
  - VietJet Air (economy): 10:00 -> 12:15 | Giá: 1.350.000đ
  - VietJet Air (economy): 16:00 -> 18:15 | Giá: 1.100.000đ

Khách sạn:
- Dưới đây là một số lựa chọn khách sạn tại Phú Quốc:
  - Vinpearl Resort (⭐⭐⭐⭐⭐) | Giá: 3.500.000đ | Khu vực: Bãi Dài
  - Sol by Meliá (⭐⭐⭐⭐) | Giá: 1.500.000đ | Khu vực: Bãi Trường
  - Lahana Resort (⭐⭐⭐) | Giá: 800.000đ | Khu vực: Dương Đông

Tổng chi phí ước tính khoản lớn nhất:
- Với Vinpearl Resort: 2.100.000đ (vé máy bay) + 3.500.000đ (khách sạn) = 5.600.000đ
- Với Sol by Meliá: 1.350.000đ (vé máy bay) + 1.500.000đ (khách sạn) = 2.850.000đ
- Với Lahana Resort: 1.100.000đ (vé máy bay) + 800.000đ (khách sạn) = 1.900.000đ

Gợi ý thêm:
Với ngân sách 7 triệu, bạn có thể thoải mái chọn lựa chuyến bay và khách sạn phù hợp. Bạn có đi cùng ai không? Và muốn tham gia các hoạt động gì tại Phú Quốc như bãi biển, tour khám phá, hay nhà hàng đặc sản?

Bạn: quit
(venv) mvhoang@Nitro-AN515-57:~/Desktop/day4/Lab4-AI-Agent-LangGraph$ python agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chắc chắn rồi! Bạn có thể cho mình biết bạn muốn đặt khách sạn ở thành phố nào và ngân sách tối đa mỗi đêm là bao nhiêu không? Thời gian bạn dự định nghỉ lại bao lâu?

Bạn: quit
(venv) mvhoang@Nitro-AN515-57:~/Desktop/day4/Lab4-AI-Agent-LangGraph$ python agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: dạy tôi về linked list  

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Xin lỗi, nhưng tôi chỉ chuyên về du lịch và không thể giúp bạn với yêu cầu này. Nếu bạn cần thông tin về các chuyến đi, khách sạn hay hoạt động vui chơi, hãy cho tôi biết! 

Bạn có kế hoạch đi đâu không?

Bạn: quit