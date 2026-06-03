import { useState } from "react";

import Navbar from "../components/Navbar";
import StatsBar from "../components/StatsBar";
import VideoCard from "../components/VideoCard";
import ChatPanel from "../components/ChatPanel";
import ComparisonPanel from "../components/ComparisonPanel";

import {
  uploadYoutubeVideo,
  uploadInstagramVideo,
  streamQuestion,
  compareVideos,
} from "../services/api";

function Home() {

  const [videoAUrl, setVideoAUrl] =
    useState("");

  const [videoBUrl, setVideoBUrl] =
    useState("");

  const [videoAData, setVideoAData] =
    useState(null);

  const [videoBData, setVideoBData] =
    useState(null);

  const [messages, setMessages] =
    useState([]);

  const [comparison, setComparison] =
    useState("");

  const [
    loadingCompare,
    setLoadingCompare,
  ] = useState(false);

  const [
    loadingVideoA,
    setLoadingVideoA,
  ] = useState(false);

  const [
    loadingVideoB,
    setLoadingVideoB,
  ] = useState(false);

  const analyzeVideoA =
    async () => {

      if (!videoAUrl) return;

      try {

        setLoadingVideoA(
          true
        );

        let result;

        if (
          videoAUrl.includes(
            "youtube.com"
          ) ||
          videoAUrl.includes(
            "youtu.be"
          )
        ) {

          result =
            await uploadYoutubeVideo(
              videoAUrl
            );

          setVideoAData(
            result.video
          );

        } else {

          result =
            await uploadInstagramVideo(
              videoAUrl
            );

          setVideoAData(
            result
          );

        }

      } catch (error) {

        console.error(
          error
        );

      } finally {

        setLoadingVideoA(
          false
        );

      }
    };

  const analyzeVideoB =
    async () => {

      if (!videoBUrl) return;

      try {

        setLoadingVideoB(
          true
        );

        let result;

        if (
          videoBUrl.includes(
            "youtube.com"
          ) ||
          videoBUrl.includes(
            "youtu.be"
          )
        ) {

          result =
            await uploadYoutubeVideo(
              videoBUrl
            );

          setVideoBData(
            result.video
          );

        } else {

          result =
            await uploadInstagramVideo(
              videoBUrl
            );

          setVideoBData(
            result
          );

        }

      } catch (error) {

        console.error(
          error
        );

      } finally {

        setLoadingVideoB(
          false
        );

      }
    };

  const askAI =
    async (
      question
    ) => {

      if (!question)
        return;

      setMessages(
        (prev) => [
          ...prev,
          {
            role:
              "user",
            content:
              question,
          },
        ]
      );

      setMessages(
        (prev) => [
          ...prev,
          {
            role:
              "assistant",
            content: "",
            sources: [],
          },
        ]
      );

      try {

        await streamQuestion(
          question,
          (
            chunk
          ) => {

            setMessages(
              (
                prev
              ) => {

                const updated =
                  [
                    ...prev,
                  ];

                const lastIndex =
                  updated.length -
                  1;

                if (
                  lastIndex >=
                  0
                ) {

                  updated[
                    lastIndex
                  ] = {
                    ...updated[
                      lastIndex
                    ],

                    content:
                      updated[
                        lastIndex
                      ]
                        .content +
                      chunk,
                  };
                }

                return updated;
              }
            );
          }
        );

      } catch (
        error
      ) {

        console.error(
          error
        );

        setMessages(
          (prev) => [
            ...prev,
            {
              role:
                "assistant",
              content:
                "Streaming failed.",
              sources:
                [],
            },
          ]
        );
      }
    };

  const runComparison =
    async () => {

      try {

        setLoadingCompare(
          true
        );

        const result =
          await compareVideos();

        setComparison(
          result.comparison
        );

      } catch (error) {

        console.error(
          error
        );

        setComparison(
          "Comparison failed."
        );

      } finally {

        setLoadingCompare(
          false
        );

      }
    };

  return (
    <div className="app-container">

      <Navbar />

      <StatsBar />

      <div className="dashboard-grid">

        <div className="left-panel">

          <VideoCard
            title="Video A (Instagram / YouTube)"
            url={videoAUrl}
            setUrl={setVideoAUrl}
            onAnalyze={analyzeVideoA}
            videoData={videoAData}
            loading={loadingVideoA}
          />

          <VideoCard
            title="Video B (Instagram / YouTube)"
            url={videoBUrl}
            setUrl={setVideoBUrl}
            onAnalyze={analyzeVideoB}
            videoData={videoBData}
            loading={loadingVideoB}
          />

          <button
            className="compare-btn"
            onClick={
              runComparison
            }
            disabled={
              loadingCompare
            }
          >
            {
              loadingCompare
                ? "Comparing..."
                : "Compare Videos"
            }
          </button>

          <ComparisonPanel
            comparison={
              comparison
            }
            loading={
              loadingCompare
            }
          />

        </div>

        <div className="right-panel">

          <ChatPanel
            messages={
              messages
            }
            onAsk={
              askAI
            }
          />

        </div>

      </div>

    </div>
  );
}

export default Home;