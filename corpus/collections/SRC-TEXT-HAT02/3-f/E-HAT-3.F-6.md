---
schema: qual/card@1
id: E-HAT-3.F-6
kind: problem
title: "$\\operatorname{Ext}(\\mathbb{Z}_{p^\\infty}, \\mathbb{Z}_p)$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $\operatorname{Ext}(\mathbb{Z}_{p^\infty}, \mathbb{Z}_p) \approx \mathbb{Z}_p$.

::: {.solution}
Choose generators $x_n$ of $\mathbb Z_{p^\infty}$ with $x_n$ of order $p^n$ and
\[
p x_{n+1}=x_n.
\]
Let $F_0$ be free on generators $e_1,e_2,\dots$, mapping $e_n\mapsto x_n$. The kernel is free on the relations
\[
r_0=p e_1,
\qquad
r_n=p e_{n+1}-e_n\quad(n\ge1).
\]
Thus we have a free resolution
\[
0\longrightarrow F_1\xrightarrow d F_0
\longrightarrow\mathbb Z_{p^\infty}\longrightarrow0,
\]
where $F_1$ is free on $r_0,r_1,\dots$ and $d$ is given by the displayed formulas.

Apply $\operatorname{Hom}(-,\mathbb Z_p)$. Since Hom out of a direct sum is a product,
\[
\operatorname{Hom}(F_0,\mathbb Z_p)\cong\prod_{n\ge1}\mathbb Z_p,
\qquad
\operatorname{Hom}(F_1,\mathbb Z_p)\cong\prod_{n\ge0}\mathbb Z_p.
\]
If a homomorphism $F_0\to\mathbb Z_p$ is represented by $(a_1,a_2,\dots)$, then $d^*$ sends it to
\[
(0,-a_1,-a_2,-a_3,\dots),
\]
because multiplication by $p$ is zero in $\mathbb Z_p$.
Therefore
\[
\operatorname{im}d^*
=\{(b_0,b_1,b_2,\dots):b_0=0\},
\]
and hence
\[
\operatorname{coker}d^*\cong\mathbb Z_p
\]
by projection onto the $r_0$ coordinate. By the definition of Ext from this free resolution,
\[
\boxed{\operatorname{Ext}(\mathbb Z_{p^\infty},\mathbb Z_p)\cong\mathbb Z_p.}
\]
:::
