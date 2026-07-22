# Local Contrast Enhancement with Nonuniform Superpixel Blocks (Gao 2025)

This repo is my reproduction of Local Contrast Enhancement with Nonuniform Superpixel Blocks, from Guangyong Gao, Sitian Yang, Xiangyang Hu, Zhihua Xia, Yun-Qing Shi, published in IEEE TCSVT, vol. 35, no. 2, 2025.

It raises contrast inside the region a radiologist actually looks at while leaving the rest of the scan faithful to the original.

I reimplemented the method from the paper and ran it from start to finish. Every number and every figure in the report is produced by the code in this repo, and reversibility is checked to be bit exact wherever the method claims it.

## Running it

Everything runs with plain Python and a handful of common libraries. From this folder:

```bash
cd source_code
python3 run_experiment.py       # runs the method, writes metrics and figures
python3 build_deliverables.py   # rebuilds the IEEE report and the slides
```

You need numpy, scipy, matplotlib, pillow, python-docx and python-pptx. Install them with `pip install numpy scipy matplotlib pillow python-docx python-pptx`. The report is exported to PDF with headless LibreOffice, so that has to be on the machine if you want the PDF rebuilt.

## What sits in this folder

```
(the original paper stays on my machine and is not republished here, to respect its copyright)
ieee_report.docx/.pdf  my IEEE format reproduction report
presentation.pptx      a short summary deck
source_code/           the scripts that do the actual work
outputs/               metrics.json and the raw numbers behind the report
figures/               the plots and images the code produces
processing_notes.md    what was reproduced, what was not, and the caveats
```

## A note on honesty

Nothing in the tables or plots was copied from the paper. Anything marked as reported, and only that, is quoted from the original for comparison. Everything else is computed here. Where the exact image set or an unstated hyperparameter differs from the paper, the absolute figures can move a little, but the behaviour and the reversibility hold. The specifics for this paper are in `processing_notes.md`.
