from os import path
from pathlib import Path
this_file = path.abspath(path.dirname(__file__))
bird_types = [
    this_file / Path("013.Bobolink\Bobolink_0001_9261.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0002_11085.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0007_9246.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0008_9289.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0013_9367.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0014_11055.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0018_9402.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0019_10552.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0020_9194.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0021_10623.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0026_11057.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0027_10569.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0032_10217.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0033_10809.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0035_11117.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0039_9779.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0040_9681.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0043_10607.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0044_9990.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0047_9204.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0048_9988.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0049_9540.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0050_9821.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0052_9423.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0053_10166.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0056_9080.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0057_10051.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0059_10041.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0064_10092.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0065_9375.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0067_11533.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0069_9085.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0070_10624.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0071_9503.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0074_9311.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0076_11093.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0079_10736.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0081_9439.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0092_10026.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0094_9823.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0097_10861.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0099_9314.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0101_9811.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0102_10807.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0104_10273.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0106_9126.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0107_10252.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0109_9869.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0110_9496.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0112_11073.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0114_10627.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0115_9265.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0117_10215.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0119_10430.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0120_10859.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0124_10182.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0126_11458.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0128_9947.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0131_9578.jpg"),
    this_file / Path("013.Bobolink\Bobolink_0133_9618.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0001_14916.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0004_14887.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0008_15195.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0009_15163.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0010_14915.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0014_14824.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0015_14690.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0020_14837.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0021_14686.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0025_15079.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0026_14669.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0027_14895.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0028_14950.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0030_14986.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0031_15018.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0032_14778.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0034_14864.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0035_14920.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0037_15021.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0039_15081.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0040_14923.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0041_15152.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0042_14820.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0045_14954.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0046_14787.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0047_14863.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0048_14844.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0052_14618.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0054_14714.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0055_15043.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0056_15032.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0057_14775.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0059_14749.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0061_15155.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0066_14914.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0067_14672.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0070_14665.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0073_14594.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0074_14854.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0076_14662.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0078_15164.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0080_14893.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0081_14709.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0082_15047.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0084_14815.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0085_14627.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0086_14992.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0087_15096.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0089_14598.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0092_14656.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0093_15030.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0094_11894.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0095_14919.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0097_14617.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0101_14873.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0102_14605.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0105_15017.jpg"),
    this_file / Path("015.Lazuli_Bunting\Lazuli_Bunting_0107_14705.jpg")
]