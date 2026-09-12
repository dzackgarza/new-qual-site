---
schema: qual/card@1
id: E-SS8.EX-2
kind: problem
title: "Supppose  is holomorphic near  and  , whi"
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
2. Supppose $F ( z )$ is holomorphic near $z = z _ { 0 }$ and $F ( z _ { 0 } ) = F ^ { \prime } ( z _ { 0 } ) = 0$ , while $F ^ { \prime \prime } ( z _ { 0 } ) \neq 0$ . Show that there are two curves $\Gamma _ { 1 }$ and $\Gamma _ { 2 }$ that pass through z<sub>0</sub>, are orthogonal at $z _ { 0 }$ , and so that $F$ restricted to $\Gamma _ { 1 }$ is real and has a minimum at $z _ { \mathrm { 0 } }$ , while $F$ restricted to $\Gamma _ { 2 }$ is also real but has a maximum at $z _ { 0 }$

[Hint: Write $F ( z ) = ( g ( z ) ) ^ { 2 }$ for $z \ \mathrm { n e a r } \ z _ { 0 }$ , and consider the mapping $z \mapsto g ( z )$ and its inverse.]
:::

::: solution
Since $F$ has a zero of order exactly two at $z_0$, there is a holomorphic function $h$ near $z_0$ such that
\[
F(z)=(z-z_0)^2h(z),\qquad h(z_0)=\frac{F''(z_0)}2\ne0.
\]
After shrinking the neighborhood, $h$ has no zeros and therefore admits a holomorphic square root $q$. Set
\[
g(z)=(z-z_0)q(z).
\]
Then $F=g^2$, $g(z_0)=0$, and $g'(z_0)=q(z_0)\ne0$. By the holomorphic inverse-function theorem, after shrinking once more, $g$ is biholomorphic from a neighborhood $U$ of $z_0$ onto a disc $V$ centered at $0$.

Let
\[
\Gamma_1=g^{-1}(V\cap\mathbb R),
\qquad
\Gamma_2=g^{-1}(V\cap i\mathbb R).
\]
These are smooth curves through $z_0$. On $\Gamma_1$, write $g(z)=t\in\mathbb R$; then
\[
F(z)=t^2\ge0=F(z_0),
\]
so $F$ is real there and has a strict local minimum at $z_0$. On $\Gamma_2$, write $g(z)=it$ with $t\in\mathbb R$; then
\[
F(z)=-t^2\le0=F(z_0),
\]
so $F$ is real there and has a strict local maximum at $z_0$.

Finally, a conformal map preserves angles. The real and imaginary axes in the $g$-plane meet orthogonally at $0$, and $g^{-1}$ is conformal at $0$ because $(g^{-1})'(0)\ne0$. Hence $\Gamma_1$ and $\Gamma_2$ meet orthogonally at $z_0$.
:::
