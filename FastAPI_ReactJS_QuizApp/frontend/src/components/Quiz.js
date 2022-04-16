import "../App.css";
import { useState } from "react";
//import { Questions } from "../helpers/Questions";
import getData from "../helpers/Questions";



import { useContext, useEffect } from "react";
import { GameStateContext } from "../helpers/Contexts";


function Quiz(){
 
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [Questions, setQuestions] = useState([]);
    const axios = require("axios");
   
    async function getData(){
        let res = await axios.get("/gexam/1"); 
        setQuestions(res.data);
    }

    useEffect(() => {
        getData();
    },[]);

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
            <h1>{Questions.length > 0 && Questions[currentQuestion].question_name}</h1>
            <div className="questions">
                <button onClick={nextQuestion}>
                    {Questions.length > 0 &&Questions[currentQuestion].opt1}
                </button>
                <button onClick={nextQuestion}>
                    {Questions.length > 0 &&Questions[currentQuestion].opt2}
                </button>
                <button onClick={nextQuestion}>
                    {Questions.length > 0 &&Questions[currentQuestion].opt3}
                </button>
                <button onClick={nextQuestion}>
                    {Questions.length > 0 &&Questions[currentQuestion].opt4}
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