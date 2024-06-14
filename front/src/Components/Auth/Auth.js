import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Auth.css';

export default function Auth() {
    const [formType, setFormType] = useState('login');
    const [nom, setNom] = useState('');
    const [prenom, setPrenom] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleFormSwitch = (type) => {
        setFormType(type);
        setError('');
        setNom('');
        setPrenom('');
        setEmail('');
        setPassword('');
    };

    const handleSignup = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/utilisateurs/create/', {
                email: email,
                nom: nom,
                prenom: prenom,
                password: password,
            });
            console.log('Inscription réussie:', response.data);
        } catch (error) {
            setError('Erreur lors de l\'inscription. Veuillez réessayer.');
            console.error('Erreur d\'inscription:', error);
        }
    };

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/token/', {
                username: email,
                password: password,
            });
            console.log('Réponse de l\'API:', response.data);
    
            // Assurez-vous que les clés 'access' et 'refresh' existent dans la réponse
            if (response.data.token) {
                localStorage.setItem('access', response.data.token);
                localStorage.setItem('refresh', response.data.token);
                console.log('Connexion réussie:', response.data);
                navigate('/todolist');
            } else {
                setError('Erreur lors de la connexion. Réponse inattendue du serveur.');
            }
        } catch (error) {
            setError('Erreur lors de la connexion. Veuillez vérifier vos identifiants.');
            console.error('Erreur de connexion:', error.response ? error.response.data : error.message);
        }
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
                {error && <p className="error-message">{error}</p>}
                {formType === 'signup' && (
                    <form className="form" onSubmit={handleSignup}>
                        <h2>Inscription</h2>
                        <label>
                            Nom:
                            <input type="text" name="nom" value={nom} onChange={(e) => setNom(e.target.value)} />
                        </label>
                        <label>
                            Prénom:
                            <input type="text" name="prenom" value={prenom} onChange={(e) => setPrenom(e.target.value)} />
                        </label>
                        <label>
                            Email:
                            <input type="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                        </label>
                        <label>
                            Mot de passe:
                            <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                        </label>
                        <button type="submit">S'inscrire</button>
                    </form>
                )}
                {formType === 'login' && (
                    <form className="form" onSubmit={handleLogin}>
                        <h2>Connexion</h2>
                        <label>
                            Email:
                            <input type="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                        </label>
                        <label>
                            Mot de passe:
                            <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                        </label>
                        <button type="submit">Se connecter</button>
                    </form>
                )}
            </main>
        </div>
    );
}
