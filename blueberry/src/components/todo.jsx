import "./todo.css";
import { useState } from "react";

const Todo = () => {
  const [todoText, setTodoText] = useState("");
  const [allTodos, setAllTodos] = useState([]);

  const handleTextChange = (e) => {
    let val = e.target.value;
    setTodoText(val);
  };

  const addTodo = () => {
    let copy = [...allTodos];
    copy.push(todoText);
    setAllTodos(copy);
  };

  return (
    <div className="todo-page">
      <h3>Shopping List!</h3>

      <div className="capture">
        <input name="todo-text" onChange={handleTextChange} type="text" />
        <button className="btn btn-sm btn-primary" onClick={addTodo}>
          Add
        </button>
      </div>

      <div className="list">
        <ul>
          {allTodos.map((t, index) => (
            <li key={index}>{t}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Todo;
