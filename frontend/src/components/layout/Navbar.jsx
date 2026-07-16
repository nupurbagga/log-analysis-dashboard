import { Link } from "react-router-dom";

function Navbar(){
    return (
        <nav 
            style={{
                background: "#6b5bd2",
                padding: "0.5rem 1rem",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
            }}
        >
            <h2 style={{color:"#112375"}}> Log Dashboard</h2>

            <div style={{display:"flex", gap: "25px"}}>
                <Link style={{color: "white"}} to="/">
                Home
                </Link>

                <Link style={{color: "white"}} to="/login">
                Login
                </Link>

                <Link style={{color: "white"}} to="/register">
                Register
                </Link>

                <Link style={{color: "white"}} to="/dashboard">
                Dashboard
                </Link>
            </div>
        </nav>
    );
}


export default Navbar;