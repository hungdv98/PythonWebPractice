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
    //debugger;
  }

  useEffect(() => {
    getResult();
  },[]);

  //console.log(handleResult);

  return (
    <div className="EndScreen">
      <h1 id="es-title">CONGRATULATIONS!</h1>
      <h2 id="es-s1">Chúc mừng bạn đã hoàn thành thử thách của chúng tôi</h2>
      <h2 id="es-s1">Số điểm của bạn đã đạt được là</h2>
      <span className="dot">
        {score}
      </span>
      <h2 id="es-s1">Bạn sẽ nhận được một phần quà từ VSEC.</h2>
      <h2 id="es-s1">Chúc bạn một ngày vui vẻ</h2>
      
    </div>
  );
};

export default EndScreen;
