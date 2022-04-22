import React,{ useContext, useState } from "react";
import { Form, Button } from "react-bootstrap";
import { useForm } from "react-hook-form";
import { GameStateContext } from "../helpers/Contexts";
import QRCode from 'qrcode.react';
import Popup from "reactjs-popup";
import Rules from "./Rules.js";
import "../index.css";

const ValidUid = () => {

    const { setGameState, setUserid, setUniid }  = useContext( GameStateContext );
    const {register,handleSubmit,reset,formState:{errors}}=useForm()
    

    const submitForm=(data)=>{
        
        let uniId;
        try{
            uniId = parseInt(window.location.href.split("?")[1].split("&")[0].split("=")[1]);
        }
        catch (e){}

        const body={
            fullname:data.fullname,
            mssv:data.mssv,
            major:data.major,
            email:data.email,
            phonenumb:data.phonenumb,
            jobpos:data.jobpos,
            uni_id:`${uniId}`
        }

        const requestOptions={
            method:"POST",
            headers:{
                "content-type":"application/json"
            },
            body:JSON.stringify(body)
        }
        fetch('/user', requestOptions)
        .then((res)=>res.json())
        .then((data)=>{
            console.log(data)
            setUserid(JSON.parse(data)["id"].toString());
            setUniid(uniId);
        })
        .catch(err=>console.log(""))
        reset();    
        setGameState("playing");
    }

    return(
        <>
        <Popup trigger={<button id="tlct">Thể lệ chương trình</button>}>
        {close => <Rules close={close} />}
        </Popup>
        <div className="form">
        <form>
            <Form.Group>
                <Form.Label>Họ và tên</Form.Label>
            </Form.Group>
            <Form.Control type="text" 
                    placeholder=""
                    {...register("fullname",{
                        required:true,
                        maxLength:25
                    })}
                    />
            {errors.fullname && <p style={{color:"red"}}><small>Bạn cần nhập họ và tên</small></p>}
            {errors.fullname?.type==="maxLength"&&<p style={{color:"red"}}><small>Số ký tự tối đa là 25</small></p>}
            <Form.Group>
                <Form.Label>Mã sinh viên</Form.Label>
            </Form.Group>
            <Form.Control type="text" 
                    placeholder=""
                    {...register("mssv",{
                        required:true,
                        maxLength:20
                    })}
                    />
            {errors.mssv && <p style={{color:"red"}}><small>Bạn cần nhập mã sinh viên</small></p>}
            {errors.mssv?.type==="maxLength"&&<p style={{color:"red"}}><small>Số ký tự tối đa là 20</small></p>}
            <Form.Group>
                <Form.Label>Ngành học</Form.Label>
            </Form.Group>
            <Form.Control type="text" 
                    placeholder=""
                    {...register("major",{
                        required:true,
                        maxLength:80
                    })}
                    />
            {errors.major && <p style={{color:"red"}}><small>Bạn cần nhập ngành học</small></p>}
            {errors.major?.type==="maxLength"&&<p style={{color:"red"}}><small>Số ký tự tối đa là 80</small></p>}
            <Form.Group>
                <Form.Label>Email</Form.Label>
            </Form.Group>
            <Form.Control type="email" 
                    placeholder=""
                    {...register("email",{
                        required:true,
                        maxLength:80
                    })}
                    />
            {errors.email && <p style={{color:"red"}}><small>Bạn cần nhập email</small></p>}
            {errors.email?.type==="maxLength"&&<p style={{color:"red"}}><small>Số ký tự tối đa là 80</small></p>}
            <Form.Group>
                <Form.Label>Số điện thoại</Form.Label>
            </Form.Group>
            <Form.Control type="text" 
                    placeholder=""
                    {...register("phonenumb",{
                        required:true,
                        maxLength:20
                    })}
                    />
            {errors.phonenumb && <p style={{color:"red"}}><small>Bạn cần nhập số điện thoại</small></p>}
            {errors.phonenumb?.type==="maxLength"&&<p style={{color:"red"}}><small>Số ký tự tối đa là 20</small></p>}
            <Form.Group>
                <Form.Label>Vị trí làm việc mong muốn (nếu có)</Form.Label>
            </Form.Group>
            <Form.Control type="text" 
                    placeholder=""
                    {...register("jobpos",{
                        required:false,
                        maxLength:80
                    })}
                    />
            <br/>
            <br/>
                <Form.Group>
                    <Button variant="primary"
                        onClick={ handleSubmit(submitForm)
                            // () => {
                            //     handleSubmit(submitForm),
                            //     // setGameState("playing")
                            //     }
                            }>
                            Bắt đầu bài thi
                    </Button> 
                </Form.Group>
        </form>
        </div>
        </>
    )
    
}

const InValidUid = () => {
    return(
        <div>
            
            <QRCode
                id='qrcode'
                value="http://jobfair.vsec.vn/?uid=27&eid=1"
                size={290}
                level={'H'}
                includeMargin={true}
            />
        </div>
    )
}


const InfoForm=()=>{

    let validId = false;
    let uniId;
    try{
        uniId = parseInt(window.location.href.split("?")[1].split("&")[0].split("=")[1]);
    }
    catch (e){}

    if(typeof uniId !== "undefined"){
        validId = true;
    }

    return(      
        <>
            {validId ? <ValidUid />: <InValidUid/>}
        </>
    )
}

export default InfoForm; 