---
schema: qual/card@1
id: E-HAT-4.2-7
kind: problem
title: "CW complexes with prescribed homotopy groups"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Construct a CW complex $X$ with prescribed homotopy groups $\pi_i(X)$ and prescribed actions of $\pi_1(X)$ on the $\pi_i(X)$'s.
:::

::: {.solution}
Let the prescribed fundamental group be \(G_1\). For \(i>1\), the prescribed group \(G_i\) is necessarily abelian, and suppose we are given a homomorphism
\[
\rho_i:G_1\to\operatorname{Aut}(G_i)
\]
for each \(i>1\).

Choose functorial CW or simplicial models \(K(G_i,i)\). Functoriality lets each automorphism of \(G_i\) act on \(K(G_i,i)\), so \(\rho_i\) gives a \(G_1\)-action on this Eilenberg--MacLane space. Form
\[
F=\prod_{i>1}K(G_i,i)
\]
with the diagonal \(G_1\)-action. Replace the product by the standard weak product CW model if desired; it has
\[
\pi_i(F)\cong G_i\qquad(i>1),
\quad
\pi_1(F)=0.
\]

Let \(EG_1\) be a contractible free \(G_1\)-CW complex and define the Borel construction
\[
X=EG_1\times_{G_1}F.
\]
There is a fiber bundle
\[
F\longrightarrow X\longrightarrow BG_1=K(G_1,1).
\]
Since \(F\) is simply connected, the long exact homotopy sequence gives
\[
\pi_1(X)\cong G_1,
\qquad
\pi_i(X)\cong\pi_i(F)\cong G_i\quad(i>1).
\]
The universal cover is \(EG_1\times F\simeq F\), and a deck transformation \(g\in G_1\) acts on the \(i\)-th homotopy group exactly through the chosen action \(\rho_i(g)\). Hence
\[
\boxed{X\text{ realizes all the prescribed homotopy groups and prescribed }\pi_1\text{-actions}.}
\]
:::
