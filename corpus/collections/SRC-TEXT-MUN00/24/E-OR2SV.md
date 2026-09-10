---
schema: qual/card@1
id: E-OR2SV
kind: problem
title: No two of the unit interval variants are homeomorphic
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that no two of the spaces $(0, 1)$, $(0, 1]$, and $[0, 1]$ are homeomorphic.
[Hint: What happens if you remove a point from each of these spaces?]

(b) Suppose that there exist imbeddings $f: X \to Y$ and $g: Y \to X$.
Show by means of an example that $X$ and $Y$ need not be homeomorphic.

(c) Show that $\mathbb{R}^n$ and $\mathbb{R}$ are not homeomorphic if $n > 1$.
:::

::: {.solution}
(a) A point $p$ of a connected interval is a cut point if deleting it disconnects the space. In $(0,1)$ every point is a cut point. In $(0,1]$, exactly one point, namely $1$, is not a cut point. In $[0,1]$, exactly the two endpoints $0,1$ are not cut points. A homeomorphism preserves the number of non-cut points, so no two of these three spaces are homeomorphic.

(b) Let
\[
X=(0,1),\qquad Y=[0,1].
\]
The inclusion embeds $X$ in $Y$. The affine map
\[
g:Y\to X,\qquad g(t)=\frac14+\frac t2
\]
embeds $Y$ in $X$. But $X$ and $Y$ are not homeomorphic by part (a).

(c) If $n>1$, the punctured space $\mathbb R^n-\{0\}$ is path connected: two points can be joined by a polygonal path avoiding the origin, using an intermediate point not lying on either line through the origin and one endpoint. By contrast,
\[
\mathbb R-\{0\}=(-\infty,0)\cup(0,\infty)
\]
is disconnected. A homeomorphism $\mathbb R^n\cong\mathbb R$ would restrict after deleting a point to a homeomorphism of these punctured spaces, impossible. Hence $\mathbb R^n\not\cong\mathbb R$ for $n>1$.
:::
