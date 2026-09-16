---
schema: qual/card@1
id: E-HAT-3.H-5
kind: problem
title: "Cohomology of graphs with group ring coefficients"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

If $X$ is a finite connected graph with $\pi_1(X)$ free on $g > 0$ generators, show that $H^n(X; \mathbb{Z}[\pi_1 X])$ is zero unless $n = 1$, when it is $\mathbb{Z}$ when $g = 1$ and the direct sum of a countably infinite number of $\mathbb{Z}$'s when $g > 1$.
[Use Proposition 3H.5 and compute $H_c^n(\tilde{X})$ as $\varinjlim H^n(\tilde{X}, \tilde{X} - T_i)$ for a suitable sequence of finite subtrees $T_1 \subset T_2 \subset \cdots$ of $\tilde{X}$ with $\bigcup_i T_i = \tilde{X}$.]

::: {.solution}
Let
\[
\pi=\pi_1(X),
\qquad
p:\widetilde X\to X
\]
be the universal cover. Proposition 3H.5 identifies
\[
H^n(X;\mathbb Z[\pi])\cong H_c^n(\widetilde X;\mathbb Z).
\]
Since $X$ is a finite connected graph with free fundamental group of rank $g>0$, $\widetilde X$ is a locally finite tree.

Choose an exhaustion by finite connected subtrees
\[
T_1\subset T_2\subset\cdots,
\qquad
\bigcup_iT_i=\widetilde X.
\]
Compactly supported cohomology is
\[
H_c^n(\widetilde X)
\cong\varinjlim_i H^n(\widetilde X,\widetilde X-T_i).
\]
Because $\widetilde X$ is contractible and one-dimensional, the long exact sequence of the pair gives
\[
H^n(\widetilde X,\widetilde X-T_i)=0\qquad(n\ne1),
\]
while
\[
H^1(\widetilde X,\widetilde X-T_i)
\cong\widetilde H^0(\widetilde X-T_i).
\]
If $c_i$ is the number of components of $\widetilde X-T_i$, this is free abelian of rank $c_i-1$.

If $g=1$, the universal cover is a line. For large interval subtrees $T_i$, the complement has exactly two components, and the transition maps identify the corresponding generators. Hence
\[
H_c^1(\widetilde X)\cong\mathbb Z.
\]

If $g>1$, the universal covering tree has branching. Choose the exhaustion so that each $T_{i+1}$ is obtained by adding a finite layer of adjacent edges. Then the maps
\[
\widetilde H^0(\widetilde X-T_i)\to
\widetilde H^0(\widetilde X-T_{i+1})
\]
are split injections: each old complementary component breaks into finitely many new components, and choosing one distinguished descendant in each component gives a splitting. The ranks $c_i-1$ tend to infinity because the tree has infinitely many ends and branching repeats indefinitely. Thus the direct limit is a free abelian group on a countably infinite set of generators.

Therefore
\[
\boxed{H^n(X;\mathbb Z[\pi])=0\quad(n\ne1),}
\]
and
\[
\boxed{H^1(X;\mathbb Z[\pi])\cong
\begin{cases}
\mathbb Z,&g=1,\\
\bigoplus_{\mathbb N}\mathbb Z,&g>1.
\end{cases}}
\]
:::
