import './App.css';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import HomePage from "./pages/Home.jsx";
import MoviesPage from "./pages/Movies.jsx";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/movies" element={<MoviesPage/>}/>
            </Routes>
        </Router>
    );
}

export default App;