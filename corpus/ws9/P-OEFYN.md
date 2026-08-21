---
schema: qual/card@1
id: P-OEFYN
kind: problem
title: Compact operators on Hilbert space are norm limits of finite-rank operators
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Hilbert Spaces
  - Compactness
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $X$ and $Y$ be Hilbert spaces and $L : X \to Y$ be a bounded linear operator.
Prove that the following two conditions are equivalent:

a. The image $L(\mathbf{B})$ of the unit ball in $X$ has compact closure in $Y$.
b. There is a sequence of bounded linear operators $\{L_n : X \to Y\}$ such that the image of $L_n(X)$ is finite dimensional and such that $\|L_n - L\| \to 0$.
(Here, $\|\cdot\|$ is the operator norm.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (b) ⟹ (a): a norm limit of finite-rank operators is compact.
Proof: each $L_n$ is finite-rank, hence compact (its image of the unit ball lies in a finite-dimensional subspace and is bounded, so precompact).
A uniform operator-norm limit of compact operators is compact: given $\epsilon > 0$, pick $n$ with $\|L_n - L\| < \epsilon/3$ and a finite $\epsilon/3$-net $\{y_i\}$ for $L_n(\mathbf B)$; then $\{y_i\}$ is an $\epsilon$-net for $L(\mathbf B)$ (for $x \in \mathbf B$: $\|Lx - y_i\| \le \|Lx - L_nx\| + \|L_nx - y_i\|$). Hence $L(\mathbf B)$ is totally bounded, so its closure is compact.
<1>2. (a) ⟹ (b): construct finite-rank approximants from a net on the image.
Proof: let $K = \overline{L(\mathbf B)}$, compact in $Y$.
For each $n$, cover $K$ by finitely many balls of radius $1/n$ centered at $y_1^{(n)}, \ldots, y_{k_n}^{(n)} \in K$ (total boundedness of $K$). Let $E_n = \mathrm{span}\{y_1^{(n)}, \ldots, y_{k_n}^{(n)}\}$, a finite-dimensional subspace of $Y$, and let $P_n : Y \to E_n$ be the orthogonal projection (defined since $Y$ is a Hilbert space and $E_n$ is closed and finite-dimensional).
Set $L_n = P_n L$; then $L_n$ is bounded and $L_n(X) \subseteq E_n$ is finite-dimensional.
<1>3. $\|L_n - L\| \to 0$.
Proof: for $x \in \mathbf B$, $Lx \in L(\mathbf B) \subseteq K$, so for some $i$: $\|Lx - y_i^{(n)}\| \le 1/n$ with $y_i^{(n)} \in E_n$.
Since $P_n$ is a contraction and fixes $E_n$, \[\|L_nx - Lx\| = \|P_nLx - Lx\| \le \|P_nLx - y_i^{(n)}\| + \|y_i^{(n)} - Lx\| \le 2\|Lx - y_i^{(n)}\| \le \frac{2}{n},\] using $\|P_nz - y\| \le \|z - y\|$ for $y \in E_n$.
Taking the supremum over $x \in \mathbf B$: $\|L_n - L\| \le 2/n \to 0$.
<1>4. Q.E.D.
:::
