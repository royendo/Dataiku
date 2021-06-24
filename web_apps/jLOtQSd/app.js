$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/apps/RUNNING'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})

 document.getElementsByTagName("base")[0].href = document.location.href;