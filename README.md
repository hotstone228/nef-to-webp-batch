# RAW to WebP Converter

A lightweight Python utility to **convert Nikon NEF (RAW) images to compressed WebP** using `rawpy` and `imageio`. It supports both individual files and full folder batch processing with multiprocessing.

---

## ⚙️ Features

- 🎞️ Converts `.nef` (RAW) files to `.webp`
- 📁 Accepts files and folders as input (recursively collects NEFs from folders)
- ⚡ Fast parallel processing with `multiprocessing`
- ♻️ Skips files that are already converted

---

## 📦 Requirements

- Python 3.8+
- [rawpy](https://pypi.org/project/rawpy/)
- [imageio](https://pypi.org/project/imageio/)

Install via pip:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python convert_nef.py image1.nef folder/ image2.nef
```

- Pass any number of `.nef` files or folders.
- Converted images are saved in a `JPEG/` subfolder next to the original file.
- Output format is `.webp`.

### Example:

```bash
python convert_nef.py ./raw_photos/ vacation.nef
```

---

## 📂 Output Structure

For any input file or folder, a `JPEG/` directory will be created in the same location:

```text
raw_photos/
├── photo1.nef
├── photo2.nef
└── JPEG/
    ├── photo1.webp
    └── photo2.webp
```

---

## 🧠 Notes

- Conversion uses `rawpy.postprocess()` with default settings.
- Existing `.webp` files are **not overwritten**.
- Adjust `multiprocessing.Pool(processes=4)` to fit your CPU.

---

## 📄 License

MIT License — free to use, adapt, and redistribute.

---

## 🙌 Contributions

PRs welcome! Feel free to suggest:

- Additional RAW format support (e.g., CR2, ARW)
- Custom postprocessing parameters
- Output format toggle (TIFF, JPEG, etc.)
