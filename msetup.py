import mrp
import platform
import os

LOG_PATH = f"/nfs/perception_logs/{platform.node()}"
if os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH, exist_ok=True)



mrp.process(
    name="topic",
    runtime=mrp.Conda(
        dependencies= [
            {"pip": [
                "alephzero",
            ]},
        ],
        run_command=["python3", "main.py"],
    ),
)


if __name__ == "__main__":
    mrp.main()