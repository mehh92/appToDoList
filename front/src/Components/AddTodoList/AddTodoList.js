import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './AddTodoList.css'; // Assurez-vous d'avoir un fichier de style pour le formulaire

const AddTodoList = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/todolists/', {
                title: title,
                description: description,
            }, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access')}`
                }
            });
            console.log('Todolist ajoutée:', response.data);
            navigate('/todolist'); // Redirection après l'ajout
        } catch (error) {
            setError('Erreur lors de l\'ajout de la Todolist. Veuillez réessayer.');
            console.error('Erreur d\'ajout:', error);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Ajouter une Todolist</h1>
                <div className="navbar-buttons">
          <button onClick={() => window.history.back()}>Retour</button>
        </div>
            </header>
            <main className="main">
                {error && <p className="error-message">{error}</p>}
                <form className="form" onSubmit={handleSubmit}>
                    <label>
                        Titre:
                        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
                    </label>
                    <label>
                        Description:
                        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
                    </label>
                    <button type="submit">Ajouter</button>
                </form>
            </main>
        </div>
    );
};

export default AddTodoList;
