import './App.css';
import HomePage from "./pages/Home.jsx";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import MoviesPage from "@/pages/Movies.jsx";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/" element={<MoviesPage/>}/>
            </Routes>
        </Router>
    );
}

export default App;