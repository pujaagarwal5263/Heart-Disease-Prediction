# Heart-Disease-Prediction
> Heart disease prediction model made with sci-kit learn.

# How to run the app?
Setup your virtual environment and run the following command:
```
python app.py
```

# What is the payload to be sent?
```
{
    "features":[[57,0,0,140,241,0,1,123,1,0.2,1,0,3]]
}
```

# URL to be hit on
Once the app is up and running the hit this endpoint with above payload: <strong>http://localhost:5000/predict</strong>

The following are the features we'll use to predict our target variable (heart disease or no heart disease)
1. age - age in years,
2. sex - (1 = male; 0 = female),
3. cp - chest pain type,
   <ul>
    <li> 0: Typical angina: chest pain related decrease blood supply to the heart </li>
     <li>1: Atypical angina: chest pain not related to heart </li>
    <li>2: Non-anginal pain: typically esophageal spasms (non heart related)</li>
     <li> 3: Asymptomatic: chest pain not showing signs of disease</li>
   </ul>
   
4. trestbps - resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern
5. chol - serum cholesterol in mg/dl 
   <br/>serum = LDL + HDL + .2 * triglycerides,
   <br/> above 200 is cause for concern,
6. fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)",
   <br/> '>126' mg/dL signals diabetes,
7. restecg - resting electrocardiographic results,
   <ul>
   <li>0: Nothing to note, </li> 
   <li>1: ST-T Wave abnormality: can range from mild symptoms to severe problems and signals,  non-normal heart beat,  </li>
  <li>2: Possible or definite left ventricular hypertrophy, Enlarged heart's main pumping chamber</li>
   </ul>
8. thalach - maximum heart rate achieved,
<br/>
9. exang - exercise induced angina (1 = yes; 0 = no),
<br/>
10. oldpeak - ST depression induced by exercise relative to rest,
<ul>
    <li> looks at stress of heart during excercise, </li>
    <li> unhealthy heart will stress more, </li>
</ul>
11. slope - the slope of the peak exercise ST segment,
<ul>
    <li> 0: Upsloping: better heart rate with excercise (uncommon), </li>
      <li> 1: Flatsloping: minimal change (typical healthy heart), </li>
     <li> 2: Downslopins: signs of unhealthy heart, </li>
</ul>
12. ca - number of major vessels (0-3) colored by flourosopy,
<ul>
    <li>colored vessel means the doctor can see the blood passing through,</li>
     <li> the more blood movement the better (no clots), </li>
    </ul>
13. thal - thalium stress result,
<ul>
    <li> 1,3: normal, </li>
    <li> 6: fixed defect: used to be defect but ok now, </li>
   <li> 7: reversable defect: no proper blood movement when excercising, </li>
</ul>
14. target - have disease or not (1=yes, 0=no) (= the predicted attribute)

**Note: No personal identifiable information (PPI) can be found in the dataset**
