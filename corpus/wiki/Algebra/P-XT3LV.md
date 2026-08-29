---
schema: qual/card@1
id: P-XT3LV
kind: problem
title: $[\QQ(\zeta+\zeta^{-1}):\QQ]=\varphi(n)/2$ for a primitive $n$th root of unity
  $\zeta$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

::: problem
Let $x = [\QQ(\zeta + \zeta\inv) : \QQ]$.

Noting that
$$
\zeta(\zeta + \zeta\inv) = \zeta^2 + 1,
$$

if we let
$$
f(x) = x^2 - (\zeta + \zeta\inv)x + 1 \in \QQ(\zeta + \zeta\inv)[x], 
$$
then $f(\zeta) = 0$.

Since $\QQ(\zeta + \zeta\inv) \subset \RR$, $\QQ(\zeta)$ is a proper extension over this field, so if $d \definedas [\QQ(\zeta) : \QQ(\zeta + \zeta\inv)]$ then $d > 1$.
The fact that $\zeta$ is a root of $f$ shows that $d \leq 2$, so $d = 2$.
We also know that $[\QQ(\zeta) : \QQ] = \phi(n)$.

We thus have
\[
\begin{align*}
[\QQ(\zeta) : \QQ] &= [\QQ(\zeta) : \QQ(\zeta + \zeta\inv)] [\QQ(\zeta + \zeta\inv) : \QQ]
\quad\implies\quad  \phi(n) = 2 x 
,\end{align*}
\]

and so $x = \frac{\phi(n)}{2}$ as desired.
$\qed$
:::
