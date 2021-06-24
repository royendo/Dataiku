$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/apps/test'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

