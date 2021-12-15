from numpy import greater
import streamlit as st
from person_info import Address, Person
from database import Database


def draw_person_info():
    """"Draw field for person and address"""
    with st.expander("Enter the person information: "):
        cola, colb = st.columns([2,1])
        name = cola.text_input("First Name: ")
        lname = colb.text_input("Last Name: ")
        gender = st.selectbox("What is yout gender: ", ["Male", "Female", "Other"])
        birthdate = st.date_input("Your birthday: ")
    
    with st.expander("Enter the Address information: "):
        cola, colb = st.columns([2,1])
        street = cola.text_input("Street Address: ")
        number = colb.text_input("Street Number: ")
        error_container = st.container()
        neighboorhood = cola.text_input("Neighboorhood: ")
        zip_code = colb.text_input("Zip code: ")
        complement = st.text_area("Any complementary information: ")
    
    try:
        number = int(number)
    except ValueError:
        error_container.error("Number must be a valid integer")
        st.stop()
        
    address = Address(
        street=street, number=number, 
        neighboorhood=neighboorhood,
        complement=complement,
        zip_code=zip_code
    )
    
    person = Person(
        name=name, last_name=lname,
        gender=gender, birthdate=birthdate,
        address=address
    )
    
    submited = st.button("Submit")
    
    if submited:
        save_data(person)
        
def save_data(person: Person):
    sql_insert_person = (
        "INSERT INTO person (name, last_name, gender, birthdate) "
        "VALUES (?, ?, ?, ?)"
    )
    
    sql_insert_address = (
        "INSERT INTO address (street, number, neighboorhood, zip_code, complement) "
        "VALUES (?, ?, ?, ?, ?)"
    )
    
    with st.spinner("Saving data..."):
        db = Database("testDB.db")
        a = db.execute_sql(sql_insert_address, values=(
            person.address.street,
            person.address.number,
            person.address.neighboorhood,
            person.address.zip_code,
            person.address.complement
        ))
        
        p = db.execute_sql(sql_insert_person, values=(
            person.name,
            person.last_name,
            person.gender,
            person.birthdate    
        ))
        
        if not p or not a:
            st.error("Error to insert data.")
        else:
            st.success("Inserted successful data")