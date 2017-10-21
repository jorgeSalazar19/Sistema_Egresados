  $(function(){
    $("#registro").popover({
      placement: 'bottom',
      html: true,
      content : '<button type="button" class="btn btn-danger btn-sm" id="admReg">Administrador</button> <button type="button" id="egresadoReg" class="btn btn-success btn-sm">Egresado</button>'
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
  });

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
});
$('body').on('click', 'button#egresadoReg', function() {
    $(location).attr('href','pre_registro_egresado');
});

$('body').on('click', 'button#admReg2', function() {
    $(location).attr('href','pre_registro_admin');
});
$('body').on('click', 'button#egresadoReg2', function() {
    $(location).attr('href','pre_registro_egresado');
});

$(function(){
    $("#ingreso").popover({
      placement: 'bottom',
      html: true,
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng">Administrador</button> <button type="button" id="egresadoIng" class="btn btn-success btn-sm">Egresado</button>'
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