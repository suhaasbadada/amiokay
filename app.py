from flask import Flask, request,render_template,redirect,url_for
from predict_diseases import rez
from google_search_api import treatment_near_me
app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template("input.html")


@app.route('/output',methods=['POST'])
def output():
    Symptom1=request.form["Symptom1"]
    Symptom2=request.form["Symptom2"]
    Symptom3=request.form["Symptom3"]

    f1=Symptom1 in list(dic1.keys())
    f2=Symptom2 in list(dic2.keys())
    f3=Symptom3 in list(dic3.keys()) 

    if (f1 and f2 and f3):
    # print(rez(Symptom1,Symptom2,Symptom3))
    
        out=rez(Symptom1,Symptom2,Symptom3)
        hosps=treatment_near_me(out[0])
        n1,r1,la1,lo1=hosps[0][0],hosps[0][3],hosps[0][1],hosps[0][2]
        n2,r2,la2,lo2=hosps[1][0],hosps[1][3],hosps[1][1],hosps[1][2]
        n3,r3,la3,lo3=hosps[2][0],hosps[2][3],hosps[2][1],hosps[2][2]
        if(r1==0):
            r1='not rated'

        if(r2==0):
            r2='not rated'

        if(r3==0):
            r3='not rated'

        return render_template("output.html",dis=out[0],about=out[1],p1=out[2],p2=out[3],p3=out[4],la1=la1,lo1=lo1,la2=la2,lo2=lo2,la3=la3,lo3=lo3,meds=out[5],n1=n1,r1=r1,n2=n2,r2=r2,n3=n3,r3=r3)
    else:
        return redirect(url_for('home'))

@app.route('/')
def go_back():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True)