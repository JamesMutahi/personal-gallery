var myVar;

function myPreloader() {
    myVar = setTimeout(showPage, 3000);
}

function showPage() {
    document.getElementById("mdb-preloader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
}

$(function() {
//animations
  $(".menu-link").click(function(e) {
    e.preventDefault();
    $(".menu").toggleClass("open");
    $(".menu-overlay").toggleClass("open");
  });

	$('.carousel-caption').hover(function(){
		$('.btn-anim').toggleClass('animated shake infinite slower');
		});

	$('.menu-link').click(function(){
		$('.real-home').toggleClass('animated fadeInUp');
		$('.home').toggleClass('animated fadeInUp  ');
		$('.gall').toggleClass('animated fadeInUp ');
		$('.featured').toggleClass('animated fadeInUp  ');
		$('.socials').toggleClass('animated fadeIn delay-1s');
		});

	$('.home').click(function(){
		$('.home-icon').toggleClass('animated lightSpeedOut faster');
				});

	$('.gall').click(function(){
		$('.gallery-icon').toggleClass('animated lightSpeedOut fast');
		});

	$('.featured').click(function(){
		$('.featured-icon').toggleClass('animated lightSpeedOut fast');
		});

		$('.home').hover(function(){
		$('.home-icon').toggleClass('animated pulse fast infinite text-white');
				});

	$('.gall').hover(function(){
		$('.gallery-icon').toggleClass('animated pulse fast infinite text-white');
		});

	$('.featured').hover(function(){
		$('.featured-icon').toggleClass('animated pulse fast infinite text-white');
		});

			$('.fa-instagram').hover(function(){
		$(this).toggleClass('animated pulse fast infinite text-white');
				});

	$('.fa-facebook-square').hover(function(){
		$(this).toggleClass('animated pulse fast infinite text-white');
		});

	$('.fa-twitter-square').hover(function(){
		$(this).toggleClass('animated pulse fast infinite text-white');
		});

	$('.fa-linkedin').hover(function(){
		$(this).toggleClass('animated pulse fast infinite text-white');
		});

	$('.pics').hover(function(){
		$(this).toggleClass('animated pulse slow infinite text-white');
		});

});

function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

showinfo = (i)=>{
  dict=eval(i)
  $('#imageimage').attr('src',dict.image);
  $('#imagedescription').text(dict.desc);
  $('#imagetitle').text(dict.name);
  $('#imagedirectlink').attr('href',window.location.origin+dict.image)
  $("#imagelink").val(window.location.origin+'/#'+dict.id);
  $("#ImageModal").modal({backdrop: false},'show');
}
copyaction = ()=>{
document.getElementById("imagelink").select();
document.execCommand("Copy");
}

filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current control button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}