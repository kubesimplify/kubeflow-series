import kfp
import kfp.dsl as dsl


@dsl.pipeline(name="cointoss", description="Example Pipeline.")
def random_coin_toss():
    random_step = dsl.ContainerOp(
        name="Flip coin",
        image="python:alpine3.7",
        command=["sh", "-c"],
        arguments=[
            "python -c \"import random; result = 'heads' if random.randint(0,1) == 0 "
            "else 'tails'; print(result)\" | tee /tmp/output"
        ],
        file_outputs={"output": "/tmp/output"},
    )
