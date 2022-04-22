#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json

ruler_all_mighty = {
    "rulername": "allmighty",
    "email": "ruler@gmail.com",
    "password": "Homnayangi@1357!",
    "is_active": True
}

uni_list = [
    "Đại học Quốc gia Hà Nội",
    "Khoa Luật - ĐHQG Hà Nội",
    "Khoa Quốc tế - ĐHQG Hà Nội",
    "Trường Đại học Công nghệ - ĐHQG Hà Nội",
    "Trường ĐH Giáo dục - ĐHQG Hà Nội",
    "Trường ĐH Khoa học Tự nhiên - ĐHQG Hà Nội",
    "Trường ĐH Khoa học Xã hội và Nhân văn - ĐHQG Hà Nội",
    "Trường Đại học Kinh tế - ĐHQG Hà Nội",
    "Trường Đại học Ngoại ngữ - ĐHQG Hà Nội",
    "Trường Đại học Việt Nhật - ĐHQG Hà Nội",
    "Trường Đại học Y Dược - ĐHQG Hà Nội",
    "Học viện Âm nhạc Quốc gia Việt Nam",
    "Học viện Báo chí Tuyên truyền",
    "Học viện Chính sách và Phát triển",
    "Học viện Công nghệ Bưu chính Viễn thông",
    "Học viện Hành chính Quốc gia",
    "Học viện Kỹ thuật Mật mã",
    "Học viện Ngân hàng",
    "Học viện Ngoại giao",
    "Học viện Nông nghiệp Việt Nam",
    "Học viện Phụ nữ Việt Nam",
    "Học viện Quản lý Giáo dục",
    "Học viện Tài chính",
    "Học viện Thanh Thiếu niên Việt Nam",
    "Học viện Tòa án",
    "Học viện Y Dược học cổ truyền Việt Nam",
    "Trường Đại học Bách khoa Hà Nội",
    "Trường Đại học Công đoàn",
    "Trường Đại học Công nghệ Giao thông vận tải",
    "Trường Đại học Công nghệ và Quản lý Hữu nghị", 
    "Trường Đại học Công nghiệp Dệt may Hà Nội",
    "Trường Đại học Công nghiệp Hà Nội",
    "Trường Đại học Công nghiệp Việt Hung",
    "Trường Đại học Dược Hà Nội",
    "Trường Đại học Đại Nam", 
    "Trường Đại học Điện lực",
    "Trường Đại học Đông Đô", 
    "Trường Đại học FPT", 
    "Trường Đại học Giao thông vận tải",
    "Trường Đại học Hà Nội",
    "Trường Đại học Hòa Bình", 
    "Trường Đại học Khoa học và Công nghệ Hà Nội",
    "Trường Đại học Kinh doanh và Công nghệ Hà Nội", 
    "Trường Đại học Kinh tế Kỹ thuật Công nghiệp",
    "Trường Đại học Kinh tế Quốc dân",
    "Trường Đại học Kiểm sát Hà Nội",
    "Trường Đại học Kiến trúc Hà Nội",
    "Trường Đại học Lao động Xã hội",
    "Trường Đại học Lâm nghiệp",
    "Trường Đại học Luật Hà Nội",
    "Trường Đại học Mỏ Địa chất Hà Nội",
    "Trường Đại học Mở Hà Nội",
    "Trường Đại học Mỹ thuật Công nghiệp",
    "Trường Đại học Mỹ thuật Công nghiệp Á Châu", 
    "Trường Đại học Mỹ thuật Việt Nam",
    "Trường Đại học Ngoại thương",
    "Trường Đại học Nguyễn Trãi", 
    "Trường Đại học Nội vụ Hà Nội",
    "Trường Đại học Phenikaa", 
    "Trường Đại học Phương Đông", 
    "Trường Đại học Sân khấu Điện ảnh",
    "Trường Đại học Sư phạm Hà Nội",
    "Trường Đại học Sư phạm Nghệ thuật Trung ương Hà Nội",
    "Trường Đại học Sư phạm Thể dục thể thao Hà nội",
    "Trường Đại học Tài chính Ngân hàng Hà Nội", 
    "Trường Đại học Tài nguyên và Môi trường Hà Nội",
    "Trường Đại học Thăng Long", 
    "Trường Đại học Thành Đô", 
    "Trường Đại học Thủ đô Hà Nội",
    "Trường Đại học Thủy lợi",
    "Trường Đại học Thương mại",
    "Trường Đại học Văn hóa Hà Nội",
    "Trường Đại học Xây dựng Hà Nội",
    "Trường Đại học Y Hà Nội",
    "Trường Đại học Y tế Công cộng"
]

