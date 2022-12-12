import kfp
import kfp.dsl as dsl


@kfp.components.create_component_from_func
def write_to_volume():
    with open("/mnt/file.txt", "w") as file:
        file.write("Hello world")


@dsl.pipeline(
    name="volumeop-basic",
    description="A Basic Example on VolumeOp Usage."
)
def volumeop_basic(size: str="1Gi"):
    vop = dsl.VolumeOp(
        name="create-pvc",
        resource_name="my-pvc",
        modes=dsl.VOLUME_MODE_RWO,
        size=size
    )

    write_to_volume().add_pvolumes({"/mnt": vop.volume})
