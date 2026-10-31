---
schema: qual/card@1
id: P-PRECALC2-11
kind: problem
title: Limit of $(x_1^n+\cdots+x_k^n)^{1/n}$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Sequences
relations: []
review: draft
---

::: {.problem}
(a) Evaluate $\displaystyle\lim_{n\to\infty}(3^n+5^n)^{1/n}$.

(b) More generally, if $x_1,\ldots,x_k>0$, evaluate $\displaystyle\lim_{n\to\infty}(x_1^n+\cdots+x_k^n)^{1/n}$.
:::

::: {.solution}

Let
$$
M=\max\{x_1,\dots,x_k\}.
$$

::: pf

::: pf-step

For every $n\ge1$,
$$
\boxed{
x_1^n+\cdots+x_k^n
\ge
M^n}.
$$


::: pf-proof

At least one of the $x_i$ equals $M$, and all terms are nonnegative.

:::

:::

::: {.pf-step #s1-2}

Taking $n$th roots,
$$
\boxed{
(x_1^n+\cdots+x_k^n)^{1/n}
\ge
M}.
$$


::: pf-proof

The function $t\mapsto t^{1/n}$ is increasing on $[0,\infty)$.

:::

:::

::: {.pf-step #s1-3}

Also, for every $i$,
$$
x_i^n\le M^n.
$$


::: pf-proof

By definition,
$$
x_i\le M,
$$
and all numbers are positive.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
x_1^n+\cdots+x_k^n
\le
kM^n.
$$


::: pf-proof

Add the $k$ inequalities from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Taking $n$th roots gives
$$
\boxed{
(x_1^n+\cdots+x_k^n)^{1/n}
\le
k^{1/n}M}.
$$


::: pf-proof

Apply the increasing $n$th-root function to step [](#s1-4){.pf-ref}:
$$
(kM^n)^{1/n}
=
k^{1/n}M.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
\lim_{n\to\infty}k^{1/n}=1}.
$$


::: pf-proof

Taking logarithms,
$$
\log(k^{1/n})
=
\frac{\log k}{n}
\longrightarrow0.
$$
Exponentiating gives the limit $1$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\lim_{n\to\infty}
(x_1^n+\cdots+x_k^n)^{1/n}
=
M
=
\max_i x_i}.
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref} give
$$
M
\le
(x_1^n+\cdots+x_k^n)^{1/n}
\le
k^{1/n}M.
$$
By step [](#s1-6){.pf-ref}, both bounding expressions tend to $M$. Apply the squeeze
theorem.

:::

:::

::: {.pf-step #s1-8}

For the specific expression
$$
(3^n+5^n)^{1/n},
$$
one has
$$
\boxed{
\lim_{n\to\infty}(3^n+5^n)^{1/n}=5}.
$$


::: pf-proof

Here
$$
M=\max\{3,5\}=5.
$$
Apply step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the general answer, and step [](#s1-8){.pf-ref} gives the requested
special case.

:::

:::

:::
