
 //http://localhost:3000/?uid=17&eid=1

import QRCode from 'qrcode.react';

const CreateQRPage = () => {



    return(
        <div>
            <QRCode
                id='qrcode'
                value="http://localhost:3000/?uid=17&eid=1"
                size={290}
                level={'H'}
                includeMargin={true}
            />
        </div>
    )
}

export default CreateQRPage;