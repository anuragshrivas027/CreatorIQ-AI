function ComparisonPanel({
  comparison,
  loading,
}) {
  return (
    <div className="comparison-panel">

      <div className="comparison-header">
        AI Comparison Report
      </div>

      {loading ? (

        <div className="comparison-loading">
          Comparing videos...
        </div>

      ) : (

        <div className="comparison-content">

          {comparison ? (
            <pre className="comparison-text">
              {comparison}
            </pre>
          ) : (
            "Upload Video A and Video B then run comparison."
          )}

        </div>

      )}

    </div>
  );
}

export default ComparisonPanel;