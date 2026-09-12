---
schema: qual/card@1
id: E-HAT-2.2-25
kind: problem
title: Unique Euler characteristic function on finite CW complexes
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 25; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked.
---

Show that for each $n \in \mathbb{Z}$ there is a unique function $\varphi$ assigning an integer to each finite CW complex, such that (a) $\varphi(X) = \varphi(Y)$ if $X$ and $Y$ are homeomorphic, (b) $\varphi(X) = \varphi(A) + \varphi(X/A)$ if $A$ is a subcomplex of $X$, and (c) $\phi(S^0) = n$.
For such a function $\varphi$, show that $\varphi(X) = \varphi(Y)$ if $X \simeq Y$.

::: {.solution}
The unique function is
\[
\boxed{\varphi(X)=n\,\widetilde\chi(X)=n(\chi(X)-1)}
\]
for every nonempty finite CW complex $X$.

<1>1. The axioms force $\varphi(\mathrm{pt})=0$.
::: {.proof}
Take $X=S^0$ and let $A$ be one of its two points. Then $X/A\cong S^0$, so
\[
n=\varphi(S^0)=\varphi(\mathrm{pt})+\varphi(S^0).
\]
Hence $\varphi(\mathrm{pt})=0$.
:::

<1>2. The axioms force $\varphi(D^k)=0$ for every $k\ge1$.
::: {.proof}
Choose a CW decomposition of $D^k$ into two closed $k$-balls $A$ and $B$ meeting along a $(k-1)$-ball, with $A$ a subcomplex. Collapsing $A$ to a point turns the other half-ball into another $k$-ball, so
\[
D^k/A\cong D^k.
\]
By homeomorphism invariance and additivity,
\[
\varphi(D^k)=\varphi(A)+\varphi(D^k/A)=2\varphi(D^k),
\]
hence $\varphi(D^k)=0$.
:::

<1>3. For every $k\ge0$,
\[
\varphi(S^k)=(-1)^k n.
\]
::: {.proof}
The case $k=0$ is axiom (c). For $k\ge1$, regard $S^{k-1}=\partial D^k$ as a subcomplex of $D^k$. Since
\[
D^k/S^{k-1}\cong S^k,
\]
additivity and <1>2 give
\[
0=\varphi(D^k)=\varphi(S^{k-1})+\varphi(S^k).
\]
Thus $\varphi(S^k)=-\varphi(S^{k-1})$, proving the formula inductively.
:::

<1>4. A finite discrete space of $r\ge1$ points has value
\[
(r-1)n.
\]
::: {.proof}
The case $r=1$ is <1>1 and $r=2$ is axiom (c). For $r>2$, choose a two-point subcomplex $A\cong S^0$. Collapsing $A$ to one point leaves a discrete space of $r-1$ points, so induction and additivity give
\[
\varphi(r\text{ points})=n+(r-2)n=(r-1)n.
\]
:::

<1>5. For every finite CW complex $X$,
\[
\varphi(X)=n\widetilde\chi(X).
\]
::: {.proof}
Let $c_k$ be the number of $k$-cells. By <1>4,
\[
\varphi(X^0)=(c_0-1)n.
\]
For $k\ge1$, collapsing $X^{k-1}$ gives
\[
X^k/X^{k-1}\cong\bigvee^{c_k}S^k.
\]
Repeated additivity for wedge summands, together with <1>1 and <1>3, yields
\[
\varphi(X^k/X^{k-1})=c_k(-1)^k n.
\]
Induction over the skeleta therefore gives
\[
\varphi(X)
=n\left((c_0-1)+\sum_{k\ge1}(-1)^kc_k\right)
=n(\chi(X)-1).
\]
This proves uniqueness.
:::

<1>6. The formula $\varphi(X)=n\widetilde\chi(X)$ satisfies axioms (a)--(c).
::: {.proof}
Homeomorphism invariance is clear. For a CW pair $(X,A)$,
\[
\widetilde\chi(X)=\widetilde\chi(A)+\widetilde\chi(X/A),
\]
which follows immediately from cell counts: the quotient has the cells of $X-A$ plus the quotient basepoint. Finally
\[
\widetilde\chi(S^0)=1,
\]
so $\varphi(S^0)=n$. Thus existence holds.
:::

<1>7. The function $\varphi$ is a homotopy invariant.
::: {.proof}
For finite CW complexes,
\[
\chi(X)=\sum_i(-1)^i\dim_{\mathbb Q}H_i(X;\mathbb Q),
\]
so Euler characteristic is preserved by homotopy equivalence. Therefore the reduced Euler characteristic, and hence $\varphi=n\widetilde\chi$, is also preserved. Thus
\[
X\simeq Y\quad\Longrightarrow\quad\varphi(X)=\varphi(Y).
\]
:::
:::
