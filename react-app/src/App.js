import React, { Component } from 'react';
import Footer from './common-componenets/footer';
import Navbar from './common-componenets/navbar';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
// import Users from './pages/users';
import SadPlaylists from './pages/sad-playlists'
import './App.css'
import Home from './pages/home';

class App extends Component {

  render() {  
      return (
        <Router>
          <Navbar />
          <Routes>
            <Route exact path="/" element={<Home />} />
            {/* <Route path="/users" element={<Users />} /> */}
            <Route exact path="/sad-playlists" element={<SadPlaylists />} />
          </Routes>
          
          <Footer />
        </Router>
      );
  }
}

export default App;
