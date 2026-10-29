---
schema: qual/card@1
id: P-APAS21F
kind: problem
title: 'Indecomposable versus irreducible complex representations of $\RR_+$'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Modules
relations: []
review: draft
---

::: {.problem}
Let $\RR_+$ be the group of positive real numbers under multiplication.
Is every indecomposable $\RR_+$-module over the complex numbers irreducible?
:::

::: {.solution}
No. Via the logarithm, the multiplicative group $\RR_+$ is isomorphic to the additive group $(\RR,+)$. Let $V=\CC^2$ and define
\[
\rho(t)=
\begin{pmatrix}
1&\log t\\
0&1
\end{pmatrix}
\qquad (t>0).
\]
Since $\log(ts)=\log t+\log s$, one has $\rho(ts)=\rho(t)\rho(s)$, so this is a representation of $\RR_+$.

The line $L=\CC e_1$ is invariant, so $V$ is not irreducible.

We claim that $V$ is nevertheless indecomposable. If
\[
V=V_1\oplus V_2
\]
were a decomposition into two nonzero submodules, then, because $\dim V=2$, both $V_1$ and $V_2$ would be invariant lines. But a line $\mathbb Cv$ is invariant under every $\rho(t)$ if and only if it is invariant under
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\]
because $\rho(t)=I+(\log t)N$ and $\log t$ ranges over all real numbers. The only one-dimensional $N$-invariant subspace is $\ker N=\CC e_1$: indeed, if $v=ae_1+be_2$ spans an invariant line and $b\ne0$, then $Nv=be_1$ would have to be a scalar multiple of $v$, which is impossible. Thus there is only one invariant line, so no direct-sum decomposition into two nonzero submodules exists.

Hence this $\RR_+$-module is indecomposable but reducible.
:::
