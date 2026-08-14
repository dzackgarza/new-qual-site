---
schema: qual/card@1
id: P-7YAGM
kind: problem
title: "Note that since $\\zeta(\\zeta+\\zeta\\inv) = \\zeta^2 + 1$, we have the r\u2026"
classification:
  areas:
  - algebra
  topics:
  - roots-of-unity
  - field-extensions
  - galois-theory
relations: []
review: draft
---

Note that since $\zeta(\zeta+\zeta\inv) = \zeta^2 + 1$, we have the relation $\zeta^2  - (\zeta+\zeta\inv)\zeta + 1 = 0$.
But then
$$
f(x) = x^2 - (\zeta + \zeta\inv)x + 1
$$

is a polynomial in $\QQ(\zeta + \zeta\inv)$ for which $f(\zeta) = 0$.
Thus $g = \min(\zeta, \QQ(\zeta + \zeta\inv))$ divides $f$, but since $\deg f = 2$ and $\QQ(\zeta + \zeta\inv)$ is totally real, $\zeta\not\in\QQ(\zeta + \zeta\inv)$.
This means that $g$ can not be linear and must have degree at least 2, but the above argument shows that $g$ has degree at *most* 2, so it must be 2. Letting $m = [\QQ(\zeta + \zeta\inv): \QQ]$, we have
\[
\begin{align*}
[\QQ(\zeta) : \QQ] &= [\QQ(\zeta): \QQ(\zeta + \zeta\inv)] [\QQ(\zeta + \zeta\inv) : \QQ] \\
\implies \phi(n) &= 2 m
,\end{align*}
\]

and so $m = \phi(n)/2$ as desired.
