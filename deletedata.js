var rollnumber = document.getElementById("rollnumber")
var deletenode = document.getElementById("delete")

deletenode.onclick = function() {
    const itemstr = localStorage.getItem(rollnumber.value)
    if (!itemstr) {
        alert("Roll Number Doesn't Exist");
    } else {
        localStorage.removeItem(rollnumber.value);
        alert("Deleted");
        console.log("Item Deleted");
    }
    rollnumber.value = '';
}