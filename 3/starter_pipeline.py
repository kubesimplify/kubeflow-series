def multiply(a: float, b: float) -> float:
    return a * b

import kfp

multiply_op = kfp.components.create_component_from_func(
    multiply, output_component_file="multiply_component.yaml"
)

import kfp.dsl as dsl
@dsl.pipeline(name="Multiply", description="An example pipeline.")
def multiply_pipeline(
    a="1",
    b="5",
):
    multiply_task = multiply_op(a, b)

arguments = {"a": "2", "b": "3"}