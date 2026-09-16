---
schema: qual/card@1
id: P-UCLARA15F-06
kind: problem
title: Difference-quotient characterization of $H^{1/2}(\mathbb R^d)$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 6 on pages 1-2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $u \in L^2(\mathbb{R}^d)$ and let us say that $u \in H^{1/2}(\mathbb{R}^d)$ (a Sobolev space) if
\[
\left( 1 + |\xi|^{1/2} \right) \hat{u}(\xi) \in L^2(\mathbb{R}^d).
\]
Here $\hat{u}$ is the Fourier transform of $u$. Show that $u \in H^{1/2}(\mathbb{R}^d)$ if and only if
\[
\iint \frac{|u(x+y) - u(x)|^2}{|y|^{d+1}}\,dx\,dy < \infty.
\]
:::
