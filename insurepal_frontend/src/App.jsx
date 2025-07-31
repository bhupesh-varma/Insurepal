import React, { useState } from "react";
import UploadDocument from "./components/UploadDocument";
import ChatBox from "./components/ChatBox";

function App() {
  const [file, setFile] = useState(null);
  const [uploaded, setUploaded] = useState(false);

  const handleFileSelect = (selectedFile) => {
    setFile(selectedFile);
    setUploaded(true);
  };

  return (
    <div style={{ margin: "2em auto", maxWidth: 600 }}>
      <h2>Document Chat - HackRx</h2>
      <UploadDocument setFile={handleFileSelect} />
      <ChatBox file={file} uploaded={uploaded} />
    </div>
  );
}

export default App;
