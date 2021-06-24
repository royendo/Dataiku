$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/apps/'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

