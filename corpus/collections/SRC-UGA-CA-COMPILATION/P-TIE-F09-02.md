---
schema: qual/card@1
id: P-TIE-F09-02
kind: problem
title: Limit of integrals over large circular arcs when $zf(z)\to k$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 2.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the garbled set-builder LaTeX against Fall 2009, question 2, page 1 of Questions_from_Tie.pdf, whose text layer reads 1 <= theta <= 2 pi, so the bound is kept as printed.
---

::: {.problem}
Let $f$ be a continuous function in the region
$$
D = \{z \mid \abs{z} > R,\ 0 \le \arg z \le \theta\} \quad \text{where} \quad 1 \le \theta \le 2\pi.
$$
If there exists $k$ such that $\lim_{z\to\infty} zf(z) = k$ for $z$ in the region $D$. Show that
$$
\lim_{R'\to\infty} \int_L f(z)\,dz = i\theta k,
$$
where $L$ is the part of the circle $\abs{z} = R'$ which lies in the region $D$.
:::
