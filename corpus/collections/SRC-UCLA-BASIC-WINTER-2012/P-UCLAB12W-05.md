---
schema: qual/card@1
id: P-UCLAB12W-05
kind: problem
title: Unique continuous solution of $y(x)=e^x+y(x^2)/2$ on $[0,1]$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Prove that there is a unique continuous function $y:[0,1]\to\RR$ satisfying
$$
y(x)=e^x+\frac{y(x^2)}2,
\qquad x\in[0,1].
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The series
$$
y(x)=\sum_{k=0}^{\infty}2^{-k}e^{x^{2^k}}
$$
converges uniformly on $[0,1]$.


::: pf-proof

For $x\in[0,1]$,
$$
0\le x^{2^k}\le1,
$$
so
$$
0<e^{x^{2^k}}\le e.
$$
Hence
$$
\abs{2^{-k}e^{x^{2^k}}}
\le
e2^{-k}.
$$
Since
$$
\sum_{k=0}^{\infty}e2^{-k}
$$
converges, the Weierstrass $M$-test gives uniform convergence.

:::

:::

::: {.pf-step #s1-2}

The function $y$ defined in step [](#s1-1){.pf-ref} is continuous on $[0,1]$.


::: pf-proof

Each function
$$
x\longmapsto 2^{-k}e^{x^{2^k}}
$$
is continuous. By step [](#s1-1){.pf-ref}, their series converges uniformly, so its sum is continuous.

:::

:::

::: {.pf-step #s1-3}

The function $y$ satisfies
$$
y(x)=e^x+\frac12y(x^2)
$$
for every $x\in[0,1]$.


::: pf-proof

Using the uniformly convergent series from step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\frac12y(x^2)
&=
\frac12\sum_{k=0}^{\infty}2^{-k}e^{(x^2)^{2^k}}\\
&=
\sum_{k=0}^{\infty}2^{-(k+1)}e^{x^{2^{k+1}}}\\
&=
\sum_{j=1}^{\infty}2^{-j}e^{x^{2^j}}.
\end{aligned}
$$
Therefore
$$
e^x+\frac12y(x^2)
=
e^x+
\sum_{j=1}^{\infty}2^{-j}e^{x^{2^j}}
=
y(x).
$$

:::

:::

::: {.pf-step #s1-4}

Any continuous solution of the functional equation is equal to the function in step [](#s1-1){.pf-ref}.


::: pf-proof

Let $z:[0,1]\to\RR$ be any continuous solution. Since $[0,1]$ is compact, $z$ is bounded; choose $M>0$ such that
$$
\abs{z(t)}\le M
$$
for every $t\in[0,1]$.

Iterating
$$
z(x)=e^x+\frac12z(x^2)
$$
$N$ times gives
$$
z(x)
=
\sum_{k=0}^{N-1}2^{-k}e^{x^{2^k}}
+
2^{-N}z(x^{2^N}).
$$
The remainder satisfies
$$
\abs{2^{-N}z(x^{2^N})}
\le
2^{-N}M
\longrightarrow0.
$$
Letting $N\to\infty$ yields
$$
z(x)
=
\sum_{k=0}^{\infty}2^{-k}e^{x^{2^k}}
=y(x).
$$
Thus every continuous solution equals $y$.

:::

:::

::: {.pf-step #s1-5}

Hence there exists exactly one continuous solution, namely
$$
\boxed{
y(x)=\sum_{k=0}^{\infty}2^{-k}e^{x^{2^k}}
}.
$$


::: pf-proof

Existence follows from steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, and uniqueness follows from step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required existence-and-uniqueness statement.

:::

:::

:::
