function ContactUs() {
  return (
    <div>
      <h2>Contact Us</h2>
      <form method="post" action="/">
        <div>
          <label htmlFor="name">Name:</label>
          <input id="name" type="text" name="name" placeholder="Name" />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input id="email" type="text" name="email" placeholder="Email" />
        </div>
        <div>
          <label htmlFor="phone">Phone:</label>
          <input id="phone" type="text" placeholder="Phone" />
          <select name="phoneType">
            <option value="" disabled>
              Select a phone type...
            </option>
            <option>Home</option>
            <option>Work</option>
            <option>Mobile</option>
          </select>
        </div>
        <div>
          <label htmlFor="comments">Comments:</label>
          <textarea id="comments" name="comments" placeholder="Comments" />
        </div>
        <button>Submit</button>
      </form>
    </div>
  );
}

export default ContactUs;
