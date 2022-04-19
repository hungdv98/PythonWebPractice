
 //http://localhost:3000/?uid=17&eid=1

import QRCode from 'qrcode.react';
import { useState, useEffect } from 'react';

const downloadQR = () => {
    const canvas = document.getElementById('qrcode');
    const pngUrl = canvas.toDataURL('image/png').replace('image/png', 'image/octet-stream');
    console.log('pngUrl', pngUrl);
    let downloadLink = document.createElement('a');
    downloadLink.href = pngUrl;
    downloadLink.download = 'vsec_exam.png';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
};

const CreateQRPage = () => {

    // const [uid, setUid] = useState(17);
    // const [eid, setEid] = useState(1);
    const [uniid, setUniid] = useState(0);
    const [uni, setUni] = useState([]);
    const [examid, setExamid] = useState(0);
    const [examlist, setExam] = useState([]);

    let token=localStorage.getItem("REACT_TOKEN_AUTH_KEY");

    useEffect(() => {
        // const timeout = setTimeout(() => {
        // }, 3000);
        getAllUni();
        getAllExam();
    });

    const getAllUni=()=>{
        const requestOptions={
            method:"GET",
            headers:{
                "content-type":"application/json",
                "Authorization": `Bearer ${JSON.parse(token)}`
            }
          }
        fetch("/uni", requestOptions)
        .then((res) => res.json())
        .then((data) => { 
            setUni(data);
            debugger;
        })
        .catch((err) => console.log(err));
    }

    const getAllExam=()=>{
        const requestOptions={
            method:"GET",
            headers:{
                "content-type":"application/json",
                "Authorization": `Bearer ${JSON.parse(token)}`
            }
          }
        fetch("/exam", requestOptions)
        .then((res) => res.json())
        .then((data) => { 
            setExam(data);
            debugger;
        })
        .catch((err) => console.log(err));
    }


    return(
        <div className="qr101">
            <div className="dropdown-template-uni">
                <select id='template-select-uni' onChange={(e) => setUniid(parseInt(e.target.value))}>
                <option>----</option>
                    {uni.map(option => <option key={option.id} value={option.id}>{option.uniname}</option>)}
                </select>
            </div>
            <div className="dropdown-template-exam">
                <select id='template-select-exam' onChange={(e) => setExamid(parseInt(e.target.value))}>
                <option>----</option>
                    {examlist.map(option => <option key={option.id} value={option.id}>{option.exam_name}</option>)}
                </select>
            </div>
            
            <QRCode
                id='qrcode'
                value="http://192.168.0.172:3000/?uid=17&eid=1"
                size={290}
                level={'H'}
                includeMargin={true}
            />
            <br />
            <button onClick={downloadQR}> Download QR </button>
        </div>
    )
}

export default CreateQRPage;