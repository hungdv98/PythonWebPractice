import React, { useState, useEffect } from "react";
import { useAuth } from "../auth";
import {Link} from "react-router-dom";
import "../App.css";


const LoggedinHome = () => {
    const [resdata, setResdata] = useState([]);
    const [uniid, setUniid] = useState(0);
    const [uni, setUni] = useState([]);

    let token=localStorage.getItem("REACT_TOKEN_AUTH_KEY");

    const axios = require("axios");
    async function getData(){
        let res = await axios.get(`/leaderboard/${uniid}`, {
            headers:{
                "content-type":"application/json",
                "Authorization": `Bearer ${JSON.parse(token)}`
            }
        });
        console.log(res.data);
        setResdata(res.data);
        //debugger;
    }

    useEffect(() => {
        const timeout = setTimeout(() => {
            getData();
        }, 3000);
        getAllUni();
    }, [resdata]);

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
            //debugger;
        })
        .catch((err) => console.log(err));
    }

    return(
        <div className="leaderboard">
            <h1>Leaderboard</h1>
            <div className="handleResult">
                <input 
                    id="uni_id"  
                    type="text"
                    onChange={(e) => setUniid(parseInt(e.target.value))}
                />
            </div>
            {/* <select id='template-select' onChange={(e) => setUniid(parseInt(e.target.value))}>
            <option>----</option>
                {uni.map(option => <option key={option.id} value={option.id}>{option.uniname}</option>)}
            </select> */}
            <table>
                <thead>
                    <tr>
                        <td className="special"><div>EMAIL</div></td>
                        <td className="special"><div>FULLNAME</div></td>
                        <td className="special"><div>PHONE</div></td>
                        <td className="special"><div>MSSV</div></td>
                        <td className="special"><div>DATETIME</div></td>
                        <td className="special"><div>SCORE</div></td>
                    </tr>
                </thead>
                <tbody>
                    {resdata.map((data, index) =>(
                        <tr key={index}>
                            <td className="special"><div>{data.email}</div></td>
                            <td className="special"><div>{data.fullname}</div></td>
                            <td className="special"><div>{data.phonenumb}</div></td>
                            <td className="special"><div>{data.mssv}</div></td>
                            <td className="special"><div>{data.datetime}</div></td>
                            <td className="special"><div>{data.score}</div></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
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
