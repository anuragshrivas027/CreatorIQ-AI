import { motion } from "framer-motion";

function VideoCard({
  title,
  url,
  setUrl,
  onAnalyze,
  videoData,
  loading,
}) {
  return (
    <motion.div
      className="video-card"
      whileHover={{
        scale: 1.01,
      }}
    >
      <h2>{title}</h2>

      <input
        type="text"
        placeholder="Paste video URL..."
        value={url}
        onChange={(e) =>
          setUrl(e.target.value)
        }
      />

      <button
        onClick={onAnalyze}
        disabled={loading}
      >
        {loading
          ? "Analyzing..."
          : "Analyze Video"}
      </button>

      {!videoData && (
        <div className="metrics-placeholder">
          Analyze a video to view
          metadata and engagement
          metrics.
        </div>
      )}

      {videoData && (
        <div className="video-metrics">

          <div className="metric-item">
            <strong>Title</strong>
            <p>
              {videoData.title ||
                "Unavailable"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Creator</strong>
            <p>
              {videoData.creator ||
                "Unavailable"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Followers</strong>
            <p>
              {videoData.follower_count?.toLocaleString?.()
                || videoData.follower_count
                || "Unavailable"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Views</strong>
            <p>
              {(
                videoData.views || 0
              ).toLocaleString()}
            </p>
          </div>

          <div className="metric-item">
            <strong>Likes</strong>
            <p>
              {(
                videoData.likes || 0
              ).toLocaleString()}
            </p>
          </div>

          <div className="metric-item">
            <strong>Comments</strong>
            <p>
              {(
                videoData.comments || 0
              ).toLocaleString()}
            </p>
          </div>

          <div className="metric-item">
            <strong>
              Engagement Rate
            </strong>
            <p>
              {videoData.engagement_rate}%
            </p>
          </div>

          <div className="metric-item">
            <strong>Duration</strong>
            <p>
              {videoData.duration
                ? `${Math.floor(
                    videoData.duration / 60
                  )}m ${
                    videoData.duration % 60
                  }s`
                : "Unavailable"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Upload Date</strong>
            <p>
              {videoData.upload_date
                ? `${String(
                    videoData.upload_date
                  ).slice(0, 4)}-${String(
                    videoData.upload_date
                  ).slice(4, 6)}-${String(
                    videoData.upload_date
                  ).slice(6, 8)}`
                : "Unavailable"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Platform</strong>
            <p>
              {videoData.platform ||
                "Unknown"}
            </p>
          </div>

          <div className="metric-item">
            <strong>Hashtags</strong>
            <p>
              {Array.isArray(
                videoData.hashtags
              ) &&
              videoData.hashtags.length > 0
                ? videoData.hashtags.join(
                    ", "
                  )
                : "None Found"}
            </p>
          </div>

        </div>
      )}
    </motion.div>
  );
}

export default VideoCard;