import './App.css';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import HomePage from "./pages/Home.jsx";
import MoviesPage from "./pages/Movies.jsx";
import MoviePage from "@/pages/Movie.jsx";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/movies" element={<MoviesPage/>}/>
                <Route path="/movies/:id" element={<MoviePage/>}/>
            </Routes>
        </Router>
    );
}

export default App;