import os, argparse
import zipfile


def buildCmdParser():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument(
        "-z",
        "--zippedFile",
        type=str,
        required=True,
        dest="zippedFile",
        help="the zipped file to be unzipped",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        dest="output_dir",
        help="the output directory",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        dest="recursive",
        help="whether to recursively unzip the zipped file",
    )

    return parser


def isZipped(filename):
    [_, ext] = os.path.splitext(filename)

    return ext == ".zip"


def extract(zippedFile, output_dir, recursive, extractedFiles=[]):
    with zipfile.ZipFile(zippedFile, "r") as zObject:
        zObject.extractall(path=output_dir)
        print("Extracted: " + zippedFile)

        if recursive:
            for root, dirs, files in os.walk(output_dir, topdown=True):
                for filename in files:
                    if os.path.join(root, filename) in extractedFiles:
                        continue

                    if isZipped(filename):
                        zippedFile = os.path.join(root, filename)
                        output_dir = root
                        extractedFiles += [zippedFile]

                        extract(zippedFile, output_dir, extractedFiles)


if __name__ == "__main__":
    parser = buildCmdParser()
    args = parser.parse_args()

    zippedFile = os.path.abspath(args.zippedFile)
    output_dir = (
        args.output_dir
        if args.output_dir is not None
        else os.path.abspath(zippedFile).rpartition(".")[0]
    )
    recursive = args.recursive

    extract(zippedFile, output_dir, recursive)
