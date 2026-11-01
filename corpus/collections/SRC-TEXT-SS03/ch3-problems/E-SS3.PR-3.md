---
schema: qual/card@1
id: E-SS3.PR-3
kind: problem
title: Laurent series on an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Chapter 3, §9, problem 3, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page 127). This card did not
    exist before: it was found missing by a completeness audit of the collection against the book,
    which located every printed Exercises and Problems item and compared it with the cards on disk.
    The transcription was taken from the OCR text layer and cleaned of OCR errors; the the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
If $f(z)$ is holomorphic in the deleted neighborhood $\{0<\abs{z-z_0}<r\}$ and has a pole of order $k$ at $z_0$, then we can write
$$
f(z)=\frac{a_{-k}}{(z-z_0)^k}+\cdots+\frac{a_{-1}}{(z-z_0)}+g(z)
$$
where $g$ is holomorphic in the disc $\{\abs{z-z_0}<r\}$. There is a generalization of this expansion that holds even if $z_0$ is an essential singularity. This is a special case of the Laurent series expansion, which is valid in an even more general setting.

Let $f$ be holomorphic in a region containing the annulus $\{z:r_1\le\abs{z-z_0}\le r_2\}$ where $0<r_1<r_2$. Then
$$
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n
$$
where the series converges absolutely in the interior of the annulus. To prove this, it suffices to write
$$
f(z)=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{\zeta-z}\,d\zeta-\frac{1}{2\pi i}\int_{C_{r_1}}\frac{f(\zeta)}{\zeta-z}\,d\zeta
$$
when $r_1<\abs{z-z_0}<r_2$, and argue as in the proof of Theorem 4.4, Chapter 2. Here $C_{r_1}$ and $C_{r_2}$ are the circles bounding the annulus.
:::

