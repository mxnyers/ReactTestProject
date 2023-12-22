import React, { Component } from 'react';
import logoImage from "./../resources/logo.png"
import hoverImage from "./../resources/black-logo.png"
import { FaCaretDown } from "react-icons/fa";
import {PlatlistGenre} from "../enum/playlist-genre.js";
 
class Navbar extends Component {
  
  
  render() {
    return (
      <div className="navbar">
        <a 
          href="/" 
          id="logo"
          onMouseOver={e => (e.currentTarget.firstElementChild.src = hoverImage)}
          onMouseOut={e => (e.currentTarget.firstElementChild.src= logoImage)} >
          <img 
            src={logoImage} 
            alt="home"/>
        </a>
        <div className="playlist-dropdown">
          <button className='dropbtn'>Playlists
            <FaCaretDown className='FaCaretDown' />
          </button>
          <div className="playlist-submenu">
            {Object.keys(PlatlistGenre).map(key => {
              if(PlatlistGenre[key].id !== "new" ){
                return <a key={key} href={"/playlists/" + PlatlistGenre[key].id}>{PlatlistGenre[key].string}</a>                
              }
              else{
                return null
              }
            })}
            {/* <a href="/sad-playlists">Sad Playlists</a>
            <a href="/hard-playlists">Hard Playlists</a>
            <a href="/euphoric-playlists">Euphoric Playlists</a> */}
          </div>
        </div>
        <a href="/add-playlist" className="right">Add Playlist</a>
        
      </div>
    );
  }
}
 
export default Navbar