---
schema: qual/card@1
id: P-UCLARA15F-03
kind: problem
title: Locally integrable functions bounded by the $L^p$ quasinorm with $0<p<1$ vanish
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 3 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^1_{\mathrm{loc}}(\mathbb{R}^d)$ be such that for some $0 < p < 1$, we have
\[
\left| \int f(x) g(x)\,dx \right| \leq \left( \int |g(x)|^p\,dx \right)^{\frac{1}{p}},
\]
for all $g \in C_0(\mathbb{R}^d)$. Show that $f(x) = 0$ a.e. Here $C_0(\mathbb{R}^d)$ is the space of continuous functions with compact support on $\mathbb{R}^d$.
:::
