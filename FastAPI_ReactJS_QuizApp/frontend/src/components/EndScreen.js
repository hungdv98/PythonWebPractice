import React from "react";
import "../App.css";
import { useContext, useEffect } from "react";
import { GameStateContext } from "../helpers/Contexts";

const EndScreen = () => {
  const { handleResult,examid, score, setScore } = useContext(
    GameStateContext
  );

  const axios = require("axios");

  async function getResult(){
    let res = await axios.post(`/gexam/${examid}`, handleResult); 
    setScore(res.data["message"])
  }

  useEffect(() => {
    getResult();
  },[]);

  console.log(handleResult);

  return (
    <div className="EndScreen">
      <h1>Chúc mừng bạn đã hoàn thành bài thi</h1>
      <h1>
        {score}
      </h1>
      
    </div>
  );
};

export default EndScreen;
