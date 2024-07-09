// constant to avoid debugging typos
const GET_ALL_TWEETS = 'tweet/getAllTweets';

//regular action creator

// thunk action creator
export const getAllTweets = () => async (dispatch) => {
    console.log("in thunk before fetch")
    const response = await fetch('/api/tweets');
    console.log("in thunk after fetch", response)
  if (response.ok) {
    const data = await response.json();
    console.log("in thunk res.ok, data from backend:", data)
    dispatch({
        type: GET_ALL_TWEETS,
        tweets: data
      });
    return data;
}
};

// state object
const initialState = {};

// reducer
const tweetsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ALL_TWEETS: {
      const newState = {};
      console.log("in tweet reducer")
      action.tweets.forEach((tweet) => (newState[tweet.id] = tweet));
      console.log("in tweet reducer; newState: ", newState)
      return newState;
    }
    default:
      return state;
  }
};

export default tweetsReducer;
