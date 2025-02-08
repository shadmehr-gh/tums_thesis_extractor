import lib_tums_ac_ir
import pdf_creator


def main():
    # Version 3
    biblioId, multimediaId, page_count = lib_tums_ac_ir.downloader()
    pdf_creator.pdf_creator(biblioId, multimediaId, page_count)


if __name__ == '__main__':
    main()
