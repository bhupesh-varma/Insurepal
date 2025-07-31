import React from "react";

function UploadDocument({ setFile }) {
  const handleChange = (e) => {
    if (e.target.files.length) {
      setFile(e.target.files[0]);
    }
  };

  return (
    <div>
      <h4>Upload Document</h4>
      <input type="file" onChange={handleChange} />
    </div>
  );
}

export default UploadDocument;
