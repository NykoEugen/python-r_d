const btn = document.getElementById("btn");

// Створюємо кнопку "Додати в друзі"
const addFriendButton = document.createElement("button");
addFriendButton.textContent = "Add friend";
addFriendButton.style.width = "33%";
addFriendButton.style.marginRight = "5px";

// Створюємо каунтер для друзів
const count = document.getElementById("friend-count");
const friendCount = document.createElement("span");
friendCount.style.fontWeight = "bold";

let randomNumber = Math.floor(Math.random() * 100);
friendCount.textContent = `Friends: ${randomNumber}`;

function addFriend() {
    randomNumber++;
    friendCount.textContent = `Friends: ${randomNumber}`;

    addFriendButton.disabled = true;
    addFriendButton.textContent = "Pending confirmation";
}

addFriendButton.addEventListener("click", addFriend);

// Створюємо кнопку "Написати повідомлення"
const sendMessageButton = document.createElement("button");
sendMessageButton.textContent = "Send message";
sendMessageButton.style.width = "33%";
sendMessageButton.style.marginRight = "5px";

// Робиму активність на кнопку надіслати повідомлення
let isColorChanged = false;
sendMessageButton.addEventListener("click", function () {
    if (isColorChanged) {
        sendMessageButton.style.backgroundColor = "";
    } else {
        sendMessageButton.style.backgroundColor = "#adadad";
    }
    isColorChanged = !isColorChanged
});

// Створюємо кнопку "Запропонувати роботу"
const jobOfferButton = document.createElement("button");
jobOfferButton.textContent = "Job offer";
jobOfferButton.style.width = "33%";
jobOfferButton.style.marginRight = "5px";

// Приховуємо кнопку додати до друзів
jobOfferButton.addEventListener("click", function (){
    if (addFriendButton.style.display === "none") {
        addFriendButton.style.display = "block";
    } else {
        addFriendButton.style.display = "none";
    }
});

// Створюємо кнопку дз
const btnHw = document.getElementById("btn-hw");
const homeWorkBtn = document.createElement("button");
homeWorkBtn.textContent = "Send homework";
homeWorkBtn.style.width = "60%";
homeWorkBtn.style.marginTop = "15px";
const homeWork = document.getElementById("home-work");
const tbody = homeWork.querySelector("tbody");

homeWorkBtn.addEventListener("click", function () {
    const newRow = document.createElement("tr");

    const numTask = document.createElement("td");
    numTask.textContent = "18";
    numTask.style.textAlign = "center";

    const themOfClasses = document.createElement("td");
    themOfClasses.textContent = "Test text";

    const rating = document.createElement("td");
    rating.textContent = "5";
    rating.style.textAlign = "center";

    newRow.appendChild(numTask);
    newRow.appendChild(themOfClasses);
    newRow.appendChild(rating);

    tbody.appendChild(newRow);
});


// Додаємо кнопки до елемента "Btn"
count.appendChild(friendCount);
btn.appendChild(addFriendButton);
btn.appendChild(sendMessageButton);
btn.appendChild(jobOfferButton);
btnHw.appendChild(homeWorkBtn);