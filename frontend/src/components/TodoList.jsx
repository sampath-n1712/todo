// frontend/src/components/TodoList.js
import React from 'react';

function TodoList({ todos }) {
  return (
    <div className="TodoList">
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>{todo.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
