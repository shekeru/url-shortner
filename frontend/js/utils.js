//Current Settings & Stuff
var preview = 1
var music = 0
var mode = 0

//Strings & Stuff
var allCharactersAlphnum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
var p0d = "JavaScript redirects will not embed the destination in apps such as Discord.";
var p1d = "Apache redirects will embed the final destination in apps such as Discord.";
var m1d = "-UNFINISHED- Returns a sketchy link that redirects to a given URL.";
var m0d = "Returns a short link that redirects to the provided URL.";

window.onload = function()
{
    document.getElementById("mode-desc").innerHTML = m0d;
    document.getElementById("preview-desc").innerHTML = p1d;
    //a clever way to get rid of autofill suggestions
    var text = "";
    for (var i = 0; i < 6; i++)
    {
        text += allCharactersAlphnum.charAt(Math.floor(Math.random() * allCharactersAlphnum.length));
    }
    document.getElementById("urlinput").setAttribute("name", text);
}

function getURL()
{   
    var qresult = "";
    var target = document.getElementById("urlinput").value;
    var url = `https://reasons-to.live/geturl?target=${target}&preview=${preview}&mode=${mode}`;
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange=(e)=>{
        qresult = Http.responseText;
        var html = "<a id=\"result-url\" target=\"_blank\" href=" + "https://" + qresult.replace(/['"]+/g, '') + ">";
        document.getElementById("title-text").innerHTML = html + qresult.replace(/['"]+/g, '') + "</a>";
        if (qresult.length > 108) { document.getElementById("result-url").style.fontSize = "14%"; }
        else if (qresult.length > 67) { document.getElementById("result-url").style.fontSize = "15%"; }
        else if (qresult.length > 48) { document.getElementById("result-url").style.fontSize = "25%"; }
    }
}

function setMode(val)
{
    if (val == 0)
    {
        document.getElementById("mode-desc").innerHTML = m0d;
        document.getElementById("mode-0").style.opacity = 1;
        document.getElementById("mode-1").style.opacity = 0;
        mode = 0;
    }
    else
    {
        document.getElementById("mode-desc").innerHTML = m1d;
        document.getElementById("mode-0").style.opacity = 0;
        document.getElementById("mode-1").style.opacity = 1;
        //currently always sets to mode 0 as mode 1 is unfinished
        mode = 0;
    }
}

function setPreview(val)
{
    if (val == 0)
    {
        document.getElementById("preview-desc").innerHTML = p0d;
        document.getElementById("preview-0").style.opacity = 1;
        document.getElementById("preview-1").style.opacity = 0;
        preview = 0;
    }
    else
    {
        document.getElementById("preview-desc").innerHTML = p1d;
        document.getElementById("preview-0").style.opacity = 0;
        document.getElementById("preview-1").style.opacity = 1;
        preview = 1;
    }
}

function toggleMusic()
{
    if (music == 0)
    {
        document.getElementById("footer-music").src = "img/unmute.png";
        document.getElementById("player").volume = 0.1;
        music = 1;
    }
    else
    {
        document.getElementById("footer-music").src = "img/mute.png";
        document.getElementById("player").volume = 0;
        music = 0;
    }
}