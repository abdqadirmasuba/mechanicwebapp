

const ctx = document.getElementById('myChart');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: 'Total invoices',
            data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById('doughnut');
new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Procurement', 'Accounts Payable', 'Finanace Manager', 'Tresuary', 'approvers'],
        datasets: [{
            label: 'Desk Invoices',
            data: [2, 4, 0, 2, 5],
            borderWidth: 1
        }]
    }
});