import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle

dic1={'itching': 33,
 'skin_rash': 24,
 'continuous_sneezing': 8,
 'shivering': 23,
 'stomach_pain': 26,
 'acidity': 0,
 'vomiting': 28,
 'indigestion': 14,
 'muscle_wasting': 17,
 'patches_in_throat': 21,
 'fatigue': 11,
 'weight_loss': 31,
 'sunken_eyes': 27,
 'cough': 9,
 'headache': 12,
 'chest_pain': 5,
 'back_pain': 1,
 'weakness_in_limbs': 29,
 'chills': 6,
 'joint_pain': 15,
 'yellowish_skin': 32,
 'constipation': 7,
 'pain_during_bowel_movements': 20,
 'breathlessness': 3,
 'cramps': 10,
 'weight_gain': 30,
 'mood_swings': 16,
 'neck_pain': 19,
 'muscle_weakness': 18,
 'stiff_neck': 25,
 'pus_filled_pimples': 22,
 'burning_micturition': 4,
 'bladder_discomfort': 2,
 'high_fever': 13}

dic2={'skin_rash': 35,
 'nodal_skin_eruptions': 27,
 'shivering': 33,
 'chills': 9,
 'acidity': 1,
 'ulcers_on_tongue': 41,
 'vomiting': 42,
 'yellowish_skin': 47,
 'stomach_pain': 37,
 'loss_of_appetite': 23,
 'indigestion': 19,
 'patches_in_throat': 30,
 'high_fever': 18,
 'weight_loss': 46,
 'restlessness': 32,
 'sunken_eyes': 38,
 'dehydration': 13,
 'cough': 11,
 'chest_pain': 8,
 'dizziness': 14,
 'headache': 17,
 'weakness_in_limbs': 43,
 'neck_pain': 26,
 'weakness_of_one_body_side': 44,
 'fatigue': 15,
 'joint_pain': 20,
 'lethargy': 22,
 'nausea': 25,
 'abdominal_pain': 0,
 'pain_during_bowel_movements': 28,
 'pain_in_anal_region': 29,
 'breathlessness': 6,
 'sweating': 39,
 'cramps': 12,
 'bruising': 7,
 'weight_gain': 45,
 'cold_hands_and_feets': 10,
 'mood_swings': 24,
 'anxiety': 2,
 'knee_pain': 21,
 'stiff_neck': 36,
 'swelling_joints': 40,
 'pus_filled_pimples': 31,
 'blackheads': 3,
 'bladder_discomfort': 4,
 'foul_smell_ofurine': 16,
 'skin_peeling': 34,
 'blister': 5}

dic3={'nodal_skin_eruptions': 35,
 'dischromic_patches': 18,
 'chills': 11,
 'watering_from_eyes': 50,
 'ulcers_on_tongue': 48,
 'vomiting': 49,
 'yellowish_skin': 53,
 'nausea': 33,
 'stomach_pain': 44,
 'burning_micturition': 9,
 'abdominal_pain': 0,
 'loss_of_appetite': 29,
 'high_fever': 24,
 'extra_marital_contacts': 20,
 'restlessness': 39,
 'lethargy': 28,
 'dehydration': 16,
 'diarrhoea': 17,
 'breathlessness': 7,
 'dizziness': 19,
 'loss_of_balance': 30,
 'headache': 23,
 'blurred_and_distorted_vision': 6,
 'neck_pain': 34,
 'weakness_of_one_body_side': 51,
 'altered_sensorium': 1,
 'fatigue': 21,
 'weight_loss': 52,
 'sweating': 45,
 'joint_pain': 26,
 'dark_urine': 15,
 'swelling_of_stomach': 47,
 'cough': 14,
 'pain_in_anal_region': 37,
 'bloody_stool': 5,
 'chest_pain': 10,
 'bruising': 8,
 'obesity': 36,
 'cold_hands_and_feets': 12,
 'mood_swings': 31,
 'anxiety': 2,
 'knee_pain': 27,
 'hip_joint_pain': 25,
 'swelling_joints': 46,
 'movement_stiffness': 32,
 'spinning_movements': 43,
 'blackheads': 3,
 'scurring': 40,
 'foul_smell_ofurine': 22,
 'continuous_feel_of_urine': 13,
 'skin_peeling': 42,
 'silver_like_dusting': 41,
 'blister': 4,
 'red_sore_around_nose': 38}


d1=pd.read_csv('metadata/data.csv')
d2=pd.read_csv('metadata/Symptom-severity.csv')
d3=pd.read_csv('metadata/sym-desc.csv')
d4=pd.read_csv('metadata/sym-prec.csv')    
d5=pd.read_csv('metadata/medicine.csv')
dn=pd.read_csv('metadata/dataset.csv')
model_knn=pickle.load(open('/home/vyper/Documents/amiokay/metadata/knn_model.pkl','rb'))
lencoder=LabelEncoder()
encoded_y = lencoder.fit_transform(dn['Disease'])


def abo(disease):
    ind=int(d3[d3['Disease']==disease].index.values)
    return d3.iloc[ind]['Description']

def precautions(disease):
    ind=int(d4[d4['Disease']==disease].index.values)
    p1=d4.iloc[ind]['Precaution_1']
    p2=d4.iloc[ind]['Precaution_2']
    p3=d4.iloc[ind]['Precaution_3']
    z=[p1,p2,p3]
    return z

def med(disease):
    ind=int(d5[d5['Disease']==disease].index.values)
    p1=d5.iloc[ind]['Medicine1']
    p2=d5.iloc[ind]['Medicine2']
    p3=d5.iloc[ind]['Medicine3']
    p1=str(p1)
    p2=str(p2)
    p3=str(p3)

    z=p1
    if(p2!="nan"):
        z=z+','+p2
    if(p3!="nan"):
        z=z+','+p3

    return z

def get_weights(symptom):
    ind=int(d2[d2['Symptom']==symptom].index.values)
    return d2.iloc[ind]['weight']

cols_to_normalize=['Symptom_1', 'Symptom_2', 'Symptom_3', 'sw_1', 'sw_2', 'sw_3']

def knnp(pre):
    final=[]
    wts=[]
    for i in pre:
        wts.append(get_weights(i))
    # small fix needed
    pre[0]=dic1[pre[0]]
    pre[1]=dic2[pre[1]]
    pre[2]=dic3[pre[2]]
    final=pre+wts
    sc=StandardScaler().fit(d1[cols_to_normalize])
    final=list((sc.transform([final]))[0])
    numerical=(model_knn.predict([final])[0])
    return (lencoder.inverse_transform([numerical])[0])

def rez(s1,s2,s3):    
    pre=[s1,s2,s3]
    dis=knnp(pre) # array
    aboutt=abo(dis.strip())
    prec=precautions(dis.strip())
    meds=med(dis.strip())        
    
    return [dis,aboutt,prec[0],prec[1],prec[2],meds]

# print(rez('shivering','dehydration','neck_pain'))
