---
schema: qual/card@1
id: P-BERK95S-13
kind: problem
title: A $2$-group acting on an odd finite set has a fixed point
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $n$ be odd, and let $G\le S_n$ have order a power of $2$. Prove that there is some
\[
i\in\{1,\dots,n\}
\]
such that
\[
\sigma(i)=i
\]
for every $\sigma\in G$.
:::

::: {.solution}
Let
$$
\Omega\coloneqq\{1,\ldots,n\}.
$$

::: pf

::: {.pf-step #s1}

Every orbit of the action of $G$ on $\Omega$ has size a power
of $2$.

::: pf-proof

For $i\in\Omega$, the orbit-stabilizer theorem gives
$$
\abs{G\cdot i}=[G:G_i],
$$
which divides $\abs G$. Since $\abs G$ is a power of $2$, so is every
orbit size.

:::

:::

::: {.pf-step #s2}

At least one orbit has size $1$.

::: pf-proof

If every orbit had size greater than $1$, then step [](#s1){.pf-ref} would make
every orbit size even. The disjoint union of the orbits is $\Omega$,
so
$$
n=\abs\Omega
$$
would be a sum of even integers and hence even. This contradicts the
hypothesis that $n$ is odd.

:::

:::

::: {.pf-step #s3}

There is $i\in\Omega$ fixed by every element of $G$.

::: pf-proof

Choose an orbit $G\cdot i$ of size $1$, which exists by step [](#s2){.pf-ref}.
Then
$$
G\cdot i=\{i\},
$$
so $\sigma(i)=i$ for every $\sigma\in G$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required common fixed point.

:::

:::

:::
