---
schema: qual/card@1
id: E-SS8.EX-24
kind: problem
title: "SS 8.24: Identities among the elliptic integrals K and K-prime"
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

::: exercise
24. The elliptic integrals K and $K ^ { \prime }$ defined for $0 < k < 1$ by

$$
K (k) = \int_ {0} ^ {1} \frac {d x}{((1 - x ^ {2}) (1 - k ^ {2} x ^ {2})) ^ {1 / 2}} \quad \text {and} \quad K ^ {\prime} (k) = \int_ {1} ^ {1 / k} \frac {d x}{((x ^ {2} - 1) (1 - k ^ {2} x ^ {2})) ^ {1 / 2}}
$$

satisfy various interesting identities.
For instance:

(a) Show that if $\tilde { k } ^ { 2 } = 1 - k ^ { 2 }$ and $0 < \tilde { k } < 1$ , then

$$
K ^ {\prime} (k) = K (\tilde {k}).
$$

[Hint: Change variables $x = ( 1 - \tilde { k } ^ { 2 } y ^ { 2 } ) ^ { - 1 / 2 }$ in the integral defining $K ^ { \prime } ( k ) . ]$

(b) Prove that if $\tilde { k } ^ { 2 } = 1 - k ^ { 2 }$ , and $0 < \tilde { k } < 1$ , then

$$
K (k) = \frac {2}{1 + \tilde {k}} K \left(\frac {1 - \tilde {k}}{1 + \tilde {k}}\right).
$$

[Hint: Change variables $x = 2 t / ( 1 + \tilde { k } + ( 1 - \tilde { k } ) t ^ { 2 } ) . ]$

(c) Show that for $0 < k < 1$ one has

$$
K (k) = \frac {\pi}{2} F (1 / 2, 1 / 2, 1; k ^ {2}),
$$

where $F$ the hypergeometric series.
[Hint: This follows from the integral representation for $F$ given in Exercise 9, Chapter 6.]
:::

::: solution
Write $k'^2=1-k^2$, with $0<k'<1$.

For (a), in $K'(k)$ make the substitution
\[
x=(1-k'^2y^2)^{-1/2}.
\]
As $x$ runs from $1$ to $1/k$, $y$ runs from $0$ to $1$. A direct calculation gives
\[
dx=\frac{k'^2y}{(1-k'^2y^2)^{3/2}}\,dy,
\]
\[
x^2-1=\frac{k'^2y^2}{1-k'^2y^2},
\qquad
1-k^2x^2=\frac{k'^2(1-y^2)}{1-k'^2y^2}.
\]
Hence
\[
K'(k)=\int_0^1\frac{dy}{\sqrt{(1-y^2)(1-k'^2y^2)}}=K(k').
\]

For (b), set
\[
x=\frac{2t}{1+k'+(1-k')t^2}.
\]
This maps $[0,1]$ onto $[0,1]$. Put
\[
\kappa=\frac{1-k'}{1+k'}.
\]
Straight substitution and simplification yield
\[
\frac{dx}{\sqrt{(1-x^2)(1-k^2x^2)}}
=\frac{2}{1+k'}\,
\frac{dt}{\sqrt{(1-t^2)(1-\kappa^2t^2)}}.
\]
Therefore
\[
K(k)=\frac2{1+k'}K\left(\frac{1-k'}{1+k'}\right).
\]

For (c), Euler's beta-integral representation of the hypergeometric function gives, for $|u|<1$,
\[
{}_2F_1\left(\frac12,\frac12;1;u\right)
=\frac1\pi\int_0^1 t^{-1/2}(1-t)^{-1/2}(1-ut)^{-1/2}\,dt.
\]
Set $u=k^2$ and then $t=x^2$. Since $dt=2x\,dx$,
\[
{}_2F_1\left(\frac12,\frac12;1;k^2\right)
=\frac2\pi\int_0^1\frac{dx}{\sqrt{(1-x^2)(1-k^2x^2)}}
=\frac2\pi K(k).
\]
Thus
\[
K(k)=\frac\pi2\,{}_2F_1\left(\frac12,\frac12;1;k^2\right).
\]
:::
