$.get(getWebAppBackendUrl('/test'))
$.get(getWebAppBackendUrl('/cluster/apps/RUNNING'), function(data) {
    console.log(data)
    $("#regTitle").html(data)
})



<li><a href="#section1">#section1</a></li>
<li><a href="#section2">#section2</a></li>