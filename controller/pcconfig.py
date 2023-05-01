import pynecone as pc

class ControllerConfig(pc.Config):
    pass

config = ControllerConfig(
    app_name="controller",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
