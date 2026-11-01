---
schema: qual/card@1
id: E-SSA.PR-1
kind: problem
title: Watson's lemma for a truncated integral with a smooth cutoff
classification:
  areas:
  - complex-analysis
  topics:
  - Asymptotics
  - Laplace Transform
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 1,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
Let $\eta$ be an indefinitely differentiable function supported in a finite interval, so that $\eta(x)=1$ for $x$ near $0$. Then, if $m>-1$ and $N>0$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O(s^{-N})
$$
for $\operatorname{Re}(s)\ge0$, $\abs{s}\to\infty$.

(a) Consider first the case $-1<m\le0$. It suffices to see that
$$
\int_0^\infty e^{-sx}x^m(1-\eta(x))\,dx=O(s^{-N}),
$$
and this can be done by repeated integration by parts since $e^{-sx}=(-1)^Ns^{-N}\bigl(\tfrac{d}{dx}\bigr)^N(e^{-sx})$.

(b) To extend this to all $m$, find an integer $k$ so that $k-1<m\le k$, write
$$
\int_0^\infty\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)e^{-sx}\eta(x)\,dx=c_{k,m}s^{-m+k-1}+O(s^{-N}),
$$
and integrate by parts $k$ times.
:::

