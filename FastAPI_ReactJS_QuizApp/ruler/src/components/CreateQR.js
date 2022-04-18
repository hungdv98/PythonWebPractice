
 //http://localhost:3000/?uid=17&eid=1

import QRCode from 'qrcode.react';
// import { useState } from 'react';

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

    return(
        <div>
            <QRCode
                id='qrcode'
                value="http://192.168.0.172:3000/?uid=17&eid=1"
                size={290}
                level={'H'}
                includeMargin={true}
            />
            <br />
            <a onClick={downloadQR}> Download QR </a>
        </div>
    )
}

export default CreateQRPage;