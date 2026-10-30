---
schema: qual/card@1
id: P-XA3WA
kind: problem
title: "Zeros of $z^6+4z^2e^{z+1}-3$ in the closed unit disk"
classification:
  areas:
    - complex-analysis
  topics:
    - Rouché
    - Zeros
relations: []
review: draft
---

::: {.problem}
Find the number of roots on $\abs{z} \leq 1$ of
$$
f(z)=z^{6}+4 z^{2} e^{z+1}-3.
$$
:::

::: {.solution}
Write $f=M+m$ with $M(z)=4z^2e^{z+1}$ and $m(z)=z^6-3$.

::: pf

::: {.pf-step #strict}
$\abs{m(z)}<\abs{M(z)}$ for $\abs{z}=1$.

::: pf-proof
For $\abs{z}=1$, $\abs{m(z)}\le\abs{z}^6+3=4$ and $\abs{M(z)}=4\abs{z}^2e^{\Re z+1}=4e^{\Re z+1}\ge4$, since $\Re z\ge-1$.
Equality $\abs{M(z)}=4$ holds only when $\Re z=-1$, that is, $z=-1$, and there $\abs{m(-1)}=\abs{1-3}=2<4$.
Hence the inequality is strict at every point of the circle.
:::

:::

::: pf-step
$f$ has $\boxed{2}$ zeros in $\abs{z}\le1$, counted with multiplicity.

::: pf-proof
By step [](#strict){.pf-ref}, $f$ has no zeros on $\abs{z}=1$, and Rouché's theorem gives that $f$ and $M$ have the same number of zeros in $\abs{z}<1$.
Since $e^{z+1}\ne0$, $M$ has exactly the double zero at $0$.
:::

:::

:::

:::
