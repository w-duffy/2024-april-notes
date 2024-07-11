import CreateTweet from "./Tweets/CreateTweet";
import TweetList from "./Tweets/TweetList";
import { createTweet, tweetLoader } from "./Tweets/loadersAndActions";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

function Layout() {
  return (
    <>
      <TweetList />
      <hr />
      <CreateTweet />
    </>
  );
}
const router = createBrowserRouter([
  {
    path: "/",
    loader: tweetLoader,
    element: <Layout />,
    action: createTweet
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
