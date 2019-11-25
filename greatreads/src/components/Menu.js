import React, { Component } from 'react';

export default class Menu extends Component {
    render() {
        return (
            <ul>
                <li><a href="/App.html">Home</a></li>
                <li><a href="/Review.html">Review</a></li>
                <li><a href="/addReview.html">addReview</a></li>
            </ul>
        );
    }
}