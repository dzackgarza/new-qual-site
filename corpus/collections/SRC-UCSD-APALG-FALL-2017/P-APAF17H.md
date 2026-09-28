---
schema: qual/card@1
id: P-APAF17H
kind: problem
title: Isomorphic subgroups of $\mathrm{GL}_2(\mathbb{C})$ need not have the same invariant Hilbert series
classification:
  areas:
  - applied-algebra
  topics:
  - Invariant Theory
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Prove or give a counterexample: Let $G$ and $H$ be two subgroups of the matrix group $\mathrm{GL}_2(\mathbb{C})$ which satisfy $G\cong H$ (group isomorphism).
Then the invariant rings $\mathbb{C}[x,y]^G$ and $\mathbb{C}[x,y]^H$ have the same Hilbert series.
:::

::: {.solution}
The statement is false.

<1>1. Let
\[
G=\left\langle\begin{pmatrix}-1&0\\0&1\end{pmatrix}\right\rangle,
\qquad
H=\langle -I_2\rangle.
\]
Then $G,H\le \mathrm{GL}_2(\mathbb C)$ and $G\cong H\cong C_2$.
::: {.proof}
Each displayed generator has order $2$ and is not the identity, so each subgroup has exactly two elements. Hence both groups are cyclic of order $2$.
:::

<1>2. The invariant ring of $G$ is
\[
\mathbb C[x,y]^G=\mathbb C[x^2,y],
\]
and its Hilbert series is
\[
\operatorname{Hilb}_{\mathbb C[x,y]^G}(t)
=\frac{1}{(1-t^2)(1-t)}.
\]
::: {.proof}
The nonidentity element of $G$ acts by
\[
(x,y)\longmapsto(-x,y).
\]
Thus a monomial $x^ay^b$ is invariant exactly when $a$ is even. Therefore the invariant monomials are precisely
\[
(x^2)^cy^b,
\qquad b,c\ge0,
\]
which form the polynomial ring $\mathbb C[x^2,y]$. Since $x^2$ has degree $2$ and $y$ has degree $1$, its Hilbert series is
\[
\frac1{(1-t^2)(1-t)}.
\]
:::

<1>3. The invariant ring of $H$ consists of the polynomials all of whose monomials have even total degree. Its Hilbert series is
\[
\operatorname{Hilb}_{\mathbb C[x,y]^H}(t)
=\frac12\left(\frac1{(1-t)^2}+\frac1{(1+t)^2}\right)
=\frac{1+t^2}{(1-t^2)^2}.
\]
::: {.proof}
The nonidentity element $-I_2$ acts by
\[
(x,y)\longmapsto(-x,-y).
\]
Hence
\[
x^ay^b\longmapsto(-1)^{a+b}x^ay^b,
\]
so a monomial is invariant exactly when $a+b$ is even. The dimension of the degree-$d$ invariant subspace is therefore $d+1$ for even $d$ and $0$ for odd $d$. Equivalently, averaging the ordinary Hilbert series over the two parity actions gives
\[
\frac12\left(\sum_{d\ge0}(d+1)t^d+\sum_{d\ge0}(d+1)(-t)^d\right)
=\frac12\left(\frac1{(1-t)^2}+\frac1{(1+t)^2}\right).
\]
A direct simplification gives
\[
\frac{1+t^2}{(1-t^2)^2}.
\]
:::

<1>4. The two Hilbert series are different.
::: {.proof}
Already in degree $1$ one has
\[
\dim_\mathbb C(\mathbb C[x,y]^G)_1=1,
\qquad
\dim_\mathbb C(\mathbb C[x,y]^H)_1=0,
\]
because $y$ is $G$-invariant while $H$ has no nonzero linear invariants. Therefore the Hilbert series cannot agree.
:::

<1>5. Thus isomorphic abstract subgroups of $\mathrm{GL}_2(\mathbb C)$ need not have invariant rings with the same Hilbert series.
::: {.proof}
The groups $G$ and $H$ from <1>1 are isomorphic, but <1>2--<1>4 show that their invariant Hilbert series differ. The Hilbert series depends on the specific representation, not only on the abstract group isomorphism type.
:::
:::
