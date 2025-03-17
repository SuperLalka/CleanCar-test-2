import React from 'react';
import {Link} from 'react-router';

import './AppNavigation.css';


export default class AppNavigation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            current_page: window.location.pathname
        };
    }

    mark_current_link() {
        let current_link = document.querySelector(`a[href="${this.state.current_page}"]`);
        if (current_link) {current_link.style.color = "black"};
    }

    componentDidMount() {
        this.mark_current_link();
    }

    render() {
        return (
            <nav className="AppNavigation__container">
                <ul className="AppNavigation__list">
                    <li>
                        <Link to="/" end="true" data-testid="link-home">Home</Link>
                    </li>
                    <li>
                        <Link to="/loader" data-testid="link-loader">Load Image</Link>
                    </li>
                    <li>
                        <Link to="/gallery" data-testid="link-gallery">Gallery</Link>
                    </li>
                </ul>
            </nav>
        );
    }
}
