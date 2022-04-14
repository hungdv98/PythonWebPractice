import "./App.css";
import Menu from "./components/Menu";
import Quiz from "./components/Quiz";

function App() {
  

  return (
    <div className="App">
        <h2 style={{color: "white"}}>Chào mừng các bạn sinh viên tham gia mini game của VSEC</h2>
        <Menu />
        {/* <Quiz />      */}
    </div>
  );
}

export default App;
