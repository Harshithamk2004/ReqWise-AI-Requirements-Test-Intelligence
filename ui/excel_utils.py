from openpyxl import Workbook

def generate_excel(result):
    wb = Workbook()

    def add_sheet(title, data):
        ws = wb.create_sheet(title)
        ws.append(["ID", "Description"])
        for i, item in enumerate(data, 1):
            ws.append([i, item])

    add_sheet("Functional Requirements", result.functional_requirements)
    add_sheet("Ambiguities", result.ambiguities)
    add_sheet("Positive Test Cases", result.positive_tests)
    add_sheet("Negative Test Cases", result.negative_tests)
    add_sheet("Edge Case Test Cases", result.edge_case_tests)

    wb.remove(wb["Sheet"])  # default sheet remove
    file_path = "Requirement_Analysis.xlsx"
    wb.save(file_path)

    return file_path
