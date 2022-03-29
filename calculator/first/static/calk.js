function clikk(val)
{
    document.getElementById("screen").value+=val;
}
function clearscreen(){
    document.getElementById("screen").value="";
}
function equalclick(){
    var text=document.getElementById("screen").value
    var result=eval(text)
    document.getElementById("screen").value=result;
    document.getElementById("bk").innerHTML=text.length;
    
}
function back(){
   var x=document.getElementById("screen").value;
   document.getElementById("screen").value=x.slice(0,-1);
   document.getElementById("bk").innerHTML=x.length-1;

}