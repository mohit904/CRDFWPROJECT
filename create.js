console.log("Entering JS")
var create = document.getElementById("create")
var rollnumber = document.getElementById("rollnumber")
var nameofperson = document.getElementById("name")
var ageofperson = document.getElementById("age")
var placeofperson = document.getElementById("place")
var ttlofperson = document.getElementById("ttl")
create.onclick = function() {
    const itemstr = localStorage.getItem(rollnumber.value)
    if (!itemstr) {
        if (ttlofperson.value == 0) {
            var object = {
                name: nameofperson.value,
                age: ageofperson.value,
                place: placeofperson.value,
                expiry: 0
            };
            localStorage.setItem(rollnumber.value, JSON.stringify(object));
            alert("Data is stored");
            console.log("Stored");
        } else {
            const now = new Date()
            var sec = now.getTime();
            var sec2 = parseInt(ttlofperson.value);
            sec = sec + sec2;
            var object = {
                name: nameofperson.value,
                age: ageofperson.value,
                place: placeofperson.value,
                expiry: sec,
            };
            localStorage.setItem(rollnumber.value, JSON.stringify(object));
            alert("Data is stored");
            console.log("Stored");
        }
    } else {
        alert("The Rollnumber already exist");
        console.log("Element already exists");
    }
    rollnumber.value = '';
    nameofperson.value = '';
    ageofperson.value = '';
    placeofperson.value = '';
    ttlofperson.value = '';
}