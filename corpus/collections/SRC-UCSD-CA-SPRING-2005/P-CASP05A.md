---
schema: qual/card@1
id: P-CASP05A
kind: problem
title: 'Roots of $z^5(z-2)=w$ in the unit disc and in $B(2,1)$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For $w \in \DD$, consider the equation in $z$: $$(*)\quad z^5(z - 2) = w.$$

(a) Show that (*) has 5 roots in $\DD$ (possibly with multiplicity).
Show that for $w \in \DD \setminus \{0\}$ the 5 roots are distinct.

(b) Show that (*) has exactly one simple root in $B(2, 1)$.
:::

::: {.solution}

The argument is the card's own, two applications of Rouché's theorem and a critical-point check; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

For $w\in\DD$ put $F_{w}(z)=z^{5}(z-2)-w=z^{6}-2z^{5}-w$.

::: pf

::: {.pf-step #five-roots}
(a) $F_{w}$ has five zeros in $\DD$, counted with multiplicity.

::: pf-proof
On the circle $\abs{z}=1$,
$$
\abs{z^{6}-w}\le\abs{z}^{6}+\abs{w}=1+\abs{w}<2=\abs{-2z^{5}} .
$$
So on that circle the term $-2z^{5}$ dominates $z^{6}-w$ strictly, and Rouché's theorem gives that $F_{w}=(-2z^{5})+(z^{6}-w)$ has in $\DD$ as many zeros as $-2z^{5}$, namely five, counted with multiplicity.
:::

:::

::: {.pf-step #distinct}
(a) For $w\ne0$ those five zeros are distinct.

::: pf-proof
$F_{w}'(z)=6z^{5}-10z^{4}=2z^{4}(3z-5)$, whose zeros are $z=0$ and $z=\tfrac53$. A multiple zero of $F_{w}$ is a common zero of $F_{w}$ and $F_{w}'$, hence is $0$ or $\tfrac53$. But $F_{w}(0)=-w\ne0$ for $w\ne0$, and $\tfrac53\notin\DD$. So no zero of $F_{w}$ in $\DD$ is multiple, and the five zeros of step [](#five-roots){.pf-ref} are distinct.
:::

:::

::: {.pf-step #one-root}
(b) $F_{w}$ has exactly one zero in $B(2,1)$, counted with multiplicity.

::: pf-proof
On the circle $\abs{z-2}=1$ one has $\abs{z}\ge\abs{2}-\abs{z-2}=1$, so
$$
\abs{z^{5}(z-2)}=\abs{z}^{5}\cdot1\ge1>\abs{w},
$$
and Rouché's theorem gives that $F_{w}=z^{5}(z-2)-w$ has in $B(2,1)$ as many zeros as $z^{5}(z-2)$. The latter is $z^{5}(z-2)$, whose zeros are $0$ with multiplicity $5$ and $2$ with multiplicity $1$; the point $0$ has $\abs{0-2}=2>1$ and lies outside $B(2,1)$, while $2\in B(2,1)$. So $z^{5}(z-2)$ has exactly one zero there, counted with multiplicity, and so does $F_{w}$.
:::

:::

::: {.pf-step #simple}
(b) That zero is simple.

::: pf-proof
Let $z_{0}\in B(2,1)$ be the zero of $F_{w}$ and suppose it is multiple; then $F_{w}'(z_{0})=0$, so $z_{0}\in\{0,\tfrac53\}$ by step [](#distinct){.pf-ref}. The point $0$ is not in $B(2,1)$, since $\abs{0-2}=2>1$; and $\tfrac53$ is not a zero of $F_{w}$, because
$$
\abs{\Big(\tfrac53\Big)^{5}\Big(\tfrac53-2\Big)}=\frac{3125}{243}\cdot\frac13=\frac{3125}{729}>1>\abs{w},
$$
so $\big(\tfrac53\big)^{5}\big(\tfrac53-2\big)-w\ne0$. Hence $z_{0}$ is a simple zero.
:::

:::

:::
:::
