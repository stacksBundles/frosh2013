
$(document).on("submit", "#lookup-house", function(e) {
                   e.preventDefault();
                   var data = $(this).serialize()
                   $.ajax({
                          type: "POST",
                          data: data,
                          url: "/houseLookup/",
                          success: function(data){
                          $(".loaded").replaceWith(data);
                          }
                          });
                   
                   });

$(document).on("submit", "#vassal-edit", function(e) {
               e.preventDefault();
               var data = $(this).serialize();
               var iD = $(this).attr("action");
               $.ajax({
                      type: "POST",
                      data: data,
                      url: "/vassalEdit/" + iD + "/",
                      success: function(data){
                      $(".loaded").replaceWith(data);
                      }
                      });
               
               });

$(document).on("click", "#exit", function(e) {
               e.preventDefault();
               window.location.replace('http://localhost:8000/logout/');
               });

$(document).on("click", ".loaded a", function(e) {
               e.preventDefault();
               var data = {};
               data["id"] = $(this).attr("id");
               $.ajax({
                      type: "POST",
                      data: data,
                      url: "/vassalLookup/",
                      success: function(data) {
                      $(".vassal").replaceWith(data);
                      }
                      });
               });

$(document).on("click", ".change-photo", function(e) {
               e.preventDefault();
               var iD = $(this).attr("id");

               $.ajax({
                      type: "POST",
                      url: "/imageForm/" + iD + "/",
                      success: function(data) {
                      $(".vassal").replaceWith(data);
                      alert("form ready");
//                      var options = {
//                      target:        '#output1',   // target element(s) to be updated with server response
//                      beforeSubmit:  showRequest,  // pre-submit callback
//                      success: showResponse,
//                      };
//                      
//                      $("#submit-photo").ajaxForm(options);
//                      }
                      }
               });
               });

$("#submit-photo").ready(function() {
                         
                  
                  });
                  
//
//$(document).on("submit", "#submit-photo", function(e) {
//               e.preventDefault();
//               alert("prevent default passed");
//               return false;
//                  });


//function showRequest(formData, jqForm, options) {
//    
//    var queryString = $.param(formData);
//    
//    
//    
//    alert("show request launched");
//    
//    alert('About to submit: \n\n' + queryString);
//    
//    $("#output1").replaceWith("<div id='output1'>" + queryString + "</div>");
//    
//    return true;
//  };
//
//function showResponse(responseText, statusText, xhr, $form)  {
//    alert('status: ' + statusText + '\n\nresponseText: \n' + responseText +
//          '\n\nThe output div should have already been updated with the responseText.');
//}

$(document).ajaxStart(function() {
                      alert("Ajax started");
                      });