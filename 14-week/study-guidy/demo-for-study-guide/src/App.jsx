import { useState } from "react";
import {
  RouterProvider,
  createBrowserRouter,
  Outlet,
  NavLink,
  useNavigate,
} from "react-router-dom";
import { createContext, useContext } from "react";

const data = [
  { someNum: 1, id: 1 },
  { someNum: 2, id: 2 },
  { someNum: 3, id: 3 },
];

const MyCountContext = createContext();
const useMyContext = () => useContext(MyCountContext);

function MyContextProvider(props) {
  const [contextCount, setContextCount] = useState(0);
  const [userName, setUserName] = useState("Will");
  return (
    <MyCountContext.Provider
      value={{ contextCount, setContextCount, userName, setUserName }}
    >
      {props.children}
    </MyCountContext.Provider>
  );
}

function Layout() {
  return (
    <div>
      <h1>Wills Guide</h1>
      <nav>
        <NavLink to="/">Home</NavLink>
        <br />
        <NavLink to="/context-counter">Context Counter</NavLink>
        <br />
        <NavLink to="/pick-a-number">Pick a Number</NavLink>
        <br />
        <NavLink to="/change-user">Change User</NavLink>
      </nav>
      <Outlet />
    </div>
  );
}

function IndexComponent() {
  let { userName } = useContext(MyCountContext);
  return <h2>User is: {userName}</h2>;
}

function Counter() {
  let { contextCount, setContextCount } = useContext(MyCountContext);
  return (
    <div>
      <button onClick={() => setContextCount(contextCount + 1)}>
        count is {contextCount}
      </button>
    </div>
  );
}

function CounterForm(props) {
  const [newNum, setNewNum] = useState(props.data[0].someNum);

  let navigate = useNavigate();

  onsubmit = (e) => {
    e.preventDefault();
    alert(`your number is: newNum`);
    navigate("/");
  };
  return (
    <form>
      <select onChange={(e) => setNewNum(e.target.value)} value={newNum}>
        {props.data.map((el) => (
          <option htmlFor={el.someNum} key={el.id}>
            {el.someNum}
          </option>
        ))}
      </select>
      <button type="submit">Submit Number</button>
    </form>
  );
}

function ChangeUserForm() {
  const { userName, setUserName } = useMyContext();

  return (
    <div>
      <h3>Will or Bri</h3>
      <label>
        <input
          type="radio"
          value="Will"
          name="instructor"
          checked={userName === "Will"}
          onChange={() => setUserName("Will")}
        />
        Will
      </label>
      <label>
        <input
          type="radio"
          value="Bri"
          name="instructor"
          checked={userName === "Bri"}
          onChange={() => setUserName("Bri")}
        />
        Bri
      </label>
    </div>
  );
}

let router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <IndexComponent />,
      },
      {
        path: "/context-counter",
        element: <Counter />,
      },
      {
        path: "/pick-a-number",
        element: <CounterForm data={data} />,
      },
      {
        path: "/change-user",
        element: <ChangeUserForm />,
      },
    ],
  },
]);

function App() {
  return (
    <MyContextProvider>
      <RouterProvider router={router} />
    </MyContextProvider>
  );
}

export default App;
