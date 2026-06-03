import { useState } from "react";

function ChatPanel({
  onAsk,
  messages,
}) {
  const [question, setQuestion] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const handleSubmit =
    async () => {

      if (!question.trim()) {
        return;
      }

      const currentQuestion =
        question;

      setQuestion("");

      setLoading(true);

      try {

        await onAsk(
          currentQuestion
        );

      } finally {

        setLoading(false);

      }
    };

  const handleKeyDown = (
    e
  ) => {

    if (e.key === "Enter") {

      handleSubmit();

    }
  };

  return (
    <div className="chat-panel">

      <div className="chat-header">
        AI Video Analyst
      </div>

      <div className="chat-messages">

        {messages.length === 0 && (

          <div className="assistant-message">
            Upload videos and ask
            questions about
            performance,
            engagement, hooks,
            content strategy, or
            comparisons.
          </div>

        )}

        {messages.map(
          (msg, index) => (
            <div
              key={index}
              className={
                msg.role === "user"
                  ? "user-message"
                  : "assistant-message"
              }
            >

              <div>
                {msg.content}
              </div>

              {msg.role ===
                "assistant" &&
                msg.sources &&
                msg.sources.length > 0 && (

                <div
                  style={{
                    marginTop: "12px",
                    paddingTop: "8px",
                    borderTop:
                      "1px solid rgba(255,255,255,0.1)",
                    fontSize: "12px",
                    color: "#9ca3af",
                  }}
                >

                  <strong>
                    Sources
                  </strong>

                  {msg.sources.map(
                    (
                      source,
                      sourceIndex
                    ) => (
                      <div
                        key={
                          sourceIndex
                        }
                      >
                        Video:
                        {" "}
                        {
                          source.video_id
                        }
                        {" "}
                        |
                        Chunk:
                        {" "}
                        {
                          source.chunk_index ??
                          "N/A"
                        }
                      </div>
                    )
                  )}

                </div>

              )}

            </div>
          )
        )}

        {loading && (

          <div className="assistant-message">
            Thinking...
          </div>

        )}

      </div>

      <div className="chat-input">

        <input
          value={question}
          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }
          onKeyDown={
            handleKeyDown
          }
          placeholder="Ask about Video A, Video B, engagement, hooks, audience retention..."
        />

        <button
          onClick={
            handleSubmit
          }
          disabled={loading}
        >
          {loading
            ? "Sending..."
            : "Send"}
        </button>

      </div>

    </div>
  );
}

export default ChatPanel;