import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Todolist from './Components/Todolist/Todolist';
import Auth from './Components/Auth/Auth';
import Profil from './Components/Profil/Profil';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Auth />} />
        <Route path="/todolist" element={<Todolist />} />
        <Route path="/profil" element={<Profil />} />
        <Route path="*" element={<h1>Error 404: Page Not Found</h1>} />
      </Routes>
    </Router>
  );
}

export default App;
