
import { Navigate, useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";
import { useEffect } from "react";
import "./SingleArticle.css";
import { loadArticles } from "../../store/articleReducer";

const SingleArticle = () => {
  const { id } = useParams();

  const singleArticle = useSelector((state) =>
    state.articleState.entries.find((article) => article.id === id)
  );



//   if(!singleArticle) return <h1>Go home this is broken</h1>

  return (
    <div className="singleArticle">
      <h1>{singleArticle.title}</h1>
      <img src={singleArticle.imageUrl} alt={singleArticle?.title} />
      <p>{singleArticle.body}</p>
    </div>
  );
};

export default SingleArticle;
