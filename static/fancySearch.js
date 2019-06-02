console.log('Page loaded');
var table = $('#rulingsTableMaster').DataTable( {
    select: {
        style: 'single'
    }
} );

table.on( 'select', function ( e, dt, type, indexes ) {
    if ( type === 'row' ) {
      var data = table.rows( indexes ).data()[0];
      console.log(data);
      var ruling_id = data[0];
      window.location.href = '/ruling/' + ruling_id;
    }
} );
