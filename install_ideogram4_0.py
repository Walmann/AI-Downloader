
from deps.installer import model_info, install_job, install, node_info



# All installers needs to include the above. And have the same structure as bellow.
# If you need to do some custom work to make things work, you can freely add functions. 

install(jobs=install_job(
models=
    [
    model_info("https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_fp8_scaled.safetensors", "models/diffusion_models"),
    model_info("https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_unconditional_fp8_scaled.safetensors", "models/diffusion_models"),
    model_info("https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors", "models/text_encoders"),
    model_info("https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors", "models/text_encoders"),
    model_info("https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors", "models/vae")
    ],
nodes=
    [
        node_info("https://github.com/kijai/ComfyUI-KJNodes", "ComfyUI-KJNodes")
    ]

))

