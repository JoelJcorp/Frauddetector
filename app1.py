import streamlit as st
import joblib
import numpy as np

st.title("Fraud Detector 1.0")
st.subheader("Auteur : Joël KALONGA")
st.write("Cette application a pour but de detecter la fraude bancaire par carte de paiement," 
         "afin de réduire l'utilisation illicite des cartes de paiement bancaire et ainsi"
         "de réduire les pertes dû à cela.")

#Chargement du modèle

model = joblib.load(filename="Model_combining.joblib")

#Définition d'une fonction d'inference

def inference (V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount):
    new_data=np.array([
        V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,
        V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,
        V24,V25,V26,V27,V28,Amount
    ])
    pred=model.predict(new_data.reshape(1,-1))
    return pred

#Entrée des données

V1 = st.number_input(label = 'Valeur 1:', value=-4.86810843844627
, format= '%f')
V2 = st.number_input(label = 'Valeur 2:', value=1.26441977404559,format= '%f')
V3 = st.number_input(label = 'Valeur 3:', value=-5.16788542660662,format= '%f')
V4 = st.number_input(label = 'Valeur 4:', value=3.19364784504611,format= '%f')
V5 = st.number_input(label = 'Valeur 5:', value=-3.04562137708228,format= '%f')
V6 = st.number_input(label = 'Valeur 6:', value=-2.09616609885545,format= '%f')
V7 = st.number_input(label = 'Valeur 7:', value=-6.44561018266068,format= '%f')
V8 = st.number_input(label = 'Valeur 8:', value=2.4225355920307,format= '%f')
V9 = st.number_input(label = 'Valeur 9:', value=-3.2140554159387,format= '%f')
V10 = st.number_input(label = 'Valeur 10:', value=-8.74597261185534,format= '%f')
V11= st.number_input(label = 'Valeur 11:', value=5.41604190908794,format= '%f')
V12= st.number_input(label = 'Valeur 12:', value=-8.16412507731485,format= '%f')
V13= st.number_input(label = 'Valeur 13:', value=-0.165010607208302,format= '%f')
V14= st.number_input(label = 'Valeur 14:', value=-10.1935303551514,format= '%f')
V15= st.number_input(label = 'Valeur 15:', value=-1.89521031032574,format= '%f')
V16= st.number_input(label = 'Valeur 16:', value=-7.36047460938421,format= '%f')
V17= st.number_input(label = 'Valeur 17:', value=-14.6687710766351,format= '%f')
V18= st.number_input(label = 'Valeur 18:', value=-4.87711900477519,format= '%f')
V19= st.number_input(label = 'Valeur 19:', value=1.38560952778492,format= '%f')
V20= st.number_input(label = 'Valeur 20:', value=0.66730977994879,format= '%f')
V21= st.number_input(label = 'Valeur 21:', value=1.26920538901712,format= '%f')
V22= st.number_input(label = 'Valeur 22:', value=0.0576572516592633,format= '%f')
V23= st.number_input(label = 'Valeur 23:', value=0.629307399675982,format= '%f')
V24= st.number_input(label = 'Valeur 24:', value=-0.168431773502721,format= '%f')
V25= st.number_input(label = 'Valeur 25:', value=0.443743902404587,format= '%f')
V26= st.number_input(label = 'Valeur 26:', value=0.276539471570389,format= '%f')
V27= st.number_input(label = 'Valeur 27:', value=1.44127396787951,format= '%f')
V28= st.number_input(label = 'Valeur 28:', value=-0.127943726430018,format= '%f')
Amount= st.number_input(label = 'Montant:', value=12.31,format= '%f')

#Button predict

if st.button("Prediction"):
    prediction= inference (
        V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,
        V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,
        V24,V25,V26,V27,V28,Amount
    )
    if prediction[0] == 1 :
        resultat = "Cette transaction est une fraude"
    elif prediction[0] == 0:
        resultat = "Cette transaction est légitime"
    st.success(resultat)