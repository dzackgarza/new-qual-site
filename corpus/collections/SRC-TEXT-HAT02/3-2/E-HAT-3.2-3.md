---
schema: qual/card@1
id: E-HAT-3.2-3
kind: problem
title: Maps $\RP^n\to\RP^m$ for $n>m$ and the Borsuk--Ulam theorem
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both parts: over $\ZZ_2$, $f^*(\alpha_m)=\alpha_n$ forces
    $0=f^*(\alpha_m^{m+1})=\alpha_n^{m+1}\ne0$ when $m+1\le n$, and for $\CP^n\to\CP^m$ the same
    computation gives $d^{m+1}\beta_n^{m+1}=0$ in a torsion-free group, so $d=0$; the Borsuk-Ulam
    half handles $n=0$ and $n=1$ separately and otherwise uses the equivariant $g$, whose induced
    map on $\RP^n\to\RP^{n-1}$ is nontrivial on $H^1(\ZZ_2)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 3 (p.229) with both parts, including the printed display defining g and the inequality f(x) != f(-x). Rechecked (a): over Z_2 the ring is Z_2[alpha]/(alpha^{m+1}) by Theorem 3.19 p.220, so f^* alpha_m = alpha_n forces 0 = f^*(alpha_m^{m+1}) = alpha_n^{m+1} != 0 when m+1 <= n; over Z the ring is Z[beta]/(beta^{m+1}) by Example 3.12 p.213, so d^{m+1} beta_n^{m+1} = 0 in the torsion-free group H^{2m+2} forces d = 0. Rechecked (b): the antipodal-equivariant g descends to RP^n -> RP^{n-1}, and the loop joining antipodal points upstairs projects to the nontrivial loop, so (a) applies. Citations added for Proposition 3.10 p.210 (f^* a ring map), Theorem 3.19 p.220 and Example 3.12 p.213. Not covered: the n = 0 and n = 1 cases of (b) are argued separately, as the card states.
---

::: {.problem}
(a) Using the cup product structure, show there is no map $\RP^n \to \RP^m$ inducing a nontrivial map $H^1(\RP^m; \ZZ_2) \to H^1(\RP^n; \ZZ_2)$ if $n > m$.
What is the corresponding result for maps $\CP^n \to \CP^m$?

(b) Prove the Borsuk–Ulam theorem by the following argument.
Suppose on the contrary that $f: S^n \to \RR^n$ satisfies $f(x) \neq f(-x)$ for all $x$.
Then define $g: S^n \to S^{n-1}$ by $g(x) = \bigl(f(x) - f(-x)\bigr) / \norm{f(x) - f(-x)}$, so $g(-x) = -g(x)$ and $g$ induces a map $\RP^n \to \RP^{n-1}$.
Show that part (a) applies to this map.
:::

::: {.solution}
With $\ZZ_2$ coefficients, Theorem 3.19 (p.220) gives
$$
H^*(\RP^r;\ZZ_2)\cong
\ZZ_2[\alpha]/(\alpha^{r+1}),\qquad \gradeddegree{\alpha}=1.
$$
Suppose $f:\RP^n\to\RP^m$ with $n>m$ induces a nonzero map on $H^1$. Since both $H^1$ groups are one-dimensional, if $\alpha_m,\alpha_n$ denote the generators then
$$
f^*(\alpha_m)=\alpha_n.
$$
Since $f^*$ is a ring homomorphism (Proposition 3.10, p.210), $f^*(\alpha_m^{m+1})=(f^*\alpha_m)^{m+1}$, and $\alpha_m^{m+1}=0$ because $m+1>m$. Hence
$$
0=f^*(\alpha_m^{m+1})=\alpha_n^{m+1},
$$
contradicting $m+1\le n$, since $\alpha_n^{m+1}\ne0$. Thus every such map is zero on $H^1$.

Similarly, by Example 3.12 (p.213),
$$
H^*(\CP^r;\ZZ)\cong
\ZZ[\beta]/(\beta^{r+1}),\qquad \gradeddegree{\beta}=2.
$$
If $n>m$ and $f:\CP^n\to\CP^m$ has $f^*(\beta_m)=d\beta_n$, then
$$
0=f^*(\beta_m^{m+1})=d^{m+1}\beta_n^{m+1}.
$$
Since $H^{2m+2}(\CP^n;\ZZ)$ is torsion-free and $\beta_n^{m+1}\ne0$, this forces $d=0$. Hence $f^*:H^2\to H^2$ is zero.

For $n=0$, the target $\RR^0$ is a point, so the theorem is immediate. For $n=1$, choose a path in $S^1$ from $x$ to $-x$. The continuous real function $y\mapsto f(y)-f(-y)$ has opposite values at the endpoints, so it vanishes somewhere. Now let $n\ge2$ and suppose $f:S^n\to\RR^n$ satisfies $f(x)\ne f(-x)$ for all $x$. Then
$$
g(x)=\frac{f(x)-f(-x)}{\norm{f(x)-f(-x)}}
$$
defines an antipodal-equivariant map $g:S^n\to S^{n-1}$, so it descends to
$$
\bar g:\RP^n\to\RP^{n-1}.
$$
The map $\bar g$ is nontrivial on $H^1(-;\ZZ_2)$: on fundamental groups it sends the nontrivial loop in $\RP^n$ to the nontrivial loop in $\RP^{n-1}$, because an equivariant lift joins antipodal endpoints upstairs. This contradicts the first part with $m=n-1$. Therefore some $x$ satisfies $f(x)=f(-x)$.
:::
