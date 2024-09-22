# Specs
# 1. Read content.toml
# 2. Read sections.toml
# 3. Generated latex content based content with mentioned sections

import toml
import argparse

class LatexGen:

    def name(type, value) -> str:
        string = f"\\name{{{value}}}{{}}\n"
        return string.encode("utf-8")

    def contact(type, value) -> str:
        string = f"\\{type}{{{value}}}\n"
        return string.encode("utf-8")
    
    def sectoins_preamble() -> str:
        string = """\
\\begin{document}
\\makecvheader
\\makecvfooter
  {\\today}
  {}
  {}
"""
        return string.encode("utf-8")
    
    def sectoins_postamble() -> str:
        string = """\
\\end{document}
"""
        return string.encode("utf-8")



# Main function which will be called from command line,
# it takes file path for content.toml as argument as -c or --content flag
# and file path for sections.toml as argument with -s or --sections flag,
# and output path for generated latex as argument with -o or --output flag
# This function sould generate a latext file with sections from content.toml
# which are mentioned in sections.toml
def main():
    parser = argparse.ArgumentParser(
        description="Generate LaTeX content from TOML files."
        )

    parser.add_argument(
        # "-c", "--content",
        help="Path to the content.toml file",
        dest="content_filepath",
        )

    parser.add_argument(
        "-s", "--sections",
        required=False,
        default=None,
        help="Path to the sections.toml file",
        dest="sections_filepath",
        )

    parser.add_argument(
        "-o", "--output",
        required=False,
        default="generated.tex",
        help="Path to the output LaTeX file",
        dest="output_filepath",
        )
    
    args = parser.parse_args()

    # Read content from files
    with open(args.content_filepath, "r") as f:
        content = toml.load(f)

    if args.sections_filepath is not None:
        with open(args.sections_filepath, "r") as f:
            sections = toml.load(f)

    # Generate latex content based on the sections mentioned in sections.toml
    # and write it to output file
    with open(args.output_filepath, "w") as f:

        # Personal information
        f.buffer.write(
            LatexGen.name("name", content["personal_info"]["name"])
        )

        f.buffer.write(
            LatexGen.contact("mobile", content["personal_info"]["mobile"])
        )

        f.buffer.write(
            LatexGen.sectoins_preamble()
        )

        # Summary

        # Education

        # Experience
        
        f.buffer.write(
            LatexGen.sectoins_postamble()
        )

if __name__ == "__main__":
    main()