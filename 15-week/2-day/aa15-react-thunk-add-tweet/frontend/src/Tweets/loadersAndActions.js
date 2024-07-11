// LOADER
export async function tweetLoader() {
  const response = await fetch("/api/tweets");
  if (response.ok) {
    const data = await response.json();
    return data;
  }
}

// ACTION
export async function createTweet({ request }) {
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
    // if there was an error deleting the tweet, I could handle it here
    // return { message: "Error deleting tweet" };
  }

  // if the intent is not delete, create a new tweet
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
