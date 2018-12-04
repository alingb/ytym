$(document).ready(function(){
    main();
});
function main() {
    show("fru");
    show("sel");
    show("smart");
}

function show(id) {
    var num = 500
    var box = document.getElementById(id);
    var text = box.innerHTML;
    var newBox = document.createElement("div");
    var btn = document.createElement("button");
    newBox.innerHTML = text.substring(0, num);
    btn.innerHTML = text.length > num ? "...显示全部" : "";
    btn.href = "###";
    btn.onclick = function () {
        if (btn.innerHTML == "...显示全部") {
            btn.innerHTML = "收起";
            newBox.innerHTML = text;
        } else {
            btn.innerHTML = "...显示全部";
            newBox.innerHTML = text.substring(0, num);
        }
    };
    box.innerHTML = "";
    box.appendChild(newBox);
    box.appendChild(btn);
}
