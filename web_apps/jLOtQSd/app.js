$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/apps/RUNNING'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

$.getJSON(getWebAppBackendUrl('/first_api_call'), function(data) {
    console.log('Received data from backend', data)
    const output = $('<pre />').text('Backend reply: ' + JSON.stringify(data));
    $('body').append(output)
});
