function create_you(article_id){
    var selecter = window.getSelection()
    var selectStr = selecter.toString()
    url = window.location.href
    location.assign(url + "create_you/?ref="+selectStr);
}

function create_ai(article_id) {
    var selecter = window.getSelection()
    var selectStr = selecter.toString()
    url = window.location.href
    location.assign(url + "create_ai/?ref="+selectStr);
}

function find2mark(searchVal, domid, bgColor) {
    var oDiv = document.getElementById(domid);
    var sText = oDiv.innerHTML;
    var reg1 = /<script[^>]*>(.|\n)*<\/script>/gi;
    sText = sText.replace(reg1, "");
    var bgColor = bgColor || "yellow";
    var num = -1;
    var rStr = new RegExp(searchVal, "gi");
    var rHtml = new RegExp("\<.*?\>", "ig");
    var aHtml = sText.match(rHtml);
    var arr = sText.match(rStr);
    a = -1;
    sText = sText.replace(rHtml, '{~}');
    sText = sText.replace(rStr, function () {
        a++;
        return "<span name='addSpan' style='background-color: " + bgColor + ";'>" + arr[a] + "</span>"
    });
    sText = sText.replace(/{~}/g, function () {
        num++;
        return aHtml[num];
    });
    oDiv.innerHTML = sText;
}