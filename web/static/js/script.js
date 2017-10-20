  $(function(){
    $("#registro").popover({
      placement: 'bottom',
      html: true,
      title : '<h6>Como</h6>', 
      content : '<button type="button" class="btn btn-danger btn-sm" id="admReg">Administrador</button> <button type="button" id="egresadoReg" class="btn btn-success btn-sm">Egresado</button>'
    })
    $('html').click(function() {
      $('#close').popover('hide');
    });
  });

$('body').on('click', 'button#1admReg', function() {
    $(location).attr('href','pre_registro_admin');
});
$('body').on('click', 'button#egresadoReg', function() {
    $(location).attr('href','pre_registro_egresado');
});

$(function(){
    $("#ingreso").popover({
      placement: 'bottom',
      html: true,
      title : '<h6>Como</h6>',
      content : '<button type="button" class="btn btn-danger btn-sm" id="admIng">Administrador</button> <button type="button" id="egresadoIng" class="btn btn-success btn-sm">Egresado</button>'
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