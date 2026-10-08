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
What is the Jordan normal form over $\mathbb{C}$ of a $7 \times 7$ matrix $A$ which satisfies all of the following conditions:

a.
$A$ has real coefficients,

b.
$\mathrm{rk} A=5$,

c.
$\mathrm{rk} A^{2}=4$,

d.
$\mathrm{rk} A-I=6$,

e.
$\mathrm{rk} A^{3}-I=4$,

f.
$\operatorname{tr} A=1 ?$
:::

::: {.solution}
Let $\zeta=e^{2\pi i/3}$. For $\lambda\in\mathbb C$, let $J_d(\lambda)$ denote the Jordan block of size $d$.

<1>1. The Jordan blocks for eigenvalue zero have sizes two and one.

::: {.proof}
Rank–nullity gives $\dim\ker A=2$ and $\dim\ker A^2=3$. The first number counts the Jordan blocks for zero; the difference $\dim\ker A^2-\dim\ker A=1$ counts the zero blocks of size at least two. Thus there are two blocks, one of size at least two and one of size one. In particular, the algebraic multiplicity of zero is at least three.
:::

<1>2. The eigenvalues whose cubes equal one have total algebraic multiplicity at least three, and exactly one Jordan block belongs to eigenvalue one.

::: {.proof}
The polynomial $x^3-1=(x-1)(x-\zeta)(x-\zeta^2)$ has distinct roots. On a Jordan block for any of these eigenvalues, the kernel of $A^3-I$ has dimension one; on all other blocks it has dimension zero. Thus $\dim\ker(A^3-I)=7-4=3$ counts three Jordan blocks associated to cube roots of unity. Moreover $\dim\ker(A-I)=7-6=1$ shows exactly one of these blocks has eigenvalue one. They occupy at least three dimensions.
:::

<1>3. The zero blocks have sizes two and one, and the three cube-root blocks have sizes two, one, and one.

::: {.proof}
By steps <1>1 and <1>2, at least six of the seven dimensions are accounted for, and the trace condition fixes the remaining one. First suppose the zero blocks occupy four or more dimensions. Then the cube-root blocks occupy exactly three, each of size one, and there is no room for any other eigenvalue. Since $A$ is real, the two nonreal cube roots must have equal multiplicities. Exactly one block has eigenvalue one, so the three cube-root eigenvalues are $\{1,\zeta,\zeta^2\}$. Their trace is zero, contradicting $\operatorname{tr}A=1$. Hence the zero blocks occupy exactly three dimensions.

There are four remaining dimensions. The three cube-root blocks must occupy three or four dimensions. If they occupy three, the final one-dimensional block would have eigenvalue $\lambda$ with $\lambda^3\neq1$ and $\lambda\neq0$. Since $A$ is real, this extra eigenvalue must be real. The three cube-root blocks have eigenvalues $\{1,\zeta,\zeta^2\}$ by the same conjugation and kernel argument, so their trace is zero. Thus $\lambda=1$, contradicting $\lambda^3\neq1$. Therefore all four remaining dimensions belong to cube-root blocks.

Since there is exactly one Jordan block for eigenvalue one and the two nonreal cube roots must occur with the same algebraic multiplicity, the trace equation forces the eigenvalue multiplicities to be $(2,1,1)$ for $(1,\zeta,\zeta^2)$: writing them $(a,b,b)$ gives $a+2b=4$ and $a+b(\zeta+\zeta^2)=a-b=1$, whence $a=2$, $b=1$. Accordingly the eigenvalue-one block has size two, while the other two blocks have size one.
:::

<1>4. The Jordan normal form is
\[
\boxed{J_2(0)\oplus J_1(0)\oplus J_2(1)\oplus J_1(\zeta)\oplus J_1(\zeta^2)}.
\]

::: {.proof}
Steps <1>1 and <1>3 determine every block and its size. Their total dimension is seven, and the blocks satisfy all five numerical conditions from the problem.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required Jordan form.
:::
:::
