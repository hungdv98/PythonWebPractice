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

questions = {
    1: {
        "question_name":"1 + 1 = ",
        "opt1": "9",
        "opt2": "4",
        "opt3": "2",
        "opt4": "11",
        "correct": 3,
        "exam_id": 1
    },
    2: {
        "question_name":"2 + 1 = ",
        "opt1": "9",
        "opt2": "3",
        "opt3": "2",
        "opt4": "11",
        "correct": 2,
        "exam_id": 1
    },
    3: {
        "question_name":"11 + 1 = ",
        "opt1": "9",
        "opt2": "4",
        "opt3": "2",
        "opt4": "12",
        "correct": 4,
        "exam_id": 1
    },
    4: {
        "question_name":"11 + 12 = ",
        "opt1": "9",
        "opt2": "23",
        "opt3": "2",
        "opt4": "11",
        "correct": 2,
        "exam_id": 1
    },
    5: {
        "question_name":"10 + 1 = ",
        "opt1": "9",
        "opt2": "4",
        "opt3": "2",
        "opt4": "11",
        "correct": 4,
        "exam_id": 1
    },
    6: {
        "question_name":"5 + 1 = ",
        "opt1": "6",
        "opt2": "4",
        "opt3": "2",
        "opt4": "11",
        "correct": 1,
        "exam_id": 1
    },
    7: {
        "question_name":"1 + 3 = ",
        "opt1": "9",
        "opt2": "4",
        "opt3": "2",
        "opt4": "11",
        "correct": 2,
        "exam_id": 1
    },
    8: {
        "question_name":"16 + 1 = ",
        "opt1": "17",
        "opt2": "4",
        "opt3": "2",
        "opt4": "11",
        "correct": 1,
        "exam_id": 1
    },
    9: {
        "question_name":"1 + 15 = ",
        "opt1": "9",
        "opt2": "16",
        "opt3": "2",
        "opt4": "11",
        "correct": 2,
        "exam_id": 1
    },
    10: {
        "question_name":"1 + 0 = ",
        "opt1": "9",
        "opt2": "4",
        "opt3": "1",
        "opt4": "11",
        "correct": 3,
        "exam_id": 1
    }
}

user_list = {
    1: {
        "fullname": "Đặng Việt Hưng",
        "mssv": "AT13CLC0113",
        "major": "An toàn thông tin",
        "email": "packetloss0709@gmail.com",
        "phonenumb": "0352345898",
        "uni_id": 17
    },
    2: {
        "fullname": "Trần Công Giang",
        "mssv": "AT13CLC0112",
        "major": "An toàn thông tin",
        "email": "giangtran@gmail.com",
        "phonenumb": "0352346899",
        "uni_id": 17
    },
    3: {
        "fullname": "Nguyễn Phúc Hiếu",
        "mssv": "AT13CLC0002",
        "major": "An toàn thông tin",
        "email": "hieunguyen@gmail.com",
        "phonenumb": "0351357898",
        "uni_id": 17
    },
    4: {
        "fullname": "Nguyễn Quang Trung",
        "mssv": "AT13CLC0224",
        "major": "An toàn thông tin",
        "email": "quangtrung@gmail.com",
        "phonenumb": "0352555899",
        "uni_id": 17
    },
    5: {
        "fullname": "Phạm Tài Tuệ",
        "mssv": "AT13CLC0104",
        "major": "An toàn thông tin",
        "email": "taitue0709@gmail.com",
        "phonenumb": "0352111998",
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
        "uni_id": 17
    },
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
)
print("Create new exam: ", json.loads(create_exam.text))

# Create questions
for k,v in questions.items():
    create_ques = requests.post(
        "http://localhost:5000/question",
        json = v,
        headers = {
            "Authorization":f"Bearer {access_token}"
        }
    )
    print("Create new question: ", json.loads(create_ques.text))

# Create users
for k,v in user_list.items():
    create_user = requests.post(
        "http://localhost:5000/user",
        json = v 
    )
    print("Create new user: ", json.loads(create_user.text))