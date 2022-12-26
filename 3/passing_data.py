from typing import NamedTuple


def multiply(a: float, b: float) -> NamedTuple("MultiplyOutput", [("result", float)]):
    from collections import namedtuple

    output = namedtuple("MultiplyOutput", ["result"])
    return output(a * b)


def add(a: float, b: float) -> float:
    return a + b


import kfp

multiply_op = kfp.components.create_component_from_func(
    multiply, output_component_file="multiply_component.yaml"
)

add_op = kfp.components.create_component_from_func(
    add, output_component_file="multiply_component.yaml"
)

import kfp.dsl as dsl


@dsl.pipeline(name="Multiply and Add", description="An example pipeline.")
def multiply_add_pipeline(a="2", b="5", c="3"):
    multiply_task = multiply_op(a, b)

    # Calculate (a * b) + c
    add_task = add_op(multiply_task.outputs["result"], c)
