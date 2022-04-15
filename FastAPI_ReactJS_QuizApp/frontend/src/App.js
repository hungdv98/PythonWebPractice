import "./App.css";
import { useState } from "react";
import Menu from "./components/Menu";
import Quiz from "./components/Quiz";
import EndScreen from "./components/EndScreen";
import { GameStateContext } from "./helpers/Contexts";

function App() {
  
  const [gameState, setGameState] = useState("menu");

  return (
    <div className="App">
        <h2 style={{color: "white"}}>Chào mừng các bạn sinh viên tham gia mini game của VSEC</h2>
        <GameStateContext.Provider
          value={{
            gameState,
            setGameState,
          }}>
        {gameState === "menu" && <Menu />}
        {gameState === "playing" && <Quiz />}   
        {gameState === "finished" && <EndScreen />}
        </GameStateContext.Provider>
    </div>
  );
}

export default App;
