import { useState } from "react";
import Layout from "../components/layout/Layout";
import { login } from "../services/auth";

function Login(){

    const[email, setEmail] = useState("");
    const[password, setPassword] = useState("");
    const[message, setMessage] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        try{
            const response = await login({
                email, password
            });

            setMessage("Welcome " + response.data.username);
        }
        catch(error){
            setMessage("Login Failed");
        }
    }

    return (
        <Layout>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <input type="email" placeholder="Email" value={email} onChange={(e)=>setEmail(e.target.value)} />
                <br/>
                <br/>
                <input type="password" placeholder="Password" value={password} onChange={(e)=>setPassword(e.target.value)} />
                <br/>
                <br/>
                <button type="submit">
                    Login
                </button>
            </form>
                <p>{message}</p>
        </Layout>
    );
}

export default Login;