
// attaching eft numbers to invoices.

$(document).ready(function() {
    // Add change event listener to checkboxes
    $('input[type="checkbox"]').change(updateAddEFTVisibility);

    // Function to update the visibility of the "Add EFT" button
    function updateAddEFTVisibility() {
        const checkedCheckboxes = $('input[type="checkbox"]:checked');
        const addEFTContainer = $('#add-eft-container');

        // Show or hide the "Add EFT" button based on the number of checked checkboxes
        if (checkedCheckboxes.length > 1) {
            addEFTContainer.show();
        } else {
            addEFTContainer.hide();
        }
    }
});