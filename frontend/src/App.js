import React, {useState, useEffect } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './App.css';

function App() {
  const [mediaType, setMediaType] = useState('movie');
  const [genre, setGenre] = useState('');
  const [selectedDate, setSelectedDate] = useState('');
  const [description, setDescription] = useState('');
  const [data, setData] = useState([]);

  const handleMediaTypeChange = (event) => {
    setMediaType(event.target.value);
  };

  const handleGenreChange = (event) => {
    setGenre(event.target.value);
  };

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    axios.post('http://localhost:5000/search', {
      selectedDate,
      mediaType,
      genre,
      description,
    })
      .then((response) => {
        console.log(response.data)
        setData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div className="App">
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <h2>Search Movies</h2>
          <div className="form-group">
            <label>Type</label>
            <div className="radio-group">
              <div className="radio-option">
                <input
                  type="radio"
                  id="movie"
                  name="mediaType"
                  value="movie"
                  checked={mediaType === 'movie'}
                  onChange={handleMediaTypeChange}
                />
                <label htmlFor="movie">Movie</label>
              </div>
              <div className="radio-option">
                <input
                  type="radio"
                  id="show"
                  name="mediaType"
                  value="show"
                  checked={mediaType === 'show'}
                  onChange={handleMediaTypeChange}
                />
                <label htmlFor="show">TV Show</label>
              </div>
            </div>
          </div>
          <div className="form-group">
            <label>Genres:</label>
            <select value={genre} onChange={handleGenreChange}>
              <option value="">Select Genres</option>
              <option value="comedy">Comedy</option>
              <option value="horror">Horror</option>
              <option value="sci-fi">Sci-fi</option>
              <option value="romance">Romance</option>
            </select>
          </div>
          <div className="form-group">
            <label>Date</label>
            <DatePicker
              // selected={selectedDate}
              // onChange={handleDateChange}
              dateFormat="MM/dd/yyyy"
              minDate={new Date()}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea value={description} onChange={handleDescriptionChange} />
          </div>
          <div className="form-group">
            <button type="submit" className="submit">Search</button>
          </div>
        </form>
      </div>
      <div className="movie-container">
        {data.map((movie) => (
          <div key={movie._id} class="movie">
            <h3>{movie.name}</h3>
            <p>{movie.description}</p>
            <p>Date: {movie.date}</p>
            <p>Genres: {movie.genres.join(', ')}</p>
            <p>Type: {movie.type}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
