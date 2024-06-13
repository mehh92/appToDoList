import React from "react";
import { useState } from "react";
import './Auth.css';

export default function Auth() {
    const [formType, setFormType] = useState(null);

  const handleFormSwitch = (type) => {
    setFormType(type);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Bienvenue sur ToDoGoal</h1>
      </header>
      <main>
        <p>Bienvenue sur ToDoGoal, votre application de gestion des tâches et de suivi de vos objectifs personnels.</p>
        <div className="button-container">
          <button onClick={() => handleFormSwitch('signup')}>Inscription</button>
          <button onClick={() => handleFormSwitch('login')}>Connexion</button>
        </div>
        {formType === 'signup' && (
          <form className="form">
            <h2>Inscription</h2>
            <label>
              Nom:
              <input type="text" name="name" />
            </label>
            <label>
              Email:
              <input type="email" name="email" />
            </label>
            <label>
              Mot de passe:
              <input type="password" name="password" />
            </label>
            <button type="submit">S'inscrire</button>
          </form>
        )}
        {formType === 'login' && (
          <form className="form">
            <h2>Connexion</h2>
            <label>
              Email:
              <input type="email" name="email" />
            </label>
            <label>
              Mot de passe:
              <input type="password" name="password" />
            </label>
            <button type="submit">Se connecter</button>
          </form>
        )}
      </main>
    </div>
  );
}