const usernameField = document.querySelector("#username");
const errorBox = document.querySelector("#error_box");

usernameField.addEventListener("keyup", (e) => {
  const usernameValue = e.target.value;

  //   make api call to server
  if (usernameValue.length > 0) {
    fetch("/valiadte_username/", { body: JSON.stringify({ username: usernameValue }), method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        if (data.username_error) {
          errorBox.innerHTML = `<p class=" text-xs text-red-600 mt-2" id="username-error">${data.username_error}</p>`;
        } else {
          errorBox.innerHTML =
            '<p class="hidden text-xs text-red-600 mt-2" id="username-error">Please include a valid email address so we can get back to you</p>';
        }
      });
  }
});
