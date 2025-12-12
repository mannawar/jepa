import torch
from omegaconf import OmegaConf
from app.vjepa.utils import init_video_model
from app.vjepa.transforms import VideoTransform

def load_encoder(cfg_path):
    cfg = OmegaConf.load(cfg_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Initialize the encoder
    encoder, _ = init_video_model(
        device,
        model_name=cfg.model.model_name,
        uniform_power=cfg.model.uniform_power,
        use_mask_tokens=False,
        zero_init_mask_tokens=False,
    )

    # Load checkpoint if specified
    if cfg.meta.load_checkpoint and cfg.meta.read_checkpoint:
        checkpoint_path = cfg.meta.read_checkpoint
        checkpoint = torch.load(checkpoint_path, map_location=device)

        # Adjust key depending on how checkpoint is saved
        if "predictor" in checkpoint:
            encoder.load_state_dict(checkpoint["predictor"])
        else:
            encoder.load_state_dict(checkpoint)  # fallback

        print(f"Loaded checkpoint from {checkpoint_path}")

    encoder.eval()
    encoder.to(device)
    return encoder, cfg


def extract_embedding(encoder, video_tensor):
    with torch.no_grad():
        feat = encoder(video_tensor)
    return feat

if __name__ == "__main__":
    cfg_path = "/Users/mannawarhussain/Desktop/Mannawar/iitp/code/jepa2/configs/myconfigs/ucf101_raw_avi.yaml"
    encoder, cfg = load_encoder(cfg_path)

    # Example: load 1 video
    video = torch.randn(1, 3, cfg.data.num_frames, 112, 112)  # dummy video
    embedding = extract_embedding(encoder, video)

    print("Embedding shape:", embedding.shape)
