// Idk why this is not working, I'm checking it btw

const btndelete = document.querySelectorAll('.btn-delete')

if (btndelete) {
    const btndeleteArray = Array.from(btndelete);
    btndeleteArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete it?')) {
                e.preventDefault();
            }
        });
    });
}
