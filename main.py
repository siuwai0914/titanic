import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression

def predict_survival(pclass, age, fare, is_alone, gender, embarked):
    if pclass == "First Class":
        pclass = 1
    elif pclass == "Second Class":
        pclass = 2
    else:
        pclass = 3
    if fare <= 8:
        fare = 0
    elif fare <= 15:
        fare = 1
    elif fare <= 31:
        fare = 2
    else:
        fare = 3

    if age <= 16:
        age = 0
    elif age <= 32:
        age = 1
    elif age <= 48:
        age = 2
    elif age <= 64:
        age = 3
    else:
        age = 4
    #elif age
    if is_alone:
        is_alone = 0
    else:
        is_alone = 1

    if gender == "Male":
        gender = 0
    else:
        gender = 1

    if embarked == "Southampton":
        embarked = 0
    elif embarked == "Queenstown":
        embarked = 1
    else:
        embarked = 2
    df1 = pd.read_csv("data.csv")
    df1 = df1.drop(df1.columns[0], axis=1)
    X = df1.drop("Survived", axis=1)
    y = df1['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    result = lr.predict([[pclass, embarked, age, gender, fare, is_alone]])

    if result[0] == 0:
        st.text("Sorry you are unlucky that you cannot survived!")
    elif result[0] == 1:
        st.text("Congrats! you can survive!")

def main():
    st.title("Prediction of Titanic Survival")
    st.text("Please fill in the following information")

    pclass = st.selectbox(
        'select your class',
        ('First Class', 'Second Class', 'Third Class'))

    age = st.slider('How old are you?', 0, 80, 25)

    fare = st.number_input("How much is your ticket?", min_value=0, max_value=512, value=50, step=1)

    is_alone = st.toggle('Are u alone?')
    print('fgjfdig')
    print(is_alone)
    gender = st.selectbox(
        'choose your gender',
        ('Male', 'Female'))

    embarked = st.radio(
        'choose your gender',
        ('Southampton', 'Queenstown', 'Cherbourg'))
    st.button("Submit", type="primary", on_click=predict_survival(pclass, age, fare,is_alone, gender, embarked))

main()