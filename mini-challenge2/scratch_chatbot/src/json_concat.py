import json
import os


def concat_json_files(file1, file2, output_file):
    try:
        # Read data from the first JSON file
        with open(file1, "r") as f1:
            data1 = json.load(f1)

        # Read data from the second JSON file
        with open(file2, "r") as f2:
            data2 = json.load(f2)

        # merge data1 and 2 with extend
        data1["intents"].extend(data2["intents"])

        # save merged data to output file
        with open(output_file, "w") as f_out:
            json.dump(data1, f_out, indent=4)

        print(f"JSON files concatenated successfully and saved to '{merged_data}'!")

    except FileNotFoundError:
        print("One or more input files not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
concat_json_files("file1.json", "file2.json", "data/output.json")
