import React,{ useContext } from "react";
import { Form, Button } from "react-bootstrap";
import { useForm } from "react-hook-form";
import { GameStateContext } from "../helpers/Contexts";


const InfoForm=()=>{

    const {register,handleSubmit,reset,formState:{errors}}=useForm()
    const { gameState, setGameState }  = useContext( GameStateContext );

    const submitForm=(data)=>{
        const body={
            fullname:data.fullname,
            mssv:data.mssv,
            major:data.major,
            email:data.email,
            phonenumb:data.phonenumb,
            uni_id:17
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
        })
        .catch(err=>console.log(err))
        reset();    
    }

    return(
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
                <br/>
                <br/>
                    <Form.Group>
                        <Button variant="primary"
                            onClick={ 
                                () => {
                                    handleSubmit(submitForm),
                                    setGameState("playing")
                                    }
                                }>
                                Bắt đầu bài thi
                        </Button> 
                    </Form.Group>
            </form>
        </div>
    )
}

export default InfoForm; 