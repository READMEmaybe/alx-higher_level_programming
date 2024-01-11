$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;
    $.get(apiUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
