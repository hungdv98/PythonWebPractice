import { StrictMode, useState, useEffect } from 'react'
import { createRoot } from "react-dom/client";

const App = () => {
    useEffect(
        () => {
            fetch("/auth/noauthen")
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setMessage(data.message)
            })
            .then(err => console.log(err))

        },[]
    )
    const [message, setMessage] = useState("");
    return(
        <div className="container">
            <h1>{message}</h1>
        </div>
    )
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
    <StrictMode>
        <App />
    </StrictMode>
)