function Random() {
    var rnd = Math.floor((Math.random() * 12 + 1) + (Math.random() * 8 + 1));
    document.getElementById('tb').value = rnd;
}