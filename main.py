import os
import openpyxl
from openpyxl.styles.colors import COLOR_INDEX
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware
from typing import List

from app.routes.auth import auth_router
from app.routes.bundle import bundle_router
from app.routes.flashcard import flashcard_router
from app.core.error_handler import Error404
app = FastAPI()

origins: list[str] = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(bundle_router)
app.include_router(flashcard_router)


@app.get("/download_file/{filename}")
async def download_file(filename: str):
    file_path = f"app/data/{filename}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename)
    else:
        return {"error": "File not found"}


@app.get("/excel")
async def download_file():
    file_path = f"app/data/excel.xlsx"
    if not os.path.exists(file_path):
        raise Error404("File not found")

    file_size = os.path.getsize(file_path)

    def iterfile():
        with open(file_path, mode="rb") as file_like:
            yield from file_like

    headers = {
        "Content-Length": str(file_size),
        "Content-Disposition": f"attachment; filename=excel.xlsx"
    }

    return StreamingResponse(
        iterfile(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers
    )


@app.get("/sheet_list", response_model=List[str])
async def get_sheet_names():
    file_path = f"app/data/excel.xlsx"
    if not os.path.exists(file_path):
        raise Error404("File not found")

    wb = openpyxl.load_workbook(file_path, read_only=True)
    sheet_names = wb.sheetnames
    return sheet_names


def convert_to_hex_color(color_code):
    if len(color_code) == 8:
        rgb_hex = color_code[2:]
        hex_color = f"#{rgb_hex}"
        return hex_color
    else:
        return "#000000"


def get_hex_color(color):
    if color is None:
        return '#FFFFFF'

    if color.type == 'rgb':
        return f"#{color.rgb[2:]}"
    elif color.type == "indexed":
        return f"#{color.rgb[2:]}"
    elif color.type == 'theme':
        return f"##{color.theme:06X}"

    return '#FFFFFF'


@app.get("/sheet_data/{sheet_name}")
async def get_sheet_data(sheet_name: str):
    file_path = "app/data/excel.xlsx"
    if not os.path.exists(file_path):
        raise Error404("File not found")

    try:
        # Load the workbook and the specific sheet
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb[sheet_name]

        # Prepare data
        cell_data = []
        border_info = []

        for row_index, row in enumerate(sheet.iter_rows()):
            for col_index, cell in enumerate(row):
                # Extract cell value
                value = "<Image>" if cell.data_type == "e" else str(cell.value) if cell.value is not None else ""

                # Add cell data
                cell_data.append({
                    "r": row_index,
                    "c": col_index,
                    "v": {
                        "v": value,
                        "ff": cell.font.name,
                        "bl": 0 if cell.font.b is False else 1,
                        "it": 0 if cell.font.i is False else 1,
                        "fs": cell.font.size,
                        "ht": 0 if cell.alignment.horizontal == 'center' else 1 if cell.alignment.horizontal == 'left' else 2,
                        "fc": convert_to_hex_color(str(cell.font.color.rgb)),
                    }
                })

                border_info.append({
                    "rangeType": "cell",
                    "value": {
                        "row_index": row_index,
                        "col_index": col_index,
                        "l":  None if cell.border.left.style is None else
                            {
                                "style": 7 if cell.border.left.style == "thin" else 8,
                                "color": "rgb(0, 0, 0)"
                            },
                        "r":  None if cell.border.left.style is None else
                            {
                                "style": 7 if cell.border.right.style == "thin" else 8,
                                "color": "rgb(0, 0, 0)"
                            },
                        "t":  None if cell.border.left.style is None else
                            {
                                "style": 7 if cell.border.top.style == "thin" else 8,
                                "color": "rgb(0, 0, 0)"
                            },
                        "b":  None if cell.border.left.style is None else
                            {
                                "style": 7 if cell.border.bottom.style == "thin" else 8,
                                "color": "rgb(0, 0, 0)"
                            },
                    }
                })

        sheet_data = {
            "name": sheet_name,
            "celldata": cell_data,
            "config": {
                "borderInfo": border_info
            },
        }

        return JSONResponse(content=sheet_data)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Sheet '{sheet_name}' not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
