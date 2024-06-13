import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Todolist.css';

export default function Todolist() {

    const navigate = useNavigate();
  const todolists = [
    { id: 1, title: 'Liste de tâches 1', description: 'Description de la liste de tâches 1' },
    { id: 2, title: 'Liste de tâches 2', description: 'Description de la liste de tâches 2' },
    { id: 3, title: 'Liste de tâches 3', description: 'Description de la liste de tâches 3' },
  ];

  return (
    <div className="Todolist">
      <nav className="navbar">
        <div className="navbar-title">TodoGoal</div>
        <div className="navbar-buttons">
        <button onClick={() => navigate('/profil')}>Utilisateur</button>
          <button>Déconnexion</button>
        </div>
      </nav>
      <main>
        <h2>Mes Todolist</h2>
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