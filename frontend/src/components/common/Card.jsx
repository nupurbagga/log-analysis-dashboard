function Card({title, value}){
    return(
        <div 
            style={{
                border: "1px solid #ddd", borderRadius: "10px", padding: "20px", minWidth: "180px"}}>
        <h3>{title}</h3>
        <h1>{value}</h1>
        </div>
    );
}

export default Card;