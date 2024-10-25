<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Haven</title>
    <link rel="stylesheet" href="styles.css">  <!-- Link to an external CSS file -->
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        section {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .chat-section {
            padding-top: 10px;
            border-top: 1px solid #ccc;
        }
        .chat-section input[type="text"] {
            padding: 10px;
            width: 80%;
            margin-right: 10px;
        }
        .chat-section button {
            padding: 10px 20px;
            background-color: #333;
            color: white;
            border: none;
        }
        footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to AI Haven</h1>
        <p>Your gateway to exploring the power of AI</p>
    </header>

    <section>
        <h2>About AI Haven</h2>
        <p>AI Haven is a space dedicated to learning and building artificial intelligence projects. From chatbots to advanced AI, we’re exploring every aspect of the digital world.</p>
    </section>

    <section class="chat-section">
        <h2>Chat with the AI</h2>
        <p>Type something to start chatting with our AI!</p>
        <form id="chat-form">
            <input type="text" id="user-input" placeholder="Type your message here...">
            <button type="submit">Send</button>
        </form>
        <div id="chatbot-response"></div>
    </section>

    <footer>
        <p>AI Haven © 2024</p>
    </footer>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $("#chat-form").on("submit", function(e) {
                e.preventDefault();
                var userInput = $("#user-input").val();

                $.ajax({
                    url: "/get_response",
                    type: "POST",
                    data: { user_input: userInput },
                    success: function(response) {
                        $("#chatbot-response").text(response.response);
                    }
                });
            });
        });
    </script>
</body>
</html>
