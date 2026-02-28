async function register() {
    const username = document.getElementById("reg_username").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;

    const res = await fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password })
    });

    const data = await res.json();
    alert(data.message || data.error);
}

async function login() {
    const email = document.getElementById("login_email").value;
    const password = document.getElementById("login_password").value;

    const res = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
        window.location.href = "/dashboard";
    } else {
        alert(data.error);
    }
}

async function createTask() {
    const title = document.getElementById("task_title").value;

    const res = await fetch("/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title })
    });

    const data = await res.json();
    alert(data.message || data.error);

    loadTasks();
}

async function loadTasks() {
    const res = await fetch("/tasks");
    const tasks = await res.json();

    const list = document.getElementById("task_list");
    list.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerText = task.title;
        list.appendChild(li);
    });
}

async function logout() {
    await fetch("/logout", { method: "POST" });
    window.location.href = "/";
}

if (window.location.pathname === "/dashboard") {
    loadTasks();
}
