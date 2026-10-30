---
schema: qual/card@1
id: P-R5QUP
kind: problem
title: Jordan form of a $7\times 7$ matrix from rank and trace conditions
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Trace
relations: []
review: draft
---

::: {.problem}
What is the Jordan normal form over $\CC$ of a $7 \times 7$ matrix $A$ which satisfies all of the following conditions:

a. $A$ has real coefficients,
b. $\operatorname{rk} A=5$,
c. $\operatorname{rk} A^{2}=4$,
d. $\operatorname{rk}(A-I)=6$,
e. $\operatorname{rk}(A^{3}-I)=4$,
f. $\operatorname{tr} A=1$?
:::

::: {.solution}

Write $\zeta=e^{2\pi i/3}$ and $J_k(\lambda)$ for the Jordan block of size $k$ with eigenvalue $\lambda$. Rank-nullity gives $\dim\ker M=7-\operatorname{rk}M$.

::: pf

::: {.pf-step #zero}

The eigenvalue $0$ has Jordan blocks of sizes exactly $1$ and $k$ for some $k\ge2$.

::: pf-proof

$\dim\ker A=2$, so $0$ has two blocks, of sizes $a\le b$. $\dim\ker A^2=\min(a,2)+\min(b,2)=3$, which forces $a=1$ and $b\ge2$.

:::

:::

::: {.pf-step #roots}

The eigenvalues $1$, $\zeta$ and $\zeta^2$ each have exactly one Jordan block.

::: pf-proof

$x^3-1=(x-1)(x-\zeta)(x-\zeta^2)$ with pairwise coprime factors, so
$$
\ker(A^3-I)=\ker(A-I)\oplus\ker(A-\zeta I)\oplus\ker(A-\zeta^2I),
$$
and this space has dimension $3$. $\dim\ker(A-I)=1$. Since $A$ is real, complex conjugation maps $\ker(A-\zeta I)$ onto $\ker(A-\zeta^2 I)$, so these have equal dimension, which is therefore $1$.

:::

:::

::: {.pf-step #other}

$A$ has no eigenvalue outside $\{0,1,\zeta,\zeta^2\}$, the blocks for $\zeta$ and $\zeta^2$ have one common size $c$, and the block for $1$ has size $c+1$.

::: pf-proof

Let the block for $1$ have size $m$, and let the remaining eigenvalues, other than $0$, $1$, $\zeta$, $\zeta^2$, have total multiplicity $r$. Conjugation of the real matrix $A$ preserves the Jordan structure, so the $\zeta$ and $\zeta^2$ blocks have one size $c$. By Step [](#zero){.pf-ref}, $1+k+m+2c+r=7$ with $k\ge2$, so $m+2c+r\le4$. The trace is
$$
1=m+c(\zeta+\zeta^2)+s=m-c+s,
$$
where $s$ is the sum of the $r$ remaining eigenvalues. If $r>0$, then $m=c=1$ and $r\le1$, so $r=1$ and $s=1$. The eigenvalue $s=1$ is not a remaining eigenvalue, a contradiction. Hence $r=0$ and $m=c+1$.

:::

:::

::: pf-qed

By Step [](#other){.pf-ref}, $1+k+(c+1)+2c=7$, so $k+3c=5$ with $k\ge2$ and $c\ge1$. Thus $c=1$, $k=2$ and $m=2$, and
$$
\boxed{J=J_1(0)\oplus J_2(0)\oplus J_2(1)\oplus J_1(\zeta)\oplus J_1(\zeta^2)
=\begin{pmatrix}
0&&&&&&\\
&0&1&&&&\\
&&0&&&&\\
&&&1&1&&\\
&&&&1&&\\
&&&&&\zeta&\\
&&&&&&\zeta^2
\end{pmatrix}.}
$$

:::

:::

:::
