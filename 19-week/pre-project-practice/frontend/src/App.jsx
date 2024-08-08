import "./App.css";
import {
  useLoaderData,
  createBrowserRouter,
  RouterProvider,
  Form,
  useActionData,
} from "react-router-dom";

function Layout() {
  let image = useActionData();
  return (
    <>
      <h1>Hello World</h1>
      <HomePage />
      <Form method="post" encType="multipart/form-data" type="file" action="/">
        <input name="image" type="file" accept="image/*" />
        <button type="submit">Submit</button>
      </Form>
      <img src={image?.image?.name} />
    </>
  );
}
let getRoot = async () => {
  return await fetch("/api");
};

let handleUpload = async ({ request }) => {
  return await fetch("/api/aws", {
    method: "POST",
    body: await request.formData(),
  });

  // let data = await request.formData()

  // let res = await fetch("/api/aws", {
  //     method: "POST",
  //     body: data
  // })
  // let resBody = await res.json()

  // return json(resBody)
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    loader: getRoot,
    action: handleUpload,
  },
]);

function HomePage() {
  let data = useLoaderData();

  return <h2>Actor is {data.actor.name}</h2>;
}

function App() {
  return <RouterProvider router={router} />;
}
export default App;
