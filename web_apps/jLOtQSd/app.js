$.get(getWebAppBackendUrl('/test')
     {console.log(data)}
     )


$.get(getWebAppBackendUrl('/cluster/apps/RUNNING'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})
