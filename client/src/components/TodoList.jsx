import React from 'react';
import { ListGroup } from 'react-bootstrap';
import TodoItem from './TodoItem';

function TodoList({ todos, deleteTodo, toggleTodo }) {
  return (
    <ListGroup>
      {todos.length === 0 ? (
        <ListGroup.Item>No todos available</ListGroup.Item>
      ) : (
        todos.map(todo => (
          <TodoItem key={todo.id} todo={todo} deleteTodo={deleteTodo} toggleTodo={toggleTodo} />
        ))
      )}
    </ListGroup>
  );
}

export default TodoList;
