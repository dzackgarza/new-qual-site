---
title: Jordan canonical form
order: 30
topics:
- Jordan Canonical Form
---

# Jordan canonical form

Let $A$ be an $n\times n$ matrix over a field $k$.
The Jordan canonical form of $A$ exists if and only if the characteristic polynomial $\chi_A$ splits over $k$; the [[algebra/linear-algebra/rational-canonical-form|rational canonical form]] exists over every field.

[[PR-5A2W4]]

[[L-CD6QT]]

## Where the form comes from

Make $V=k^n$ a $k[x]$-module with $x$ acting by $A$.
If $\chi_A$ splits, every invariant factor of $V$ is a power of a linear polynomial, so every elementary divisor is some $(x-\lambda)^e$, and that summand $k[x]/\generates{(x-\lambda)^e}$ is the Jordan block $J_e(\lambda)$ in the basis $(x-\lambda)^{e-1},\ldots,(x-\lambda),1$.

[[L-W5S2W]]

[[D-JQNJQ]]

[[PR-UVUS6]]

## Jordan blocks from the minimal and characteristic polynomials

::: {.example title="From the two polynomials"}
Suppose $A$ is $5\times 5$ with
$$
\begin{aligned}
\min_A(t) &= (t-4)^2(t+6), \\
\chi_A(t) &= (t-4)^3(t+6)^2.
\end{aligned}
$$

For $\lambda = 4$, the block sizes sum to $3$ and the largest is $2$, so the blocks are $J_2(4) \oplus J_1(4)$.
For $\lambda = -6$, the block sizes sum to $2$ and the largest is $1$, so the blocks are $J_1(-6)\oplus J_1(-6)$.
:::

::: {.warnings title="The two polynomials do not determine the form"}
For $4\times 4$ matrices with $\min_A(t) = t^2$ and $\chi_A(t) = t^4$ there are two similarity classes, $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$.
They are distinguished by $\dim\ker A$, which is $2$ and $3$ respectively.
In general, $\dim\ker(A-\lambda I)^k-\dim\ker(A-\lambda I)^{k-1}$ is the number of Jordan blocks for $\lambda$ of size at least $k$, which is the rank-sequence computation of [[PR-5A2W4]].
:::

## Generalized eigenspaces

The generalized eigenspace of $\lambda$ is $\ker(A-\lambda I)^n$ for $n=\dim V$, the largest of the subspaces $\ker(A-\lambda I)^m$; when $\chi_A$ splits these subspaces are the primary components of $V$ as a $k[x]$-module, and they are the summands the Jordan blocks are written in.

[[D-JQNJQ]]

## Problems

[[E-23SLE]]

[[E-GNYRR]]

[[E-GEVBZ]]

[[E-2KJEL]]
