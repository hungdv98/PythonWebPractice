import React from "react";
import "../App.css";
import { useContext } from "react";
import { GameStateContext } from "../helpers/Contexts";
import { Questions } from "../helpers/Questions";

const EndScreen = () => {
  const { setGameState } = useContext(
    GameStateContext
  );

  return (
    <div className="EndScreen">
      <h1>Chúc mừng bạn đã hoàn thành bài thi</h1>
      <h1>
        0 / {Questions.length}
      </h1>
    </div>
  );
};

export default EndScreen;
