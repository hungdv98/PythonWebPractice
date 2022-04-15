import "../App.css";
import { useState } from "react";
import { Questions } from "../helpers/Questions";


import { useContext } from "react";
import { GameStateContext } from "../helpers/Contexts";

function Quiz(){
   
    const [currentQuestion, setCurrentQuestion] = useState(0);

    const nextQuestion = () => {
        setCurrentQuestion(currentQuestion + 1);
    };

    const finishQuiz = () => {
        setGameState("finished");
    };

    const { gameState, setGameState } = useContext(
        GameStateContext
    );
    

    return(
        <div className="Quiz">
            <h1>{Questions[currentQuestion].question_name}</h1>
            <div className="questions">
                <button onClick={nextQuestion}>
                    {Questions[currentQuestion].opt1}
                </button>
                <button onClick={nextQuestion}>
                    {Questions[currentQuestion].opt2}
                </button>
                <button onClick={nextQuestion}>
                    {Questions[currentQuestion].opt3}
                </button>
                <button onClick={nextQuestion}>
                    {Questions[currentQuestion].opt4}
                </button>
            </div>
            {currentQuestion === Questions.length - 1 ? (
                <button onClick={finishQuiz} id="nextQuestion">
                    Hoàn thành
                </button>
            ) : (
                <button onClick={nextQuestion} id="nextQuestion">
                    Câu tiếp
                </button>
            )}
        </div>
    )
}

export default Quiz;