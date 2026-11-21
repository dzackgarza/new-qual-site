---
schema: qual/card@1
id: P-CAF05A
kind: problem
title: "Analytic functions with prescribed boundary modulus and zeros in a disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Find all functions $f \in H(B(0; 2))$ such that:

(a) $\abs{f(z)} = 1$ if $\abs{z} = 1$.

(b) $f$ has a zero of multiplicity 2 at $z = 1/2$ and no other zeroes.

Hint: Consider first the case where $f$ satisfies (a), but has no zeroes.
:::

::: {.solution}

The argument is the card's own, by a Blaschke factor, the maximum modulus principle and the identity theorem; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $B(0;2)$ be the open disc of radius $2$ about $0$ and put
$$
B(z)=\frac{z-\tfrac12}{1-\tfrac12 z},\qquad z\in B(0;2).
$$

::: pf

::: {.pf-step #factor}
$B$ is holomorphic on $B(0;2)$, has a simple zero at $\tfrac12$ and no other zero there, and $\abs{B(z)}=1$ for $\abs{z}=1$.

::: pf-proof
The denominator $1-z/2$ vanishes only at $z=2\notin B(0;2)$, so $B$ is holomorphic on the disc; its numerator vanishes only at $\tfrac12$, and the denominator does not vanish there, so that zero is simple. For $\abs{z}=1$,
$$
\abs{B(z)}=\frac{\abs{z-\tfrac12}}{\abs{1-\tfrac12 z}}=\frac{\abs{z-\tfrac12}}{\abs{z}\abs{\bar z-\tfrac12}}=\frac{\abs{z-\tfrac12}}{\abs{\overline{z-\tfrac12}}}=1 .
$$
:::

:::

::: {.pf-step #quotient}
$h=f/B^{2}$ extends holomorphically and without zeros to $B(0;2)$, and $\abs{h}=1$ on the unit circle.

::: pf-proof
Since $f$ has a zero of multiplicity exactly $2$ at $\tfrac12$ and no other zeros in $B(0;2)$, one has $f(z)=(z-\tfrac12)^{2}g(z)$ with $g$ holomorphic and zero-free on $B(0;2)$. By step [](#factor){.pf-ref},
$$
h(z)=\frac{(z-\tfrac12)^{2}g(z)}{\big(z-\tfrac12\big)^{2}\big/\big(1-\tfrac12 z\big)^{2}}=g(z)\Big(1-\frac{z}{2}\Big)^{2},
$$
which is holomorphic and zero-free on $B(0;2)$, the factor $1-z/2$ never vanishing there. On $\abs{z}=1$ one has $\abs{f}=1$ by hypothesis and $\abs{B}=1$ by step [](#factor){.pf-ref}, so $\abs{h}=\abs{f}/\abs{B}^{2}=1$.
:::

:::

::: {.pf-step #constant}
$h$ is constant on $B(0;2)$.

::: pf-proof
On the closed unit disc $h$ is holomorphic, so the maximum modulus principle applied on $\DD$ and the boundary values $\abs{h}=1$ give $\abs{h(z)}\le1$ for $\abs{z}\le1$. Since $h$ is zero-free on $B(0;2)$, the function $1/h$ is holomorphic on the closed unit disc, and the same argument gives $\abs{1/h(z)}\le1$, that is $\abs{h(z)}\ge1$. So $\abs{h}\equiv1$ on $\DD$. A holomorphic function of constant modulus on a domain is constant: by the open mapping theorem the image of $\DD$ is open, while it lies in the circle $\abs{w}=1$, which has empty interior, so $h(\DD)$ is a single point. Since $B(0;2)$ is connected and $h-c$ vanishes on the nonempty open subset $\DD$, the identity theorem gives $h\equiv c$ on $B(0;2)$.
:::

:::

::: {.pf-step #answer}
The solutions are exactly $f(z)=c\left(\dfrac{z-\frac12}{1-\frac12z}\right)^{2}$ with $\abs{c}=1$.

::: pf-proof
If $f$ satisfies (a) and (b), step [](#constant){.pf-ref} gives $f=hB^{2}$ with $h\equiv c$ on $B(0;2)$, and $\abs{c}=\abs{h(z)}=1$ since $\abs{h}=1$ on the unit circle. Conversely, for $c\ne0$ the function $f=hB^{2}$ is holomorphic on $B(0;2)$ by step [](#factor){.pf-ref}; it has a zero of multiplicity exactly $2$ at $\tfrac12$ and no other zero there, since $c\neq0$ and $B$ has that simple zero; and $\abs{f(z)}=\abs{c}\abs{B(z)}^{2}=1$ on $\abs{z}=1$. So every such $c$ with $\abs{c}=1$ gives a solution and there are no others.
:::

:::

:::
:::
