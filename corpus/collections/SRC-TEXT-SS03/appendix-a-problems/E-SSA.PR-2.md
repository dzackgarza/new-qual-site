---
schema: qual/card@1
id: E-SSA.PR-2
kind: problem
title: Stirling's formula with an asymptotic expansion in powers of $s^{-1}$
classification:
  areas:
  - complex-analysis
  topics:
  - Asymptotics
  - Gamma Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 2,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
The following is a more precise version of Stirling's formula. There are real constants $a_1=1/12$, $a_2,\dots,a_n,\dots$, so that for every $N>0$
$$
\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N})\Bigr)\qquad\text{when } s\in S_\delta .
$$
This can be proved by using the results of Problem 1 in place of Proposition 1.3.
:::

