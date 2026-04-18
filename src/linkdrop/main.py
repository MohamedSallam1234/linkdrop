from fastapi import FastAPI


def create_app() -> FastAPI:
    # The kwargs below aren't mandatory, but they control how /docs
    # and /openapi.json appear. It pays to set them early — your future
    # self (and API consumers) will thank you.
    app = FastAPI(
        title="LinkDrop",
        description="A personal URL shortener with tags and analytics.",
        version="0.1.0",
        contact={"name": "Mohamed Sallam", "email": "Sallamm733@gmail.com"},
        license_info={"name": "MIT"},
    )

    @app.get("/health", tags=["meta"])
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
