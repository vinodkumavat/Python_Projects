import patoolib


def zipConvert():
    # (namebof file.extension to convert, (actual file that need to be converted, 2nd file to be converted) )
    # 1st and 2nd file will be converted into zip
    patoolib.create_archive("test.zip", ("instruction.txt", "ttp.txt"))
    print("File zipped successfully....")


def unZip():
    # ("name of zip file to extract", outdir="location to store extracted file")
    patoolib.extract_archive("test.zip", outdir="extract")
    print("File un-zipped successfully....")
