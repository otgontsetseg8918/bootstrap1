let body = document.querySelector("body");

let popupUserAgreement = document.querySelector(".popup_user_agreement");
let popupUserAgreementBody = popupUserAgreement.querySelector(".popup_content .popup_body");
let popupUserAgreementButtonClose = popupUserAgreement.querySelector(".popup_close");

let popupUserAgreementButtonOpen = document.querySelector("#button_open_agreement");

let functionCloseCheck = true;

popupUserAgreementButtonOpen.addEventListener("click", (e) => {
    e.preventDefault();
    body.classList.add("lock");
    popupUserAgreement.classList.remove("none");
    popupUserAgreement.classList.add("_active");

    if(functionCloseCheck){
        popupPostBookClose();
    }
});


function popupPostBookClose(){
    functionCloseCheck = false;

    popupUserAgreementButtonClose.addEventListener("click", () => {
        popupUserAgreement.classList.remove("_active");
        body.classList.remove("lock");
        popupUserAgreement.classList.add("none");
    });

    document.addEventListener("click", (e) => {
        if(!popupUserAgreementBody.contains(e.target) && popupUserAgreement.contains(e.target)){
            popupUserAgreement.classList.remove("_active");
            body.classList.remove("lock");
            popupUserAgreement.classList.add("none");
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.which === 27){
            popupUserAgreement.classList.remove("_active");
            body.classList.remove("lock");
            popupUserAgreement.classList.add("none");
        }
    });
}