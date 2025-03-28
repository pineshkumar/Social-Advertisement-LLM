from fastapi import FastAPI
app = FastAPI()
@app.post('/generate_ad')
def generate_ad(product: str, platform: str):
    return {'ad': f'Best {product} for {platform}!'}