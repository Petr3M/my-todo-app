# web apps are easier to maintain, user friendlier, more modern than desktop apps
# streamlit run web.py
# script is executed for each user separately; when we deploy app on webserver,
# it means that web server CPU is handling request. If app has a lot of visitors, it must have sufficient HW (RAM, CPU).
# add interactivity, complete todo item
# deploy streamlit app on a live server > visit a webapp thru a public URL
# pip freeze > requirements.txt >>> a file which will be uploaded to the server where we host this web app so the server has python installed needing all packages needed to run the app correctly
    # server gets this file and installs all python packages
# upload project to Github > I need enable version control

import streamlit as st
import functions # functions is our backend

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" #local variable; extract hello from session_state key:value JSON
    todos.append(todo) # update todos list here
    functions.write_todos(todos) # write updated todos into todos.txt file

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity.")

#st.checkbox("Buy grocery.")
#st.checkbox("Throw the trash.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) # pop out checked item from the list
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() # needed for checkboxes

st.text_input(label="", placeholder="Add new todo.",
              on_change=add_todo, key='new_todo')

st.session_state # session state JSON file