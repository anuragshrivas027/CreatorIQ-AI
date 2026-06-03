import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const uploadYoutubeVideo =
  async (url) => {

    const response =
      await API.post(
        "/api/videos/youtube",
        {
          url,
        }
      );

    return response.data;
  };

export const uploadInstagramVideo =
  async (url) => {

    const response =
      await API.post(
        "/api/videos/instagram",
        {
          url,
        }
      );

    return response.data;
  };

export const askQuestion =
  async (question) => {

    const response =
      await API.post(
        "/api/chat/ask",
        {
          question,
        }
      );

    return response.data;
  };

export const streamQuestion =
  async (
    question,
    onChunk
  ) => {

    const response =
      await fetch(
        "http://127.0.0.1:8000/api/chat/stream",
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify(
            {
              question,
            }
          ),
        }
      );

    if (!response.ok) {

      throw new Error(
        "Streaming request failed"
      );

    }

    const reader =
      response.body.getReader();

    const decoder =
      new TextDecoder();

    while (true) {

      const {
        done,
        value,
      } =
        await reader.read();

      if (done) {

        break;

      }

      const chunk =
        decoder.decode(
          value,
          {
            stream: true,
          }
        );

      onChunk(chunk);
    }
  };

export const compareVideos =
  async () => {

    const response =
      await API.get(
        "/api/compare/"
      );

    return response.data;
  };

export default API;