---
schema: qual/card@1
id: P-BKS05-8B
kind: problem
title: A differentiable function with $|f'|\le|f|$ and $f(0)=0$ vanishes
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently verified the conclusion using monotonic weighted squares on the
    positive and negative half-lines rather than the source's interval iteration.
---

::: {.problem}
Let $f : \mathbb { R } \to \mathbb { R }$ be differentiable on R. Suppose that $f ( 0 ) = 0$ , and that $| f ^ { \prime } ( x ) | \leq | f ( x ) |$ for all $x \in \mathbb { R }$ . Prove that $f ( x ) = 0$ for all $x \in \mathbb { R }$
:::

::: {.solution}
<1>1. One has $f(x)=0$ for every $x\geq0$.

::: {.proof}
Define
$$
g(x)\coloneqq e^{-2x}f(x)^2.
$$
For every $x\in\RR$,
$$
g'(x)
=
2e^{-2x}f(x)\bigl(f'(x)-f(x)\bigr).
$$
The hypothesis gives
$$
f(x)f'(x)
\leq
\abs{f(x)}\abs{f'(x)}
\leq
f(x)^2,
$$
and therefore $g'(x)\leq0$. Thus $g$ is nonincreasing. Since
$$
g(0)=f(0)^2=0
$$
and $g(x)\geq0$, for every $x\geq0$ one has
$$
0\leq g(x)\leq g(0)=0.
$$
Hence $g(x)=0$, so $f(x)=0$.
:::

<1>2. One has $f(x)=0$ for every $x\leq0$.

::: {.proof}
Define
$$
h(x)\coloneqq e^{2x}f(x)^2.
$$
Then
$$
h'(x)
=
2e^{2x}f(x)\bigl(f'(x)+f(x)\bigr).
$$
The hypothesis also gives
$$
f(x)f'(x)
\geq
-\abs{f(x)}\abs{f'(x)}
\geq
-f(x)^2,
$$
so $h'(x)\geq0$. Thus $h$ is nondecreasing. For every $x\leq0$,
$$
0\leq h(x)\leq h(0)=f(0)^2=0.
$$
Hence $h(x)=0$, so $f(x)=0$.
:::

<1>3. The function $f$ vanishes identically on $\RR$.

::: {.proof}
Step <1>1 gives the conclusion on $[0,\infty)$, and step <1>2 gives it on
$(-\infty,0]$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
