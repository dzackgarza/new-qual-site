---
schema: qual/card@1
id: P-UCLARA18S-06
kind: problem
title: UCLA analysis Spring 2018, Problem 6
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let $\mathbb T$ denote the unit circle in the complex plane, let $\mathcal P(\mathbb T)$ denote the space of Borel probability measures on $\mathbb T$, and let $\mathcal P(\mathbb T\times\mathbb T)$ denote the space of Borel probability measures on $\mathbb T\times\mathbb T$. Fix $\mu,\nu\in\mathcal P(\mathbb T)$ and define
\[
\mathcal M=\left\{\gamma\in\mathcal P(\mathbb T\times\mathbb T):
\iint_{\mathbb T\times\mathbb T}f(x)g(y)\,d\gamma(x,y)
=\int_{\mathbb T}f(x)\,d\mu(x)\int_{\mathbb T}g(y)\,d\nu(y)
\text{ for all }f,g\in C(\mathbb T)\right\}.
\]
Show that $F:\mathcal M\to\mathbb R$ defined by
\[
F(\gamma)=\iint_{\mathbb T\times\mathbb T}
\sin^2\!\left(\frac{\theta-\phi}{2}\right)
\,d\gamma(e^{i\theta},e^{i\phi})
\]
achieves its minimum on $\mathcal M$.
:::
