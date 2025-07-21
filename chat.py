import re
def get_response(user_message):# Xử lý tin nhắn đầu vào
    #lower chuyển toàn bộ ký tự trong chuỗi sang chữ thường
    #strip loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi

    user_message = user_message.lower().strip()
     #chuẩn hóa khoảng trắng trong chuỗi đầu vào bằng cách thay thế tất cả các khoảng trắng liên tiếp bằng 1 khoảng trắng duy nhất
    user_message = re.sub(r'\s+', ' ', user_message)


    # Dữ liệu từ khóa và câu trả lời
    responses = {
        ("ban giám hiệu hiện tại", "ban giám hiệu", "lãnh đạo", "phó hiệu trưởng", "hiệu trưởng"): "Ban giám hiệu hiện tại: <br>1) Hiệu Trưởng: PGS.TS. Nguyễn Tất Toàn<br>2) Phó Hiệu Trưởng: TS. Trần Đình Lý<br>3) Phó Hiệu Trưởng: PGS.TS Phan Tại Huân",
        ("cảm ơn", "thank you", "thanks"): "Không có gì, rất vui được giúp đỡ bạn",
        ("chào", "xin chào", "bắt đầu", "hi", "hello"): "Xin chào! Tôi có thể giúp gì cho bạn?",
        ("có bao nhiêu khoa", "khoa", "các khoa ở trường"): "Tính đến năm 2024 có 12 khoa bao gồm: <br>1) Cơ khí – Công nghệ <br>2) Công nghệ thông tin <br>3) Quản lý đất đai và Bất động sản <br>4) Lâm nghiệp <br>5) Công nghệ hóa học và thực phẩm <br>6) Chăn nuôi – Thú y <br>7) Nông học <br>8) Công nghệ sinh học <br>9) Môi trường và Tài nguyên <br>10) Thủy sản <br>11) Ngoại ngữ - Sư phạm <br>12) Kinh tế",
        ("có bao nhiêu ngành đào tạo", "ngành đào tạo", "ngành"): "Tính đến năm 2024 trường có 35 ngành đào tạo",
        ("cơ sở đào tạo", "địa chỉ", "cơ sở"): "Cơ sở chính tại TPHCM tọa lạc trên khu đất rộng 118 ha, thuộc Khu phố 6, Phường Linh Trung, thành phố Thủ Đức, Thành phố Hồ Chí Minh và thành phố Dĩ An, Tỉnh Bình Dương, ngoài ra có 2 phân hiệu tại Ninh Thuận và Gia Lai",
        ("số tín chỉ mỗi học kì","tín chỉ","tín chỉ tối đa","tín chỉ tối thiểu"): "Số tín chỉ mỗi sinh viên có thể đăng kí học mỗi học kì là: <br>Tối thiểu là 14 tín chỉ, tối đa là 28 tín chỉ",
        ("ca học hàng ngày", "mỗi ngày có bao nhiêu ca học","ca học", "giờ các ca học", "giờ học"): "Mỗi ngày có 5 ca học:<br> Ca 1 từ 7 giờ đến 9 giờ 30 phút<br> Ca 2 từ 9 giờ 35 phút đến 12 giờ 05 phút<br> Ca 3 từ 12 giờ 15 phút đến 14 giờ 45 phút<br> Ca 4 từ 14 giờ 50 phút đến 17 giờ 20 phút<br> Ca 5 từ 17 giờ 30 phút đến 20 giờ",
        ("mỗi ca học bao nhiêu tiếng", "thời gian", "mỗi ca học bao nhiêu phút"): "Mỗi ca kéo dài 3 tiết, mỗi tiết có 50 phút",
        ("ca đầu tiên bắt đầu lúc mấy giờ", "bắt đầu học","mấy giờ học"): "Trường sẽ bắt đầu học lúc 7 giờ sáng ",
        ("xếp loại điểm học phần trên thang điểm 4", "thang điểm 4", "1"): "Xếp loại điểm học phần trên thang điểm 4: <br>Điểm A: 4,0 <br>Điểm B+: 3,5 <br>Điểm B: 3,0 <br>Điểm C+: 2,5 <br>Điểm C: 2,0 <br>Điểm D+: 1,5 <br>Điểm D: 1 <br>Điểm F: 0",
        ("xếp loại điểm học phần trên thang điểm 10", "thang điểm 10", "2"): "Xếp loại điểm học phần trên thang điểm 10 <br>Điểm A: 8,5-10,0 <br>Điểm B+: 8,0-8,4 <br>Điểm B: 7,0-7,9 <br>Điểm C+: 6,5-6,9 <br>Điểm C: 5,5-6,4 <br>Điểm D+: 5,0-5,4 <br>Điểm D: 4,0-4,9 <br>Điểm F: <4,0",
        ("cần phải đạt tối thiểu bao nhiêu điểm mỗi môn", "qua môn", "số điểm cần đạt"): "Phải đạt từ 4,0 trở lên đối với thang điểm 4. Với các học phần cốt lõi cần đạt từ 5,5 trở lên",
        ("xếp loại học lực", "học lực", "3"): "Xếp loại học lực sẽ được tính theo điểm trung bình chung học kỳ (ĐTBCHK), Điểm trung bình chung năm học (ĐTBCNH), hoặc Điểm trung bình chung tích lũy (ĐTBCTL): <br>3,6-4,0: Xuất sắc <br>3,2-3,59: Giỏi <br>2,5-3,19: Khá <br>2,0-2,49: Trung Bình <br>1,0-1,99: Yếu",
        ("xếp loại tốt nghiệp", "tốt nghiệp", "4"): "Xếp loại tốt nghiệp được căn cứ vào Điểm trung bình chung tích lũy (ĐTBCTL) <br>Loại Xuất Sắc: ĐTBCTL từ 3,6-4,0 <br>Loại Giỏi: ĐTBCTL từ 3,2-3,59 <br>Loại Khá: ĐTBCTL từ 2,5-3,19 <br>Loại Trung Bình: ĐTBCTL từ 2,0-2,49 <br>Đối với loại Xuất Sắc và loại Giỏi, hạng tốt nghiệp sẽ bị giảm một mức nếu rơi vào một trong các trường hợp sau: <br>- Có khối lượng các học phần học lại (chỉ tính học phần bắt buộc) vượt quá 5% tổng số tín chỉ quy định cho toàn Chương trình đào tạo <br>- Đã bị kỷ luật từ mức cảnh cáo trở lên trong thời gian học ",
        ("điểm rèn luyện","phân loại điểm rèn luyện","ĐRL","phân loại ĐRL","đánh giá đrl","đánh giá điểm rèn luyện"):"<br> Xuất sắc: Từ 90 đến 100 điểm<br> Tốt: T 80 đến < 90 điểm<br> Khá: Từ 65 đến < 80 điểm<br> Trung bình: Từ 50 đến < 65 điểm<br> Yếu: Từ 35 đến < 50 điểm<br> Kém: Dưới 35 điểm",
        ("các khu giảng đường, phòng chức năng ở trường", "giảng đường", "phòng chức năng","tòa"): "Trường có tổng cộng 6 giảng đường như: Phượng Vỹ, Thiên Lý, Rạng Đông, Tường Vy, Cát Tường, Hướng Dương và Cẩm Tú. Và các khu phòng chức năng như: Phòng Đào tạo, Phòng CTSV, Phòng Hành chính,...",
        ("clb", "câu lạc bộ", "đội", "nhóm","đội nhóm"): "Trường gồm nhiều CLB, đội nhóm như:<br>"
                                              "1. CLB Cán Bộ Đoàn Ngôi Sao Xanh<br>"
                                              "2. BEC English Club<br>"
                                              "3. CLB Bóng rổ đại học Nông Lâm<br>"
                                              "4. CLB Du lịch sinh thái<br>"
                                              "5. CLB Dược thú y<br>"
                                              "6. CLB Đồng hành-AC<br>"
                                              "7. FIRE English Club<br>"
                                              "8. CLB Học thuật-Kỹ năng quản trị (B.A.S) <br>"
                                              "9. CLB KARATE-DO<br>"
                                              "10. CLB Kết nối thành công<br>"
                                              "11. CLB Khởi nghiệp (NLU Startup Club) NSC<br>"
                                              "12. CLB Một sức khỏe TP.HCM (HCMC One Health Club)<br>"
                                              "13. CLB Sách và hành động Nông Lâm TP.HCM<br>"
                                              "14. CLB Tiếng anh khoa công nghệ hóa học và thực phẩm (Seeds For Future) SFF<br>"
                                              "15. CLB Tiếng anh khoa kinh tế EFB (English For Business Club) EFB<br>"
                                              "16. CLB Thể thao điện tử PWF-CLB PWF Gaming<br>"
                                              "17. CLB Thú y Engscope<br>"
                                              "18. CLB Truyền thông Nông Lâm Radio<br>"
                                              "19. WILDLIFE VET STUDENT CLUB<br>"
                                              "20. CLB Yêu môi trường<br>"
                                              "21. Tổ tu dưỡng rèn luyện hạt giống đỏ<br>"
                                              "22. Đội công tác xã hội<br>"
                                              "23. Đội khát vọng tuổi trẻ khoa chăn nuôi thú y<br>"
                                              "24. Đội nhiệt huyết rừng xanh<br>"
                                              "25. Đội văn nghệ MFB–MELODY FROM BIO<br>"
                                              "26. Đội văn nghệ rạng đông<br>"
                                              "27. Đội văn nghệ xung kích nhịp điệu xanh<br>"
                                              "28. Đội xung kích khoa khoa học sinh học<br>"
                                              "29. Hội cổ động viên (NONG LAM BUFFALOES) NLB ",
        ("website", "trang web", "link trường", "trang chủ"): "Website chính thức của trường là: https://www.hcmuaf.edu.vn/",
        ("đăng kí môn học", "đkmh", " trang web đăng kí môn học"): "Website đăng kí môn học tại: https://dkmh.hcmuaf.edu.vn/#/<br> Đăng nhập tài khoản là MSSV và mật khẩu để đăng kí môn hoặc xem thời khóa biểu.",
        ("đăng ký môn học", "chọn môn", "đăng ký học phần", "đăng ký môn"): "Đăng ký môn học được thực hiện trên hệ thống trực tuyến theo địa chỉ: https://dkmh.hcmuaf.edu.vn/#/ ",
        ("thanh toán học phí", "nộp học phí", "nộp tiền", "đóng tiền học", "đóng học phí", "đóng BHYT", "thanh toán lệ phí tốt nghiệp", "nộp tiền BHYT", "nộp tiền BHYT"): "Thanh toán học phí, BHYT, lệ phí xét tốt nghiệp qua các cách sau:<br>"
                                                                         "1. Thanh toán tại quầy giao dịch của BIDV<br>"
                                                                         "2. Thanh toán qua kênh BIDV Smart banking<br>"
                                                                         "3. Thanh toán qua kênh BIDV Online<br>"
                                                                         "4. Thanh toán qua ATM của BIDV<br>"
                                                                         "5. Thanh toán qua website sinh viên<br>"
                                                                         "Xem chi tiết hướng dẫn sử dụng các kênh thanh toán tại địa chỉ: https://pkhtc.hcmuaf.edu.vn/pkhtc-24817-1/vn/huong-dan-thanh-toan-hoc-phi-online.html ",

    }

    # Phản hồi riêng cho "xếp loại"
    if user_message == "xếp loại":
        return "Bạn muốn tìm thông tin về xếp loại nào? Hãy nhập số thứ tự tương ứng, tôi sẽ giúp bạn trả lời <br>1. Xếp loại điểm học phần trên thang điểm 4 <br>2. Xếp loại điểm học phần trên thang điểm 10 <br>3. Xếp loại học lực <br>4. Xếp loại tốt nghiệp"

    # Tìm từ khóa phù hợp trong dữ liệu
    for keywords, response in responses.items():
        if any(keyword in user_message for keyword in keywords):
            return response

    # Phản hồi mặc định nếu không tìm thấy
    return "Xin lỗi, tôi chưa hiểu câu hỏi của bạn. Vui lòng đặt câu hỏi rõ ràng hơn!"


