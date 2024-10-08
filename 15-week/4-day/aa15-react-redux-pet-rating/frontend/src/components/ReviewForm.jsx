import { useState } from 'react';
import { useDispatch } from 'react-redux';
import PawsRatingInput from './PawsRatingInput';

const ReviewForm = ({ review, formType, onSubmit, closeForm }) => {
  const [rating, setRating] = useState(review.rating);
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(onSubmit({ ...review, rating }));
    closeForm();
  };


  const onChange = (number) => {
    setRating(parseInt(number));
  };

  return (
    <form onSubmit={handleSubmit} >
      <PawsRatingInput
        disabled={false}
        onChange={onChange}
        rating={rating}
      />
      <input type="submit" value={formType} />
      <button onClick={closeForm}>Cancel</button>
    </form>
  );
}

export default ReviewForm;
