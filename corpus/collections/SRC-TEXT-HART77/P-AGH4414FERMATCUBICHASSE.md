---
schema: qual/card@1
id: P-AGH4414FERMATCUBICHASSE
kind: problem
title: The primes where the Fermat cubic has Hasse invariant $0$ have density $\frac{1}{2}$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.14 together with Proposition IV.4.21, which identifies
    the Hasse invariant with the coefficient of (xyz)^(p-1) in the (p-1)-st
    power of a homogeneous cubic equation. Cross-checked the resulting
    congruence criterion with the standard supersingularity criterion for j=0.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
The Fermat curve $X: x^3+y^3=z^3$ gives a nonsingular curve in characteristic $p$ for every $p \neq 3$.
Determine the set $\mfp=\ts{p \neq 3 \st X_{(p)} \text{ has Hasse invariant } 0}$, and observe (modulo Dirichlet's theorem) that it is a set of primes of density $\frac{1}{2}$.
:::

::: {.solution}
Write the homogeneous equation as
$$
F=x^3+y^3-z^3.
$$

::: pf

::: {.pf-step #s1}

By Proposition IV.4.21, the Hasse invariant of $X_{(p)}$ is nonzero
if and only if the coefficient of
$$
(xyz)^{p-1}
$$
in $F^{p-1}$ is nonzero modulo $p$.

::: pf-proof

This is exactly Proposition IV.4.21 applied to the plane cubic $F=0$.

:::

:::

::: {.pf-step #s2}

If $p\equiv2\pmod3$, then the coefficient in step [](#s1){.pf-ref} is zero.

::: pf-proof

Every monomial occurring in
$$
(x^3+y^3-z^3)^{p-1}
$$
has each exponent divisible by $3$. For the monomial
$$
x^{p-1}y^{p-1}z^{p-1}
$$
to occur, one must therefore have
$$
3\mid p-1.
$$
If $p\equiv2\pmod3$, this is impossible. Hence the required coefficient is
zero, so the Hasse invariant vanishes.

:::

:::

::: {.pf-step #s3}

If $p\equiv1\pmod3$, then the coefficient in step [](#s1){.pf-ref} is nonzero.

::: pf-proof

Put
$$
m=\frac{p-1}{3}.
$$
There is exactly one way to obtain
$$
x^{p-1}y^{p-1}z^{p-1}=x^{3m}y^{3m}z^{3m}
$$
from the multinomial expansion: choose $x^3$, $y^3$, and $-z^3$ each
$m$ times. Its coefficient is
$$
(-1)^m\frac{(p-1)!}{(m!)^3}.
$$
Since $0<m<p$, neither $m!$ nor $(p-1)!$ is divisible by $p$. Therefore
this coefficient is nonzero in $\FF_p$, and so the Hasse invariant is
nonzero.

:::

:::

::: {.pf-step #s4}

Consequently
$$
\boxed{
\mfp=\{p\text{ prime}:p\equiv2\pmod3\}.
}
$$

::: pf-proof

The excluded prime is $p=3$. Every other prime is congruent to $1$ or $2$
modulo $3$. Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that the Hasse invariant vanishes exactly
in the second residue class. This includes $p=2$.

:::

:::

::: {.pf-step #s5}

The set $\mfp$ has density $1/2$.

::: pf-proof

By Dirichlet's theorem on primes in arithmetic progressions, the primes are
equidistributed between the two reduced residue classes $1$ and $2$ modulo
$3$. The single excluded prime $3$ has density zero. Hence
$$
\delta(\mfp)=\frac{1}{\varphi(3)}=\frac12.
$$

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} determine the required set of primes and its density.

:::

:::

:::
