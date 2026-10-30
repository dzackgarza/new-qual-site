---
schema: qual/card@1
id: P-CAFA25F
kind: problem
title: 'Constancy of positive harmonic functions on simply connected regions and on $\CC\setminus\theset{0}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
  - Positive Functions
relations: []
review: draft
---

::: {.problem}
(i) Let $G \subset \CC$ be a nonempty simply connected region.
Show that $G = \CC$ if and only if every positive harmonic function $h : G \to \RR$ is constant.

(ii) Let $G = \CC \setminus \{0\}$.
If $h : G \to \RR$ is a positive harmonic function, show that $h$ is constant.
:::

::: {.solution}
(i) First suppose $G=\CC$. Let $h>0$ be harmonic. Since $\CC$ is
simply connected, $h$ has a global harmonic conjugate $v$, and
$$
F=h+iv
$$
is entire with positive real part. The Cayley transform
$$
\frac{F-1}{F+1}
$$
is a bounded entire function, hence constant by Liouville's theorem. Therefore
$F$, and in particular $h$, is constant.

Conversely suppose $G\subsetneq\CC$ is nonempty and simply connected.
By the Riemann mapping theorem there is a biholomorphism
$$
\phi:G\to\DD.
$$
Then
$$
h(z)=\operatorname{Re}\frac{1+\phi(z)}{1-\phi(z)}
$$
is a positive nonconstant harmonic function on $G$. Thus every positive
harmonic function on $G$ is constant exactly when $G=\CC$.

(ii) Let $h>0$ be harmonic on $\CC^*$. Pull it back by the universal
covering map:
$$
H(w)=h(e^w).
$$
Then $H$ is a positive harmonic function on all of $\CC$, so by part (i)
$H$ is constant. Since the exponential map is onto $\CC^*$, $h$ is
constant as well.
:::
