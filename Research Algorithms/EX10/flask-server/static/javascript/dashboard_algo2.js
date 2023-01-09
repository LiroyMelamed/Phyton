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

  const ExmpleAlgo2 = document.getElementById('ExampleAlgo2')
  const ExAlgo2 = document.getElementById('Algo2')
  ExAlgo2.hidden = false



  // Listener
  Algo1BTN.addEventListener("click", function (){
    Greeting.hidden = true
    Algo1.hidden = false
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo2.hidden = true
  })

  Algo2BTN.addEventListener("click", function (){
    Algo1.hidden = true
    Algo2.hidden = false
    Greeting.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo2.hidden = true
  })

  Partner.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = false
    Expl.hidden = true
    ExAlgo2.hidden = true
  })

  Explain.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = false
    ExAlgo2.hidden = true
  })

  Exmple.addEventListener("click", function(){
    window.location.href = 'http://127.0.0.1:5000/אלגוריתם_דוגמא'
  })

  ExmpleAlgo1.addEventListener("click", function(){
    window.location.href = 'http://127.0.0.1:5000/אלגוריתם_ראשון'
  })

  ExmpleAlgo2.addEventListener("click", function(){
    Greeting.hidden = true
    Algo1.hidden = true
    Algo2.hidden = true
    Part.hidden = true
    Expl.hidden = true
    ExAlgo2.hidden = false
  })

})()
