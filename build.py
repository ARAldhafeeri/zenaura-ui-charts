from zenaura.server import ZenauraServer
from public.main import my_app_layout

ZenauraServer.hydrate_app_layout(my_app_layout, scripts=[
        '<link rel="stylesheet" href="public/gigavolt.min.css">',
        '<link rel="stylesheet" href="public/output.css">',
        '<script src="public/highlight.min.js"></script>',  
        '<script src="public/python.min.js"></script>',
        '<script>hljs.highlightAll();</script>',
        """
        <script>
            const ws = new WebSocket("ws://localhost:5000/refresh");
            ws.onmessage = () => {
            console.log("Reloading...");
            location.reload();
            };
        </script>
        """,
        """
        <script>
        window.addEventListener('message', (e) => {
        let data = e.data
        console.log("message", data)
        if (data === 'light-theme') {
            document.documentElement.classList.remove('dark');

        } else {
            document.documentElement.classList.add('dark');

        }
        })
        </script>
        """,
                """    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>"""

])