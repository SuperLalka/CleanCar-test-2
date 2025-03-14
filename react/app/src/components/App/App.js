import React from "react";
import { BrowserRouter, Routes, Route } from "react-router";

import './App.css';
import AppNavigation from "../AppNavigation/AppNavigation";
import Gallery from "../Gallery/Gallery";
import Loader from '../Loader/Loader';


class App extends React.Component {

    render() {
        return (
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<AppNavigation />}/>
                    <Route path="/loader" element={<Loader />} />
                    <Route path="/gallery" element={<Gallery />} />
                </Routes>
            </BrowserRouter>
        )
    }
}

export default App;
