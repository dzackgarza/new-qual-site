---
schema: qual/card@1
id: E-SSA.PR-4
kind: problem
title: Coefficients of a generating function with poles on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Generating Functions
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 4,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
Suppose $F(z)=\sum_{n=0}^{\infty}F_nw^n$ is meromorphic in a region containing the closed unit disc, and the only poles of $F$ are on the unit circle at the points $\alpha_1,\dots,\alpha_k$, and their orders are $r_1,\dots,r_k$ respectively. Then for some $\epsilon>0$
$$
F_n=\sum_{j=1}^{k}P_j(n)+O(e^{-\epsilon n})\qquad\text{as } n\to\infty,
$$
where each $P_j$ is a polynomial of degree $r_j-1$.
:::

