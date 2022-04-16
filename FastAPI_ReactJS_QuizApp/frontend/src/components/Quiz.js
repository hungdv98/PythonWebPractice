import "../App.css";
import { useState, useContext, useEffect } from "react";
import { GameStateContext } from "../helpers/Contexts";

let handleRequest = {
    "user_id":0,
    "ans":[]
};

function Quiz(){
 
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [Questions, setQuestions] = useState([]);
    
    const { gameState, setGameState, userid, setUserid } = useContext(
        GameStateContext
    );

    const axios = require("axios");
   
    async function getData(){
        let res = await axios.get("/gexam/1"); 
        setQuestions(res.data);
        console.log("data = ",res.data);
    }

    useEffect(() => {
        getData();
    },[]);

    const nextQuestion = (e) => {
        e.preventDefault();
        handleRequest["ans"].push({"id":Questions[currentQuestion].id,"correct":parseInt(e.target.value)});
        setCurrentQuestion(currentQuestion + 1);
        if (currentQuestion === Questions.length - 1){
            handleRequest["ans"].push({"id":Questions[currentQuestion].id,"correct":parseInt(e.target.value)});
            setGameState("finished");
            handleRequest["ans"].pop();
            handleRequest["user_id"] = parseInt(userid);
            console.log(handleRequest);
            debugger;
        }
    };

    const finishQuiz = (e) => {
        e.preventDefault();
        handleRequest["ans"].push({"id":Questions[currentQuestion].id,"correct":e.target.value});
        setGameState("finished");
        console.log(handleRequest);
    };
    
    return(
        <div className="Quiz">
            <h1>{Questions.length > 0 && Questions[currentQuestion].question_name}</h1>
            <div className="questions">
                <button onClick={nextQuestion} value="1">
                    {Questions.length > 0 &&Questions[currentQuestion].opt1}
                </button>
                <button onClick={nextQuestion} value="2">
                    {Questions.length > 0 &&Questions[currentQuestion].opt2}
                </button>
                <button onClick={nextQuestion} value="3">
                    {Questions.length > 0 &&Questions[currentQuestion].opt3}
                </button>
                <button onClick={nextQuestion} value="4">
                    {Questions.length > 0 &&Questions[currentQuestion].opt4}
                </button>
            </div>
            {/* {currentQuestion === Questions.length - 1 ? (
                <button onClick={finishQuiz} id="nextQuestion">
                    Hoàn thành
                </button>
            ) : (
                <button onClick={nextQuestion} id="nextQuestion">
                    Câu tiếp
                </button>
            )} */}
        </div>
    )
}

export default Quiz;