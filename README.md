# Heart-Disease-Prediction
> Heart disease prediction model made with sci-kit learn.

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
      <li>1: ST-T Wave abnormality,</li> 
       <ul>
         <li>    - can range from mild symptoms to severe problems, </li> 
          <li>   - signals non-normal heart beat, </li> 
      </ul>
  <li> 2: Possible or definite left ventricular hypertrophy,</li> 
       <br/>   - Enlarged heart's main pumping chamber,
   </ul>
8. thalach - maximum heart rate achieved,
9. exang - exercise induced angina (1 = yes; 0 = no),
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
    <li> 1,3: normal, </li>
    <li> 6: fixed defect: used to be defect but ok now, </li>
   <li> 7: reversable defect: no proper blood movement when excercising, </li>
14. target - have disease or not (1=yes, 0=no) (= the predicted attribute),

    <strong>**Note:** No personal identifiable information (PPI) can be found in the dataset   </strong>