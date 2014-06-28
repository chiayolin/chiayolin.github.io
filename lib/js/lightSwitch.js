/* 
 +======== Ligit Switch (Night Mode) =========+
 | This file is released to the public domain.|
 | Chiayo Lin - www.chiayolin.org - 06272014. |
 +============================================+
 | PATH:                /lib/js/lightSwitch.js|
 +============================================+
*/

function lightSwitch() {
   if (document.body.style.backgroundImage.match("/lib/images/night.png")) {
    document.body.style.backgroundImage = "url('/lib/images/day.png')";
    document.getElementById("mode").innerHTML = "Night Mode: OFF";
    document.getElementById("foot").style.color = "black";
    document.getElementById("foot-link").style.color = "black";
    document.getElementById("foot-link").style.borderBottom = "1px dotted black";
   } 
   else {
    document.body.style.backgroundImage="url('/lib/images/night.png')";
    document.getElementById("mode").innerHTML = "Night Mode: ON";
    document.getElementById("foot").style.color = "white";
    document.getElementById("foot-link").style.color = "white";
    document.getElementById("foot-link").style.borderBottom = "1px dotted white";
     }
 }
