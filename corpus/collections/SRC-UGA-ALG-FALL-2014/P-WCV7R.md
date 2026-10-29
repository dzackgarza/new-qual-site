---
schema: qual/card@1
id: P-WCV7R
kind: problem
title: $\CC[x,y]$ is not a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Polynomials
  - Ideals
relations: []
review: draft
---
::: {.problem}
Give a careful proof that the polynomial ring $\CC[x, y]$ is not a principal ideal domain (PID).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The ideal $I=(x,y)$ is proper in $\CC[x,y]$.

::: pf-proof

Evaluation at the origin is a surjective ring homomorphism
\[
\operatorname{ev}_{(0,0)}:\CC[x,y]\to\CC,\qquad f\mapsto f(0,0).
\]
Its kernel consists of polynomials with zero constant coefficient, which is precisely $(x,y)$. The quotient by $I$ is therefore the nonzero field $\CC$, so $I$ is proper.

:::

:::

::: {.pf-step #s2}

The ideal $I$ is not principal.

::: pf-proof

Suppose $I=(f)$. Since $x\in I$, the polynomial $f$ divides $x$. As $\CC[x,y]$ is a polynomial ring over a field, it is a unique factorization domain and $x$ is irreducible; hence $f$ is either a unit or an associate of $x$. The unit case contradicts properness from step [](#s1){.pf-ref}. In the other case $I=(x)$, yet $y\in I$ would imply $y=xh(x,y)$ for a polynomial $h$, which is impossible after evaluation at $x=0$. Thus $I$ is not principal.

:::

:::

::: {.pf-step #s3}

The ring $\CC[x,y]$ is not a principal ideal domain.

::: pf-proof

Step [](#s2){.pf-ref} exhibits a non-principal ideal in this integral domain. Thus it fails the defining property of a principal ideal domain.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the assertion.

:::

:::

:::
