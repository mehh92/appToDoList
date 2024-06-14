import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Todolist.css';

export default function Todolist() {
  const [todolists, setTodolists] = useState([]);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTodolists = async () => {
      const accessToken = localStorage.getItem('access');
      if (!accessToken) {
        setError('Erreur: utilisateur non authentifié.');
        navigate('/');
        return;
      }

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/todolists/', {
          headers: {
            'Authorization': `Bearer ${accessToken}`
          }
        });
        setTodolists(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération des todolists:', error);
        if (error.response) {
          setError(`Erreur: ${error.response.status} ${error.response.data.detail || error.response.data}`);
        } else if (error.request) {
          setError('Erreur: aucune réponse reçue du serveur.');
        } else {
          setError(`Erreur: ${error.message}`);
        }
        // Optionally, you could also navigate the user back to the login page on a 403 error
        if (error.response && error.response.status === 403) {
          console.log('erreur 403');
          // navigate('/');
        }
      }
    };

    fetchTodolists();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/');
  };

  return (
    <div className="Todolist">
      <nav className="navbar">
        <div className="navbar-title">TodoGoal</div>
        <div className="navbar-buttons">
          <button onClick={() => navigate('/profil')}>Utilisateur</button>
          <button onClick={handleLogout}>Déconnexion</button>
        </div>
      </nav>
      <main>
        <h2>Mes Todolists</h2>
        {error && <p className="error-message">{error}</p>}
        <div className="todolist-container">
          {todolists.map(list => (
            <div key={list.id} className="todolist-card">
              <h3>{list.title}</h3>
              <p>{list.description}</p>
            </div>
          ))}
          <button className="add-button">+</button>
        </div>
      </main>
    </div>
  );
}
