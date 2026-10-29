---
schema: qual/card@1
id: P-GCNAR
kind: problem
title: Invariant factors, indecomposable $\CC[x]$-modules, and Jordan form of a $5\times
  5$ matrix
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Jordan Canonical Form
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: buffy
  date: 2026-10-27
  note: Corrected the Jordan structure for the matrix as printed. With $A_{23}=1$ the kernels of $T-I$, $(T-I)^2$, $(T-I)^3$ have dimensions $2,3,4$, so the eigenvalue-one blocks are $J_3(1)$ and $[1]$; the earlier version used the dimensions $3,4$ of the matrix with $A_{23}=0$.
---

::: {.problem}
Consider the following matrix as a linear transformation from $V\definedas \CC^5$ to itself:
\[
A=\left(\begin{array}{ccccc}
-1 & 1 & 0 & 0 & 0 \\
-4 & 3 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 2
\end{array}\right)
.\]

a. 
Find the invariant factors of $A$.

b. 
Express $V$ in terms of a direct sum of indecomposable $\CC[x]\dash$modules.

c.
Find the Jordan canonical form of $A$.
:::

Let $T$ denote the operator with matrix $A$, and let $x$ act on $V$ by $T$.

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The elementary divisors of $T$ are $(x-1)^3$, $(x-1)$, and $(x-2)$.


::: pf-proof

The block upper-triangular matrix has characteristic polynomial
\[
\chi_T(x)=((x+1)(x-3)+4)(x-1)^2(x-2)=(x-1)^4(x-2).
\]
For $N=T-I$, the first two coordinates form the nilpotent block
\(\begin{psmallmatrix}-2&1\\-4&2\end{psmallmatrix}\), whose square is zero, while the entry $A_{23}=1$ couples the two diagonal blocks. Direct calculation gives $\dim\ker N=2$, $\dim\ker N^2=3$, and $\dim\ker N^3=4$. The successive kernel increments $2,1,1$ show that the two Jordan blocks for eigenvalue one have sizes three and one. Eigenvalue two has algebraic multiplicity one, giving one further block.

:::

:::

::: {.pf-step #s1-2}

The invariant factors are
\[
\boxed{d_1=x-1,\quad d_2=(x-1)^3(x-2)}.
\]


::: pf-proof

The elementary divisors from step [](#s1-1){.pf-ref} comprise $(x-1)^3$, $(x-1)$, and $(x-2)$. Ordering the powers of $x-1$ in decreasing order and combining the sole $x-2$ factor with the largest power yields the displayed monic invariant factors. They satisfy $d_1\mid d_2$ and $d_1d_2=\chi_T$.

:::

:::

::: {.pf-step #s1-3}

The decomposition into indecomposable $\CC[x]$-modules is
\[\boxed{V\cong\CC[x]/((x-1)^3)\oplus
\CC[x]/(x-1)\oplus \CC[x]/(x-2)}.
\]


::: pf-proof

The structure theorem over the PID $\CC[x]$ gives the elementary-divisor decomposition from step [](#s1-1){.pf-ref}. Each cyclic module killed by a power of an irreducible polynomial is indecomposable: its submodules form a chain, so it cannot split as a direct sum of two nonzero submodules.

:::

:::

::: {.pf-step #s1-4}

The Jordan canonical form is
\[
\boxed{J_3(1)\oplus[1]\oplus[2]}.
\]


::: pf-proof

The elementary divisors determined in step [](#s1-1){.pf-ref} correspond to Jordan blocks of sizes three and one at eigenvalue one, and a single block at eigenvalue two. The kernel dimensions computed there force the larger block to have size three.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
