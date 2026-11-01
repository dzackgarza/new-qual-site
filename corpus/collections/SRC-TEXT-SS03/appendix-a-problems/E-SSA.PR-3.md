---
schema: qual/card@1
id: E-SSA.PR-3
kind: problem
title: Power series for the Bessel and Airy functions
classification:
  areas:
  - complex-analysis
  topics:
  - Special Functions
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 3,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
The Bessel functions and Airy function have the following power series expansions:
$$
J_\nu(x)=\Bigl(\frac{x}{2}\Bigr)^{\nu}\sum_{m=0}^{\infty}\frac{(-1)^m}{m!\,\Gamma(\nu+m+1)}\Bigl(\frac{x^2}{4}\Bigr)^{m},
$$
$$
\operatorname{Ai}(-x)=\frac{1}{\pi}\sum_{n=0}^{\infty}\frac{x^n}{n!}\sin\bigl(2\pi(n+1)/3\bigr)3^{n/3-2/3}\Gamma\bigl(n/3+1/3\bigr).
$$

(a) From this, verify that when $x>0$,
$$
\operatorname{Ai}(-x)=\frac{x^{1/2}}{3}\Bigl[J_{1/3}\Bigl(\frac{2}{3}x^{3/2}\Bigr)+J_{-1/3}\Bigl(\frac{2}{3}x^{3/2}\Bigr)\Bigr].
$$

(b) The function $\operatorname{Ai}(x)$ extends to an entire function of order $3/2$.

[Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for $\operatorname{Ai}$. Compare also with Problem 1, Chapter 4.]
:::

