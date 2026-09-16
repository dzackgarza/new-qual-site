---
schema: qual/card@1
id: E-HAT-4.2-22
kind: problem
title: "$H_{n+1}(K(G,n); \\mathbb{Z}) = 0$ for $n > 1$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $H_{n+1}(K(G, n); \mathbb{Z}) = 0$ if $n > 1$.
:::

::: {.solution}
For \(n>1\), choose an \((n-1)\)-connected Moore space \(M(G,n)\), so
\[
\widetilde H_i(M(G,n);\mathbb Z)=
\begin{cases}
G,&i=n,\\
0,&i\ne n.
\end{cases}
\]
By Hurewicz, \(\pi_n(M(G,n))\cong G\).

Construct a \(K(G,n)\) from \(M(G,n)\) by killing \(\pi_{n+1},\pi_{n+2},\dots\) successively. To kill \(\pi_k\) one attaches \((k+1)\)-cells. Thus the first cells added have dimension \(n+2\), and all later cells have still larger dimension. No \((n+1)\)-cells are added.

Initially
\[
H_{n+1}(M(G,n))=0.
\]
Attaching cells of dimension \(n+2\) can only quotient \(H_{n+1}\) by images of new cellular boundaries; it cannot create a new \((n+1)\)-cycle. Cells of still higher dimension do not affect \(H_{n+1}\). Therefore the resulting Eilenberg--MacLane space satisfies
\[
\boxed{H_{n+1}(K(G,n);\mathbb Z)=0\qquad(n>1).}
\]
:::
