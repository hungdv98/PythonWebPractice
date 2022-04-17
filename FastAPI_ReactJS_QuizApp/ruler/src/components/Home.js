import { useAuth } from "../auth";

const HomePage = () => {
    const [logged] = useAuth();
    
    console.log("logged = ", logged);

    return(
        <div className="Home">
            {logged}
        </div>
    )
  };
  
  export default HomePage;
  