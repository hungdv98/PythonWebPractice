import { useAuth } from "../auth";

const HomePage = () => {
    const [logged] = useAuth();
    
    console.log("logged = ", logged);

    return <div>{logged}</div>;
  };
  
  export default HomePage;
  