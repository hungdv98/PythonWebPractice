import { useState } from "react";
import { Questions } from "../helpers/Questions";

function Quiz(){
   
    const [currentQuestion, setCurrentQuestion] = useState(0);

    check()
    return(
        <div className="Quiz">
            <h1>{Questions[currentQuestion].question_name}</h1>
        </div>
    )
}

export default Quiz;