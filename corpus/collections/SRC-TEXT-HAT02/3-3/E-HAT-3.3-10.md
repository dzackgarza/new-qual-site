---
schema: qual/card@1
id: E-HAT-3.3-10
kind: problem
title: "Degree 1 implies surjection on $\\pi_1$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that for a degree 1 map $f: M \to N$ of connected closed orientable manifolds, the induced map $f_*: \pi_1 M \to \pi_1 N$ is surjective, hence also $f_*: H_1(M) \to H_1(N)$.
:::

::: {.solution}
Let
\[
H=\operatorname{Im}\bigl(f_*:\pi_1(M)\to\pi_1(N)\bigr).
\]
Let
\[
p:\widetilde N\to N
\]
be the connected covering corresponding to $H$. By the lifting criterion, $f$ lifts to
\[
\widetilde f:M\to\widetilde N,
\qquad p\circ\widetilde f=f.
\]

If $p$ has infinitely many sheets, then $\widetilde N$ is a connected noncompact $n$-manifold. Hence
\[
H_n(\widetilde N;\mathbb Z)=0.
\]
Therefore
\[
f_*[M]=p_*\widetilde f_*[M]=0,
\]
contradicting $\deg f=1$.

Thus $p$ is finite-sheeted, say of degree $d=[\pi_1(N):H]$. Since $N$ is orientable, so is $\widetilde N$, and Exercise 9 gives
\[
|\deg p|=d.
\]
Degrees multiply under composition, so
\[
1=|\deg f|=|\deg p|\,|\deg\widetilde f|=d\,|\deg\widetilde f|.
\]
Hence $d=1$. Therefore $H=\pi_1(N)$ and
\[
\boxed{f_*:\pi_1(M)\twoheadrightarrow\pi_1(N)}.
\]
Passing to abelianizations gives the surjection
\[
f_*:H_1(M)\twoheadrightarrow H_1(N).
\]
:::
