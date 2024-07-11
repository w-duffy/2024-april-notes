# React Router - Loaders and Actions

The docs have examples for each of these APIs.  These are in addition to what we've learned in class `useBrowserRouter`, `RouterProvider` and `useNavigate`, for example.

Here are some of the ones you'd likely use if you want to incorporate this into your App:

- [loader](https://reactrouter.com/en/main/route/loader)

- [action](https://reactrouter.com/en/main/route/action)

- [Form](https://reactrouter.com/en/main/components/form)

- [useLoaderData](https://reactrouter.com/en/main/hooks/use-loader-data)

- [useActionData](https://reactrouter.com/en/main/hooks/use-action-data)

- [useFetcher](https://reactrouter.com/en/main/hooks/use-fetcher)

## Loaders

- Loaders are functions that return a promise
- Loaders are used to fetch data
- Loaders are used to load data before rendering a component

```js
// in App.jsx
const router = createBrowserRouter([
  {
    path: "/albums/:id",
    loader: async ({params}) => {
       return fetch(`/api/albums/${params.id}`)
    },
    element: <SingleAlbum />,
  },
]);

// in a component file
import { SingleAlbum } from "react-router-dom";

export function Albums() {
  const singleAlbum = useLoaderData();
  return(
    <>
      <p>{singleAlbum.title}</p>
    </>
  )
}
```

## Actions

- Actions are functions that return a promise
- Actions are used to perform an action
- Actions are used to perform an action before rendering a component
- After the action is completed, the loaders automatically re-run to revalidate all data 🔥

```js
import { useActionData } from "react-router-dom";

const Action = () => {
  const data = useActionData();
  return <h1>{data.title}</h1>;
};
```

## useFetcher

- useFetcher is a hook that returns a fetcher object
- Fetcher object has a state property that can be used to check the current state of the fetcher
- Fetcher object has a Form component that can be used to create a form
- Fetcher object has a useForm method that can be used to create a form

```js
import { useFetcher } from 'react-router-dom';

const Fetcher = () => {
  const fetcher = useFetcher();
  return (
    <div>
      <h1>Fetcher</h1>
      <p>State: {fetcher.state}</p>
      <fetcher.Form method="post" action="/">
        <input type="text" name="message" />
        <button type="submit">Submit</button>
      </fetcher.Form>
    </div>
  );
}

```

## useLoaderData

- useLoaderData is a hook that returns the data for the current route
- useLoaderData is used to fetch data for the current route
- useLoaderData is used to load data for the current route before rendering a component

```js
import { useLoaderData } from 'react-router-dom';

const Loader = () => {
  const data = useLoaderData();
  return <h1>{data.title}</h1>;
};
```

## useActionData to handle errors

- This hook provides the returned value from the previous navigation's action result, or undefined if there was no submission.
- The most common use-case for this hook is form validation errors. If the form isn't right, you can return the errors and let the user try again:

```js
import {
  useActionData,
  Form,
  redirect,
} from "react-router-dom";

export default function SignUp() {
  const errors = useActionData();

  return (
    <Form method="post">
      <p>
        <input type="text" name="email" />
        {errors?.email && <span>{errors.email}</span>}
      </p>

      <p>
        <input type="text" name="password" />
        {errors?.password && <span>{errors.password}</span>}
      </p>

      <p>
        <button type="submit">Sign up</button>
      </p>
    </Form>
  );
}

export async function action({ request }) {
  const formData = await request.formData();
  const email = formData.get("email");
  const password = formData.get("password");
  const errors = {};

  // validate the fields
  if (typeof email !== "string" || !email.includes("@")) {
    errors.email =
      "That doesn't look like an email address";
  }

  if (typeof password !== "string" || password.length < 6) {
    errors.password = "Password must be > 6 characters";
  }

  // return data if we have errors
  if (Object.keys(errors).length) {
    return errors;
  }

  // otherwise create the user and redirect
  await createUser(email, password);
  return redirect("/dashboard");
}
```

## Handeling Multiple Types of Intents in a Single Action

- We can use the form "intent" to handle multiple types of intents in a single action
- The form "intent" is a hidden input field that is used to specify the intent of the form
- The form "intent" is used to specify the intent of the form
- The form "intent" is used to specify the intent of the form

```js
import { useFetcher } from "react-router-dom";

const Fetcher = () => {
  const fetcher = useFetcher();
  return (
    <div>
      <h1>Fetcher</h1>
      <p>State: {fetcher.state}</p>
      <fetcher.Form method="post" action="/">
        <input type="text" name="message" />
        <button type="submit">Submit</button>
        <input type="hidden" name="intent" value="delete" />
      </fetcher.Form>
    </div>
  );
};
```

Then in our action, we can check the intent and perform the appropriate action:

```js
export async function createTweetAction({ request }) {
  let formData = await request.formData();
  let data = Object.fromEntries(formData);

  let intent = formData.get("intent");

  // if the intent is delete, delete the tweet
  if (intent === "delete") {
    const response = await fetch(`/api/tweets/${data.id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      return { message: "Successfully deleted" };
    }
  }

  if (intent === "create") {
    const response = await fetch(`/api/tweets`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const tweet = await response.json();

      return tweet;
    }
    // if there was an error creating the tweet, I could handle it here
    // return { message: "Error creating tweet" };
  }
}
```
