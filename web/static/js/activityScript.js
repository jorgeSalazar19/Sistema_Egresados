$(document).ready(function(){
    var flag = false;
    try{
      flag = $('#valorCreation').val();
    }catch(err){
      flag = false;
    }
    console.log(flag);
    if (flag) {
       $('#modalCreation').modal('show');
    }

});

$(document).ready(function(){
    var flag = false;
    try{
      flag = $('#valorEdit').val();
    }catch(err){
      flag = false;
    }
    console.log(flag);
    if (flag) {
       $('#modalEdit').modal('show');
    }

});