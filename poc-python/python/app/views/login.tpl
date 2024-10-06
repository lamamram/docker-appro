<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>{{ title }}</title>

  <!-- Bootstrap core CSS -->
  <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="/static/css/simple-sidebar.css" rel="stylesheet">

</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-3">
            </div>
            <div class="col-6">
                <form method=post action="#">
                    <div class="form-group">
                        <label for="username">User Name</label>
                        <input type="text" class="form-control" id="username" name="username" aria-describedby="userHelp" placeholder="Enter user">
                    </div>
                    <div class="form-group">
                        <label for="passwd">Password</label>
                        <input type="password" class="form-control" id="passwd" name="passwd" placeholder="Password">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
            <div class="col-3">
            </div>
        </div>
    </div>
</body>
</html>
