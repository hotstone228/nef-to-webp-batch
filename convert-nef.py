import rawpy
import imageio.v3 as iio
import sys
import os
import multiprocessing


def convert_nef_to_tiff(nef_path):
    try:
        nef_dir = os.path.dirname(nef_path)
        jpeg_dir = os.path.join(nef_dir, "JPEG")
        os.makedirs(jpeg_dir, exist_ok=True)

        tiff_path = os.path.join(
            jpeg_dir, os.path.splitext(os.path.basename(nef_path))[0] + ".webp"
        )
        if os.path.exists(tiff_path):
            print(f"Exists: {nef_path} -> {tiff_path}")
            return
        with rawpy.imread(nef_path) as raw:
            rgb = raw.postprocess()
        iio.imwrite(tiff_path, rgb)
        print(f"Converted: {nef_path} -> {tiff_path}")
    except Exception as e:
        print(f"Error processing {nef_path}: {e}")


def process_folder(folder_path):
    nef_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".nef")
    ]
    return nef_files


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <image1.nef> <folder1> <image2.nef> ...")
        sys.exit(1)

    all_nef_files = []

    for path in sys.argv[1:]:
        if os.path.isdir(path):
            all_nef_files.extend(process_folder(path))
        elif os.path.isfile(path) and path.lower().endswith(".nef"):
            all_nef_files.append(path)
        else:
            print(f"Skipping non-NEF or invalid file: {path}")

    if not all_nef_files:
        print("No NEF files found to process.")
        sys.exit(1)

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(convert_nef_to_tiff, all_nef_files)
