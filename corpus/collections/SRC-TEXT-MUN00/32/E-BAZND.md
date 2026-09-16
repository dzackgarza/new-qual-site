---
schema: qual/card@1
id: E-BAZND
kind: problem
title: Uncountable powers of the line are not normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
If $J$ is uncountable, then $\mathbb{R}^J$ is not normal.

Proof.
(This proof is due to A. H. Stone, as adapted in [S-S].) Let $X = (\mathbb{Z}_+)^J$; it will suffice to show that $X$ is not normal, since $X$ is a closed subspace of $\mathbb{R}^J$.
We use functional notation for the elements of $X$, so that the typical element of $X$ is a function $\mathbf{x}: J \to \mathbb{Z}_+$.

(a) If $\mathbf{x} \in X$ and if $B$ is a finite subset of $J$, let $U(\mathbf{x}, B)$ denote the set consisting of all those elements $\mathbf{y}$ of $X$ such that $\mathbf{y}(\alpha) = \mathbf{x}(\alpha)$ for $\alpha \in B$.
Show the sets $U(\mathbf{x}, B)$ are a basis for $X$.

(b) Define $P_n$ to be the subset of $X$ consisting of those $\mathbf{x}$ such that on the set $J - \mathbf{x}^{-1}(n)$, the map $\mathbf{x}$ is injective.
Show that $P_1$ and $P_2$ are closed and disjoint.

(c) Suppose $U$ and $V$ are open sets containing $P_1$ and $P_2$, respectively.
Given a sequence $\alpha_1, \alpha_2, \ldots$ of distinct elements of $J$, and a sequence

$$
0 = n_0 < n_1 < n_2 < \dots
$$

of integers, for each $i \geq 1$ let us set

$$
B_i = \ts{\alpha_1, \dots, \alpha_{n_i}}
$$

and define $\mathbf{x}_i \in X$ by the equations

$$
\begin{array}{ll}
\mathbf{x}_i(\alpha_j) = j & \text{for } 1 \leq j \leq n_{i-1}, \\
\mathbf{x}_i(\alpha) = 1 & \text{for all other values of } \alpha.
\end{array}
$$

Show that one can choose the sequences $\alpha_j$ and $n_j$ so that for each $i$, one has the inclusion

$$
U(\mathbf{x}_i, B_i) \subset U.
$$

[Hint: To begin, note that $\mathbf{x}_1(\alpha) = 1$ for all $\alpha$; now choose $B_1$ so that $U(\mathbf{x}_1, B_1) \subset U$.]

(d) Let $A$ be the set $\ts{\alpha_1, \alpha_2, \ldots}$ constructed in (c). Define $\mathbf{y}: J \to \mathbb{Z}_+$ by the equations

$$
\mathbf{y}(\alpha_j) = j \quad \text{for } \alpha_j \in A,
$$

$$
\mathbf{y}(\alpha) = 2 \quad \text{for all other values of } \alpha.
$$

Choose $B$ so that $U(\mathbf{y}, B) \subset V$.
Then choose $i$ so that $B \cap A$ is contained in the set $B_i$.
Show that

$$
U(\mathbf{x}_{i+1}, B_{i+1}) \cap U(\mathbf{y}, B)
$$

is not empty.
:::

::: {.solution}
Let \(X=(\mathbb Z_+)^J\), with each factor discrete.

(a) In the product topology, a basic open set specifies open conditions in only finitely many coordinates. Since the factors are discrete, we may refine each specified coordinate condition to a singleton. Thus the sets
\[
U(\mathbf x,B)=\{\mathbf y:\mathbf y(\alpha)=\mathbf x(\alpha)\text{ for all }\alpha\in B\},
\]
with \(B\subset J\) finite, form a basis.

(b) The complement of \(P_n\) is open. Indeed, \(\mathbf x\notin P_n\) exactly when there are distinct \(\alpha,\beta\in J\) and an integer \(m\ne n\) such that
\[
\mathbf x(\alpha)=\mathbf x(\beta)=m.
\]
The cylinder imposing these two equalities is an open neighborhood of \(\mathbf x\) contained in \(X\setminus P_n\). Hence \(P_n\) is closed.

