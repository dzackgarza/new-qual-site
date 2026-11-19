---
schema: qual/card@1
id: E-HAT-3.3-16
kind: problem
title: Associativity of cap product
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 16; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Checked the chain-level identity with Hatcher's conventions on a simplex: capping with
    $\varphi$ then $\psi$ truncates the simplex twice, which is the same as capping once with
    $\varphi\smile\psi$, and both sides are the product of the two evaluations on the doubly
    truncated simplex. The module statement follows from naturality of the boundary formula.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    One gap closed. The module conclusion listed associativity but not the unit, which the graded
    ring needs; the solution now checks $\sigma\frown 1=\sigma$ on a simplex from the augmentation on
    the front $0$-face. The chain-level identity and the descent to homology are as previously
    checked. Not checked: the boundary formula for the cap product is cited from p.240.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 16 of §3.3, printed p. 259, and
    the printed page is added, the card having had none. Checked the chain-level identity against
    Hatcher's conventions on a simplex: capping with $\varphi$ truncates to $[v_\ell,..,v_k]$ times the
    evaluation, so capping twice truncates twice and multiplies the two evaluations, which is exactly
    the cap product with $\varphi smi \psi$ because the cup product evaluates as the product of the two
    evaluations on $[v_0,..,v_{\ell+m}]$. Checked the descent to homology through the boundary
    formula, associativity on classes, and the unit from the augmentation on the front $0$-face.
---

::: {.problem}
Show that $(\alpha \frown \var\varphi) \frown \\psi = \alpha \frown (\var\varphi \smile \\psi)$ for all $\alpha \in C_k(X; R)$, $\var\varphi \in C^\\ell(X; R)$, and $\\psi \in C^m(X; R)$.
Deduce that cap product makes $H_*(X; R)$ a right $H^*(X; R)$ module.
:::

::: {.solution}
The exercise is §3.3 Exercise 16, printed p. 259.

It is enough to check the identity on a singular $k$-simplex
$$
\sigma=[v_0,\ldots,v_k].
$$
With Hatcher's conventions, for $\var\varphi\in C^\\ell(X;R)$,
$$
\sigma\frown\var\varphi
=
\var\varphi([v_0,\ldots,v_\\ell])
[v_\\ell,\ldots,v_k].
$$
Applying $\frown\\psi$ with $\\psi\in C^m(X;R)$ gives
$$
(\sigma\frown\var\varphi)\frown\\psi
=
\var\varphi([v_0,\ldots,v_\\ell])
\\psi([v_\\ell,\ldots,v_{\\ell+m}])
[v_{\\ell+m},\ldots,v_k].
$$
On the other hand, the cup product is
$$
(\var\varphi\smile\\psi)([v_0,\ldots,v_{\\ell+m}])
=
\var\varphi([v_0,\ldots,v_\\ell])
\\psi([v_\\ell,\ldots,v_{\\ell+m}]),
$$
so
$$
\sigma\frown(\var\varphi\smile\\psi)
=
\var\varphi([v_0,\ldots,v_\\ell])
\\psi([v_\\ell,\ldots,v_{\\ell+m}])
[v_{\\ell+m},\ldots,v_k].
$$
The two expressions are identical. By linearity,
$$
\boxed{(\alpha\frown\var\varphi)\frown\\psi
=\alpha\frown(\var\varphi\smile\\psi)}
$$
for every chain $\alpha$.

The boundary formula for cap product implies that a cycle capped with a cocycle is a cycle, and changing either by a boundary or coboundary changes the cap product by a boundary. Hence cap product descends to
$$
H_k(X;R)\times H^\\ell(X;R)\longrightarrow H_{k-\\ell}(X;R).
$$
The chain-level identity then gives on homology
$$
([\alpha]\frown[\var\varphi])\frown[\\psi]
=[\alpha]\frown([\var\varphi]\smile[\\psi]),
$$
and the unit in $H^0(X;R)$ acts as the identity: on a $k$-simplex $\sigma$, $\sigma\frown 1=\sigma$ because the augmentation on the front $0$-face is the identity, so $H_*(X;R)$ is a right module over the graded ring $H^*(X;R)$.
:::