user_list = {
    1: {
        "fullname": "Đặng Việt Hưng",
        "mssv": "AT13CLC0113",
        "major": "An toàn thông tin",
        "email": "packetloss0709@gmail.com",
        "phonenumb": "0352345898",
        "jobpos": "SWE",
        "uni_id": 17
    },
    2: {
        "fullname": "Trần Công Giang",
        "mssv": "AT13CLC0112",
        "major": "An toàn thông tin",
        "email": "giangtran@gmail.com",
        "phonenumb": "0352346899",
        "jobpos": "SWE",
        "uni_id": 17
    },
    3: {
        "fullname": "Nguyễn Phúc Hiếu",
        "mssv": "AT13CLC0002",
        "major": "An toàn thông tin",
        "email": "hieunguyen@gmail.com",
        "phonenumb": "0351357898",
        "jobpos": "SWE",
        "uni_id": 17
    },
    4: {
        "fullname": "Nguyễn Quang Trung",
        "mssv": "AT13CLC0224",
        "major": "An toàn thông tin",
        "email": "quangtrung@gmail.com",
        "phonenumb": "0352555899",
        "jobpos": "SWE",
        "uni_id": 17
    },
    5: {
        "fullname": "Phạm Tài Tuệ",
        "mssv": "AT13CLC0104",
        "major": "An toàn thông tin",
        "email": "taitue0709@gmail.com",
        "phonenumb": "0352111998",
        "jobpos": "SWE",
        "uni_id": 17
    },
}

# SignUp
signupRes = requests.post(
    "http://localhost:5000/auth/signup",
    json = ruler_all_mighty
)

# Login
loginRes = requests.post(
    "http://localhost:5000/auth/login",
    json = {
        "email": "ruler@gmail.com",
        "password": "Homnayangi@1357!"
    }
)

# Get access_token
access_token = json.loads(loginRes.text)["access"]

# Create universities
for uni in uni_list:
    create_uni = requests.post(
        "http://localhost:5000/uni",
        json = {
            "uniname":uni
        },
        headers = {
            "Authorization":f"Bearer {access_token}"
        }
    )
    print("Create new university: ", json.loads(create_uni.text))

# Create sample exam
create_exam = requests.post(
    "http://localhost:5000/exam",
    json = {
        "exam_name": "Trac nghiem vui",
        "uni_id": 27
    },
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
)
print("Create new exam: ", json.loads(create_exam.text))

# Create users
for k,v in user_list.items():
    create_user = requests.post(
        "http://localhost:5000/user",
        json = v 
    )
    print("Create new user: ", json.loads(create_user.text))

