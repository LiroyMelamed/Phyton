/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Variables
  const Greeting = document.getElementById('Greeting')

  const Algo1 = document.getElementById('FirstAlgo')
  const Algo1BTN = document.getElementById('FirstAlgoBTN')

  const Algo2 = document.getElementById('SecondAlgo')
  const Algo2BTN = document.getElementById('SecondAlgoBTN')

  const Partner = document.getElementById('Partners')
  const Part = document.getElementById('Part')

  const Explain = document.getElementById('Explain')
  const Expl = document.getElementById('Expl')

  const Exmple = document.getElementById('Example')

  const ExmpleAlgo1 = document.getElementById('ExampleAlgo1')
  const ExAlgo1 = document.getElementById('Algo1')
  ExAlgo1.hidden = false

  const ExmpleAlgo2 = document.getElementById('ExampleAlgo2')


  // Listener
  Algo1BTN.addEventListener("click", function (){
    Greeting.hidden = true
    Algo1.hidden = false
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo1.hidden = true
  })

  Algo2BTN.addEventListener("click", function (){
    Algo1.hidden = true
    Algo2.hidden = false
    Greeting.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo1.hidden = true
  })

  Partner.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = false
    Expl.hidden = true
    ExAlgo1.hidden = true
  })

  Explain.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = false
    ExAlgo1.hidden = true
  })

  Exmple.addEventListener("click", function(){
    window.location.href = 'http://127.0.0.1:5000/אלגוריתם_דוגמא'
  })

  ExmpleAlgo1.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo1.hidden = false
  })

  ExmpleAlgo2.addEventListener("click", function(){
    window.location.href = 'http://127.0.0.1:5000/אלגוריתם_שני'
  })


  // Graphs
//   const ctx = document.getElementById('myChart')
//   // eslint-disable-next-line no-unused-vars
//   const myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//       labels: [
//         'Sunday',
//         'Monday',
//         'Tuesday',
//         'Wednesday',
//         'Thursday',
//         'Friday',
//         'Saturday'
//       ],
//       datasets: [{
//         data: [
//           15339,
//           21345,
//           18483,
//           24003,
//           23489,
//           24092,
//           12034
//         ],
//         lineTension: 0,
//         backgroundColor: 'transparent',
//         borderColor: '#007bff',
//         borderWidth: 4,
//         pointBackgroundColor: '#007bff'
//       }]
//     },
//     options: {
//       scales: {
//         yAxes: [{
//           ticks: {
//             beginAtZero: false
//           }
//         }]
//       },
//       legend: {
//         display: false
//       }
//     }
//   })
})()
