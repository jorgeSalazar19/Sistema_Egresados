$(function(){
  $("#registro1").popover({
    placement: 'bottom',
    html: true,
    content : '<button type="button" class="btn btn-danger btn-sm" id="admReg" style=" background-color: #3a906d;" >Administrador</button> <button type="button" id="egresadoReg" style=" background-color: #3a906d;" class="btn btn-success btn-sm">Egresado</button>'
  })
  $('html').click(function() {
    $('#close').popover('hide');
  });
});

$('body').on('click', 'button#admReg', function() {
    $(location).attr('href','pre_registro_admin');
});
$('body').on('click', 'button#egresadoReg', function() {
    $(location).attr('href','pre_registro_egresado');
});

$(function(){
  $("#registro2").popover({
    placement: 'bottom',
    html: true,
    content : '<button type="button" class="btn btn-danger btn-sm" id="admReg" style=" background-color: #3a906d;" >Administrador</button> <button type="button" id="egresadoReg" style=" background-color: #3a906d;" class="btn btn-success btn-sm">Egresado</button>'
  })
  $('html').click(function() {
    $('#close').popover('hide');
  });
});

$('body').on('click', 'button#admReg', function() {
    $(location).attr('href','pre_registro_admin');
});
$('body').on('click', 'button#egresadoReg', function() {
    $(location).attr('href','pre_registro_egresado');
});

$(function(){
    $("#ingreso1").popover({
      placement: 'bottom',
      html: true,
<<<<<<< HEAD
      content : '<button type="button" class="btn btn-danger btn-sm" id="admReg">Administrador</button> <button type="button" id="egresadoReg" class="btn btn-success btn-sm">Egresado</button>'
=======
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng" style=" background-color: #3a906d;" >Administrador</button> <button type="button" id="egresadoIng" style=" background-color: #3a906d;" class="btn btn-success btn-sm">Egresado</button>'
>>>>>>> 6c39f7786ac300aa435981834659aca7031733ca
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
  });
<<<<<<< HEAD

$(function(){
    $("#registro2").popover({
      placement: 'bottom',
      html: true,
      content : '<button type="button" class="btn btn-danger btn-sm" id="admReg2">Administrador</button> <button type="button" id="egresadoReg2" class="btn btn-success btn-sm">Egresado</button>'
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
});

$('body').on('click', 'button#admReg', function() {
    $(location).attr('href','pre_registro_admin');
=======
$('body').on('click', 'button#admIng', function() {
    $(location).attr('href','login_admin');
>>>>>>> 6c39f7786ac300aa435981834659aca7031733ca
});
$('body').on('click', 'button#egresadoIng', function() {
    $(location).attr('href','login_egresado');
});

$('body').on('click', 'button#admReg2', function() {
    $(location).attr('href','pre_registro_admin');
});
$('body').on('click', 'button#egresadoReg2', function() {
    $(location).attr('href','pre_registro_egresado');
});

$(function(){
    $("#ingreso2").popover({
      placement: 'bottom',
      html: true,
<<<<<<< HEAD
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng">Administrador</button> <button type="button" id="egresadoIng" class="btn btn-success btn-sm">Egresado</button>'
=======
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng" style=" background-color: #3a906d;" >Administrador</button> <button type="button" id="egresadoIng" style=" background-color: #3a906d;" class="btn btn-success btn-sm">Egresado</button>'
>>>>>>> 6c39f7786ac300aa435981834659aca7031733ca
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
  });

$(function(){
    $("#ingreso2").popover({
      placement: 'bottom',
      html: true,
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng2">Administrador</button> <button type="button" id="egresadoIng2" class="btn btn-success btn-sm">Egresado</button>'
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
  });
$('body').on('click', 'button#admIng', function() {
    $(location).attr('href','login_admin');
});
$('body').on('click', 'button#egresadoIng', function() {
    $(location).attr('href','login_egresado');
});

$('body').on('click', 'button#admIng2', function() {
    $(location).attr('href','login_admin');
});
$('body').on('click', 'button#egresadoIng2', function() {
    $(location).attr('href','login_egresado');
});