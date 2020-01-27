import firebase from 'firebase';

const config = {
  apiKey: 'AIzaSyDOLJxV1mriIabjjhTRVBC64gVoE_T4qpE',
  authDomain: 'test-c5d7d.firebaseapp.com',
  databaseURL: 'https://test-c5d7d.firebaseio.com',
  projectId: 'test-c5d7d',
  storageBucket: 'test-c5d7d.appspot.com',
  messagingSenderId: '241521020210',
  appId: '1:241521020210:web:1e3a57ded05546ba611b2b',
  measurementId: 'G-RF7ZR2KR8G'
};

const fire = firebase.initializeApp(config);

export default fire;
