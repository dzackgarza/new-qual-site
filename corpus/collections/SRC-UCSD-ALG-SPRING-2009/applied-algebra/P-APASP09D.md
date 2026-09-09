---
schema: qual/card@1
id: P-APASP09D
kind: problem
title: "Schur function coefficient from trace of tensor power of a representation"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Restored all three parts from Problem 1 of Part II of the official UCSD Spring 2009 Applied Algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Computed the symmetrizer trace as a complete symmetric function, used Pieri twice for the Schur coefficient, and used Schur-Weyl duality plus the hook-content formula for the Specht multiplicity.
---

::: problem
For $n\ge 1$, let
\[
p_n=\frac{1}{n!}\sum_{\sigma\in S_n}\sigma,
\]
and let $d=\operatorname{diag}(x_1,\ldots,x_N)$, where $V=\mathbb C^N$.
The matrix $d$ acts on each factor of $V^{\otimes n}$, and $S_n$ acts on $V^{\otimes n}$ by permuting tensor factors.

(a) Calculate
\[
\operatorname{Tr}_{V^{\otimes n}}(p_n d^{\otimes n}).
\]

(b) The value of
\[
\operatorname{Tr}_{V^{\otimes 10}}
\bigl((p_4\otimes p_3\otimes p_3)d^{\otimes10}\bigr)
\]
can be written as a linear combination of Schur functions.
Calculate the coefficient of $s_{[6,3,1]}$.

(c) Calculate the multiplicity of the simple $S_{10}$-module $S^{[3,3,3,1]}$ in $V^{\otimes10}$ for $\dim V=N=5$ and for $N=3$.
:::

::: {.solution}
<1>1. The trace in part (a) is
\[
h_n(x_1,\ldots,x_N)=s_{(n)}(x_1,\ldots,x_N).
\]
::: {.proof}
The operator $p_n$ is the averaging idempotent for the $S_n$-action, so its image is
\[
\operatorname{Sym}^n(V)\subseteq V^{\otimes n}.
\]
The operator $d^{\otimes n}$ commutes with the permutation action and hence with $p_n$.
Therefore
\[
\operatorname{Tr}_{V^{\otimes n}}(p_nd^{\otimes n})
=\operatorname{Tr}_{\operatorname{Sym}^n(V)}(d).
\]
A basis of $\operatorname{Sym}^n(V)$ is indexed by weak compositions
\[
a_1+\cdots+a_N=n,
\qquad a_i\ge0,
\]
and the corresponding basis vector has $d$-eigenvalue
\[
x_1^{a_1}\cdots x_N^{a_N}.
\]
Summing these eigenvalues gives the complete homogeneous symmetric function $h_n=s_{(n)}$.
:::

<1>2. The trace in part (b) is the symmetric function
\[
s_{(4)}s_{(3)}s_{(3)}.
\]
::: {.proof}
The operator $p_4\otimes p_3\otimes p_3$ projects
\[
V^{\otimes10}=V^{\otimes4}\otimes V^{\otimes3}\otimes V^{\otimes3}
\]
onto
\[
\operatorname{Sym}^4(V)\otimes\operatorname{Sym}^3(V)\otimes\operatorname{Sym}^3(V).
\]
By <1>1, the characters of the three factors are $s_{(4)},s_{(3)},s_{(3)}$, so the character of their tensor product is their product.
:::

<1>3. The coefficient of $s_{(6,3,1)}$ in $s_{(4)}s_{(3)}s_{(3)}$ is $3$.
::: {.proof}
By the Pieri rule,
\[
s_{(4)}s_{(3)}
=s_{(7)}+s_{(6,1)}+s_{(5,2)}+s_{(4,3)}.
\]
Multiplication by the final $s_{(3)}$ adds a horizontal $3$-strip.
For the target partition
\[
\lambda=(6,3,1),
\]
the partitions in the preceding sum for which $\lambda/\mu$ is a horizontal $3$-strip are exactly
\[
\mu=(6,1),\qquad(5,2),\qquad(4,3).
\]
Each occurs with Pieri coefficient $1$.
Hence
\[
[s_{(6,3,1)}]\,s_{(4)}s_{(3)}s_{(3)}=3.
\]
:::

<1>4. The multiplicity of $S^{(3,3,3,1)}$ in $V^{\otimes10}$ is
\[
175\quad\text{when }N=5,
\qquad
0\quad\text{when }N=3.
\]
::: {.proof}
Schur-Weyl duality gives
\[
V^{\otimes10}
\cong
\bigoplus_{\substack{\lambda\vdash10\\\ell(\lambda)\le N}}
\mathbf S_\lambda(V)\otimes S^\lambda
\]
as a $GL(V)\times S_{10}$-module.
Thus the multiplicity of $S^\lambda$ is
\[
\dim\mathbf S_\lambda(\mathbb C^N)=s_\lambda(1^N).
\]
For $N=3$, the partition $(3,3,3,1)$ has four nonzero parts, so the Schur functor vanishes and the multiplicity is $0$.

For $N=5$, the hook-content formula gives
\[
s_{(3,3,3,1)}(1^5)
=\prod_{(i,j)\in(3,3,3,1)}\frac{5+j-i}{h_{ij}}.
\]
The hook lengths, row by row, are
\[
(6,4,3),\qquad(5,3,2),\qquad(4,2,1),\qquad(1),
\]
and the corresponding numerators $5+j-i$ are
\[
(5,6,7),\qquad(4,5,6),\qquad(3,4,5),\qquad(2).
\]
Therefore
\[
\frac{5\cdot6\cdot7\cdot4\cdot5\cdot6\cdot3\cdot4\cdot5\cdot2}
{6\cdot4\cdot3\cdot5\cdot3\cdot2\cdot4\cdot2\cdot1\cdot1}
=175.
\]
:::
:::
