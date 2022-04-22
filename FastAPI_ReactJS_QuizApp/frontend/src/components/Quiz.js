import "../App.css";
import { useState, useContext, useEffect } from "react";
import { GameStateContext } from "../helpers/Contexts";

let handleRequest = {
    "user_id":0,
    "ans":[]
};

const formatCD = (cc) => {
    let c = new Date(parseInt(cc) * 1000).toISOString().substr(14, 5);
    return c;
}

function Quiz(){
 
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [Questions, setQuestions] = useState([]);
    
    const [counter, setCounter] = useState(1200);

    const { setGameState, userid, setHandleResult, setExamid } = useContext(
        GameStateContext
    );

    const axios = require("axios");

    //http://localhost:3000/?uid=17&eid=1
    let examId = parseInt(window.location.href.split("?")[1].split("&")[1].split("=")[1]);
   
    async function getData(){
        let res = await axios.get(`/gexam/${examId}`); 
        setQuestions(res.data);
        setExamid(examId);
        console.log("data = ",res.data);
    }

    useEffect(() => {
        const timer = counter > 0 && setInterval(() => setCounter(counter - 1), 1000);
        return () => clearInterval(timer);
    },[counter]);

    useEffect(() => {
        getData();
    },[]) 


    const nextQuestion = (e) => {
        e.preventDefault();
        handleRequest["ans"].push({"id":Questions[currentQuestion].id,"correct":parseInt(e.target.value)});
        setCurrentQuestion(currentQuestion + 1);
        if (currentQuestion === Questions.length - 1){
            handleRequest["ans"].push({"id":Questions[currentQuestion].id,"correct":parseInt(e.target.value)});
            setGameState("finished");
            handleRequest["ans"].pop();
            handleRequest["user_id"] = parseInt(userid);
            //console.log(handleRequest);
            setHandleResult(handleRequest);
        }
    };
    
    return(
        <>
        <div className="Quiz">
        <div style={{color: "red"}}>Thời gian còn lại: {formatCD(counter)}</div>
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
        </>
    )
}

export default Quiz;