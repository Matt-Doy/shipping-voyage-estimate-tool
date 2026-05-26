# Excel/VBA Template Instructions

This folder contains a VBA module that can be imported into an Excel macro-enabled workbook.

## Suggested Excel Layout

Create an `.xlsm` workbook with the following cells:

| Cell | Input |
|---|---|
| B2 | Freight revenue |
| B3 | Sea days |
| B4 | Port days |
| B5 | Daily consumption |
| B6 | Bunker price |
| B7 | Port costs |
| B8 | Canal costs |
| B9 | Other costs |
| B10 | Commission rate |

Suggested output cells:

| Cell | Output |
|---|---|
| E2 | Total days |
| E3 | Bunker cost |
| E4 | Commission |
| E5 | Total costs |
| E6 | Profit/Loss |
| E7 | TCE |

## How to Import the VBA Code

1. Open Excel.
2. Save your workbook as `.xlsm`.
3. Press `ALT + F11`.
4. Go to `File > Import File`.
5. Select `voyage_estimate_vba.bas`.
6. Insert a button in Excel.
7. Assign the macro `RunVoyageEstimate` to the button.

## Business Use

This VBA version can be used as a simple front-office style Excel tool where the user enters voyage assumptions and generates a quick TCE estimate.
