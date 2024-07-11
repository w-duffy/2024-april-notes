const initialState = [{ 1: "banana", 2: "pear", 3: "orange", 4: "peach" }];

const fruitReducer = (state = initialState, action) => {
  console.log("IN FRUIT REDUCER", state);
  let newState = {...state}
  return newState;
};

export default fruitReducer;
