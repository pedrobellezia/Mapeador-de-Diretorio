from pathlib import Path
import json


def dir_flattener(directory: str, base_path: str) -> dict:
    p = Path(directory)
    filerelations: dict = {}
    for item in p.iterdir():
        if item.is_file():
            relative_path = str(item.relative_to(base_path))
            filerelations[relative_path] = item.name

    return filerelations


def save_json(json_data: dict, j_name: str) -> None:
    with open(f"{j_name}.json", "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    print(f"Arquivo '{j_name}.json' salvo com sucesso!")


def main(directory: str, j_name: str) -> None:
    all_data: dict = {}
    stack = [directory]
    base_path = Path(directory)

    while stack:
        current_dir = stack.pop()
        dir_name = str(Path(current_dir).relative_to(base_path))
        all_data[dir_name] = dir_flattener(current_dir, base_path)

        for item in Path(current_dir).iterdir():
            if item.is_dir():
                stack.append(str(item))

    save_json(all_data, j_name)


if __name__ == "__main__":
    directory_path = r"Caminho do diretório"
    json_name = "Nome do arquivo JSON"

    main(directory_path, json_name)