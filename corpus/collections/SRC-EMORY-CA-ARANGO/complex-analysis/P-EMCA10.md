---
schema: qual/card@1
id: P-EMCA10
kind: problem
title: "Rouche's theorem and local injectivity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
(a) State Rouche's theorem.

(b) Let $f$ be analytic in a neighborhood of $0$, and satisfying $f'(0) \neq 0$.
Use Rouche's theorem to show that there exists a neighborhood $U$ of $0$ such that $f$ is a bijection in $U$.
:::

::: solution
**Rouché's theorem.** Let $C$ be a positively oriented simple closed contour,
and suppose $f$ and $g$ are holomorphic on a neighborhood of $C$ and its
interior. If
\[
|g(z)|<|f(z)|\qquad(z\in C),
\]
then $f$ and $f+g$ have the same number of zeros inside $C$, counted with
multiplicity.

For the local injectivity statement, replace $f$ by $f-f(0)$, so that
$f(0)=0$ and still $f'(0)\ne0$. Then
\[
f(z)=az+z\varepsilon(z),
\qquad a=f'(0)\ne0,
\qquad \varepsilon(z)\to0.
\]
Choose $r>0$ so small that $f$ is holomorphic on $\overline{B(0,r)}$ and
\[
|\varepsilon(z)|<\frac{|a|}{2}
\qquad (|z|\le r).
\]
Then on $|z|=r$,
\[
|f(z)-az|=|z\varepsilon(z)|<|az|.
\]
Rouché's theorem shows that $f$ and $az$ have the same number of zeros in
$B(0,r)$, namely one, counted with multiplicity. Thus $0$ is the unique zero of
$f$ in this disk.

To prove injectivity, shrink $r$ if necessary so that
\[
|f'(z)-a|<\frac{|a|}{2}
\qquad (|z|<r).
\]
For distinct $z,w\in B(0,r)$, the line segment joining them lies in the disk,
and
\[
f(z)-f(w)=\int_0^1 f'(w+t(z-w))(z-w)\,dt.
\]
Hence
\[
\left|\frac{f(z)-f(w)}{z-w}-a\right|
\le \frac{|a|}{2},
\]
so $(f(z)-f(w))/(z-w)\ne0$ and therefore $f(z)\ne f(w)$. Thus $f$ is injective
on $U=B(0,r)$. Since a nonconstant holomorphic map is open, it is a bijection
from $U$ onto the open set $f(U)$.
:::
