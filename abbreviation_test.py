import re
import pysbd
import os

lang_mapping = {
    'hi': "\u0900-\u097F",
    'te': "\u0C01-\u0C7F"
}


def testHelper(text,lang_code):
    """
    text: Single string of multiple sentences
    return: a list of individual sentences.
    """
    print("Running Test...")
    seg = pysbd.Segmenter(language=lang_code, clean=False)
    return seg.segment(text)


def mask(lang_code, input):
    if lang_code not in os.listdir():
        os.mkdir(lang_code)

    file_name = os.path.split(input)[-1]

    regex_expression = r'(([' + lang_mapping.get(lang_code) + '\u200c\u200b\u200d]){1,}\.){2,}?([' + lang_mapping.get(
        lang_code) + '\u200c\u200b\u200d]|[ \.])'
    # print(regex_expression)

    with open(input, "r", encoding="utf8") as f:
        data = f.read()

    abbreviation = []

    # Finding all abbreviations and storing it in a list
    for match in re.finditer(regex_expression, data):
        s = match.start()
        e = match.end()
        abbreviation.append(data[s:e])
        # print(data[s:e])

    sorted_result = sorted(abbreviation, key=lambda x: -len(x))
    print(sorted_result)

    # Masking the found abbreviations
    for match in sorted_result:
        pattern = match
        replace = "###" + str(sorted_result.index(match) + 1) + " "
        data = re.sub(pattern, replace, data)

    # Removing all newline Characters
    data = data.replace("\n", "")

    if not os.path.exists(os.path.join("temp","output",lang_code, file_name + "_output")):
        os.mkdir(os.path.join("temp","output",lang_code, file_name + "_output"))

    # Writing the Masked data
    with open(os.path.join("temp","output",lang_code, file_name + "_output", "masked.txt"), 'w', encoding='utf8') as f:
        f.write(data)

    # Writing the processed data
    f1 = open(os.path.join("temp","output",lang_code, file_name + "_output", 'unmasked_processed.txt'), 'w', encoding='utf8')
    processed_data = testHelper(data,lang_code)

    # Unmasking the processed data
    for i in range(0, len(sorted_result)):
        pattern = "###" + str(i + 1)
        replace = sorted_result[i]
        data = re.sub(pattern, replace, data)

    for line in processed_data:
        f1.write(line + "\n")


input_directory = os.path.join("te","input")
# input_directory = r'C:\Users\Shashank\PycharmProjects\Reverie\input'
for file in os.listdir(input_directory):
    # mask("hi", os.path.join(input_directory, file))
    mask("te", os.path.join(input_directory, file))
# print(testHelper("నిర్వహిస్తున్నారు. కేటగిరి,","te"))