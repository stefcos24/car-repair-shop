$(function() {
    $(".message").each(function() {
        const level = $(this).data('level');
        const message = $(this).data('message');

        switch (level) {
            case 'success':
                toastr.success(message);
                break;
            case 'info':
                toastr.info(message);
                break;
            case 'error':
                toastr.error(message);
                break;
            case 'warning':
                toastr.warning(message);
                break;
        }
    });
});
