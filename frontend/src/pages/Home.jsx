import { useEffect, useState } from "react";
import api from "../services/api";
import Layout from "../components/layout/Layout";

function Home(){
    const[message, setMessage] = useState("");
    useEffect(() => {
        api.get("/api/test")
            .then((response) => {
                setMessage(response.data.message);
            })
            .catch((error) => {
                console.error(error);
            });
    },[]);

    return (
        <Layout>
        <h1> Log Analysis Dashboard </h1>
        
        <p> {message} </p>

        </Layout>
    );
}

export default Home;