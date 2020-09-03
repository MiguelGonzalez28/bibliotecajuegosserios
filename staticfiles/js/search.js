var ico_down = true;
function change_icon() {
    var btn = document.getElementById('buscar_btn');
    ico_down?btn.setAttribute('class', 'fas fa-caret-up'):btn.setAttribute('class', 'fas fa-caret-down');
    ico_down = !ico_down;
}
