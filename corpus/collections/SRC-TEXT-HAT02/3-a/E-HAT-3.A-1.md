---
schema: qual/card@1
id: E-HAT-3.A-1
kind: problem
title: "Euler characteristic is independent of coefficient field"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Use the universal coefficient theorem to show that if $H_*(X; \mathbb{Z})$ is finitely generated, so the Euler characteristic $\chi(X) = \sum_n (-1)^n \operatorname{rank} H_n(X; \mathbb{Z})$ is defined, then for any coefficient field $F$ we have $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$.
:::

::: {.solution}
Write each finitely generated integral homology group as
\[
H_n(X;\mathbb Z)\cong \mathbb Z^{r_n}\oplus T_n,
\]
with $T_n$ finite. We compare the alternating sum of the dimensions of homology over a field $F$ with $\sum(-1)^nr_n$.

If $\operatorname{char}F=0$, then $F$ is torsionfree as a $\mathbb Z$-module, so the homology universal coefficient theorem gives
\[
H_n(X;F)\cong H_n(X;\mathbb Z)\otimes F\cong F^{r_n}.
\]
Thus $\dim_FH_n(X;F)=r_n$ in every degree.

Now suppose $\operatorname{char}F=p$. Since $F$ is a vector space over $\mathbb F_p$, it is enough to compute with $\mathbb F_p$ and then extend scalars. Let
\[
t_n=\dim_{\mathbb F_p}(T_n/pT_n).
\]
For a finite abelian group the $p$-torsion subgroup $T_n[p]$ has the same $\mathbb F_p$-dimension $t_n$. The universal coefficient short exact sequence gives
\[
0\to H_n(X;\mathbb Z)\otimes\mathbb F_p
\to H_n(X;\mathbb F_p)
\to \operatorname{Tor}(H_{n-1}(X;\mathbb Z),\mathbb F_p)\to0.
\]
Hence
\[
\dim_{\mathbb F_p}H_n(X;\mathbb F_p)=r_n+t_n+t_{n-1}.
\]
Taking the alternating sum, the two torsion contributions cancel:
\[
\sum_n(-1)^n(t_n+t_{n-1})=0.
\]
Therefore
\[
\sum_n(-1)^n\dim_FH_n(X;F)
=\sum_n(-1)^nr_n
=\chi(X).
\]
:::
