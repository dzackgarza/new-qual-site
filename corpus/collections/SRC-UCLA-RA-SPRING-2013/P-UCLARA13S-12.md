---
schema: qual/card@1
id: P-UCLARA13S-12
kind: problem
title: Cauchy-transform representation of a self-map of the upper half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $\mathbb H$ be the upper half-plane and let $f:\mathbb H\to\mathbb H$ be holomorphic. Assume
\[
\lim_{y\to\infty} y f(iy)=i,
\qquad
|f(z)|\le \frac{1}{\operatorname{Im}z}
\quad(z\in\mathbb H).
\]
For $\varepsilon>0$, define
\[
g_\varepsilon(x)=\frac1\pi\operatorname{Im}f(x+i\varepsilon).
\]

(a) Show that
\[
f(z+i\varepsilon)=\int_{\mathbb R}\frac{g_\varepsilon(x)}{x-z}\,dx.
\]

(b) Show that there exists a Borel probability measure $\mu$ on $\mathbb R$ such that
\[
f(z)=\int_{\mathbb R}\frac{d\mu(x)}{x-z}.
\]
:::
