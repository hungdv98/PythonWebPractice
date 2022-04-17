import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import SignUpPage from "./components/SignUp";
import LoginPage from "./components/Login";
import NavBar from "./components/Navbar";
import HomePage from "./components/Home";

import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css';

function App() {
  return (
    <BrowserRouter>
    <div className="">
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />}/>
        <Route path="/signup" element={<SignUpPage />}/>
        <Route path="/login" element={<LoginPage />}/>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
