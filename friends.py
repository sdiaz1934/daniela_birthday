# components.html(
#     """
# <!DOCTYPE html>
# <html>
# <head>
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <style>
# * {box-sizing: border-box;}
# body {font-family: Verdana, sans-serif;}
# .mySlides {display: none;}
# img {vertical-align: middle;}
#
# /* Slideshow container */
# .slideshow-container {
#   max-width: 1000px;
#   position: relative;
#   margin: auto;
# }
#
# /* Caption text */
# .text {
#   color: #f2f2f2;
#   font-size: 15px;
#   padding: 8px 12px;
#   position: absolute;
#   bottom: 8px;
#   width: 100%;
#   text-align: center;
# }
#
# /* Number text (1/3 etc) */
# .numbertext {
#   color: #f2f2f2;
#   font-size: 12px;
#   padding: 8px 12px;
#   position: absolute;
#   top: 0;
# }
#
# /* The dots/bullets/indicators */
# .dot {
#   height: 15px;
#   width: 15px;
#   margin: 0 2px;
#   background-color: #bbb;
#   border-radius: 50%;
#   display: inline-block;
#   transition: background-color 0.6s ease;
# }
#
# .active {
#   background-color: #717171;
# }
#
# /* Fading animation */
# .fade {
#   animation-name: fade;
#   animation-duration: 1.5s;
# }
#
# @keyframes fade {
#   from {opacity: .4}
#   to {opacity: 1}
# }
#
# /* On smaller screens, decrease text size */
# @media only screen and (max-width: 300px) {
#   .text {font-size: 11px}
# }
# </style>
# </head>
# <body>
#
# <h2>Happy Birthday :)</h2>
#
#
# <div class="slideshow-container">
#
# <div class="mySlides fade">
#   <div class="numbertext">1 / 3</div>
#   <img src="https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Text</div>
# </div>
#
# <div class="mySlides fade">
#   <div class="numbertext">2 / 3</div>
#   <img src="https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Two</div>
# </div>
#
# <div class="mySlides fade">
#   <iframe src="https://drive.google.com/file/d/1zjWpACFWw49a78Y6A8NKADx2eGN-7XfX/preview" width="640" height="480" allow="autoplay"></iframe>
# </div>
#
# </div>
# <br>
#
# <div style="text-align:center">
#   <span class="dot"></span>
#   <span class="dot"></span>
#   <span class="dot"></span>
# </div>
#
# <script>
# let slideIndex = 0;
# showSlides();
#
# function showSlides() {
#   let i;
#   let slides = document.getElementsByClassName("mySlides");
#   let dots = document.getElementsByClassName("dot");
#   for (i = 0; i < slides.length; i++) {
#     slides[i].style.display = "none";
#   }
#   slideIndex++;
#   if (slideIndex > slides.length) {slideIndex = 1}
#   for (i = 0; i < dots.length; i++) {
#     dots[i].className = dots[i].className.replace(" active", "");
#   }
#   slides[slideIndex-1].style.display = "block";
#   dots[slideIndex-1].className += " active";
#   setTimeout(showSlides, 3000); // Change image every 5 seconds
# }
# </script>
#
# </body>
# </html>
#
#     """,
#     height=600,
# )
# presentation_friends = """
#                     <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTET8ry04fbuSnefLbggq7-irLL9EV99X25miz6gSVmWDuB_WkG7GifjNvGHeumqQ/embed?start=true&loop=false&delayms=3000" frameborder="0" width="600" height="500" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
#             """
# st.markdown(presentation_friends, unsafe_allow_html=True)



components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTET8ry04fbuSnefLbggq7-irLL9EV99X25miz6gSVmWDuB_WkG7GifjNvGHeumqQ/embed?start=true&loop=false&delayms=2000",height=565)