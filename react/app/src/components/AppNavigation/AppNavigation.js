import React from 'react';
import {NavLink} from "react-router";

import './AppNavigation.css';


class AppNavigation extends React.Component {

    render() {
        return (
            <nav className="AppNavigation__container">
                <ul className="AppNavigation__list">
                    <li>
                        <NavLink to="/" end>Home</NavLink>
                    </li>
                    <li>
                        <NavLink to="/loader" end>Load Image</NavLink>
                    </li>
                    <li>
                        <NavLink to="/gallery">Gallery</NavLink>
                    </li>
                </ul>
            </nav>
        );
    }
}

export default AppNavigation;
