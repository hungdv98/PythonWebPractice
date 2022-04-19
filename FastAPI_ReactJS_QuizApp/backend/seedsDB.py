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
# for k,v in questions.items():
#     create_ques = requests.post(
#         "http://localhost:5000/question",
#         json = v,
#         headers = {
#             "Authorization":f"Bearer {access_token}"
#         }
#     )
#     print("Create new question: ", json.loads(create_ques.text))

# Create users
for k,v in user_list.items():
    create_user = requests.post(
        "http://localhost:5000/user",
        json = v 
    )
    print("Create new user: ", json.loads(create_user.text))



question_list = {
    1: {
        "question_name":"What is the definition of ransomware?",
        "opt1": "A computer program that is used for extorting money",
        "opt2": "A computer program that is used for decrypting data",
        "opt3": "A computer program that is used by attackers to encrypt user data in order to extort their money",
        "opt4": "A legit computer program created by Microsoft",
        "correct": 3,
        "exam_id": 1
    },
    2: {
        "question_name":"A set of rules that governs data communication",
        "opt1": "Protocols",
        "opt2": "Standards",
        "opt3": "RFCs",
        "opt4": "None of the mentioned",
        "correct": 1,
        "exam_id": 1
    },
    3: {
        "question_name":"Which of the following is not a reconnaissance tool or technique for information gathering?",
        "opt1": "NMAP",
        "opt2": "Hping",
        "opt3": "Nexpose",
        "opt4": "Google Dorks",
        "correct": 3,
        "exam_id": 1
    },
    4: {
        "question_name":"How many layers does OSI have?",
        "opt1": "4",
        "opt2": "7",
        "opt3": "5",
        "opt4": "6",
        "correct": 2,
        "exam_id": 1
    },
    5: {
        "question_name":"What is a Firewall in Computer Network?",
        "opt1": "The physical boundary of Network",
        "opt2": "An operating System of Computer Network  ",
        "opt3": "A system designed to prevent unauthorized access",
        "opt4": "A web browsing Software",
        "correct": 3,
        "exam_id": 1
    },
    6: {
        "question_name":"Which of the following is known as Malicious software?",
        "opt1": "maliciousware",
        "opt2": "illegalware",
        "opt3": "badware",
        "opt4": "malware",
        "correct": 4,
        "exam_id": 1
    },
    7: {
        "question_name":"The altering of data so that it is not usable unless the changes are undone is",
        "opt1": "biometrics",
        "opt2": "encryption",
        "opt3": "ergonomics",
        "opt4": "compression",
        "correct": 2,
        "exam_id": 1
    },
    8: {
        "question_name":"The ................... portion of LAN management software restricts access, records user activities and audit data etc.",
        "opt1": "Configuration management",
        "opt2": "Security management",
        "opt3": "Performance management",
        "opt4": "None of these",
        "correct": 2,
        "exam_id": 1
    },
    9: {
        "question_name":"………….transform message into format (cipher text) that cannot be read by hackers.",
        "opt1": "Decryption",
        "opt2": "Encryption",
        "opt3": "Transformation",
        "opt4": "None of these",
        "correct": 2,
        "exam_id": 1
    },
    10: {
        "question_name":"Why is one time password (OTP) safe ?",
        "opt1": "It is easy to generated ",
        "opt2": "It cannot be shared",
        "opt3": "It is different for every access",
        "opt4": "It is a complex encrypted password",
        "correct": 3,
        "exam_id": 1
    },
    11: {
        "question_name":"What is major drawback of anomaly detection IDS ?",
        "opt1": "These are very slow at detection",
        "opt2": "It generates many false alarms",
        "opt3": "It doesn’t detect novel attacks",
        "opt4": "None of these",
        "correct": 2,
        "exam_id": 1
    },
    12: {
        "question_name":"What is used to classify and identify software or hardware vulnerabilities for building a database of security vulnerabilities?",
        "opt1": "CVSS",
        "opt2": "OWASP",
        "opt3": "CVE",
        "opt4": "CWE",
        "correct": 3,
        "exam_id": 1
    },
    13: {
        "question_name":"What is not a role of encryption ?",
        "opt1": "It is used to protect data from unauthorized access during transmission",
        "opt2": "It is used to ensure user authentication",
        "opt3": "It is used to ensure data integrity",
        "opt4": "It is used to ensure data corruption doesn’t happens",
        "correct": 4,
        "exam_id": 1
    },
    14: {
        "question_name":"What is not an encryption standard ?",
        "opt1": "AES",
        "opt2": "TES",
        "opt3": "Triple DES",
        "opt4": "DES",
        "correct": 2,
        "exam_id": 1
    },
    15: {
        "question_name":"What is a Hash Function ?",
        "opt1": "It creates a small flexible block of data ",
        "opt2": "It creates a small, fixed block of data ",
        "opt3": "It creates a encrypted block of data ",
        "opt4": "none of the mentioned",
        "correct": 2,
        "exam_id": 1
    },
    16: {
        "question_name":"MD5 produces __ bits hash data ?",
        "opt1": "128",
        "opt2": "150",
        "opt3": "160",
        "opt4": "112",
        "correct": 1,
        "exam_id": 1
    },
    17: {
        "question_name":"WPA2 is used for security in",
        "opt1": "ethernet",
        "opt2": "bluetooth",
        "opt3": "wi-fi",
        "opt4": "none of the mentioned",
        "correct": 3,
        "exam_id": 1
    },
    18: {
        "question_name":"Which is a malware type that steals sensitive information like passwords, bank accounts?",
        "opt1": "Ransomware",
        "opt2": "Virus",
        "opt3": "Backdoor",
        "opt4": "Keylogger",
        "correct": 4,
        "exam_id": 1
    },
    19: {
        "question_name":"Which are symmetric encryption algorithms?",
        "opt1": "AES, Diffie-Hellman, DES, IDEA",
        "opt2": "AES, RSA, RC4, DES",
        "opt3": "AES, RC4, 3DES, IDEA",
        "opt4": "AES, RSA, DSS, DES",
        "correct": 3,
        "exam_id": 1
    },
    20: {
        "question_name":"Which are asymmetric encryption algorithms? ",
        "opt1": "AES, Diffie-Hellman, DES, IDEA",
        "opt2": "DSS, RSA, RC4, DES",
        "opt3": "AES, RC4, 3DES, IDEA",
        "opt4": "DSS, RSA, ElGamal, Diffie-Hellman",
        "correct": 4,
        "exam_id": 1
    },
    21: {
        "question_name":"Which is a tool that does not use to capture traffic? ",
        "opt1": "Tcpdump ",
        "opt2": "NetworkMiner ",
        "opt3": "Dsniff",
        "opt4": "hping3",
        "correct": 4,
        "exam_id": 1
    },
    22: {
        "question_name":"What is the data type of “0x50”? ",
        "opt1": "Decimal",
        "opt2": "Hexadecimal",
        "opt3": "Binary",
        "opt4": "ASCII",
        "correct": 2,
        "exam_id": 1
    },
    23: {
        "question_name":"SHA256, MD5 is:",
        "opt1": "Hash algorithm",
        "opt2": "Digest",
        "opt3": "Secret Key",
        "opt4": "Public Key",
        "correct": 1,
        "exam_id": 1
    },
    24: {
        "question_name":"Which is the type of firewall that can prevent SQL injection attacks?",
        "opt1": "Data-driven firewall",
        "opt2": "Web application firewall",
        "opt3": "Stateful firewall",
        "opt4": "Packet firewall",
        "correct": 4,
        "exam_id": 1
    },
    25: {
        "question_name":"Hashing is a ….. process. ",
        "opt1": "One-way",
        "opt2": "Two-way",
        "opt3": "Three-way",
        "opt4": "None of the above",
        "correct": 1,
        "exam_id": 1
    },
    26: {
        "question_name":"Shellshock had the potential for an unauthorized user to gain access to a server. It affected many internet-facing services, which OS did it not directly affect?",
        "opt1": "Unix",
        "opt2": "Linux",
        "opt3": "OS X",
        "opt4": "Windows",
        "correct": 4,
        "exam_id": 1
    },
    27: {
        "question_name":"What is the difference between AES and RSA?",
        "opt1": "Both algorithms are symmetric encryption but the AES key has 256 bits in length",
        "opt2": "AES is asymmetric and RSA is symmetric encryption",
        "opt3": "Both algorithms are asymmetric encryption but the RSA key has 1024 bits in length",
        "opt4": "RSA is asymmetric and AES is symmetric encryption",
        "correct": 4,
        "exam_id": 1
    },
    28: {
        "question_name":"What is a type of malware that targets Microsoft Office document files?",
        "opt1": "Polymorphic virus",
        "opt2": "Macro virus",
        "opt3": "Trojan",
        "opt4": "Stealth virus",
        "correct": 4,
        "exam_id": 1
    },
    29: {
        "question_name":"Hash function are used for?",
        "opt1": "Authentication",
        "opt2": "Data Confidentially",
        "opt3": "Data Availability",
        "opt4": "Data Integrity",
        "correct": 4,
        "exam_id": 1
    },
    30: {
        "question_name":"Which is the next version of the SSL protocol?",
        "opt1": "GRE",
        "opt2": "IPSec",
        "opt3": "TLS",
        "opt4": "RSA",
        "correct": 3,
        "exam_id": 1
    },
    31: {
        "question_name":"Which is the network that usually places a Web, FTP, Mail server?",
        "opt1": "VLAN",
        "opt2": "DMZ network",
        "opt3": "Intranet",
        "opt4": "LAN",
        "correct": 2,
        "exam_id": 1
    },
    32: {
        "question_name":"Which is the language that does not the Object-oriented programing?",
        "opt1": "C++",
        "opt2": "Java",
        "opt3": "Assembly",
        "opt4": "Python",
        "correct": 3,
        "exam_id": 1
    },
    33: {
        "question_name":"What is the common executable file format in Windows?",
        "opt1": "PE file",
        "opt2": "ELF file",
        "opt3": "Mach-O file",
        "opt4": "Ext file",
        "correct": 1,
        "exam_id": 1
    },
    34: {
        "question_name":"What is the secure remote protocol from one computer to another?",
        "opt1": "SSL",
        "opt2": "TLS",
        "opt3": "SSH",
        "opt4": "HTTP",
        "correct": 3,
        "exam_id": 1
    },
    35: {
        "question_name":"How long is the SHA256 hash?",
        "opt1": "16 bytes",
        "opt2": "32 bytes",
        "opt3": "64 bytes",
        "opt4": "8 bytes",
        "correct": 2,
        "exam_id": 1
    },
    36: {
        "question_name":"What is the status response code indicates that the request has succeeded?",
        "opt1": "302",
        "opt2": "500",
        "opt3": "200",
        "opt4": "504",
        "correct": 3,
        "exam_id": 1
    },
    37: {
        "question_name":"Which is an information security certificate?",
        "opt1": "CCIE",
        "opt2": "CISSP",
        "opt3": "JNCIE",
        "opt4": "CCNA",
        "correct": 2,
        "exam_id": 1
    },
    38: {
        "question_name":"Which vulnerability occurs due to insufficent access control?",
        "opt1": "Insecure Direct Object Reference (IDOR)",
        "opt2": "XML External Entities (XXE)",
        "opt3": "Cross-Site Scripting (XSS)",
        "opt4": "Insecure Deserialization",
        "correct": 1,
        "exam_id": 1
    },
    39: {
        "question_name":"Which of the followings is the most critical vulnerability?",
        "opt1": "XSS",
        "opt2": "CSRF",
        "opt3": "SQL injection",
        "opt4": "RCE",
        "correct": 4,
        "exam_id": 1
    },
    40: {
        "question_name":"Which of the following is considered an element of cyber security?",
        "opt1": "Network security",
        "opt2": "Operational security",
        "opt3": "Application security",
        "opt4": "All of the above",
        "correct": 4,
        "exam_id": 1
    },
    41: {
        "question_name":"Which is a command that can displays the contents of a text file on Windows?",
        "opt1": "read",
        "opt2": "type",
        "opt3": "reads",
        "opt4": "mores",
        "correct": 2,
        "exam_id": 1
    },
    42: {
        "question_name":"To what does a DNS translate a domain name?",
        "opt1": "IP",
        "opt2": "HEX",
        "opt3": "URL",
        "opt4": "Binary",
        "correct": 1,
        "exam_id": 1
    },
    43: {
        "question_name":"Identify the term which denotes the protection of data from modification by unknown users.",
        "opt1": "Confidentiality",
        "opt2": "Authentication",
        "opt3": "Availability",
        "opt4": "Integrity",
        "correct": 4,
        "exam_id": 1
    },
    44: {
        "question_name":"Applications communicate with kernel by using:",
        "opt1": "System Calls",
        "opt2": "C Programs",
        "opt3": "Shell Script",
        "opt4": "Shell",
        "correct": 1,
        "exam_id": 1
    },
    45: {
        "question_name":"The dmesg command",
        "opt1": "Shows user login logoff attempts",
        "opt2": "Shows the syslog file for info messages",
        "opt3": "kernel log messages",
        "opt4": "Shows the daemon log messages",
        "correct": 3,
        "exam_id": 1
    },
    46: {
        "question_name":"Which command is used to view compressed text file contents",
        "opt1": "cat",
        "opt2": "type",
        "opt3": "zcat",
        "opt4": "print",
        "correct": 3,
        "exam_id": 1
    },
    47: {
        "question_name":"Which of the followings is not a type of IDS?",
        "opt1": "Network IDS",
        "opt2": "Host IDS",
        "opt3": "Data IDS",
        "opt4": "Signature-based IDS",
        "correct": 3,
        "exam_id": 1
    },
    48: {
        "question_name":"Which is the 7th layer in the OSI model?",
        "opt1": "Presentation",
        "opt2": "Transport",
        "opt3": "Data-link",
        "opt4": "Application",
        "correct": 4,
        "exam_id": 1
    },
    49: {
        "question_name":"In digital signature, public key used for?",
        "opt1": "To sign",
        "opt2": "To verify signature",
        "opt3": "To encrypt",
        "opt4": "To decrypt",
        "correct": 2,
        "exam_id": 1
    },
    50: {
        "question_name":"Which command enables a router to become a DHCP client?",
        "opt1": "ip address dhcp",
        "opt2": "ip helper-address",
        "opt3": "ip dhcp pool",
        "opt4": "ip dhcp client",
        "correct": 1,
        "exam_id": 1
    },
    51: {
        "question_name":"Which IPv6 address type provides communication between subnets and cannot route on the Internet?",
        "opt1": "global unicast",
        "opt2": "unique local",
        "opt3": "link-local",
        "opt4": "multicast",
        "correct": 2,
        "exam_id": 1
    },
    52: {
        "question_name":"Which command prevents passwords from being stored in the configurationas plaintext on a router or switch?",
        "opt1": "enable secret",
        "opt2": "service password-encryption",
        "opt3": "username Cisco password encrypt",
        "opt4": "enable password",
        "correct": 2,
        "exam_id": 1
    },
    53: {
        "question_name":"Which type of address is the public IP address of a NAT device?",
        "opt1": "outside global",
        "opt2": "inside global",
        "opt3": "inside public",
        "opt4": "outside public",
        "correct": 2,
        "exam_id": 1
    },
    54: {
        "question_name":"How does HSRP provide first hop redundancy?",
        "opt1": "It load-balances traffic by assigning the same metric value to more than one route to the same destination m the IP routing table.",
        "opt2": "It load-balances Layer 2 traffic along the path by flooding traffic out all interfaces configured with the same VLAN.",
        "opt3": "It forwards multiple packets to the same destination over different routed links n the data path.",
        "opt4": "It uses a shared virtual MAC and a virtual IP address to a group of routers that serve as the default gateway for hosts on a LAN.",
        "correct": 4,
        "exam_id": 1
    },
    55: {
        "question_name":"A network engineer must back up 20 network router configurations globallywithin a customer environment. Which protocol allows the engineer to perform this function using the Cisco IOS MIB?",
        "opt1": "CDP",
        "opt2": "SNMP",
        "opt3": "SMTP",
        "opt4": "ARP",
        "correct": 2,
        "exam_id": 1
    },
    56: {
        "question_name":"What is the primary different between AAA authentication and authorization?",
        "opt1": "Authentication verifies a username and password, and authorization handles the communication between the authentication agent and the user database.",
        "opt2": "Authentication identifies a user who is attempting to access a system, and authorization validates the users password.",
        "opt3": "Authentication identifies and verifies a user who is attempting to access a system, and authorization controls the tasks the user can perform.",
        "opt4": "Authentication controls the system processes a user can access and authorization logs the activities the user initiates.",
        "correct": 3,
        "exam_id": 1
    },
    57: {
        "question_name":"An engineer must configure a /30 subnet between two routers. Which usable IP address and subnet mask combination meets this criteria?",
        "opt1": "interface e0/0 description to HQ-A370:98968 ip address 10.2.1.3 255.255.255.252",
        "opt2": "interface e0/0 description to HQ-A370:98968 ip address 192.168.1.1 255.255.255.248",
        "opt3": "interface e0/0 description to HQ-A370:98968 ip address 172.16.1.4 255.255.255.248",
        "opt4": "interface e0/0 description to HQ-A370:98968 ip address 209.165.201.2 255.255.255.252",
        "correct": 4,
        "exam_id": 1
    },
    58: {
        "question_name":"Which statement identifies the functionality of virtual machines?",
        "opt1": "Virtualized servers run most efficiently when they are physically connected to a switch that is separate from the hypervisor.",
        "opt2": "The hypervisor can virtualize physical components including CPU, memory, and storage.",
        "opt3": "Each hypervisor can support a single virtual machine and a single software switch.",
        "opt4": "The hypervisor communicates on Layer 3 without the need for additional resources.",
        "correct": 2,
        "exam_id": 1
    },
    59: {
        "question_name":"An organization has decided to start using cloud-provided services. Which cloud service allows the organization to install its own operating system on a virtual machine?",
        "opt1": "platform-as-a-service",
        "opt2": "software-as-a-service",
        "opt3": "network-as-a-service",
        "opt4": "infrastructure-as-a-service",
        "correct": 4,
        "exam_id": 1
    },
    60: {
        "question_name":"Which exfiltration method does an attacker use to hide and encode data inside DNS requests and queries?",
        "opt1": "DNS tunneling",
        "opt2": "DNSCrypt",
        "opt3": "DNS security",
        "opt4": "DNSSEC",
        "correct": 1,
        "exam_id": 1
    },
    61: {
        "question_name":"Which algorithm provides encryption and authentication for data plane communication?",
        "opt1": "AES-GCM",
        "opt2": "SHA-96",
        "opt3": "AES-256",
        "opt4": "SHA-384",
        "correct": 1,
        "exam_id": 1
    },
    62: {
        "question_name":"Which of the following commands erases the contents of the /dev/sdb3 partition?",
        "opt1": "rm /dev/sdb3",
        "opt2": "dd if=/dev/zero of=/dev/sdb3",
        "opt3": "dd of=/dev/zero if=/dev/sdb3",
        "opt4": "umount /dev/sdb3",
        "correct": 2,
        "exam_id": 1
    },
    63: {
        "question_name":"Which single command simulates a failed device within a RAID 5 array?",
        "opt1": "mdadm --remove /dev/md0 /dev/sdd1",
        "opt2": "mdadm --zero-superblock /dev/sdf3",
        "opt3": "mdadm --force-fault /dev/md2 /dev/sde2",
        "opt4": "mdadm --fail /dev/md0 /dev/sdc1",
        "correct": 4,
        "exam_id": 1
    },
    64: {
        "question_name":"What is the minimum number of disks required in a fully redundant RAID5 array?",
        "opt1": "1",
        "opt2": "2",
        "opt3": "3",
        "opt4": "4",
        "correct": 3,
        "exam_id": 1
    },
    65: {
        "question_name":"Which command is used to make an exact copy, at a single point in time, of a logical volume while still allowing the original logical volume to be updated?",
        "opt1": "lvcclone",
        "opt2": "lvcreate",
        "opt3": "lvm2",
        "opt4": "lvsnap",
        "correct": 2,
        "exam_id": 1
    },
    66: {
        "question_name":"Which of the following parameters instructs the kernel at boot time to use only one of the available processors?",
        "opt1": "maxcpus=1",
        "opt2": "usecpus=1",
        "opt3": "smpcpus=1",
        "opt4": "vcpumx=1",
        "correct": 1,
        "exam_id": 1
    },
    67: {
        "question_name":"Which of the following commands by default provides the PIDs of the processes sorted by which are using the most CPU cycles on the Linux system?",
        "opt1": "top",
        "opt2": "uptime",
        "opt3": "ps aux",
        "opt4": "vmstat",
        "correct": 1,
        "exam_id": 1
    },
    68: {
        "question_name":"Which of the following commands adds a static IPv6 address to the network interface eth0?",
        "opt1": "ip add addr 2001:db8::1337/64 dev eth0",
        "opt2": "ip -6 add addr 2001:db8::1337/64 dev eth0",
        "opt3": "ip addr add 2001:db8::1337/64 dev eth0",
        "opt4": "ip -6 addr add new 2001:db8::1337/64 dev eth0",
        "correct": 4,
        "exam_id": 1
    },
    69: {
        "question_name":"What action should be performed after increasing the size of a logical volume?",
        "opt1": "Run vgresize",
        "opt2": "Increase the size of the filesystem used for the logical volume",
        "opt3": "Run 1vresize",
        "opt4": "Remount the logical volume",
        "correct": 2,
        "exam_id": 1
    }
}


for k,v in question_list.items():
    create_ques = requests.post(
        "http://localhost:5000/question",
        json = v,
        headers = {
            "Authorization":f"Bearer {access_token}"
        }
    )
    print("Create new question: ", json.loads(create_ques.text))