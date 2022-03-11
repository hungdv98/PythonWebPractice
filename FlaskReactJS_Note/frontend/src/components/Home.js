import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../auth";
import Note from "./Note";
import { Modal, Form, Button } from "react-bootstrap";
import { useForm } from "react-hook-form";


const LoggedinHome = () => {
  const [notes, setNotes] = useState([]);
  const [show, setShow] = useState(false);
  const {register,handleSubmit,setValue,formState:{errors}}=useForm();
  const [noteId, setNoteId]=useState(0);


  useEffect(() => {
    fetch("/note/notes")
      .then((res) => res.json())
      .then((data) => { 
        setNotes(data);
      })
      .catch((err) => console.log(err));
  }, []);

  const getAllNotes=()=>{
    fetch("/note/notes")
    .then((res) => res.json())
    .then((data) => { 
      setNotes(data);
    })
    .catch((err) => console.log(err));
  }

  const closeModal = () => {
    setShow(false);
  };

  const showModal = (id) => {
    setShow(true)
    setNoteId(id)
    notes.map(
        (note)=>{
            if(note.id===id){
                setValue("title",note.title)
                setValue("description",note.description)
            }
        }
    )
  };

  let token=localStorage.getItem("REACT_TOKEN_AUTH_KEY")

  const updateNote=(data)=>{
      console.log(data)
      
     
      const requestOptions={
          method:"PUT",
          headers:{
              "content-type":"application/json",
              "Authorization": `Bearer ${JSON.parse(token)}`
          },
          body:JSON.stringify(data)
      }

      fetch(`/note/note/${noteId}`,requestOptions)
      .then(res => res.json())
      .then(data => {
          console.log(data)
          const reload = window.location.reload()
          reload()
        //window.location.reload()
      })
      .catch(err => console.log(err))
  }

  const deleteNote=(id)=>{
      console.log(id)

      const requestOptions={
        method:"DELETE",
        headers:{
            "content-type":"application/json",
            "Authorization": `Bearer ${JSON.parse(token)}`
        }
      }

      fetch(`/note/note/${id}`,requestOptions)
      .then(res => res.json())
      .then(data => {
          console.log(data)
          getAllNotes()
      })
      .catch(err => console.log(err))
  }

  return (
    <div className="notes">
      <Modal show={show} size="lg" onHide={closeModal}>
        <Modal.Header closeButton>
          <Modal.Title>Update Note</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <form>
            <Form.Group>
              <Form.Label>Title</Form.Label>
              <Form.Control
                type="text"
                {...register("title", {
                  required: true,
                  maxLength: 25,
                })}
              />
            </Form.Group>
            {errors.title && (
              <p style={{ color: "red" }}>
                <small>Title is required</small>
              </p>
            )}
            {errors.title?.type === "maxLength" && (
              <p style={{ color: "red" }}>
                <small>Max characters should be 25</small>
              </p>
            )}
            <Form.Group>
              <Form.Label>Description</Form.Label>
              <Form.Control
                as="textarea"
                rows={5}
                {...register("description", {
                  required: true,
                  maxLength: 255,
                })}
              />
            </Form.Group>
            {errors.description && (
              <p style={{ color: "red" }}>
                <small>Description is required</small>
              </p>
            )}
            {errors.description?.type === "maxLength" && (
              <p style={{ color: "red" }}>
                <small>Max characters should be 255</small>
              </p>
            )}
            <br />
            <Form.Group>
              <Button variant="primary" onClick={handleSubmit(updateNote)}>
                Save
              </Button>
            </Form.Group>
          </form>
        </Modal.Body>
      </Modal>

      <h1>List of Notes</h1>
      {notes.map((note,index) => (
        <Note
          title={note.title}
          key={index}
          description={note.description}
          onClick={()=>{showModal(note.id)}}
          onDelete={()=>{deleteNote(note.id)}}
        />
      ))}
    </div>
  );
};

const LoggedoutHome = () => {
  return (
    <div className="home container">
      <h1 className="heading">Welcome to the Notes</h1>
      <Link to="/signup" className="btn btn-primary btn-lg">
        Get Started
      </Link>
    </div>
  );
};

const HomePage = () => {
  const [logged] = useAuth();

  return <div>{logged ? <LoggedinHome /> : <LoggedoutHome />}</div>;
};

export default HomePage;
