var setBodyScale = function () {
    var scaleSource = Math.min(window.innerWidth, window.innerHeight),
        scaleFactor = 0.35,
        maxScale = 600,
        minScale = 30;
    if (scaleSource > 500)
        scaleFactor = 0.25;
    else if (scaleSource < 350)
        scaleFactor = 0.4;
    var fontSize = scaleSource * scaleFactor;
    if (fontSize > maxScale)
        fontSize = maxScale;
    if (fontSize < minScale)
        fontSize = minScale;
    document.body.style.fontSize = fontSize + '%';
};
window.onresize = function () {
    // setBodyScale();
};
setBodyScale();