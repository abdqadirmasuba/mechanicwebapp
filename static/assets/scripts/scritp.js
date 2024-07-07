

/********************* code section begin*************************/
// Js for collapsing side nave bar
$(document).ready(function () {
  $('#msbo').on('click', function () {
    if ($(window).width() > 701) {
      if ($('body').hasClass('msb-x')) {
        $('body').removeClass('msb-x');
        
      }
      else {
        $('body').addClass('msb-x');
      }
    }
    if ($(window).width() < 700) {
      $('body').removeClass('msb-x');
      $('.mobile-sb-close').show()
      $('#mcw').hide();
    }
  });

  if ($(window).width() < 700) {
    $('body').addClass('msb-x');
    $('.mobile-sb-close').hide()
  }

  $('.mobile-sb-close').click(function(){
    $('body').addClass('msb-x');
    $('#mcw').show();
    $('.mobile-sb-close').hide()

  })

});
/********************* end code section *************************/

/********************* code section begin*************************/
$(document).ready(function(){
$('.toast').toast('show');
});
/********************* end code section *************************/


/********************* code section begin*************************/

$(document).ready(function () {
  $('#invoices').DataTable();
}); 

$(document).ready(function () {
  $('#notifications-logs').DataTable();
});  

//  js for data table
$(document).ready(function () {
  $('#dtBasicExample').DataTable();
  $('.dataTables_length').addClass('bs-select');
});
/********************* end code section *************************/

/********************* code section begin*************************/
// notifications dropdown menu
$('#notifi-icon').click(function (event) {
  if ($(".notifi-drop").hasClass("notifi-hide")) {
    $('.notifi-drop').removeClass("notifi-hide");
  }
  else {
    $('.notifi-drop').addClass("notifi-hide");
  }

});

$('#profile-img').click(function (event) {
  if ($(".my-drop").hasClass("hide")) {
    $('.my-drop').removeClass("hide");
  }
  else {
    $('.my-drop').addClass("hide");
  }

});
/********************* end code section *************************/

/********************* code section begin*************************/
// Side menu toggles and active classes
$(document).ready(function () {
  // Tab Click Event
  $('.side-menu li a').on('click', function () {
    
    // Check if the clicked tab has a dropdown menu
    if ($(this).parent().hasClass('dropdown')) {
      $('.side-menu .inner-menu').addClass('show')
    } 

    if ($(this).parent().hasClass('dropdown-invoice')) {
      $('.side-menu .inner-menu.invoice').addClass('show')
    } 

    if ($(this).parent().hasClass('dropdown-user')) {
      $('.side-menu .inner-menu.user').addClass('show')
    } 
  });
});
/********************* end code section *************************/

/********************* code section begin*************************/
$(document).ready(function() {
  var currentPath = window.location.pathname;
  $('a[href="' + currentPath + '"]').each(function() {
    $(this).parent().addClass('active');
    // Check if the parent has a dropdown menu
    var dropdown = $(this).closest('.dropdown');
    var dropdownUser = $(this).closest('.dropdown-user');
    var dropdownInvoice = $(this).closest('.dropdown-invoice');
    if (dropdown.length > 0) {
      dropdown.find(".inner-menu").addClass('show');
    }
    if (dropdownUser.length > 0 ) {
      dropdownUser.find(".inner-menu").addClass('show');
    }
    if ( dropdownInvoice.length > 0 ) {
      dropdownInvoice.find(".inner-menu").addClass('show');
    }
  });
});
/********************* end code section *************************/

/********************* code section begin*************************/
  // for reasons in tables set to character limits
const limitTextElements = document.querySelectorAll('.limit-text');
const characterLimit = 30; // Set the desired character limit

limitTextElements.forEach(element => {
  const text = element.textContent.trim();
  if (text.length > characterLimit) {
    const truncatedText = text.slice(0, characterLimit) + "...";
    element.textContent = truncatedText;
  }
});
/********************* end code section *************************/

/********************* code section begin*************************/
// myy profile tabs
function opentab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
/********************* end code section *************************/


/********************* code section begin*************************/
//  handling navigeting back to edit content
function refreshPage() {
  location.reload();
}
window.addEventListener('popstate', refreshPage);

/********************* end code section *************************/

/********************* code section begin*************************/
$(document).ready(function () {
  // Function to handle the click event on the table cell
  function cellClicked() {
    const value = $(this).data("value"); // Retrieve the value from the data-value attribute

    // Pass the value to another function or use it as needed
    console.log("Clicked value: ", value);
  }

  // Attach a click event listener to the table cells
  $(document).on("click", "#myTable td", cellClicked);
  }); 

  /********************* end code section *************************/