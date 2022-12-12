import kfp
from kfp import dsl
from kfp.components import func_to_container_op, InputPath, OutputPath


@func_to_container_op
def get_random_int_op(minimum: int, maximum: int) -> int:
    """Generate a random number between minimum and maximum (inclusive)."""
    import random

    result = random.randint(minimum, maximum)
    print(result)
    return result


@func_to_container_op
def process_small_op(data: int):
    """Process small numbers."""
    print("Processing small result", data)
    return


@func_to_container_op
def process_medium_op(data: int):
    """Process medium numbers."""
    print("Processing medium result", data)
    return


@func_to_container_op
def process_large_op(data: int):
    """Process large numbers."""
    print("Processing large result", data)
    return


@dsl.pipeline(
    name="Conditional execution pipeline",
    description="Shows how to use dsl.Condition().",
)
def conditional_pipeline():
    number = get_random_int_op(0, 100).output
    with dsl.Condition(number < 10):
        process_small_op(number)
    with dsl.Condition(number > 10 and number < 50):
        process_medium_op(number)
    with dsl.Condition(number > 50):
        process_large_op(number)
