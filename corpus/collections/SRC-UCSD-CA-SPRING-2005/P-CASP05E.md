---
schema: qual/card@1
id: P-CASP05E
kind: problem
title: 'Roots of $z^n=e^{z-\lambda}$ by Rouché''s theorem'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $n$ be a positive integer and $\lambda > 1$ a real number.
Consider the equation $$(**)\quad z^n - e^{z - \lambda} = 0.$$

(a) Find all the roots of (**) with $\abs{z} = 1$.

(b) Show that there are exactly $n$ distinct simple roots of (**) with $\abs{z} < 1$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the estimate on the circle, the count and the simplicity test as separate steps.

Let $F(z)=z^{n}-e^{z-\lambda}$ with $n\ge1$ and $\lambda>1$.

::: pf

::: {.pf-step #circle}
$F$ has no zeros with $\abs{z}=1$.

::: pf-proof
On $\abs{z}=1$ one has $\abs{e^{z-\lambda}}=e^{\operatorname{Re}z-\lambda}\le e^{1-\lambda}<1=\abs{z^{n}}$, since $\operatorname{Re}z\le1$ and $\lambda>1$. If $F(z)=0$ then $z^{n}=e^{z-\lambda}$, so the two sides would have equal modulus, contradicting the strict inequality. This answers (a): there are no roots on $\abs{z}=1$.
:::

:::

::: {.pf-step #count}
$F$ has exactly $n$ zeros in $\DD$, counted with multiplicity.

::: pf-proof
$F$ and $z^{n}$ are entire, and on $\abs{z}=1$ one has $\abs{z^{n}-F(z)}=\abs{e^{z-\lambda}}<\abs{z^{n}}$ by step [](#circle){.pf-ref}; so Rouché's theorem gives that $F$ has as many zeros in $\DD$ as $z^{n}$, namely $n$ (the zero $0$ of order $n$).
:::

:::

::: {.pf-step #simple}
Every zero of $F$ in $\DD$ is simple.

::: pf-proof
If $z$ is a multiple zero then $F(z)=F'(z)=0$, that is $z^{n}=e^{z-\lambda}$ and $nz^{n-1}=e^{z-\lambda}$. Since $e^{z-\lambda}\ne0$, such a $z$ is nonzero, so dividing gives $nz^{n-1}=z^{n}$, hence $z=n$. But $n\ge1$ means $\abs{n}=n\ge1$, so $z\notin\DD$; therefore no zero in $\DD$ is multiple.
:::

:::

::: {.pf-qed}
By steps [](#circle){.pf-ref}, [](#count){.pf-ref} and [](#simple){.pf-ref}: no roots on the unit circle, and exactly $n$ roots in $\DD$, all simple, hence distinct.
:::

:::

:::
