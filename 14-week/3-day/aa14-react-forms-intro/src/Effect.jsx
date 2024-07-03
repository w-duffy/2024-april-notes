import { useState, useEffect } from "react";

export default function Page() {
  let [person, setPerson] = useState("Alice");

  const [count, setCount] = useState(0);



  useEffect(() => {
    console.log("DID EFFECT RUN?");
  });

//   console.log("DID I RUN");
//   function userCanAccessSet(){
//     setPerson("Will")
//   }

  return (
    <>
      <select
        value={person}
        onChange={(e) => {
          setPerson(e.target.value);
        }}
      >
        <option value="Alice">Alice</option>
        <option value="Bob">Bob</option>
        <option value="Taylor">Taylor</option>
      </select>
      <hr />
      <button onClick={() => setCount(count + 1)}>{count} click me</button>
    </>
  );
}
