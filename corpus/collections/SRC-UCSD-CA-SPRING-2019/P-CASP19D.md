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

::: problem
Let $\Omega \neq \mathbb{C}$ be a simply connected region with $a \in \Omega$ and $f$ a one-to-one analytic function from $\Omega$ onto $\mathbb{D}$.
Assume $f(a) = 0$ and $f'(a) > 0$.
Prove that
$$
\inf_{z \in \partial \Omega} |z - a| \leq \frac{1}{f'(a)} \leq \sup_{z \in \partial \Omega} |z - a|.
$$
:::

::: solution
Set
\[
r=\inf_{z\in\partial\Omega}|z-a|,
\qquad
R=\sup_{z\in\partial\Omega}|z-a|.
\]
The disk $D(a,r)$ is contained in $\Omega$. Therefore
\[
F(\zeta)=f(a+r\zeta)
\]
is a holomorphic map from $\mathbb D$ to $\mathbb D$ with $F(0)=0$. Schwarz's
lemma gives
\[
r f'(a)=F'(0)\le1,
\]
so
\[
r\le \frac1{f'(a)}.
\]

For the other inequality, let $g=f^{-1}:\mathbb D\to\Omega$. Then
\[
g(0)=a,
\qquad
g'(0)=\frac1{f'(a)}.
\]
If $R=\infty$, there is nothing to prove. Suppose $R<\infty$. Then
\[
\Omega\subset D(a,R).
\]
Indeed, if $\Omega$ met the exterior of $\overline{D(a,R)}$, then, because no
boundary point of $\Omega$ lies there, the connected set
$\mathbb C\setminus\overline{D(a,R)}$ would be contained in $\Omega$.
Consequently $\mathbb C\setminus\Omega$ would be a nonempty compact set.
But then the complement of $\Omega$ in the Riemann sphere would be the
disjoint union $(\mathbb C\setminus\Omega)\cup\{\infty\}$, contradicting the
standard characterization of simply connected proper plane domains by
connectedness of their complement in the sphere. Hence
\[
G(\zeta)=\frac{g(\zeta)-a}{R}
\]
maps $\mathbb D$ into itself and satisfies $G(0)=0$. Schwarz's lemma yields
\[
\frac1{R f'(a)}=|G'(0)|\le1.
\]
Thus
\[
\boxed{r\le \frac1{f'(a)}\le R}.
\]
:::
