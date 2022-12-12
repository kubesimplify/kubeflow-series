import kfp
import kfp.dsl as dsl


@dsl.pipeline(name="cointoss", description="Example Pipeline.")
def random_coin_toss():
    random_step = kfp.components.load_component_from_text("""
    name: Flip Coin
    description: Example Pipeline.

    inputs:
    - {name: text, type: String}

    outputs:
    - {name: data, type: Data}

    implementation:
      container:
        image: python:alpine3.7
        command:
        - sh
        - -c
        - |
          python -c \"import random; result = 'heads' if random.randint(0,1) == 0
          else 'tails'; print(result)\" | tee /tmp/output
""")
