import os

IMAGE = "C:\\Work\\Houdini\\OTL_TEST\\Cam2.exr"
OUTPUT = "C:\\Work\\Houdini\\OTL_TEST\\Cam2_denoise.exr"
ALBEDO = "lpe_diffuse_reflection_albedo"
NORMAL = "world_normal"
FRAME_START = 0
FRAME_END = 0
FRAME_STEP = 1
STRENGTH = 1

TOOL = '"C:\\\\Program Files\\\\Isotropix\\\\Clarisse 5.0\\\\Clarisse\\\\cdenoise.exe"'
COMMAND = "{tool} {image} {start}:{end}%{step} -albedo {albedo} -world_normal {world_normal} -strength {strength} -output {output}"

def run():
    cmd = (COMMAND.format(
        tool=TOOL,
        image=IMAGE,
        start=FRAME_START,
        end=FRAME_END,
        step=FRAME_STEP,
        albedo=ALBEDO,
        world_normal=NORMAL,
        strength=STRENGTH,
        output=OUTPUT
    ))
    os.system(cmd)

run()