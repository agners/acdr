/*
 * Asterisk CDR specific javascript
 */



$(document).ready(function() {
	var oTable = $('#cdrentries').dataTable( {
		"bProcessing": true,
		"bServerSide": true,
		"sAjaxSource": "/entries.json",
		"aaSorting": [],
		"aoColumns": [
			{ "mDataProp": "AcctId", "bVisible": false },
			{ "mDataProp": "src", "sWidth": "120px" },
			{ "mDataProp": "dst", "sWidth": "120px" },
			{ "mDataProp": "disposition", "sWidth": "60px",
				"fnRender": function ( oObj ) {
					if(oObj.aData.disposition == 8)
						return '<img src="images/answered.png" alt="Answered" title="Answered" />';
					else if(oObj.aData.disposition == 4)
						return '<img src="images/noanswer.png" alt="No answer" title="No answer" />';
					else if(oObj.aData.disposition == 2)
						return '<img src="images/busy.png" alt="Busy" title="Busy" />';
					else if(oObj.aData.disposition == 1)
						return "Failed";
					else if(oObj.aData.disposition == 0)
						return "";
					else
						return "Unknown: " + oObj.aData.disposition;
				} },
			{ "mDataProp": "answer", "sWidth": "130px" },
			{ "mDataProp": "end", "sWidth": "130px" },
			{ "mDataProp": "duration", "sWidth": "80px", "sType": "numeric", 
				"fnRender": function ( oObj ) {
					var dur = oObj.aData.duration;
					var min = (dur / 60).toFixed();
					if(min>0)
						return (dur / 60).toFixed() + "min, " + (dur % 60) + "s";
					else
						return (dur % 60) + "s";
				} },
			{ "mDataProp": "detail", "sWidth": "80px", 
				"fnRender": function ( oObj ) {
					return "<a onclick=\"showDetail(" + oObj.aData.AcctId + ");\">Detail</a>";
				} }
		],
		"fnServerData": function ( sSource, aoData, fnCallback ) {
			$.ajax( {
				"dataType": 'json', 
				"type": "POST", 
				"url": sSource, 
				"data": aoData, 
				"success": fnCallback
			} );
		}
	} );
	$("#cdrentries tfoot input").keyup( function () {
		/* Filter on the column (the index) of this element */
		oTable.fnFilter( this.value, $("tfoot th").index(this.parentNode) );
	} );
	$("#cdrentries tfoot select").change( function () {
		/* Filter on the column (the index) of this element */
		oTable.fnFilter( this.value, $("tfoot th").index(this.parentNode) );
	} );
/*
	$("#cdrentries tbody").click( function(event) {
		$(oTable.fnSettings().aoData).each(function (){
			$(this.nTr).removeClass('row_selected');
		});
		$(event.target.parentNode).addClass('row_selected');
	} );
*/
} );

function showDetail(id)
{
	alert(id);
};
