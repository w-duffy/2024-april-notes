import { useDispatch } from "react-redux";
import { loadArticles } from "../../store/articleReducer";
import { useEffect } from "react";
import { useSelector } from "react-redux";
import {NavLink} from 'react-router-dom'


const ArticleList = () => {
  let dispatch = useDispatch();
let articles = useSelector((state) => state.articleState.entries)
console.log("flag", articles)

  useEffect(() => {
    dispatch(loadArticles());
  }, [dispatch]);


  return (
    <div>
      <h1>Article List</h1>
      <ol>
      {articles.map(({ id, title }) => (
          <li key={id}>
            <NavLink to={`${id}`}>{title}</NavLink>
          </li>
        ))}
        {/* <li>Gilligan&apos;s Island. Is it true?</li>
        <li>A Baseball Moment</li>
        <li>Poke Moment</li>
        <li>Cool Cats</li>
        <li>Why Am I At Home</li> */}
      </ol>
    </div>
  );
};

export default ArticleList;
