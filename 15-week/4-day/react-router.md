# React Router - Loaders and Actions

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
import { useLoaderData } from 'react-router-dom';

const Loader = () => {
  const data = useLoaderData();
  return <h1>{data.title}</h1>;
};
```

## Actions

- Actions are functions that return a promise
- Actions are used to perform an action
- Actions are used to perform an action before rendering a component

```js
import { useActionData } from 'react-router-dom';

const Action = () => {
  const data = useActionData();
  return <h1>{data.title}</h1>;
};
```
