$.get(getWebAppBackendUrl('/cluster/apps/test'), function(data) {
    console.log(data)
})

$.get(getWebAppBackendUrl('/cluster/apps/RUNNING'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

