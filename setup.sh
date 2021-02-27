mkdir -p ~/.streamlit/
echo "[general]
email = \"vinit.gupta@tmf.co.in\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
