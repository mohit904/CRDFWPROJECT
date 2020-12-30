var rollnumber = document.getElementById("rollnumber")
var read = document.getElementById("read")
var nameofperson = document.getElementById("name")
var ageofperson = document.getElementById("age")
var placeofperson = document.getElementById("place")


read.onclick = function() {
    var jsonString = localStorage.getItem(rollnumber.value);
    if (jsonString) {
        var retrievedObject = JSON.parse(jsonString);
        if (retrievedObject.expiry != 0) {
            const now = new Date();
            console.log(retrievedObject.expiry)
            var sec = now.getTime();
            console.log(sec)
            if (sec > retrievedObject.expiry) {
                localStorage.removeItem(rollnumber.value);
                alert("The Given Roll Number has expired with respect to Time to Live");
                nameofperson.value = '';
                ageofperson.value = '';
                placeofperson.value = '';
            } else {
                nameofperson.textContent = retrievedObject.name;
                ageofperson.textContent = retrievedObject.age;
                placeofperson.textContent = retrievedObject.place;
                console.log("Printed");
            }
        } else {
            nameofperson.textContent = retrievedObject.name;
            ageofperson.textContent = retrievedObject.age;
            placeofperson.textContent = retrievedObject.place;
            console.log("Printed");
        }
    } else {
        alert("The Following Roll Number Doesn't Exist");
        nameofperson.value = '';
        ageofperson.value = '';
        placeofperson.value = '';
    }
    rollnumber.value = '';

}