// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import TodoList from './components/TodoList';
import './styles.css';
import { fetchTodos, addTodo } from './services/api';

function App() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    fetchTodos()
      .then(data => setTodos(data))
      .catch(error => console.error('Error fetching todos:', error));
  }, []);

  const handleAddTodo = async () => {
    try {
      if (!inputValue.trim()) return;
      await addTodo({ content: inputValue });
      setInputValue('');
      fetchTodos()
        .then(data => setTodos(data))
        .catch(error => console.error('Error fetching todos:', error));
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Todo List</h1>
        <form onSubmit={(e) => { e.preventDefault(); handleAddTodo(); }}>
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Enter new todo..."
          />
          <button type="submit">Add Todo</button>
        </form>
        <TodoList todos={todos} />
      </header>
    </div>
  );
}

export default App;
