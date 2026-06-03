function StatsBar() {
  return (
    <div className="stats-bar">

      <div className="stat-card">
        <h4>Total Videos</h4>
        <span>2</span>
      </div>

      <div className="stat-card">
        <h4>Platforms</h4>
        <span>
          <span style={{ color: "#f7f5f5" }}>
            YouTube
          </span>
          {" + "}
          <span style={{ color: "#e9e9e9" }}>
            Instagram
          </span>
        </span>
      </div>

      <div className="stat-card">
        <h4>RAG Search</h4>
        <span style={{ color: "#22c55e" }}>
          Enabled
        </span>
      </div>

      <div className="stat-card">
        <h4>AI Status</h4>
        <span style={{ color: "#22c55e" }}>
          Ready
        </span>
      </div>

    </div>
  );
}

export default StatsBar;