import React, { Component } from 'react'
import * as faceapi from 'face-api.js'
import * as api from '../api'

export default class Webcam extends Component {

  state = {
    expressions: []
  }
  
  componentDidMount() {
    // import * as api from 'api'
    const video = document.querySelector("#videoElement");
    const canvas = document.querySelector('#canvasElement')

    console.log('in script.js')

    const startVideo = () => {
      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(function (stream) {
            video.srcObject = stream;
          })
          .catch(function (error) {
            console.log("Something went wrong!");
          });
      }
    }

    Promise.all([
      faceapi.nets.tinyFaceDetector.loadFromUri('/weights'),
      faceapi.nets.faceRecognitionNet.loadFromUri('/weights'),
      faceapi.nets.faceLandmark68Net.loadFromUri('/weights'),
      faceapi.nets.faceExpressionNet.loadFromUri('/weights')
    ]).then(startVideo())

    video.addEventListener('play', () => {
      //const canvas = faceapi.createCanvasFromMedia(video)
      //document.body.append(canvas)
      const displaySize = { width: video.width, height: video.height }
      faceapi.matchDimensions(canvas, displaySize)
      setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()

        // console.log(detections)
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        //faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
      }, 100)

    })

    video.addEventListener('play', () => {
      setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
        const date = new Date()
        if(detections[0]) {
          
          const data = api.makeInt(detections[0])
          console.log("data", data)
      
          // const data = { "neutral": 12, "happy": 13, "sad": 14, "angry": 15, "fearful": 0, "disgusted": 0, "surprised": 0, "timestamp": date.toGMTString() }
          api.postData({ ...data, "timestamp": date.toGMTString() })
  

        } else {
          api.postData({"neutral": 0, "happy": 0, "sad": 0, "angry": 0, "fearful":0, "disgusted": 0, "surprised": 0, "timestamp": date.toGMTString()}).catch(err => {
            console.log(err)
          })
        }

        // console.log(detections[0].expressions)
        // api.getData().then(data => {
        //   console.log(data)
        // })
      }, 10000)
    })
  }
  
  render() {
    return (
      <div id="container">
        <video autoPlay={true} id="videoElement" width="640" height="480">

        </video>
        <canvas id="canvasElement"></canvas>
      </div>
      
    )
  }
}

