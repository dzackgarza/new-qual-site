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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $G$ be the group of $2 \times 2$ invertible matrices with entries in the finite
field $\mathbb{Z}_p$. Then $|G| = (p-1)^2 p(p+1)$. Assume that $p = 17$, so
$|G| = 2^9 \cdot 3^2 \cdot 17$.

(a) Let $x$ be an element of $G$ of order 17. Prove that $x$ is conjugate to an element
of the form $\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$.

(b) Prove that $G$ contains 18 Sylow 17-subgroups.

Hint: Use the fact that the upper triangular matrices contain a Sylow 17-subgroup as a
normal subgroup.

(c) How many elements in $G$ have order 17?
:::

::: {.solution}
<1>1. Let
\[
U=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb F_{17}\right\}.
\]
Then \(U\cong (\mathbb F_{17},+)\), so \(|U|=17\) and \(U\) is a Sylow \(17\)-subgroup
of \(G=\operatorname{GL}(2,\mathbb F_{17})\).
::: {.proof}
The displayed matrices multiply by adding their upper-right entries. Since \(17\) occurs
to the first power in \(|G|=16^2\cdot17\cdot18\), every subgroup of order \(17\) is
Sylow.
:::

<1>2. If \(x\in G\) has order \(17\), then \(x\) is conjugate to
\(\begin{pmatrix}1&1\\0&1\end{pmatrix}\), hence to a matrix of the required form.
::: {.proof}
In characteristic \(17\),
\[
t^{17}-1=(t-1)^{17}.
\]
Since \(x^{17}=I\), the minimal polynomial \(m_x(t)\) divides \((t-1)^{17}\). Because
\(x\) is a \(2\times2\) matrix, \(\deg m_x\le2\). Also \(x\ne I\), since \(x\) has order
\(17\). Therefore \(m_x(t)=(t-1)^2\). The Jordan form of \(x\) is consequently the
single block \(J_2(1)=\begin{pmatrix}1&1\\0&1\end{pmatrix}\).
:::

<1>3. Let \(B\) be the subgroup of invertible upper-triangular matrices. Then
\(U\trianglelefteq B\), so \(B\le N_G(U)\).
::: {.proof}
For \(g=\begin{pmatrix}a&c\\0&d\end{pmatrix}\in B\), direct multiplication gives
\[
g\begin{pmatrix}1&b\\0&1\end{pmatrix}g^{-1}
 =\begin{pmatrix}1&(a/d)b\\0&1\end{pmatrix}\in U.
\]
Thus \(gUg^{-1}=U\).
:::

<1>4. Conversely, \(N_G(U)\le B\). Hence \(N_G(U)=B\).
::: {.proof}
The common fixed subspace of \(U\) on \(\mathbb F_{17}^2\) is exactly the line
\(L=\mathbb F_{17}e_1\): a vector \((r,s)^T\) is fixed by every
\(\begin{pmatrix}1&b\\0&1\end{pmatrix}\) iff \(bs=0\) for every \(b\), hence iff
\(s=0\).

If \(g\in N_G(U)\), then \(gUg^{-1}=U\), so \(g\) carries the common fixed subspace of
\(U\) to itself. Thus \(gL=L\). The stabilizer of \(L\) in \(G\) is precisely the
upper-triangular subgroup \(B\). Therefore \(g\in B\).
:::

<1>5. The group \(G\) has exactly \(18\) Sylow \(17\)-subgroups.
::: {.proof}
There are \(16\) choices for each nonzero diagonal entry and \(17\) choices for the
upper-right entry, so
\[
|B|=16^2\cdot17.
\]
Sylow subgroups conjugate transitively, and the stabilizer of \(U\) under conjugation is
\(N_G(U)=B\). Hence
\[
n_{17}=[G:N_G(U)]
 =\frac{16^2\cdot17\cdot18}{16^2\cdot17}=18.
\]
:::

<1>6. Exactly \(288\) elements of \(G\) have order \(17\).
::: {.proof}
Every Sylow \(17\)-subgroup is cyclic of order \(17\), so each contains \(16\)
nonidentity elements, all of order \(17\). Two distinct subgroups of order \(17\)
intersect trivially. Therefore the nonidentity elements from the \(18\) Sylow
\(17\)-subgroups are disjoint, giving
\[
18(17-1)=18\cdot16=288.
\]
:::
:::
