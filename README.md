# Mapeador de diretórios

O intuito desde projeto é percorrer uma serie de diretórios e subdiretórios, coletando os arquivos encontrados e armazenando em um arquivo JSON.
Este script funciona tanto no windows quanto no linux.
## Pré-requisitos

- Python 3.x
- Módulo `pathlib` e `json` (padrão do Python)


## Como Funciona

1. O script recebe o caminho para um diretório como entrada e começa a iterar por ele e suas subpastas.
2. Para cada diretório, ele coleta os arquivos e os armazena no formato JSON.
3. O JSON contém o caminho relativo do arquivo dentro da estrutura de diretórios.
   
### Input:

```python
directory_path = r"C:\Users\teste\Desktop"
json_name = "directory_structure"
```

### Output:
```json
{
    ".": {
        "file1.txt": "file1.txt",
        "file2.txt": "file2.txt"
    },
    "subdir1": {
        "subdir1\\file3.txt": "file3.txt"
    },
    "subdir1\\subsubdir1": {
        "subdir1\\subsubdir1\\file4.txt": "file4.txt"
    },
    "subdir2": {}
}


