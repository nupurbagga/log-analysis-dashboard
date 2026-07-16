import Card from "../common/Card";

function StatCards(){
    return (
        <div 
            style={{display: "flex", gap: "20px", marginTop: "30px"}}>
            
            <Card title="Critical Alerts" value="0" />
            <Card title="Warning" value="0" />
            <Card title="Info" value="0" />
            <Card title="Uploads" value="0" />
        </div>
    );
}

export default StatCards;