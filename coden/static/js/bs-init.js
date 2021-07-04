
if (window.innerWidth < 768) {
	[].slice.call(document.querySelectorAll('[data-bss-disabled-mobile]')).forEach(function (elem) {
		elem.classList.remove('animated');
		elem.removeAttribute('data-bss-hover-animate');
		elem.removeAttribute('data-aos');
	});
}

document.addEventListener('DOMContentLoaded', function() {
	AOS.init();

	var hoverAnimationTriggerList = [].slice.call(document.querySelectorAll('[data-bss-hover-animate]'));
	var hoverAnimationList = hoverAnimationTriggerList.forEach(function (hoverAnimationEl) {
		hoverAnimationEl.addEventListener('mouseenter', function(e){ e.target.classList.add('animated', e.target.dataset.bssHoverAnimate) });
		hoverAnimationEl.addEventListener('mouseleave', function(e){ e.target.classList.remove('animated', e.target.dataset.bssHoverAnimate) });
	});
}, false);

setTimeout(function() {
	$('#message').fadeOut('slow');
  }, 3000);


  

  $("#features").attr("data-aos","flip-down")

// course accordian animation fix
let ca = document.getElementsByClassName('course-accordian')
let cae = ca[ca.length-1]
console.log(cae)
  $('#accordion-2').on('hidden.bs.collapse', function (e) {
	if(e.target == cae)
	{
		$("#features").attr("data-aos","")
		$("#footer").attr("data-aos","")
		$('#features').show()
		$('#footer').show()
		
		// $("#features").attr("data-aos","flip-down")
		// $("#footer").attr("data-aos","flip-down")

		console.log($('#features'))
	}
})


$('#accordion-2').on('shown.bs.collapse', function (e) {
	if(e.target == cae)
	{
		// $("#features").attr("data-aos","")
		// $("#footer").attr("data-aos","")
		// $('#features').show()
		// $('#footer').show()
		
		// $("#features").attr("data-aos","flip-down")
		// $("#footer").attr("data-aos","flip-down")

		console.log($('#features'))
	}
})