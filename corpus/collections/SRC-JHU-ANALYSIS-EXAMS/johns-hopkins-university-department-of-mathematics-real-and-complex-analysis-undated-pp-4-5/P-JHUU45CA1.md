---
schema: qual/card@1
id: P-JHUU45CA1
kind: problem
title: Entire functions with pointwise modulus bound are proportional
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the two entire functions and the pointwise inequality with Problem 4 of the undated JHU exam on pages 4–5 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the identically zero denominator case, extension across each isolated zero, preservation of the quotient bound, and the equality on the zero set."
---

Suppose that $f, g$ are entire functions with $|f(z)| \leq |g(z)|$ for all $z \in \mathbb{C}$.
Prove that there is a constant $c \in \mathbb{C}$ such that $f = cg$.

::: solution
<1>1. If $g$ is not identically zero, the quotient $f/g$ extends to a bounded entire function.

::: proof
Let $Z=\{z:g(z)=0\}$. The zeros of a nonzero entire
function are isolated [@SS03]. On $\mathbb C\setminus Z$,
the quotient $h=f/g$ is holomorphic and satisfies
$|h|\leq1$ by hypothesis. In a sufficiently small punctured
disk around each point of $Z$, this bound makes the
singularity removable [@SS03]. The resulting local
extensions agree with the same quotient off $Z$, so
they define one entire function $H$. Continuity at
the removed points preserves $|H|\leq1$ on the whole plane.
:::

<1>2. The functions are proportional in every case.

::: proof
Under the assumption of step <1>1, Liouville's theorem
makes $H$ a constant $c$ with $|c|\leq1$ [@SS03].
Thus $f=cg$ off $Z$. At a point of $Z$, the original
inequality forces $f=0=cg$, so the equality holds everywhere.

If instead $g$ is identically zero, the same inequality
forces $f$ to be identically zero. Then $f=cg$ with
$c=0$. These cases exhaust the possibilities.
:::
:::
