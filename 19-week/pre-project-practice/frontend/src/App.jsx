import "./App.css";
import {
  useLoaderData,
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

function Layout() {
  return (
    <>
      <h1>Hello World</h1>
      <HomePage />
    </>
  );
}
let getRoot = async () => {
  return await fetch("/api");
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    loader: getRoot,
  },
]);

function HomePage() {
  let data = useLoaderData();

  return <h2>My Home {data.spot_name}</h2>;
}

function App() {
  return <RouterProvider router={router} />;
}
export default App;
