import React from "react";
import "../index.css";

export default ({ close }) => (
  <div className="modal">
    <div className="header"> Chào mừng các bạn sinh viên tham gia mini game của VSEC </div>
    <div className="content">
      {" "}
        Thể lệ chương trình:
        <ul>
            <li>Người chơi sẽ trải qua 26 câu hỏi trong 20 phút</li>
            <li>Với mỗi câu trả lời đúng sẽ nhận được số điểm tương ứng</li>
            <li>100% người chơi sẽ nhận được 1 phần quà</li>
            <li>Những người chơi có số điểm cao nhất sẽ có cơ hội tiến vào vòng trong</li>
        </ul>
        Hãy điền thông tin dưới đây để tham gia thử thách

    </div>
    <div className="footer">
        <button className="close" onClick={close} id="confirm101">Đã rõ</button>
    </div>
    
  </div>
);