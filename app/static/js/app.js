
//ポップアップ

// $(function () {
//     $('span').hover(function() {
//       $(this).next('p').show();
//     }, function(){
//       $(this).next('p').hide();
//     });
//   });
  
 

//date-targetからidを取得して、関係するid同士をリレーションしている
// マウスオーバーでのshow,hide
$(function () {
    $('il').hover(function() {
    var id =  $(this).attr('data-target');    
      $(id).show();
    }, function(){
    var id =  $(this).attr('data-target');
      $(id).hide();
    });
  });

  // マウスオーバーでの塗り潰し　線をかく
  // ちゃんと色を指定すること！
  $(function () {
    $('pnt').hover(function() {
    var id =  $(this).attr('data-pnt');    
      $(id).css({border : "solid 1.3px #86b5e9"});
    }, function(){
    var id =  $(this).attr('data-pnt');
      $(id).css({border : "dashed 1.3px #86b5e9"});
    });
  });

  // チケットを追加
  $(function () {
    $('tck').hover(function() {
    var id =  $(this).attr('data-tck');    
      $(id).show();
    }, function(){
    var id =  $(this).attr('data-tck');
      $(id).hide();
    });
  });

// チェックボックス用！
  $(function() {
    $('input').on("click",function(){
      var id =  $(this).attr('data-check');  
      $(id).prop("checked", $(this).prop("checked"));
    });
  });

// 連続ディレイ
$(function(){
	// リストを非表示
	$('#container  label').hide();
	// 繰り返し処理
	$('#container label').each(function(i) {
		// 遅延させてフェードイン
		$(this).delay(15 * i).fadeIn(20);
	});
});

$(function(){
 
	// リストを非表示
	$('#cont span').hide();
 
	// 繰り返し処理
	$('#cont span').each(function(i) {
 
		// 遅延させてフェードイン
		$(this).delay(30 * i).fadeIn(1);
 
	});
 
});