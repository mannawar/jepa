import torch

ckpt_path = "/Users/mannawarhussain/Desktop/Mannawar/iitp/outputs/vid-output/latest.pt"

ckpt = torch.load(ckpt_path, map_location="cpu")

print("\n=== TOP-LEVEL CHECKPOINT KEYS ===")
for k in ckpt.keys():
    print(" -", k)

# Inspect encoder
if "encoder" in ckpt:
    print("\n=== ENCODER PARAMETER SHAPES ===")
    for k, v in ckpt["encoder"].items():
        print(f"{k}: {tuple(v.shape)}")

# Inspect predictor
if "predictor" in ckpt:
    print("\n\n=== PREDICTOR PARAMETER SHAPES ===")
    for k, v in ckpt["predictor"].items():
        print(f"{k}: {tuple(v.shape)}")

# Inspect target_encoder (EMA teacher)
if "target_encoder" in ckpt:
    print("\n\n=== EMA TEACHER PARAMETER SHAPES ===")
    for k, v in ckpt["target_encoder"].items():
        print(f"{k}: {tuple(v.shape)}")

print("\n=== DONE ===")