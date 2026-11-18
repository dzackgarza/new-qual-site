---
schema: qual/card@1
id: P-HCAX12
kind: problem
title: Zeros and poles of a doubly periodic function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
relations: []
review: draft
---

::: {.problem}
Show that a nonconstant doubly periodic meromorphic function has equally many zeros and poles, counted with multiplicity, in a fundamental parallelogram.
:::

::: {.solution}

The argument is the card's own, by the argument principle and the periodicity of $f'/f$; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f$ be nonconstant and meromorphic on $\CC$ with periods $\omega_{1},\omega_{2}$ linearly independent over $\RR$.

::: pf

::: {.pf-step #parallelogram}
There is a fundamental parallelogram $P$ whose boundary contains no zero and no pole of $f$.

::: pf-proof
The zeros and poles of a nonconstant meromorphic function are isolated, so their union $Z$ is a discrete closed set, in particular countable and with empty interior. The fundamental parallelogram for the lattice $\Lambda=\ZZ\omega_{1}+\ZZ\omega_{2}$ with a corner at $\alpha$ has boundary lying in finitely many translates $\alpha+\RR\omega_{j}+\Lambda+\text{(edge)}$, and translating $\alpha$ to $\alpha+\zeta$ moves the boundary off $Z$ unless $\zeta$ lies in the countable set $Z-Z$; since $\CC$ is uncountable there is such a $\zeta$ arbitrarily small. So a translate of any fundamental parallelogram has boundary disjoint from $Z$.
:::

:::

::: {.pf-step #argument}
$N_{0}-N_{\infty}=\dfrac{1}{2\pi i}\displaystyle\int_{\partial P}\frac{f'(z)}{f(z)}\,dz$, where $N_{0}$ and $N_{\infty}$ count the zeros and poles of $f$ in $P$ with multiplicity.

::: pf-proof
$f'/f$ is meromorphic on a neighbourhood of the closed parallelogram, its only poles being the zeros and poles of $f$ inside $P$; at a zero of $f$ of multiplicity $m$ it has a simple pole with residue $m$, and at a pole of $f$ of multiplicity $m$ a simple pole with residue $-m$ (local expansion of $f$ as $c(z-z_{0})^{m}$). Applying the residue theorem to $f'/f$ on the positively oriented boundary gives the display, the argument principle in this form.
:::

:::

::: {.pf-step #g-periodic}
$f'/f$ is doubly periodic with the periods $\omega_{1},\omega_{2}$.

::: pf-proof
Differentiating $f(z+\omega_{j})=f(z)$ gives $f'(z+\omega_{j})=f'(z)$, so both $f'$ and $f$ are invariant under $z\mapsto z+\omega_{j}$, hence so is their quotient $f'/f$ wherever it is defined.
:::

:::

::: {.pf-step #vanishes}
$\displaystyle\int_{\partial P}\frac{f'(z)}{f(z)}\,dz=0$.

::: pf-proof
Label the parallelogram with vertices $\alpha$, $\alpha+\omega_{1}$, $\alpha+\omega_{1}+\omega_{2}$, $\alpha+\omega_{2}$. The two edges parallel to $\omega_{1}$ are the segment from $\alpha$ to $\alpha+\omega_{1}$ and the segment from $\alpha+\omega_{2}$ to $\alpha+\omega_{1}+\omega_{2}$, the latter traversed in the opposite direction; their integrals of the doubly periodic function $g=f'/f$ differ by the substitution $z\mapsto z+\omega_{2}$ and hence cancel, since $g(z+\omega_{2})=g(z)$ by step [](#g-periodic){.pf-ref}. The same cancellation holds for the two edges parallel to $\omega_{2}$, using $g(z+\omega_{1})=g(z)$. So the integral over $\partial P$ is the sum of four terms that cancel in pairs.
:::

:::

::: {.pf-step #equal}
$N_{0}=N_{\infty}$: $f$ has equally many zeros and poles in $P$, counted with multiplicity.

::: pf-proof
Steps [](#argument){.pf-ref} and [](#vanishes){.pf-ref} give $N_{0}-N_{\infty}=0$, that is $N_{0}=N_{\infty}$.
:::

:::

:::
:::
