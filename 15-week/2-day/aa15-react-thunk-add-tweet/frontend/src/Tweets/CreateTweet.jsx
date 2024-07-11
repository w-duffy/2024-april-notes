import { useFetcher } from "react-router-dom";
import { useEffect, useState } from "react";

const CreateTweet = () => {
  let fetcher = useFetcher();
  let [text, setText] = useState("");

  useEffect(() => {
    if (fetcher.state == "loading") setText("");
  }, [fetcher.state]);

  return (
    <fetcher.Form method="post" action="/">
      <input
        onChange={(e) => setText(e.target.value)}
        value={text}
        name="message"
      />
      <button type="submit">Create Tweet</button>
    </fetcher.Form>
  );
};

export default CreateTweet;
