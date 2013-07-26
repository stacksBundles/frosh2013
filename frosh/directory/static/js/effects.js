$(document).on("click", ".boxed", function() {
               
               var view = $(this).attr("id");
               
               view = "/" + view + "/";
               
               if (view == "/index/") {
                   window.location.replace('http://localhost:8000/');
               }
               
               if (view == "/register/") {
                   window.location.replace('http://ssmu-frosh.openface.ca');
               }
               
               
               $.ajax({
                      type: "GET",
                      url: view,
                      success: function(response) {
                      $("#main").replaceWith(response);
                      }
                      });

               
               $("#myTable").replaceWith("<table id='myTable'><td class='boxed' id='index'><img src='static/images/buttons/index.png' onmouseover='this.src=&quot;static/images/buttons/indexhover.png&quot'; onmouseout='this.src=&quot;static/images/buttons/index.png&quot;'/></td><td class='boxed' id='propaganda'><img src='static/images/buttons/propaganda.png' onmouseover='this.src=&quot;static/images/buttons/propagandahover.png&quot;'onmouseout='this.src=&quot;static/images/buttons/propaganda.png&quot;'/></td><td class='boxed' id='faq'><img src='static/images/buttons/faq.png' onmouseover='this.src=&quot;static/images/buttons/faqhover.png&quot;'onmouseout='this.src=&quot;static/images/buttons/faq.png&quot;'/></td><td class='centerPiece'><br><br><br><img src='static/images/coming.png' width='140'><br><br><iframe src='http://free.timeanddate.com/countdown/i3ozcnz0/n165/cf11/cm0/cu4/ct1/cs0/ca0/co0/cr0/ss0/cacfff/cpc000/pct/tcfff/fs100/szw448/szh189/iso2013-08-29T17:00:00' frameborder='0' width='160' height='28'></iframe></td><td class='boxed' id='sponsors'><img src='static/images/buttons/sponsors.png' onmouseover='this.src=&quot;static/images/buttons/sponsorshover.png&quot;'onmouseout='this.src=&quot;static/images/buttons/sponsors.png&quot;'/></td><td class='boxed' id='houses'><img src='static/images/buttons/houses.png' onmouseover='this.src=&quot;static/images/buttons/houseshover.png&quot;'onmouseout='this.src=&quot;static/images/buttons/houses.png&quot;'/></td><td class='boxed' id='register'><img src='static/images/buttons/register.png' onmouseover='this.src=&quot;static/images/buttons/registerhover.png&quot;'onmouseout='this.src=&quot;static/images/buttons/register.png&quot;'/></td></tr></table>")
               
               var string = $(this).attr("id");
               
               if (string == "index") {
               $("#myTable #index").replaceWith("<td class='boxed' id='index'><img src='static/images/buttons/indexhover.png' /></td>");
               };
               
               if (string == "propaganda") {
               $("#myTable #propaganda").replaceWith("<td class='boxed' id='index'><img src='static/images/buttons/propagandahover.png' /></td>");
               };
               
               if (string == "faq") {
               $("#myTable #faq").replaceWith("<td class='boxed' id='faq'><img src='static/images/buttons/faqhover.png' /></td>");
               };
               
               if (string == "sponsors") {
               $("#myTable #sponsors").replaceWith("<td class='boxed' id='sponsors'><img src='static/images/buttons/sponsorshover.png' /></td>");
               };
               
               if (string == "houses") {
               $("#myTable #houses").replaceWith("<td class='boxed' id='houses'><img src='static/images/buttons/houseshover.png' /></td>");
               };
               
               if (string == "register") {
               $("#myTable #register").replaceWith("<td class='boxed' id='register'><img src='static/images/buttons/registerhover.png' /></td>");
               };
               
               });

//$(document).ajaxStart(function() {
//                      alert("Ajax started");
//                      });

$(document).ready( function() {
    $("#hidden1").hide();
    $("#hidden2").hide();
    $("#hidden3").hide();
    $("#hidden4").hide();
    $(".exit").hide();
                  });

$(document).on("click", ".box1", function() {
               $(".box2").hide();
               $(".box3").hide();
               $(".box4").hide();
               $("#hidden1").show();
               $(".exit").show();
               $(".box1").animate({width: "964px"});
               $(".exit").click(function() {
                                $(".box1").css({width: ""});
                                $(".box2").show();
                                $(".box3").show();
                                $(".box4").show();
                                $("#hidden1").hide();
                                $(".exit").hide();
                                });
               });

$(document).on("click", ".box2", function() {
               $(".box1").hide();
               $(".box3").hide();
               $(".box4").hide();
               $("#hidden2").show();
               $(".exit").show();
               $(".box2").animate({width: "964px"});
               $(".exit").click(function() {
                                $( ".box2" ).css({width: ""});
                                $(".box1").show();
                                $(".box3").show();
                                $(".box4").show();
                                $("#hidden2").hide();
                                $(".exit").hide();
                                });
               });

$(document).on("click", ".box3", function() {
               $(".box1").hide();
               $(".box2").hide();
               $(".box4").hide();
               $("#hidden3").show();
               $(".exit").show();
               $(".box3").animate({width: "964px"});
               $(".exit").click(function() {
                                $( ".box3" ).css({width: ""});
                                $(".box1").show();
                                $(".box2").show();
                                $(".box4").show();
                                $("#hidden3").hide();
                                $(".exit").hide();
                                });
               });

$(document).on("click", ".box4", function() {
               $(".box1").hide();
               $(".box2").hide();
               $(".box3").hide();
               $("#hidden4").show();
               $(".exit").show();
               $(".box4").animate({width: "964px"});
               $(".exit").click(function() {
                                $( ".box4" ).css({width: ""});
                                $(".box1").show();
                                $(".box2").show();
                                $(".box3").show();
                                $("#hidden4").hide();
                                $(".exit").hide();
                                });
               });




$(document).ready(function() {
                  $(document).on("click", ".housetitle", function() {
                                 
                                 var iD = $(this).attr("id");
                                 $(".hiddenHouse").animate({"height": "-=379px"}, 700, function(){
                                                           $.ajax({
                                                                  type: "POST",
                                                                  url: "/houseRetrieve/" + iD + "/",
                                                                  success: function(data) {
                                                                  $("#loadHouse").replaceWith(data);
                                                                  
                                                                  }
                                                                  });
                                                           });
                                 
                                 
                                 });
                  $(document).ajaxStop(function() {
                                       $(".hiddenHouse").css({"height": "0px"}).delay('900').css({"background-color": "rgb(0, 0, 0)"}).animate({"height": "+=379px"}, 700);
                                       
                                       });
                  
                  });

$(document).ready(function() {
                  $(".fadein img").css({"display": "none"});
                                      setInterval(function(){
                                                  $('.fadein :first-child').fadeOut("slow").next('img').fadeIn("slow").end().appendTo('.fadein');}, 11000);
                                      });

$(document).ready(function() {
                  $(".fadein2 img").css({"display": "none"});
                  setInterval(function(){
                              $('.fadein2 :first-child').fadeOut("slow").next('img').fadeIn("slow").end().appendTo('.fadein2');}, 11000);
                  });

$(document).ready(function() {
                  $(".fadein3 img").css({"display": "none"});
                  setInterval(function(){
                              $('.fadein3 :first-child').fadeOut("slow").next('img').fadeIn("slow").end().appendTo('.fadein3');}, 11000);
                  });
