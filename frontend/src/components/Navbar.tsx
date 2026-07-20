export default function Navbar() {
  return (
    <div
      style={{
        height: "70px",
        borderBottom: "1px solid #2a2140",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 24px",
      }}
    >
      <h2>Smart Hiring Assistant</h2>

      <button
        style={{
          padding: "10px 18px",
          borderRadius: "8px",
          border: "none",
          cursor: "pointer",
        }}
      >
        Sign Out
      </button>
    </div>
  );
}