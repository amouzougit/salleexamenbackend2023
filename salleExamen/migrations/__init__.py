 
{
    "builds": [{
        "src": "gestion_examen/wsgi.py",
        "use": "@ardnt/vercel-python-wsgi",
        "config": { "maxLambdaSize": "15mb" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "gestion_examen/wsgi.py"
        }
    ]
}