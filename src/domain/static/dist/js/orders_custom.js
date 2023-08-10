$(function () {
    $("#example1").DataTable({
        "order": [[0, 'desc']],
      "responsive": true, "lengthChange": false, "autoWidth": false,
      "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
    }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
    $('#example2').DataTable({
      "order": [[0, 'desc']],
      "buttons": ["csv", "excel", "pdf", "print"],
      "paging": true,
      "lengthChange": false,
      "searching": true,
      "ordering": true,
      "info": true,
      "autoWidth": false,
      "responsive": true,
    }).buttons().container().appendTo('#example2_wrapper .col-md-6:eq(0)');
  });