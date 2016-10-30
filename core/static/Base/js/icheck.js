jQuery(window).load(function() {
	$('.single-row input').click(function(){
		var childclass=$(this).parent();
		if(childclass.hasClass('checked'))
			$(childclass).removeClass('checked');
		else
			$(childclass).addClass('checked');
    });
});