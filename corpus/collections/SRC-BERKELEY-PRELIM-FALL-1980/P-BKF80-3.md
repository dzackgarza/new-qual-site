---
schema: qual/card@1
id: P-BKF80-3
kind: problem
title: Analytic interpolation at the points $\pm1/n$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Determine whether there exist functions $f$ and $g$, analytic at $0$, such that for every positive integer $n$,
$$
f(1/n)=f(-1/n)=1/n^2,
$$
and
$$
g(1/n)=g(-1/n)=1/n^3.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #f-exists}
A function $f$ satisfying the first interpolation condition exists; one may take
$$
\boxed{f(z)=z^2}.
$$

::: pf-proof
The polynomial $f(z)=z^2$ is analytic at $0$, and for every positive integer $n$,
$$
f(1/n)=\frac1{n^2}=f(-1/n).
$$
:::

:::

::: {.pf-step #g-does-not-exist}
No function $g$ analytic at $0$ can satisfy the second interpolation condition.

::: pf-proof
Suppose such a function $g$ existed. There is a disk $D$ centered at $0$ on which $g$ is analytic. For every sufficiently large positive integer $n$, the point $1/n$ lies in $D$, and
$$
g(1/n)=\frac1{n^3}=\left(\frac1n\right)^3.
$$
Thus the analytic function
$$
h(z)\coloneqq g(z)-z^3
$$
has infinitely many zeros $1/n$ in $D$ accumulating at the interior point $0$. By the identity theorem, $h\equiv0$ on $D$, so $g(z)=z^3$ on $D$.

For all sufficiently large $n$, also $-1/n\in D$, and hence
$$
g(-1/n)=\left(-\frac1n\right)^3=-\frac1{n^3},
$$
contradicting the required equality $g(-1/n)=1/n^3$.
:::

:::

::: pf-qed
Step [](#f-exists){.pf-ref} settles the existence of $f$, and step [](#g-does-not-exist){.pf-ref} proves the nonexistence of $g$.
:::

:::
:::
