# Заполняем SVG-шаблоны

Это скрипт для заполнения SVG-шаблонов и рендера их в PDF.

## Требования

Для запуска вам понадобится:

- Python 3.6 или выше
- [Inkscape](https://inkscape.org/ru/) для создания шаблонов и для рендера.

## Установка

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

## Переменные окружения

Настройки берутся из переменных окружения. Чтобы их определить, создайте файл `.env` в корне проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `INKSCAPE` — путь для запуска Inkscape. Нужен для рендера SVG в PDF и другие форматы.

Пример:

```env
INKSCAPE=/path/to/inkscape.exe
```

## Подготовка

### Шаблон

SVG шаблон удобно подготовить в Inkscape. Верстаете необходимый документ, затем расставляете плейсходеры, которые будут заменены на реальные данные. Например, `{title}` для заголовка или `{date}` для даты.

### Данные

Удобнее всего создать таблицу с данными в Excel или LibreOffice Calc, а потом экспортировать её как CSV.

__Важно:__ Первой строкой в таблице должны быть названия полей в шаблоне. Значения в CSV должны быть разделены табуляцией (при экспорте выбирайте что-то вроде `Tab` или `\t`).

## Запуск

Запустите скрипт в терминале:

```sh
python main.py --template template/example.svg --data /path/to/data.csv --output tmp
```

Можно использовать сокращенную запись:

```sh
python main.py -t template/example.svg -d /path/to/data.csv -o tmp
```
