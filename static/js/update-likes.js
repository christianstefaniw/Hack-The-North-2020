function update_coins(post, user, elem) {
    $.ajax({
      method: "POST",
      url: `update_like/${user}/${post}`,
      data: {},
      success: function(data) {
        elem.getElementsByClassName('likes')[0].innerText = data.count;
      }
    })
  }