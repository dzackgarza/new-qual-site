---
schema: qual/card@1
id: P-CASP19D
kind: problem
title: "Growth bound for the derivative of a conformal map via distance to boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Riemann Mapping Theorem
  - Derivative Estimates
relations: []
review: draft
---

::: {.problem}
Let $\Omega \neq \CC$ be a simply connected region with $a \in \Omega$ and $f$ a one-to-one analytic function from $\Omega$ onto $\DD$.
Assume $f(a) = 0$ and $f'(a) > 0$.
Prove that
$$
\inf_{z \in \partial \Omega} \abs{z - a} \leq \frac{1}{f'(a)} \leq \sup_{z \in \partial \Omega} \abs{z - a}.
$$
:::

::: {.solution}
Set
$$
r=\inf_{z\in\partial\Omega}\abs{z-a},
\qquad
R=\sup_{z\in\partial\Omega}\abs{z-a}.
$$
The disk $D(a,r)$ is contained in $\Omega$. Therefore
$$
F(\zeta)=f(a+r\zeta)
$$
is a holomorphic map from $\DD$ to $\DD$ with $F(0)=0$. Schwarz's
lemma gives
$$
r f'(a)=F'(0)\le1,
$$
so
$$
r\le \frac1{f'(a)}.
$$

For the other inequality, let $g=f^{-1}:\DD\to\Omega$. Then
$$
g(0)=a,
\qquad
g'(0)=\frac1{f'(a)}.
$$
If $R=\infty$, there is nothing to prove. Suppose $R<\infty$. Then
$$
\Omega\subset D(a,R).
$$
Indeed, if $\Omega$ met the exterior of $\overline{D(a,R)}$, then, because no
boundary point of $\Omega$ lies there, the connected set
$\CC\setminus\overline{D(a,R)}$ would be contained in $\Omega$.
Consequently $\CC\setminus\Omega$ would be a nonempty compact set.
But then the complement of $\Omega$ in the Riemann sphere would be the
disjoint union $(\CC\setminus\Omega)\cup\{\infty\}$, contradicting the
standard characterization of simply connected proper plane domains by
connectedness of their complement in the sphere. Hence
$$
G(\zeta)=\frac{g(\zeta)-a}{R}
$$
maps $\DD$ into itself and satisfies $G(0)=0$. Schwarz's lemma yields
$$
\frac1{R f'(a)}=\abs{G'(0)}\le1.
$$
Thus
$$
\boxed{r\le \frac1{f'(a)}\le R}.
$$
:::
