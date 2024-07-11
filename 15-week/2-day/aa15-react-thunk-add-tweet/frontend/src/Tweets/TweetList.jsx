import { Form, useLoaderData } from "react-router-dom";

const TweetList = () => {
  let tweetList = useLoaderData();

  return (
    <>
      <h1>Tweet List</h1>
      {tweetList?.map(({ id, message }) => (
        <div key={id}>
          <p>{message}</p>
          <Form method="delete" action="/">
            <button name="intent" value="delete" type="submit">
              Delete
            </button>
            <input type="hidden" name="id" value={id} />
          </Form>
        </div>
      ))}
    </>
  );
};

export default TweetList;
