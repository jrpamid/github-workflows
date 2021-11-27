def diwali_wishes(request):
    return """
    <!doctype html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>Virtual Fireworks</title>
    <style>
    html,* { margin:0; padding:0}
    body { width:100%; height:100%;}
    .display { margin:0 auto; width:100%; height:100%;}
    h1 { margin:150px auto 30px auto; text-align:center; font-family:'Roboto';}
    </style>
    </head>
    <body style='background-color:#060C59;'>
    <h1 style='padding-top:100px;font-size:48px;color:white;text-align:center;'>Happy Diwali 2021 ...<br></h1>
    <div class='display'>
    </div>
    <script src='https://code.jquery.com/jquery-3.1.1.min.js'></script>
    <script src='https://www.jqueryscript.net/demo/Realistic-Fireworks-Animations-Using-jQuery-And-Canvas-fireworks-js/jquery.fireworks.js'></script>
    <script>
    $('.display').fireworks({ sound: true, opacity: 0.9, width: '100%', height: '100%' });
    </script>
    </body>
    </html>
    """