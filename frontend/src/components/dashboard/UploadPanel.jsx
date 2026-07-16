import { useState } from "react";

function UploadPanel(){

    const[selectedFile, setSelectedFile] = useState(null);

    return (
        
        <div
            style={{ 
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "30px",
            }}>
            
            <h2>Upload Log File to Analyze</h2>

            <input type="file"
                accept=".log,.txt"
                onChange={(e) => setSelectedFile(e.target.files[0])} />

            {selectedFile && (
                <p style={{ marginTop: "10px" }}>
                    Selected File: <strong>{selectedFile,name}</strong>
                </p>
            )}

            <button
                style={{marginTop:"15px", padding: "10px 20px", cursor:"pointer"}}>
                    Analyze Log
                </button>
            </div>
    );
}

export default UploadPanel;