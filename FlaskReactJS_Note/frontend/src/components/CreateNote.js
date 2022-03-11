import React from "react";
import { Form, Button } from "react-bootstrap";
import {useForm} from "react-hook-form";


const CreateNotePage=()=>{

    const {register,handleSubmit,reset,formState:{errors}}=useForm()

    const createNote=(data)=>{
        console.log(data)
        const token=localStorage.getItem("REACT_TOKEN_AUTH_KEY")

        console.log(token)
    
        const requestOptions={
            method:"POST",
            headers:{
                "content-type":"application/json",
                "Authorization":`Bearer ${JSON.parse(token)}`
            },
            body:JSON.stringify(data)
        }

        fetch("/note/notes", requestOptions)
        .then(res => res.json())
        .then(data => {
            reset()
        })
        .catch(err => console.log(err))
    }

    return (
        <div className="container">
            <h1>Create A Note</h1>
            <form>
                <Form.Group>
                    <Form.Label>Title</Form.Label>
                    <Form.Control type="text"
                        {...register("title",{
                            required:true,
                            maxLength:25
                        })}
                    />
                </Form.Group>
                {errors.title && <p style={{color:"red"}}><small>Title is required</small></p>}
                {errors.title?.type==="maxLength"&&<p style={{color:"red"}}><small>Max characters should be 25</small></p>}
                <Form.Group>
                    <Form.Label>Description</Form.Label>
                    <Form.Control as="textarea" rows={5}
                        {...register("description", {
                            required:true,
                            maxLength:255
                        })}
                    />
                </Form.Group>
                {errors.description && <p style={{color:"red"}}><small>Description is required</small></p>}
                {errors.description?.type==="maxLength"&&<p style={{color:"red"}}><small>Max characters should be 255</small></p>}
                <br/>
                <Form.Group>
                    <Button variant="primary" onClick={handleSubmit(createNote)}>
                        Save
                    </Button>
                </Form.Group>
            </form>
        </div>
    )
}

export default CreateNotePage;