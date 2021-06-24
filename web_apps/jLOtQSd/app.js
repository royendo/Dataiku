$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

