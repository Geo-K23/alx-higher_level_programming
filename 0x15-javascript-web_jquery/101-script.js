$(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    const list = $('UL.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
