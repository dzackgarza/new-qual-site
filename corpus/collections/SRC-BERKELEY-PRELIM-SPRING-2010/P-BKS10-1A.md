---
schema: qual/card@1
id: P-BKS10-1A
kind: problem
title: A compact-space isometry is surjective
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the positive-distance contradiction and the use of distance preservation under iterates of the isometry.
---

::: {.problem}
Let $X$ be a compact metric space and let $f:X\to X$ be an isometry.
Show that $f$ is surjective.

Hint: for a point $x$, find $m<n$ such that $f^n(x)$ is close to $f^m(x)$.
:::

::: {.solution}

::: pf

::: {.pf-step #not-surjective-assumption}
Suppose, for contradiction, that $f$ is not surjective. Then there are
$x\in X$ and $\varepsilon>0$ such that
$$
B(x,\varepsilon)\cap f(X)=\varnothing.
$$

::: pf-proof
If $f$ is not surjective, choose
$$
x\in X\setminus f(X).
$$
An isometry is continuous, so $f(X)$ is compact because $X$ is compact.
Hence the continuous function
$$
y\longmapsto d(x,y)
$$
attains a minimum on $f(X)$. Since $x\notin f(X)$, this minimum is some
positive number $\delta$. Taking, for example,
$$
\varepsilon=\frac{\delta}{2}
$$
gives the stated disjoint ball.
:::

:::

::: {.pf-step #close-iterates-exist}
There exist integers $0\leq j<k$ such that
$$
d\bigl(f^j(x),f^k(x)\bigr)<\varepsilon.
$$

::: pf-proof
The sequence
$$
x,f(x),f^2(x),\ldots
$$
lies in the compact metric space $X$, so it has a convergent subsequence.
Every convergent sequence is Cauchy. Hence two distinct terms of that
subsequence, say with indices $j<k$, have distance less than
$\varepsilon$.
:::

:::

::: {.pf-step #iterate-close-to-x}
One has
$$
d\bigl(x,f^{k-j}(x)\bigr)<\varepsilon.
$$

::: pf-proof
Every iterate $f^j$ is again an isometry. Therefore
$$
d\bigl(f^j(x),f^k(x)\bigr)
=
d\bigl(f^j(x),f^j(f^{k-j}(x))\bigr)
=
d\bigl(x,f^{k-j}(x)\bigr).
$$
Step [](#close-iterates-exist){.pf-ref} gives the strict inequality.
:::

:::

::: {.pf-step #assumption-impossible}
The assumption that $f$ is not surjective is impossible.

::: pf-proof
Since $k-j\geq1$,
$$
f^{k-j}(x)
=
f\bigl(f^{k-j-1}(x)\bigr)
\in
f(X).
$$
By step [](#iterate-close-to-x){.pf-ref} this point also lies in $B(x,\varepsilon)$, contradicting
step [](#not-surjective-assumption){.pf-ref}.
:::

:::

::: {.pf-step #f-surjective}
The map $f$ is surjective.

::: pf-proof
Step [](#assumption-impossible){.pf-ref} rules out failure of surjectivity.
:::

:::

::: pf-qed
Step [](#f-surjective){.pf-ref} is the required conclusion.
:::

:::

:::
