---T5-base exposed through fast API---

How to run?
Build a docker image

Porformance concerns: 
- Image is composed with CPU versions of torch and related libraries for maximal compatibility. If you wish to modify that, modify download links for torch, torchvision and torchaudio in pyproject.toml file.

T5-base minimum inference hardware requirements:
