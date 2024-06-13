import React from 'react';
import './Profil.css';

export default function Profil() {
  // Simuler des informations utilisateur
  const user = {
    name: 'John Doe',
    email: 'john.doe@example.com',
  };

  return (
    <div className="Profile">
      <nav className="navbar">
        <div className="navbar-title">TodoGoal</div>
        <div className="navbar-buttons">
          <button onClick={() => window.history.back()}>Retour</button>
        </div>
      </nav>
      <main>
        <h2>Profil Utilisateur</h2>
        <div className="profile-info">
          <p><strong>Nom:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      </main>
    </div>
  );
}