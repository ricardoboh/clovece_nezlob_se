function sleep(milliseconds) {
    const date = Date.now();
    let current_date = null;
    do {
        current_date = Date.now();
    } while (current_date - date < milliseconds);
}
function cislo_na_kostce() {
    const list_of_dice = ["jedna","dva","tri","ctyri","pet","sest"];
    const random = Math.floor(Math.random() * list_of_dice.length);
    for (var i in list_of_dice) {
        document.getElementById(list_of_dice[i]).style.display = "none";
    }
    document.getElementById(list_of_dice[random]).style.display = "block";
}