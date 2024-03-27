let csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

let body = document.querySelector("body");

let popupSubscription = document.querySelector(".popup_subscription");
let popupSubscriptionBody = popupSubscription.querySelector(".popup_content .popup_body");
let popupSubscriptionClose = popupSubscription.querySelector(".popup_close");

let popupSubscriptionButtonOpen = document.querySelector("#button-subscription");

let subscriptionButtonSend = document.querySelector("#subscription-button-send");

let functionCloseCheck = true;

popupSubscriptionButtonOpen.addEventListener("click", (e) => {
    e.preventDefault();

    body.classList.add("lock");
    body.style.marginRight = "20px";
    popupSubscription.classList.remove("none");
    popupSubscription.classList.add("_active");

    if(functionCloseCheck){
        popupPostBookClose();
    }
});

subscriptionButtonSend.addEventListener("click", (e) => {
    e.preventDefault();

    const email = popupSubscriptionBody.querySelector("#subscription-user-email").value;
    const name = popupSubscriptionBody.querySelector("#subscription-user-name").value;

    $.ajax({
        url: `/subscription/`,
        type: 'post',
        headers: {'X-CSRFToken': csrfToken},
        data: {user_email: email, user_name: name},
        success: function(response){
            popupSubscription.classList.remove("_active");
            body.classList.remove("lock");
            popupSubscription.classList.add("none");

            alert(response.message);
        },
        error: function() {
            console.log("error");
        }
    });
});



function popupPostBookClose(){
    functionCloseCheck = false;

    popupSubscriptionClose.addEventListener("click", () => {
        popupSubscription.classList.remove("_active");
        body.classList.remove("lock");
        popupSubscription.classList.add("none");
    });

    document.addEventListener("click", (e) => {
        if(!popupSubscriptionBody.contains(e.target) && popupSubscription.contains(e.target)){
            popupSubscription.classList.remove("_active");
            body.classList.remove("lock");
            popupSubscription.classList.add("none");
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.which === 27){
            popupSubscription.classList.remove("_active");
            body.classList.remove("lock");
            popupSubscription.classList.add("none");
        }
    });
}