---
schema: qual/card@1
id: E-SS8.EX-9
kind: problem
title: "SS 8.9: An unbounded harmonic function with zero boundary values"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
9. Prove that the function u defined by

$$
u (x, y) = \operatorname{Re} \left(\frac {i + z}{i - z}\right) \quad \text { and } \quad u (0, 1) = 0
$$

is harmonic in the unit disc and vanishes on its boundary.
Note that u is not bounded in D.
:::

::: {.solution}
Let
\[
F(z)=\frac{i+z}{i-z}.
\]
Its only pole is at $z=i$, which lies on $\partial\mathbb D$, so $F$ is holomorphic in $\mathbb D$. Hence
\[
u(z)=\Re F(z)
\]
is harmonic in $\mathbb D$.

If $|z|=1$ and $z\ne i$, then $\bar z=1/z$. A direct computation gives
\[
\overline{F(z)}
=\frac{-i+\bar z}{-i-\bar z}
=\frac{-iz+1}{-iz-1}
=-\frac{i+z}{i-z}
=-F(z).
\]
Thus $F(z)$ is purely imaginary and
\[
u(z)=\Re F(z)=0
\]
on $\partial\mathbb D\setminus\{i\}$. With the stipulated boundary value $u(i)=u(0,1)=0$, the boundary values vanish everywhere.

The function is not bounded in the disc. Along the radius $z=ri$, $0<r<1$,
\[
u(ri)=\Re\frac{i+ri}{i-ri}=\frac{1+r}{1-r}\longrightarrow+\infty
\qquad(r\uparrow1).
\]
So $u$ is harmonic in $\mathbb D$, has zero boundary values, but is unbounded.
:::
