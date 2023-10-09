$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
    if (textStatus === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
