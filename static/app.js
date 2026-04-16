const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe.user;
let user_id = user ? user.id : Math.floor(Math.random()*100000);

function loadBalance() {
    fetch("/balance", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({user_id})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("balance").innerText =
            "Balance: " + data.balance;
    });
}

function mine() {
    fetch("/mine", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({user_id})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("balance").innerText =
            "Balance: " + data.balance;
    });
}

loadBalance();
