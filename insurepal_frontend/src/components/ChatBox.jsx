import React, { useState } from "react";
import axios from "axios";

function ChatBox({ file, uploaded }) {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!query || !file) return;

    setMessages([...messages, { sender: "user", text: query }]);
    setLoading(true);

    const formData = new FormData();
    formData.append("query", query);
    formData.append("file", file);

    try {
      const res = await axios.post(
        "http://localhost:8000/hackrx/run", // Update with your backend URL
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: res.data.result || "No response" },
      ]);
      setQuery("");
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error communicating with API." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "2em" }}>
      <h4>Chat</h4>
      <div
        style={{
          background: "#f2f2f2",
          padding: "1em",
          height: 300,
          overflow: "auto",
          marginBottom: "1em",
        }}
      >
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              textAlign: msg.sender === "user" ? "right" : "left",
              margin: "0.5em 0",
            }}
          >
            <b>{msg.sender === "user" ? "You" : "Bot"}:</b> {msg.text}
          </div>
        ))}
        {loading && <div>Bot is typing...</div>}
      </div>
      <form onSubmit={sendMessage} style={{ display: "flex", gap: 8 }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={file ? "Ask a question..." : "Upload a document first"}
          disabled={!file}
          style={{ flex: 1 }}
        />
        <button type="submit" disabled={!file || loading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default ChatBox;