The sets \(P_1\) and \(P_2\) are disjoint. If \(\mathbf x\) belonged to both, then no two distinct coordinates could have the same value: a repetition at value \(1\) is forbidden by membership in \(P_2\), a repetition at value \(2\) is forbidden by membership in \(P_1\), and a repetition at any other value is forbidden by both. Thus \(\mathbf x:J\to\mathbb Z_+\) would be injective, impossible because \(J\) is uncountable.

(c) We construct the sequences recursively. For \(i=1\), \(\mathbf x_1\) is the constant function \(1\), hence lies in \(P_1\subset U\). By (a), choose a finite set \(C_1\subset J\) such that
\[
U(\mathbf x_1,C_1)\subset U.
\]
Enumerate the elements of \(C_1\) among distinct points \(\alpha_1,\dots,\alpha_{n_1}\), enlarging if necessary so \(n_1>0\). Then
\[
U(\mathbf x_1,B_1)\subset U(\mathbf x_1,C_1)\subset U.
\]

Suppose \(\alpha_1,\dots,\alpha_{n_{i-1}}\) and \(n_{i-1}\) have been chosen. Define \(\mathbf x_i\) as in the problem. Outside the value \(1\), its values are among \(2,\dots,n_{i-1}\), each occurring at most once, so \(\mathbf x_i\in P_1\subset U\). Choose a finite \(C_i\subset J\) with
\[
U(\mathbf x_i,C_i)\subset U.
\]
Since \(J\) is uncountable and only finitely many \(\alpha_j\) have been used, extend the sequence by finitely many new distinct \(\alpha_j\)'s so that \(C_i\subset B_i=\{\alpha_1,\dots,\alpha_{n_i}\}\) for some \(n_i>n_{i-1}\). Then
\[
U(\mathbf x_i,B_i)\subset U.
\]
This completes the recursion.

(d) The function \(\mathbf y\) lies in \(P_2\): outside the value \(2\), its values on \(A=\{\alpha_j\}\) are distinct, and all points outside \(A\) have value \(2\). Hence \(\mathbf y\in V\). Choose a finite \(B\subset J\) with
\[
U(\mathbf y,B)\subset V.
\]
Because \(B\cap A\) is finite, choose \(i\) such that
\[
B\cap A\subset B_i.
\]

The coordinate prescriptions defining \(U(\mathbf x_{i+1},B_{i+1})\) and \(U(\mathbf y,B)\) are compatible. On \(B\cap B_{i+1}\), every coordinate lies in \(B\cap A\subset B_i\), and for \(\alpha_j\in B_i\) both functions take the value \(j\). On coordinates of \(B\setminus A\), only \(\mathbf y\) prescribes a value, and on coordinates of \(B_{i+1}\setminus B\), only \(\mathbf x_{i+1}\) does. Hence one can define a function \(\mathbf z:J\to\mathbb Z_+\) agreeing with both prescriptions on \(B\cup B_{i+1}\), arbitrarily elsewhere. Then
\[
\mathbf z\in U(\mathbf x_{i+1},B_{i+1})\cap U(\mathbf y,B).
\]
Thus every open \(U\supset P_1\) and \(V\supset P_2\) intersect, so the disjoint closed sets \(P_1,P_2\) cannot be separated by disjoint open neighborhoods. Hence \(X\) is not normal.

Finally, \(X=(\mathbb Z_+)^J\) is closed in \(\mathbb R^J\), since
\[
X=\bigcap_{\alpha\in J}\pi_\alpha^{-1}(\mathbb Z_+)
\]
and \(\mathbb Z_+\) is closed in \(\mathbb R\). If \(\mathbb R^J\) were normal, its closed subspace \(X\) would be normal, contradiction. Therefore \(\mathbb R^J\) is not normal for uncountable \(J\).
:::
