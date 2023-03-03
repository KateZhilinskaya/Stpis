$('.burger span').on('click', function() {
    $(this).toggleClass('active')
    $(".menu").toggleClass("burger-active")
})

$(".delete").click(function(event) {
    var req = confirm("Вы уверены?");
    if (!req){
        event.preventDefault();
    }
})