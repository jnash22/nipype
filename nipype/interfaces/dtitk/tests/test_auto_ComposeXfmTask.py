# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import ComposeXfmTask


def test_ComposeXfmTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_aff=dict(
            argstr='-aff %s',
            exists=True,
            mandatory=False,
            position=0,
        ),
        in_df=dict(
            argstr='-df %s',
            exists=True,
            mandatory=False,
            position=1,
        ),
        out_file=dict(
            argstr='-out %s',
            exists=True,
            mandatory=False,
            name_source='in_df',
            name_template='%s_comboaff.nii.gz',
            position=2,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = ComposeXfmTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ComposeXfmTask_outputs():
    output_map = dict(out_file=dict(), )
    outputs = ComposeXfmTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
