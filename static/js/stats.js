const ctx = document.getElementById("myChart");

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],

        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      // y: {
      //   beginAtZero: true,
      // },
    },
  },
});

const dash_bar = document.getElementById("dash_bar");
new Chart(dash_bar, {
  type: "bar",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: "#7dd3fc",
        borderWidth: 0.2,
        borderRadius: 0.9,
      },
    ],
  },
  options: {
    scales: {
      // y: {
      //   beginAtZero: true,
      // },
    },
  },
});

const dash_pie = document.getElementById("dash_pie");
new Chart(dash_pie, {
  type: "doughnut",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 0.2,
        borderRadius: 0.9,
      },
    ],
  },
  options: {
    scales: {
      // y: {
      //   beginAtZero: true,
      // },
    },
  },
});
