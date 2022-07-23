const id_store = document.getElementById('id_store');
const id_target_people = document.getElementById('id_target_people');
const id_target_time = document.getElementById('id_target_time');
const id_target_money = document.getElementById('id_target_money');
const id_receive_place = document.getElementById('id_receive_place');
const id_chat_room = document.getElementById('id_chat_room');

id_store.placeholder = "상호";
id_target_people.placeholder = "펀딩 희망 인원";
id_target_time.placeholder = "완료 시간";
id_target_money.placeholder = "펀딩 필요 금액";
id_receive_place.placeholder = "배송 희망 위치";
id_chat_room.placeholder = "오픈채팅방 링크";

function checkBoxClick(target) {
    let targetInput;
    
    if (target == "target_people") {
        targetInput = document.getElementById('id_target_people');
        const chk = document.querySelector("input[name=target_people_checkbox]").checked;

        if (chk) {
            targetInput.value = "무관";
            targetInput.setAttribute("disabled", "true");
        } else {
            targetInput.value = "";
            targetInput.removeAttribute("disabled");
        }
    } else if (target == "target_money") {
        targetInput = document.getElementById('id_target_money');
        const chk = document.querySelector("input[name=target_money_checkbox]").checked;

        if (chk) {
            targetInput.value = "무관";
            targetInput.setAttribute("disabled", "true");
        } else {
            targetInput.value = "";
            targetInput.removeAttribute("disabled");
        }
    }
}