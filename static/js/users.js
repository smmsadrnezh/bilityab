/**
 * Created by Arman on 2015-08-17.
 */
function validateForm() {
    var users = document.getElementsByName("users[]");
    var superusers = document.getElementsByName('superusers[]');
    var counter = 0;

    for (var i = 0; users[i]; i++) {
        if (users[i].checked && superusers[i].checked) {
            alert("برای هر کاربر حداکثر یکی از گزینه ها باید انتخاب شود");
            return false;
        }
        if (users[i].checked) {
            counter++;
        }
        if (superusers[i].checked) {
            counter++;
        }
    }
    if (counter == 0) {
        alert("هیچ گزینه ای انتخاب نشده است");
        return false;
    }
    return true;
}