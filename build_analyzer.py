class BuildAnalyzer:
    def __init__(self) -> None:
        pass

    def analyze_build(self, build_results: dict, output_file: str = "build_analysis.txt") -> str:
        # Analyze the build results and write a summary to a text file
        with open(output_file, "w") as file:
            file.write("Build Analysis Summary\n")
            file.write("======================\n\n")

            for key, value in build_results.items():
                if isinstance(value, dict):
                    file.write(f"{key}:\n")
                    for subkey, subvalue in value.items():
                        file.write(f"  {subkey}: {subvalue}\n")
                else:
                    file.write(f"{key}: {value}\n")

            file.write("\nEnd of Build Analysis Summary\n")

        return f"Build analysis summary has been written to {output_file}"
