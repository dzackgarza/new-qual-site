---
schema: qual/card@1
id: P-OEFYN
kind: problem
title: "Compact operators are norm limits of finite-rank operators"
classification:
  areas:
  - real-analysis
  topics:
  - Compact Operators
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the Fall 2014 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

3. Let X and Y be Hilbert spaces and $L : X \to Y$ be a bounded linear operator.
   Prove that the following two conditions are equivalent:

(a) The image $L ( \mathbf { B } )$ of the unit ball in X has compact closure in $Y .$

(b) There is a sequence of bounded linear operators $\{ L _ { n } : X \to Y \}$ such that the image of $L _ { n } ( X )$ is finite dimensional and such that $| | L _ { n } - L | |  0$ . (Here, || · || is the operator norm.)

::: solution
<1>1. Assume (a) and approximate $L(B)$ by a finite-dimensional subspace.
::: proof
Let $B$ be the closed unit ball of $X$, and assume
\[
K:=\overline{L(B)}
\]
is compact in $Y$.

Fix $n\ge1$. By compactness, choose points
\[
y_1,\dots,y_{N_n}\in K
\]
such that
\[
K\subseteq\bigcup_{j=1}^{N_n}B_Y(y_j,1/n).
\]
Let
\[
Y_n:=\operatorname{span}\{y_1,\dots,y_{N_n}\}.
\]
This is finite dimensional, hence closed. Let $P_n:Y\to Y_n$ be the orthogonal projection and define
\[
L_n:=P_nL.
\]
Then $L_n$ is bounded and $L_n(X)\subseteq Y_n$, so $L_n$ has finite-dimensional range.
:::

<1>2. Prove $L_n\to L$ in operator norm.
::: proof
If $\|x\|\le1$, then $Lx\in K$, so there is some $j$ with
\[
\|Lx-y_j\|<1/n.
\]
Because $P_nLx$ is the best approximation to $Lx$ from the subspace $Y_n$,
\[
\|Lx-P_nLx\|
\le \|Lx-y_j\|<1/n.
\]
Hence
\[
\|L-L_n\|
=\sup_{\|x\|\le1}\|(I-P_n)Lx\|
\le\frac1n.
\]
Thus $\|L-L_n\|\to0$, proving (b).
:::

<1>3. Assume (b) and prove that $L(B)$ is relatively compact.
::: proof
Suppose $L_n$ has finite-dimensional range and
\[
\|L_n-L\|\longrightarrow0.
\]
Fix $\varepsilon>0$ and choose $n$ so that
\[
\|L-L_n\|<\varepsilon/3.
\]
The set $L_n(B)$ is bounded in the finite-dimensional space $L_n(X)$, so its closure is compact and therefore totally bounded. Hence there are points
\[
z_1,\dots,z_N\in Y
\]
such that
\[
L_n(B)\subseteq\bigcup_{j=1}^N B_Y(z_j,\varepsilon/3).
\]

For every $x\in B$, choose $j$ with
\[
\|L_nx-z_j\|<\varepsilon/3.
\]
Then
\[
\|Lx-z_j\|
\le\|(L-L_n)x\|+\|L_nx-z_j\|
<\frac{2\varepsilon}{3}<\varepsilon.
\]
Thus $L(B)$ is totally bounded. Its closure is also totally bounded; since $Y$ is complete, the closure of a totally bounded set is compact. Therefore
\[
\overline{L(B)}
\]
is compact, proving (a).
:::
:::
