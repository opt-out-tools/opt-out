console.log("here");
document.getElementById("slider").remove();
var sliderStyle = document.createElement('style');
document.head.appendChild(sliderStyle);
document.getElementById("slider").addEventListener("input", function (evt) {
		var rule;
    if (evt.target.value < 1) 
        rule = "background: url('angry.svg')";
    else
        rule = "background: url('happy.svg')";

    sliderStyle.textContent = 
            "#slider::-webkit-slider-thumb{ "+rule+" } " +
            "#slider::-ms-thumb{ "+rule+" } " +
            "#slider::-moz-range-thumb{  "+rule+" } ";
})