// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// nice select
$(document).ready(function () {
    $('select').niceSelect();
});

// date picker
$(function () {
    $("#inputDate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', new Date());
});

// owl carousel slider js
$('.team_carousel').owlCarousel({
    loop: true,
    margin: 15,
    dots: true,
    autoplay: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1,
            margin: 0
        },
        576: {
            items: 2,
        },
        992: {
            items: 3
        }
    }
})


// For toggling the dropdown when clicked
document.querySelector('.dropdown-toggle').addEventListener('click', function(event) {
    const dropdown = event.target.closest('.nav-item');
    dropdown.classList.toggle('show'); // Toggle the 'show' class to display the dropdown
    event.preventDefault();
  });
  
  // Close the dropdown if clicked outside
  window.addEventListener('click', function(event) {
    if (!event.target.closest('.dropdown')) {
      const dropdown = document.querySelector('.nav-item.dropdown');
      dropdown.classList.remove('show');
    }
  });


  document.getElementById("subscribeForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    const email = document.getElementById("email").value;
    
    if (email) {
      alert("Thank you for subscribing with " + email);
    } else {
      alert("Please enter a valid email.");
    }
  });

   // Wait for the DOM to load completely
   document.addEventListener("DOMContentLoaded", function() {
    // Get the form element
    const form = document.getElementById("subscribeForm");

    // Add event listener for form submission
    form.addEventListener("submit", function(event) {
      event.preventDefault();  // Prevent the form from submitting

      // Get the email value
      const email = document.getElementById("email").value;
      
      // Display alert based on whether email is entered or not
      if (email) {
        alert("Thank you for subscribing with " + email);
      } else {
        alert("Please enter a valid email.");
      }
    });
  });