question_list_vn = {1: {'question_name': 'Chức năng của  Internet layer trong mô hình TCP/IP là?', 'opt1': 'Đóng gói dữ liệu IP vào Frame', 'opt2': 'Điều khiển luồng', 'opt3': 'Định tuyến', 'opt4': 'Ánh xạ địa chỉ IP sang địa chỉ vật lý', 'correct': 3, 'exam_id': 1}, 2: {'question_name': 'Địa chỉ IP lớp C có bao nhiêu bit dành cho phần mạng?', 'opt1': '8', 'opt2': '24', 'opt3': '20', 'opt4': '16', 'correct': 2, 'exam_id': 1}, 3: {'question_name': 'Các giao thức hoạt động tại tầng Transport?', 'opt1': 'FTP, HTTP', 'opt2': 'SMTP, FTP', 'opt3': 'TCP, UDP', 'opt4': 'DNS, TFTP', 'correct': 3, 'exam_id': 1}, 4: {'question_name': 'Cổng mặc định của giao thức DNS?', 'opt1': '21', 'opt2': '20', 'opt3': '53', 'opt4': '69', 'correct': 3, 'exam_id': 1}, 5: {'question_name': 'Giao thức dùng để phân giải từ địa chỉ IP sang địa chỉ MAC là?', 'opt1': 'ARP', 'opt2': 'ICMP', 'opt3': 'RARP', 'opt4': 'TCP', 'correct': 1, 'exam_id': 1}, 6: {'question_name': 'Kỹ thuật traceroute (tracert) sử dụng giao thức nào trong các giao thức sau?', 'opt1': 'ICMP', 'opt2': 'TCP', 'opt3': 'ARP', 'opt4': 'A và B', 'correct': 4, 'exam_id': 1}, 7: {'question_name': 'Giao thức HTTP thuộc layer nào trong mô hình TCP/IP', 'opt1': 'Application', 'opt2': 'Presentation', 'opt3': 'Sessions', 'opt4': 'Internet', 'correct': 1, 'exam_id': 1}, 8: {'question_name': 'Phương thức nào sau đây không phải là phương thức HTTP', 'opt1': 'HEAD', 'opt2': 'PUT', 'opt3': 'DEL', 'opt4': 'OPTIONS', 'correct': 3, 'exam_id': 1}, 9: {'question_name': 'Header nào sau đây bắt buộc phải có trên một yêu cầu HTTP phiên bản 1.1', 'opt1': 'User-Agent', 'opt2': 'Connection', 'opt3': 'Host', 'opt4': 'Content-type', 'correct': 3, 'exam_id': 1}, 10: {'question_name': 'Chọn câu trả lời sai khi nói về giao thức HTTP 1.1', 'opt1': 'Có thể sử dụng nhiều website trên cùng 1 IP, cùng 1 port', 'opt2': 'Có thể sử dụng nhiều website trên cùng 1 IP và trên nhiều port khác nhau', 'opt3': 'Một cặp IP - port chỉ sử dụng duy nhất cho 1 website', 'opt4': 'Trên một IP, có thể sử dụng nhiều port khác nhau để trỏ về cùng một website', 'correct': 3, 'exam_id': 1}, 11: {'question_name': 'Ngôn ngữ lập trình web nào sau đây có thể sử dụng trên client-side?', 'opt1': 'Javascript', 'opt2': 'PHP', 'opt3': 'Java', 'opt4': 'JSP', 'correct': 1, 'exam_id': 1}, 12: {'question_name': 'Phương thức HTTP nào sau đây cần có phần body trong HTTP request', 'opt1': 'GET', 'opt2': 'POST', 'opt3': 'OPTIONS', 'opt4': 'A và B', 'correct': 2, 'exam_id': 1}, 13: {'question_name': 'Lỗ hổng bảo mật nào sau đây có thể  cho phép hacker đọc toàn bộ dữ liệu trong database', 'opt1': 'XSS', 'opt2': 'IDOR', 'opt3': 'SQL Injection', 'opt4': 'LDAP Injection', 'correct': 3, 'exam_id': 1}, 14: {'question_name': 'Cookie của một website không thể bị lấy cắp thông qua khai thác lỗ hổng XSS khi cookie sử dụng flag:', 'opt1': 'HTML only', 'opt2': 'Secure', 'opt3': 'Host only', 'opt4': 'HTTP only', 'correct': 4, 'exam_id': 1}, 15: {'question_name': 'Lỗ hổng SQL injection dạng blind bao gồm:', 'opt1': 'Boolean-based blind', 'opt2': 'Time-based blind', 'opt3': 'A và B đúng ', 'opt4': 'A và B sai', 'correct': 3, 'exam_id': 1}, 16: {'question_name': 'Chọn câu trả lời sai Lỗ hổng XSS có thể khai thác để', 'opt1': 'Lấy cắp cookie của người dùng', 'opt2': 'Truy vấn dữ liệu trong cơ sở dữ liệu', 'opt3': 'Cài đặt javascript keyloger để ghi lại nhật ký keyboard của người dùng', 'opt4': 'Trigger CSRF', 'correct': 2, 'exam_id': 1}, 17: {'question_name': 'Chọn câu trả lời sai khi nói về local storage và cookie của trình duyệt', 'opt1': 'Cả local storage và cookie đều có thể lưu session của người dùng', 'opt2': 'Khi session lưu trong cookie có thể bật cơ chế bảo vệ khỏi việc bị lấy cắp thông  qua lỗ hổng XSS', 'opt3': 'Khi session/token lưu trong local storage sẽ không thể bị lấy cắp qua tấn công XSS', 'opt4': 'Việc lưu session/token trong local storage sẽ không sợ bị tấn công CSRF', 'correct': 3, 'exam_id': 1}, 18: {'question_name': 'Công cụ nmap có thể sử dụng để ', 'opt1': 'Bắt gói tin TCP', 'opt2': 'Bắt gói tin UDP', 'opt3': 'Trace route', 'opt4': 'Chuyển hướng gói tin', 'correct': 3, 'exam_id': 1}, 19: {'question_name': 'Lỗ hổng Cross-stie scripting (XSS) không có dạng nào trong các dạng dưới đây:', 'opt1': 'Reflected XSS', 'opt2': 'DOM Based XSS', 'opt3': 'Stored XSS', 'opt4': 'Server Side XSS', 'correct': 4, 'exam_id': 1}, 20: {'question_name': 'Công cụ sqlmap có thể được sử dụng để', 'opt1': 'Khai thác tự động lỗ hổng SQL injection', 'opt2': 'Kết nối trực tiếp vào Database', 'opt3': 'Tấn công brute-force vào database.', 'opt4': 'Cả A, B, C đều đúng', 'correct': 1, 'exam_id': 1}, 21: {'question_name': 'Công cụ nào dưới đây không được sử dụng để tấn công brute-force', 'opt1': 'Hydra', 'opt2': 'Medusa', 'opt3': 'Ncrack', 'opt4': 'Nping', 'correct': 4, 'exam_id': 1}, 22: {'question_name': 'Chức năng nào dưới đây là của công cụ metasploit', 'opt1': 'Thực hiện pivoting từ máy đã chiếm quyền để tấn công các máy khác trong mạng nội bộ', 'opt2': 'Thực hiện gọi reverse shell thông qua khai thác lỗ hổng SQL injection', 'opt3': 'Thực hiện tấn công khai thác các dịch vụ dựa vào các mã khai thác có sắn', 'opt4': 'Cả A, B, C đều đúng', 'correct': 4, 'exam_id': 1}, 23: {'question_name': 'Lỗ hổng MS-17-010 (a.k.a Eternal Blue) là lỗ hổng trên dịch vụ nào?', 'opt1': 'RDP', 'opt2': 'SMB', 'opt3': 'HTTP', 'opt4': 'SSH', 'correct': 2, 'exam_id': 1}, 24: {'question_name': 'Một website chỉ phát hiện là có lỗ hổng SQL injection. Đâu là tác động lớn nhất khi lỗ hổng này bị khai thác', 'opt1': 'Toàn bộ database có thể bị xóa', 'opt2': 'Toàn bộ dữ liệu trong database có thể bị lộ', 'opt3': 'Website có thể bị deface', 'opt4': 'Kẻ tấn công có thể chiếm quyền điều khiển máy chủ', 'correct': 4, 'exam_id': 1}, 25: {'question_name': 'Lỗ hổng log4shell là:', 'opt1': 'Lỗ hổng trên một thư viện được viết bằng ngôn ngữ PHP', 'opt2': 'Lỗ hổng trên một thư viện được viết bằng ngôn ngữ C#', 'opt3': 'Lỗ hổng trong chức năng message lookup của thư viện log4j2', 'opt4': 'A và C đúng', 'correct': 3, 'exam_id': 1}, 26: {'question_name': 'Lỗ hổng file inclusion có các dạng:', 'opt1': 'Local file inclusion', 'opt2': 'Self file inclusion', 'opt3': 'Second order file inclusion', 'opt4': 'Cả A, B, C đều đúng', 'correct': 1, 'exam_id': 1}, 27: {'question_name': 'Vai trò của tường lửa là gì?', 'opt1': 'Giám sát lưu lượng mạng', 'opt2': 'Kiểm soát hành vi truy cập mạng', 'opt3': 'Phát hiện xâm nhập mạng', 'opt4': 'cả 3 đáp án trên', 'correct': 2, 'exam_id': 1}, 28: {'question_name': 'Hệ thống ghi nhận việc nhập sai password truy cập đến tài khoản admin liên tục trong 3h liên tục. Theo bạn đây là loại hình tấn công gì?', 'opt1': 'Brute-force', 'opt2': 'Backdoor', 'opt3': 'Sâu', 'opt4': 'TCP/IP hijacking', 'correct': 1, 'exam_id': 1}, 29: {'question_name': 'Giao thức xác thực nào sau đây sử dụng KDC- Key Distribution Center?', 'opt1': 'CHAP', 'opt2': 'EAP', 'opt3': 'PAP', 'opt4': 'Kerberos', 'correct': 4, 'exam_id': 1}, 30: {'question_name': 'deauthentication attack vào mạng không dây là loại tấn công nào sau đây?', 'opt1': 'Downgrade attack', 'opt2': 'DoS', 'opt3': 'Timing attacks', 'opt4': '  Brute-force', 'correct': 2, 'exam_id': 1}, 31: {'question_name': 'Đảm bảo an toàn thông tin có nghĩa là gì? ', 'opt1': 'Đảm bảo tính bí mật của thông tin', 'opt2': 'Đảm bảo tính toàn vẹn của thông tin', 'opt3': 'Đảm bảo tính sẵn sàng của thông tin', 'opt4': 'Cả 3 đáp án trên', 'correct': 4, 'exam_id': 1}, 32: {'question_name': 'Giải thuật Diffie-Hellman dùng để làm gì?', 'opt1': 'Bảo mật thông điệp', 'opt2': 'xác thực thông điệp', 'opt3': 'phân phối khóa trước', 'opt4': 'lấy chữ ký số', 'correct': 3, 'exam_id': 1}, 33: {'question_name': 'Cách bảo vệ nào sau đây là tốt nhất để chống lại tấn công DoS kiểu làm tràn băng thông và bộ nhớ đệm của hệ thống?', 'opt1': 'Cài đặt phần nềm bảo vệ Antivirus', 'opt2': 'Disable web server', 'opt3': 'Triển khai hệ thống IDS', 'opt4': 'Chặn giao thức ICMP', 'correct': 4, 'exam_id': 1}, 34: {'question_name': 'Giao thức nào sau đây cho phép truy cập từ xa an toàn hơn telnet?', 'opt1': 'SSL', 'opt2': 'VPN', 'opt3': 'SSH', 'opt4': 'IPVSEC', 'correct': 3, 'exam_id': 1}, 35: {'question_name': 'Hệ thống nào có chức năng giám sát và ngăn chặn xâm nhập?', 'opt1': 'SIEM', 'opt2': 'IDS', 'opt3': 'IPS', 'opt4': 'honeynet', 'correct': 3, 'exam_id': 1}, 36: {'question_name': 'Nhận định nào sau đây là sai: "Độ mạnh" của mật khẩu được hiểu là ...', 'opt1': 'Yếu tố phức tạp của mật khẩu', 'opt2': 'Yếu tố đặc biệt của mật khẩu', 'opt3': 'Yếu tố đa dạng của mật khẩu', 'opt4': 'Yếu tố lặp của mật khẩu', 'correct': 4, 'exam_id': 1}, 37: {'question_name': 'Lớp nào sau đây chỉ được sử dụng trong mô hình TCP/IP?', 'opt1': 'Application', 'opt2': 'Network', 'opt3': 'Transport', 'opt4': 'Internet', 'correct': 4, 'exam_id': 1}, 38: {'question_name': 'Tên gọi của dữ liệu từ tầng 7 xuống tầng 1 trong mô hình OSI là:', 'opt1': 'Data, segment, frame, packet, bit', 'opt2': 'Data, frame, packet, segment, bit', 'opt3': 'Data, packet, segment, frame, bit', 'opt4': 'Data, segment, packet, frame, bit', 'correct': 4, 'exam_id': 1}, 39: {'question_name': 'Dịch vụ DNS Server có chức năng chính là gì?', 'opt1': 'Phân giải tên miền sang địa chỉ IP và ngược lại', 'opt2': 'Phân giải địa chỉ MAC sang IP và ngược lại', 'opt3': 'Phân giải tên miền sang địa chỉ MAC và ngược lại', 'opt4': 'Cho phép tạo gmail để có thể sử dụng dịch vụ SMTP và POP3', 'correct': 1, 'exam_id': 1}, 40: {'question_name': 'Trong các địa chỉ sau, địa chỉ nào là địa chỉ broadcast', 'opt1': '149.255.12.255/20', 'opt2': '149.6.67.255/17', 'opt3': '149.6.254.255/16', 'opt4': '149.6.63.255/18', 'correct': 4, 'exam_id': 1}, 41: {'question_name': 'Tập tin cấu hình DNS Server trên các máy chủ Linux?', 'opt1': '/etc/named', 'opt2': '/etc/resolv.conf', 'opt3': '/var/named/server.com.vn.dns', 'opt4': 'tất cả đều sai', 'correct': 2, 'exam_id': 1}, 42: {'question_name': 'Dịch vụ web service chạy ở port nào?', 'opt1': '21', 'opt2': '22', 'opt3': '80', 'opt4': '110', 'correct': 3, 'exam_id': 1}, 43: {'question_name': 'Tại sao cần phải xây dựng hệ thống an ninh mạng máy tính?', 'opt1': 'Ngăn chặn các truy cập không được phép từ bên ngoài tới các hệ thống mạng riêng ', 'opt2': 'Nhằm để tránh các lỗi do bản thân mạng sinh ra', 'opt3': 'Nhằm để nâng cao tốc độ truyền thông', 'opt4': 'Nhằm để nâng cao hiệu suất truyền thông', 'correct': 1, 'exam_id': 1}, 44: {'question_name': 'Khi gói tin bị mất hoặc bị lỗi thì tầng Data Link sẽ làm gì?', 'opt1': 'Tự khôi phục hoặc sửa lại gói tin bị mất hoặc lỗi hoặc đó', 'opt2': 'Đưa ra yêu cầu cho trạm nguồn gửi lại gói tin bị lỗi hoặc mất', 'opt3': 'Huỷ phiên trao đổi dữ liệu, đưa ra thông báo lỗi cho trạm nguồn', 'opt4': 'Cả 3 đáp án trên', 'correct': 4, 'exam_id': 1}, 45: {'question_name': 'RSA là thuật toán mã hóa gì?', 'opt1': 'Mã hóa công khai', 'opt2': 'Mã hóa mật khẩu', 'opt3': 'Mã khóa riêng', 'opt4': 'Tất cả đều sai', 'correct': 1, 'exam_id': 1}, 46: {'question_name': 'ADSL là thuật ngữ viết tắt của cụm từ nào?', 'opt1': 'Address digital symetrical line', 'opt2': 'Asymmetrical digital subscriber line', 'opt3': 'Asymmetrical data subscriber line', 'opt4': 'Asymmetrical digital subscriber link', 'correct': 2, 'exam_id': 1}, 47: {'question_name': 'MAC filter được định nghĩa như', 'opt1': 'Tường lửa cá nhân', 'opt2': 'Chặn truy cập từ một địa chỉ MAC nhất định.', 'opt3': 'Cho phép truy cập đến một địa chỉ MAC nhất định.', 'opt4': 'Tất cả đều đúng', 'correct': 4, 'exam_id': 1}, 48: {'question_name': 'Tham số NMAP dò quét địa chỉ IP đang hoạt động trong mạng từ bên ngoài là gì?', 'opt1': '-sO', 'opt2': '-sP', 'opt3': '-sS', 'opt4': '-sU', 'correct': 2, 'exam_id': 1}, 49: {'question_name': 'A muốn gửi email có chức mã hóa cho B và không muốn trả các chi phí (lisence hoặc server). Giải pháp nào trong các phương án bên dưới là hiệu quả nhất?', 'opt1': 'IP Security (IPSEC)', 'opt2': 'Multi purpose Internet Mail Extensions (MIME)', 'opt3': 'Pretty Good Privacy (PGP)', 'opt4': 'Hyper Text Transfer Protocol with Secure Socket Layer (HTTPS)', 'correct': 3, 'exam_id': 1}, 50: {'question_name': 'Trong các công cụ sau đây, công cụ nào được sử dụng để tấn công MITM?', 'opt1': 'Ettercap', 'opt2': 'PsExec', 'opt3': 'Rootkit', 'opt4': 'Metasploits', 'correct': 1, 'exam_id': 1}, 51: {'question_name': 'Tiêu chuẩn mã hóa mạng wifi IEEE 802.11i sử dụng mã hóa và cơ chế xác thực nào sau đây?', 'opt1': 'TKIP và WEP', 'opt2': 'TKIP và Passphrase hayRADIUS (802.1x/EAP)', 'opt3': 'AES và WEP', 'opt4': 'AES và  Passphrase hayRADIUS (802.1x/EAP)', 'correct': 4, 'exam_id': 1}, 52: {'question_name': 'Địa chỉ IP nào sau đây là địa chỉ Public', 'opt1': '192.168.0.1', 'opt2': '172.16.0.1', 'opt3': '169.254.10.5', 'opt4': '54.239.98.2', 'correct': 4, 'exam_id': 1}, 53: {'question_name': 'NAT là viết tắt của cụm từ nào sau đây trong hệ thống mạng?', 'opt1': 'Network Address Translation', 'opt2': 'Network Attack Technique', 'opt3': 'Network Architecture Technology', 'opt4': 'Network Area Topology ', 'correct': 1, 'exam_id': 1}, 54: {'question_name': 'Trung tâm điều hành an toàn thông tin SOC là viết tắt của cụm từ nào?', 'opt1': 'Solution Organization over Continental', 'opt2': 'Security Operations Center', 'opt3': 'Security Operations Centre', 'opt4': 'Security Orchestration Center', 'correct': 2, 'exam_id': 1}, 55: {'question_name': 'Mã lỗi HTTP status code 504 có ý nghĩa gì?', 'opt1': 'Service Unavailable', 'opt2': 'Bad Gateway', 'opt3': 'Gateway Timeout Error', 'opt4': 'Internet Server Error', 'correct': 3, 'exam_id': 1}, 56: {'question_name': 'VPN là viết tắt của cụm từ nào?', 'opt1': 'Virtual Private Network', 'opt2': 'Virtual Public Network', 'opt3': 'Virtual Protection Network', 'opt4': 'Virus Protection Network', 'correct': 1, 'exam_id': 1}, 57: {'question_name': 'Trong mô hình OSI, Các thiết bị ở Layer 2 giao tiếp với nhau bằng gì ?', 'opt1': 'IP', 'opt2': 'URL', 'opt3': 'MAC', 'opt4': 'Bit', 'correct': 3, 'exam_id': 1}, 58: {'question_name': 'An toàn thông tin là gì?', 'opt1': 'Bí mật, toàn vẹn và sẵn dùng', 'opt2': 'Bí mât, toàn vẹn và chi phí', 'opt3': 'Bí mật, toàn vẹn và linh hoạt', 'opt4': 'Toàn vẹn, sẵn dùng và dễ sử dụng', 'correct': 1, 'exam_id': 1}, 59: {'question_name': 'Có thể theo đuổi những công việc nào trong ATTT', 'opt1': 'An toàn sản phẩm và an toàn vận hành', 'opt2': 'Phát triển công cụ', 'opt3': 'Tìm diệt mã độc và các nguy cơ khác', 'opt4': 'Cả 3 đáp án trên', 'correct': 4, 'exam_id': 1}, 60: {'question_name': 'Nguyên tắc đảm bảo an toàn thông tin, hệ thống và mạng', 'opt1': 'Phòng vệ nhiều lớp có chiều sâu', 'opt2': 'Không tồn tại hệ thống thông tin an toàn tuyệt đối', 'opt3': 'Luôn cập nhật bản vá lỗ hổng', 'opt4': 'Cả 3 đáp án trên', 'correct': 4, 'exam_id': 1}, 61: {'question_name': 'Viết tắt của hệ thống phát hiện xâm nhập', 'opt1': 'IPS', 'opt2': 'Firewall', 'opt3': 'IDS', 'opt4': 'VPN', 'correct': 3, 'exam_id': 1}, 62: {'question_name': 'Đâu là rủi ro lớn nhất đối với ứng dụng web trong năm 2021', 'opt1': 'Injection', 'opt2': 'Broken Access Control', 'opt3': 'XSS', 'opt4': 'Broken Authentication', 'correct': 2, 'exam_id': 1}, 63: {'question_name': 'Bạn hãy cho biết mối đe dọa đối với thông tin là gì', 'opt1': 'Bất kì hành động nào gây hại đến tài nguyên hệ thống', 'opt2': 'Là một lỗi khiếm khuyết gây nên mất an toàn thông tin', 'opt3': 'Là một điểm yếu để cho mối đe dọa gây hại', 'opt4': 'Là một hệ thống thiết kế không an toàn', 'correct': 1, 'exam_id': 1}, 64: {'question_name': 'Để một cuộc tấn công mạng thành công, cần có yếu tố gì?', 'opt1': 'Mối đe dọa ', 'opt2': 'Lỗ hổng', 'opt3': 'Điểm yếu', 'opt4': 'Cả A và C', 'correct': 4, 'exam_id': 1}, 65: {'question_name': 'Những kỹ thuật kiểm thử ứng dụng nào giúp tìm kiếm những xử lý đầu vào không đúng?', 'opt1': 'Fuzzing', 'opt2': 'Overloading', 'opt3': 'Kiểm thử xâm nhập', 'opt4': 'Quét lỗ hổng', 'correct': 1, 'exam_id': 1}, 66: {'question_name': 'Giao thức nào sử dụng cổng TCP 445', 'opt1': 'FTPS', 'opt2': 'HTTPS', 'opt3': 'SMB', 'opt4': 'SSH', 'correct': 3, 'exam_id': 1}, 67: {'question_name': 'Loại lỗ hổng nào dẫn đến việc ghi dữ liệu vượt qua ngoài ranh giới bộ nhớ dự kiến?', 'opt1': 'Pointer dereference', 'opt2': 'Integer overflow', 'opt3': 'Buffer overflow', 'opt4': 'Rò rỉ bộ nhớ', 'correct': 3, 'exam_id': 1}, 68: {'question_name': 'Thuật ngữ nào mô tả quá trình che dấu dữ liệu trong một tệp tin?', 'opt1': 'Trojan', 'opt2': 'Steganography', 'opt3': 'Mã hóa', 'opt4': 'Chữ ký số', 'correct': 2, 'exam_id': 1}, 69: {'question_name': 'Giải pháp nào sau đây là giải pháp tốt nhất cho công ty cần dịch vụ bảo mật IT nhưng thiếu nhân sự cần thiết?', 'opt1': 'MSA', 'opt2': 'MaaS', 'opt3': 'MSP', 'opt4': 'MSSP', 'correct': 4, 'exam_id': 1}, 70: {'question_name': 'Khía cạnh nào của lập trình là quan trọng đối với quá trình phát triển ứng dụng an toàn?', 'opt1': 'Quản lý bản vá', 'opt2': 'Xác thực đầu vào', 'opt3': 'Bảo vệ mật khẩu', 'opt4': 'Whitelist ứng dụng', 'correct': 2, 'exam_id': 1}, 71: {'question_name': 'Tên nào sau đây đề cập đến tổ chức phi lợi nhuận tập trung vào bảo mật phần mềm?', 'opt1': 'CSIRT', 'opt2': 'IETF', 'opt3': 'OWASP', 'opt4': 'CERT', 'correct': 3, 'exam_id': 1}, 72: {'question_name': 'Kỹ thuật nào được mã độc sử dụng để vượt qua các cơ chế phát hiện?', 'opt1': 'Payload', 'opt2': 'Pack', 'opt3': 'Dropper', 'opt4': 'Cell', 'correct': 2, 'exam_id': 1}, 73: {'question_name': 'Những thuật toán nào sau đây là thuật toán mã hóa đối xứng ?', 'opt1': 'RC5', 'opt2': 'IDEA', 'opt3': 'DES', 'opt4': 'A , B và C đúng', 'correct': 4, 'exam_id': 1}, 74: {'question_name': 'Giao thức SSL và TSL hoạt động ở tầng nào của mô hình OSI', 'opt1': 'Network', 'opt2': 'Sesion', 'opt3': 'Transport', 'opt4': 'Presentation', 'correct': 4, 'exam_id': 1}, 75: {'question_name': 'Trong các hình thức tân công bên dưới, hình thức nào không phải là tấn công DDoS?', 'opt1': 'UDP Flood', 'opt2': 'Smurf Attack', 'opt3': 'Ping of Death', 'opt4': 'Downgrade attack', 'correct': 4, 'exam_id': 1}, 76: {'question_name': 'Hệ thống nào không phải là hệ thống ATTT?', 'opt1': 'WAF', 'opt2': 'PAM', 'opt3': 'NAC', 'opt4': 'Solarwind', 'correct': 4, 'exam_id': 1}, 77: {'question_name': 'Port nào là port mặc định của giao thức SSH?', 'opt1': '20', 'opt2': '21', 'opt3': '22', 'opt4': '23', 'correct': 3, 'exam_id': 1}, 78: {'question_name': 'Đâu là IP broadcast của dải mạng: 192.168.1.1/24', 'opt1': '192.168.1.255', 'opt2': '192.168.1.254', 'opt3': '192.168.1.256', 'opt4': '192.168.1.253', 'correct': 1, 'exam_id': 1}, 79: {'question_name': 'Dải IP 192.168.10.100/30 có bao nhiêu IP', 'opt1': '1', 'opt2': '2', 'opt3': '3', 'opt4': '4', 'correct': 4, 'exam_id': 1}, 80: {'question_name': 'Giao thức POP3 không mã hóa trong Email sử dụng port nào?', 'opt1': '587', 'opt2': '110', 'opt3': '25', 'opt4': '995', 'correct': 2, 'exam_id': 1}, 81: {'question_name': 'Giao thức SMTP sử dụng port nào?', 'opt1': '25', 'opt2': '993', 'opt3': '465', 'opt4': '110', 'correct': 1, 'exam_id': 1}}

for k,v in question_list_vn.items():
    create_ques = requests.post(
        "http://localhost:5000/question",
        json = v,
        headers = {
            "Authorization":f"Bearer {access_token}"
        }
    )
    print("Create new question: ", json.loads(create_ques.text))