---
schema: qual/card@1
id: P-EMCA6
kind: problem
title: "Riemann mapping theorem uniqueness"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
State the Riemann mapping theorem and prove the uniqueness part.
:::

::: solution
The Riemann mapping theorem states that if $\Omega\subsetneq\mathbb C$ is a
nonempty simply connected domain, then there is a conformal bijection
$f:\Omega\to\mathbb D$.

For the normalized uniqueness statement, fix $a\in\Omega$. There is exactly one
such map satisfying
\[
f(a)=0,\qquad f'(a)>0.
\]
Indeed, suppose $f,g:\Omega\to\mathbb D$ are conformal bijections with these
normalizations. Then
\[
h=g\circ f^{-1}:\mathbb D\to\mathbb D
\]
is an automorphism with $h(0)=0$. Schwarz's lemma applied to $h$ and to
$h^{-1}$ gives $|h(z)|=|z|$ for all $z$, so the equality case of Schwarz's
lemma gives
\[
h(z)=e^{i\theta}z.
\]
By the chain rule,
\[
e^{i\theta}=h'(0)=\frac{g'(a)}{f'(a)}.
\]
The quotient on the right is positive real, while its modulus is $1$; hence it
equals $1$. Thus $h$ is the identity and $g=f$.
:::
