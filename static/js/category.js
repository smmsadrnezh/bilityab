/**
 * Created by Arman on 2015-08-12.
 */
function handle() {
    var selectCategory = document.getElementById("event-type");
    var selectedItem = selectCategory.options[selectCategory.selectedIndex];
    var cinema = document.getElementById("cinema-extra-data");
    var music = document.getElementById("music-extra-data");
    var sport = document.getElementById("sport-extra-data");
    switch (selectedItem.value) {
        case "2":
        case "3":
        case "4":
        case "5":
            sport.style.display = "block";
            cinema.style.display = "none";
            music.style.display = "none";
            break;
        case "7":
        case "8":
        case "9":
            sport.style.display = "none";
            cinema.style.display = "block";
            music.style.display = "none";
            break;
        case "11":
        case "12":
            sport.style.display = "none";
            cinema.style.display = "none";
            music.style.display = "block";
            break;
        default:
            sport.style.display = "none";
            cinema.style.display = "none";
            music.style.display = "none";
            break;
    }

}