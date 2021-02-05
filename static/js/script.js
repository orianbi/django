$(function() {

	
	$('.tombolTambahData').on('click', function() {
		$('#formModalLabel').html('Tambah Data Mahasiswa');
		$('.modal-footer button[type=submit]').html('Tambah Data');
		$('#nama').val('');
        $('#nrp').val('');
        $('#email').val('');
        $('#jurusan').val('');
        $('#id').val('');
	});



$('.tampilModalUbah').on('click', function() {
	
	$('#formModalLabel').html('Ubah Data Mahasiswa');
	$('.modal-footer button[type=submit]').html('Ubah Data');

	
	var id = $(this).data('id');
	
	$.ajax({

		 url: 'http://localhost/phpmvc/public/mahasiswa/getubah',
		 data: {id : id},
		 method: 'post',
		 dataType: 'json',
		 success: function(data){
		 	console.log(data);
		 	$('#nama').val(data.nama);
		 	$('#nrp').val(data.nrp);
		 	
		 }


	});
	

	});


});