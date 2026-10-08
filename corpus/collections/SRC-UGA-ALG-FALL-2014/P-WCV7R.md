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
Give a careful proof that the polynomial ring $\mathbb{C}[x, y]$ is not a principal ideal domain (PID).
:::

::: {.solution}
<1>1. The ideal $I=(x,y)$ is proper in $\mathbb C[x,y]$.

::: {.proof}
Evaluation at the origin is a surjective ring homomorphism
\[
\operatorname{ev}_{(0,0)}:\mathbb C[x,y]\to\mathbb C,\qquad f\mapsto f(0,0).
\]
Its kernel consists of polynomials with zero constant coefficient, which is precisely $(x,y)$. The quotient by $I$ is therefore the nonzero field $\mathbb C$, so $I$ is proper.
:::

<1>2. The ideal $I$ is not principal.

::: {.proof}
Suppose $I=(f)$. Since $x\in I$, the polynomial $f$ divides $x$. As $\mathbb C[x,y]$ is a polynomial ring over a field, it is a unique factorization domain and $x$ is irreducible; hence $f$ is either a unit or an associate of $x$. The unit case contradicts properness from step <1>1. In the other case $I=(x)$, yet $y\in I$ would imply $y=xh(x,y)$ for a polynomial $h$, which is impossible after evaluation at $x=0$. Thus $I$ is not principal.
:::

<1>3. The ring $\mathbb C[x,y]$ is not a principal ideal domain.

::: {.proof}
Step <1>2 exhibits a non-principal ideal in this integral domain. Thus it fails the defining property of a principal ideal domain.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the assertion.
:::
:::
