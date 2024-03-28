import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state["new_todo"].title() + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app exists to help you increase your productivity.📊")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # this means "true" if the box is checked
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

print("Python code was just executed.")

#  st.session_state
