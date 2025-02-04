import React from 'react';
import { ListGroup, Button, Form } from 'react-bootstrap';

function TodoItem({ todo, deleteTodo, toggleTodo }) {
  return (
    <ListGroup.Item className="d-flex justify-content-between align-items-center">
      <div>
        <Form.Check
          type="checkbox"
          checked={todo.completed}
          onChange={() => toggleTodo(todo.id)}
          label={todo.title}
        />
      </div>
      <Button variant="danger" size="sm" onClick={() => deleteTodo(todo.id)}>Delete</Button>
    </ListGroup.Item>
  );
}

export default TodoItem;
