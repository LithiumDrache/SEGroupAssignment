document.addEventListener('DOMContentLoaded', () => {    
    // List of IDs for the response lists
    const lists = ['tops', 'pants', 'footwear', 'accessories'];
    // Add click event listeners to all items
       document.querySelectorAll('.item-image').forEach((item, index) => {
        item.addEventListener('click', () => {
            // Remove 'clicked' class from all items
            document.querySelectorAll('.item-image').forEach((i) => i.classList.remove('clicked'));
            
            // Add 'clicked' class to the clicked item
            item.classList.add('clicked');

            // Hide all response lists
            document.querySelectorAll('.response').forEach((list) => {
                list.classList.remove('active'); // Use active class for visibility
                list.style.display = 'none'; // Hide the list
            });

            // Show the respective list based on the clicked image
            const selectedListId = lists[index];
            const selectedList = document.getElementById(selectedListId);
            if (selectedList) {
                selectedList.style.display = 'flex'; // Show the list
                selectedList.classList.add('active'); // Add active class
            }

            // Adjust the height of the container dynamically
            const responseContainer = document.getElementById('generated-response');
            responseContainer.style.height = `${selectedList.offsetHeight}px`; // Fit to the active list
        });
    });

    // Initial state: show "tops" list
    const initialList = document.getElementById('tops');
    initialList.style.display = 'flex'; // Show the default list
    initialList.classList.add('active'); // Add active class
    document.getElementById('generated-response').style.height = `${initialList.offsetHeight}px`; // Set initial height
    
});