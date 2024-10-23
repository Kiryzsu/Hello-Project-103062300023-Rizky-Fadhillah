document.addEventListener('DOMContentLoaded', function() {
    const balanceElement = document.getElementById('balance');
    const toggleBalanceButton = document.getElementById('toggleBalance');
    const eyeIcon = document.getElementById('eyeIcon');

    let balanceVisible = true;

    toggleBalanceButton.addEventListener('click', function() {
        if (balanceVisible) {
            balanceElement.textContent = '**********';
            eyeIcon.classList.remove('fa-eye');
            eyeIcon.classList.add('fa-eye-slash');
            toggleBalanceButton.textContent = ' Tampilkan Saldo';
        } else {
            balanceElement.textContent = 'Rp {{ balance }}';
            eyeIcon.classList.remove('fa-eye-slash');
            eyeIcon.classList.add('fa-eye');
            toggleBalanceButton.textContent = ' Sembunyikan Saldo';
        }

        balanceVisible = !balanceVisible;
    });
});
