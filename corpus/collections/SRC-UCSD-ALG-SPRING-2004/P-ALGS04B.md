---
schema: qual/card@1
id: P-ALGS04B
kind: problem
title: "Sylow 17-subgroups and elements of order 17 in GL(2, Z_17)"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $G$ be the group of $2 \times 2$ invertible matrices with entries in the finite field $\mathbb{Z}_p$.
Then $|G| = (p-1)^2 p(p+1)$.
Assume that $p = 17$, so $|G| = 2^9 \cdot 3^2 \cdot 17$.

(a) Let $x$ be an element of $G$ of order 17. Prove that $x$ is conjugate to an element of the form $\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$.

(b) Prove that $G$ contains 18 Sylow 17-subgroups.

Hint: Use the fact that the upper triangular matrices contain a Sylow 17-subgroup as a normal subgroup.

(c) How many elements in $G$ have order 17?
:::

::: {.solution}
<1>1. Let
\[
U=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb F_{17}\right\}.
\]
Then \(U\) is a Sylow \(17\)-subgroup of \(G=\mathrm{GL}_2(\mathbb F_{17})\).
::: {.proof}
The map \(b\mapsto \begin{pmatrix}1&b\\0&1\end{pmatrix}\) identifies \(U\) with the additive group of \(\mathbb F_{17}\), so \(|U|=17\). Since \(|G|=16^2\cdot17\cdot18\) has exactly one factor of \(17\), \(U\) is Sylow.
:::

<1>2. If \(x\in G\) has order \(17\), then \(x\) is conjugate to \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\), hence to a matrix of the required form.
::: {.proof}
Because \(x^{17}=I\), the minimal polynomial of \(x\) divides
\[
t^{17}-1=(t-1)^{17}
\]
in characteristic \(17\). Thus the only eigenvalue of \(x\) is \(1\). Since \(x\neq I\) and \(x\) is \(2\times2\), its minimal polynomial is \((t-1)^2\), so its Jordan form is the single block \(J_2(1)=\begin{pmatrix}1&1\\0&1\end{pmatrix}\).
:::

<1>3. Let \(B\le G\) be the subgroup of invertible upper-triangular matrices. Then \(N_G(U)=B\).
::: {.proof}
The subgroup \(B\) normalizes \(U\), because for \(g=\begin{pmatrix}a&c\\0&d\end{pmatrix}\in B\),
\[
g\begin{pmatrix}1&b\\0&1\end{pmatrix}g^{-1}
=\begin{pmatrix}1&(a/d)b\\0&1\end{pmatrix}\in U.
\]
Conversely, the common fixed subspace of \(U\) on \(\mathbb F_{17}^2\) is exactly the line \(L=\mathbb F_{17}e_1\). If \(g\in N_G(U)\), then \(g\) must carry the common fixed subspace of \(U\) to itself, so \(gL=L\). Hence \(g\) is upper triangular, i.e. \(g\in B\).
:::

<1>4. The number of Sylow \(17\)-subgroups is \(18\).
::: {.proof}
Sylow conjugacy identifies the set of Sylow \(17\)-subgroups with the conjugacy orbit of \(U\), so
\[
n_{17}=[G:N_G(U)]=[G:B].
\]
Now \(|B|=16^2\cdot17\), while \(|G|=16^2\cdot17\cdot18\). Therefore
\[
n_{17}=\frac{|G|}{|B|}=18.
\]
:::

<1>5. Exactly \(288\) elements of \(G\) have order \(17\).
::: {.proof}
Every nonidentity element of a Sylow \(17\)-subgroup has order \(17\), and two distinct subgroups of prime order intersect only in the identity. Thus the \(18\) Sylow subgroups contribute disjoint sets of \(16\) nonidentity elements, giving
\[
18\cdot16=288.
\]
:::
:::
