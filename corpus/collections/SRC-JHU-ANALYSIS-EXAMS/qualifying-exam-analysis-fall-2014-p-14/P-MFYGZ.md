---
schema: qual/card@1
id: P-MFYGZ
kind: problem
title: "The Hardy-Littlewood maximal function is weak (1,1)"
classification:
  areas:
  - real-analysis
  topics:
  - Hardy-Littlewood Maximal Function
  - Weak Type Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the Fall 2014 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

2. Let $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ and $M _ { f }$ denote the Hardy-Littlewood maximal function of $f ;$ in other words,

$$
M _ { f } ( x ) = \operatorname* { s u p } _ { B } { \frac { 1 } { m ( B ) } } \int _ { B } | f ( y ) | d y , \quad x \in \mathbb { R } ^ { d }
$$

where the supremum is taken over all balls containing the point x. Prove that

$$
m \big ( \{ x : M _ { f } ( x ) > \alpha \} \big ) \leq \frac { A } { \alpha } | | f | | _ { L ^ { 1 } ( \mathbb { R } ^ { d } ) } , \quad \forall \alpha > 0
$$

where A is a constant depending only on d and $\begin{array} { r } { | | f | | _ { L ^ { 1 } ( \mathbb { R } ^ { d } ) } = \int _ { \mathbb { R } ^ { d } } | f ( x ) | d x . } \end{array}$

::: solution
<1>1. Associate a good ball to every point of the superlevel set.
::: proof
Fix $\alpha>0$ and write
\[
E_\alpha:=\{x\in\mathbb R^d:M_f(x)>\alpha\}.
\]
For every $x\in E_\alpha$, by definition of $M_f(x)$ there is a ball $B_x$ containing $x$ such that
\[
\frac1{m(B_x)}\int_{B_x}|f(y)|\,dy>\alpha.
\]
Hence
\[
\alpha\,m(B_x)<\int_{B_x}|f|\le \|f\|_1.
\]
In particular the radii of all such balls are uniformly bounded in terms of $\alpha$, $d$, and $\|f\|_1$.
:::

<1>2. Apply the $5r$ covering lemma.
::: proof
Apply the $5r$ covering lemma to the family $\{B_x:x\in E_\alpha\}$. There is a finite or countable pairwise disjoint subfamily $\{B_j\}$ such that
\[
E_\alpha\subseteq\bigcup_j 5B_j,
\]
where $5B_j$ denotes the ball with the same center and five times the radius.

Therefore
\[
m(E_\alpha)
\le \sum_j m(5B_j)
=5^d\sum_j m(B_j).
\]
:::

<1>3. Use disjointness and the defining average inequality.
::: proof
For each selected ball,
\[
\alpha\,m(B_j)<\int_{B_j}|f|.
\]
Since the $B_j$ are pairwise disjoint,
\[
\alpha\sum_j m(B_j)
<\sum_j\int_{B_j}|f|
\le\int_{\mathbb R^d}|f|
=\|f\|_1.
\]
Combining this with Step 2 gives
\[
m(E_\alpha)
\le \frac{5^d}{\alpha}\|f\|_1.
\]
Thus the desired estimate holds with, for example,
\[
\boxed{A=5^d.}
\]
:::
:::
