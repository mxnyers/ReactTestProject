import React, { Component } from 'react';
 
class Navbar extends Component {
  render() {
    return (
      <div className="navbar">
        <a href="/">Home</a>
        <a href="/sad-playlists">Sad Playlists</a>
        <a href="#" className="right">Contact</a>
      </div>
    );
  }
}
 
export default Navbar