python3 -m app.main --debugmode True --devices cpu \
        --fname /Users/mannawarhussain/Desktop/Mannawar/iitp/code/jepa2/configs/pretrain/vitl16.yaml

python3 -m app.main \
    --fname /Users/mannawarhussain/Desktop/Mannawar/iitp/code/jepa2/configs/myconfigs/ucf101_raw_avi.yaml \
    --devices cpu \
    --debugmode True


python3 -m app.main \
    --mode extract_embeddings \
    --devices cpu \
    --fname /Users/mannawarhussain/Desktop/Mannawar/iitp/code/jepa2/configs/ucf101_raw_avi.yaml \
    --ckpt /Users/mannawarhussain/Desktop/Mannawar/iitp/outputs/vid-output/latest.pt \
    --out_dir /Users/mannawarhussain/Desktop/Mannawar/iitp/outputs/ufc-output
