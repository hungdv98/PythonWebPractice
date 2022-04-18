import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../auth";
import "../App.css";


const LoggedinHome = () => {
    const [resdata, setResdata] = useState([]);

    let token=localStorage.getItem("REACT_TOKEN_AUTH_KEY");
    // fetch("/leaderboard/17", {
    //     method:"GET",
    //     headers:{
    //         "content-type":"application/json",
    //         "Authorization": `Bearer ${JSON.parse(token)}`
    //     },
    // })
    // .then(res => res.json())
    // .then(data => {
    //     console.log(data);
    //     setResdata(data);
    // })
    // .catch((err) => console.log(err));

    const axios = require("axios");
    async function getData(){
        let res = await axios.get("/leaderboard/17", {
            headers:{
                "content-type":"application/json",
                "Authorization": `Bearer ${JSON.parse(token)}`
            }
        });
        console.log(res.data);
        setResdata(res.data);
       debugger;
    }

    useEffect(() => {
        getData();
    },[]);

    return(
        <div>
            <h1>Leaderboard</h1>


            <div className="leaderboard">
                <ul>
                    {resdata.map(
                        (info) => {
                            <li>{info.fullname}</li>
                        }
                    )}
                </ul>
            </div>
        </div>
       
    )
  

// //   const closeModal = () => {
// //     setShow(false);
// //   };

//   return (
//     <div className="leaderboard">
//       {/* <Modal show={show} size="lg" onHide={closeModal}>
//         <Modal.Body>
//           <form>
//             <Form.Group>
//               <Form.Label>Title</Form.Label>
//               <Form.Control
//                 type="text"
//                 {...register("title", {
//                   required: true,
//                   maxLength: 25,
//                 })}
//               />
//             </Form.Group>
//             {errors.title && (
//               <p style={{ color: "red" }}>
//                 <small>Title is required</small>
//               </p>
//             )}
//             {errors.title?.type === "maxLength" && (
//               <p style={{ color: "red" }}>
//                 <small>Max characters should be 25</small>
//               </p>
//             )}
//             <Form.Group>
//               <Form.Label>Description</Form.Label>
//               <Form.Control
//                 as="textarea"
//                 rows={5}
//                 {...register("description", {
//                   required: true,
//                   maxLength: 255,
//                 })}
//               />
//             </Form.Group>
//             {errors.description && (
//               <p style={{ color: "red" }}>
//                 <small>Description is required</small>
//               </p>
//             )}
//             {errors.description?.type === "maxLength" && (
//               <p style={{ color: "red" }}>
//                 <small>Max characters should be 255</small>
//               </p>
//             )}
//             <br />
//             <Form.Group>
//               <Button variant="primary" onClick={handleSubmit(updateNote)}>
//                 Save
//               </Button>
//             </Form.Group>
//           </form>
//         </Modal.Body>
//       </Modal> */}

//       {/* <h1>Leaderboard</h1>
//       {res.map((data) => (
//         <h1>{data.fullname}</h1>
//       ))} */}
//     </div>
//   );
};

const LoggedoutHome = () => {
  return (
    <div className="home container">
      <h1 className="heading">Welcome to Leaderboard</h1>
      <Link to="/signup" className="btn btn-primary btn-lg">
        Get Started
      </Link>
    </div>
  );
};

const Leaderboard = () => {
  const [logged] = useAuth();

  return <div>{logged ? <LoggedinHome /> : <LoggedoutHome />}</div>;
};

export default Leaderboard;
