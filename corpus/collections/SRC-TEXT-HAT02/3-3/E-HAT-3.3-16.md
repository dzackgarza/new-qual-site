---
schema: qual/card@1
id: E-HAT-3.3-16
kind: problem
title: "Associativity of cap product"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $(\alpha \frown \varphi) \frown \psi = \alpha \frown (\varphi \smile \psi)$ for all $\alpha \in C_k(X; R)$, $\varphi \in C^\ell(X; R)$, and $\psi \in C^m(X; R)$.
Deduce that cap product makes $H_*(X; R)$ a right $H^*(X; R)$ module.
:::

::: {.solution}
It is enough to check the identity on a singular $k$-simplex
\[
\sigma=[v_0,\ldots,v_k].
\]
With Hatcher's conventions, for $\varphi\in C^\ell(X;R)$,
\[
\sigma\frown\varphi
=
\varphi([v_0,\ldots,v_\ell])
[v_\ell,\ldots,v_k].
\]
Applying $\frown\psi$ with $\psi\in C^m(X;R)$ gives
\[
(\sigma\frown\varphi)\frown\psi
=
\varphi([v_0,\ldots,v_\ell])
\psi([v_\ell,\ldots,v_{\ell+m}])
[v_{\ell+m},\ldots,v_k].
\]
On the other hand, the cup product is
\[
(\varphi\smile\psi)([v_0,\ldots,v_{\ell+m}])
=
\varphi([v_0,\ldots,v_\ell])
\psi([v_\ell,\ldots,v_{\ell+m}]),
\]
so
\[
\sigma\frown(\varphi\smile\psi)
=
\varphi([v_0,\ldots,v_\ell])
\psi([v_\ell,\ldots,v_{\ell+m}])
[v_{\ell+m},\ldots,v_k].
\]
The two expressions are identical. By linearity,
\[
\boxed{(\alpha\frown\varphi)\frown\psi
=\alpha\frown(\varphi\smile\psi)}
\]
for every chain $\alpha$.

The boundary formula for cap product implies that a cycle capped with a cocycle is a cycle, and changing either by a boundary or coboundary changes the cap product by a boundary. Hence cap product descends to
\[
H_k(X;R)\times H^\ell(X;R)\longrightarrow H_{k-\ell}(X;R).
\]
The chain-level identity then gives on homology
\[
([\alpha]\frown[\varphi])\frown[\psi]
=[\alpha]\frown([\varphi]\smile[\psi]),
\]
and the unit in $H^0(X;R)$ acts as the identity. Therefore $H_*(X;R)$ is a right module over the graded ring $H^*(X;R)$.
:::
