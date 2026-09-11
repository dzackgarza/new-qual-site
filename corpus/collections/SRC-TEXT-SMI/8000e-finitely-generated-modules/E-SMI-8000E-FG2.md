---
schema: qual/card@1
id: E-SMI-8000E-FG2
kind: problem
title: Classifying structures annihilated by a fixed element
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three annihilator/minimal-polynomial requests with the PDF text layer and local 8000e extraction, finitely-generated-modules problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used primary decomposition and the squarefree annihilator to force elementary primary summands; enumerated all multiplicities in dimension seven and then imposed both eigenvalues for the exact minimal polynomial."
---

::: {.exercise}
(a) Write down all abelian groups of order 648 annihilated by 6 (always up to isomorphism).

(b) Write down all $k[t]$ modules of $k$-dimension 7 annihilated by $(t - 2)(t - 3)$.

(c) Write down all 7 by 7 Jordan matrices with minimal polynomial $(t - 2)(t - 3)$.
:::


::: solution
<1>1. There is exactly one abelian group of order $648$ annihilated by $6$.
::: proof
Let $G$ have order
$$
648=2^3 3^4.
$$
Its primary decomposition is
$$
G=G_{(2)}\oplus G_{(3)},
$$
with
$$
|G_{(2)}|=2^3,
\qquad
|G_{(3)}|=3^4.
$$

The condition that $6G=0$ implies in particular that every element of
$G_{(2)}$ has order dividing $2$: multiplication by $3$ is an automorphism of
the $2$-primary group, so $6x=0$ forces $2x=0$. Hence
$$
G_{(2)}\cong(\mathbb Z/2)^3.
$$
Similarly, multiplication by $2$ is an automorphism of $G_{(3)}$, so
$6x=0$ forces $3x=0$, and therefore
$$
G_{(3)}\cong(\mathbb Z/3)^4.
$$
Thus the unique isomorphism class is
$$
\boxed{G\cong(\mathbb Z/2)^3\oplus(\mathbb Z/3)^4.}
$$
Equivalently,
$$
G\cong(\mathbb Z/6)^3\oplus\mathbb Z/3.
$$
:::

<1>2. Classify the seven-dimensional $k[t]$-modules annihilated by $(t-2)(t-3)$.
::: proof
Put
$$
p(t)=(t-2)(t-3).
$$
The two linear factors are distinct because they differ by $1$. Thus $p$ is
squarefree. If $pV=0$, the Chinese remainder theorem gives
$$
k[t]/(p)
\cong k[t]/(t-2)\times k[t]/(t-3),
$$
and consequently
$$
V=V(2)\oplus V(3),
$$
where $t$ acts as the scalar $2$ on $V(2)$ and as the scalar $3$ on $V(3)$.
There can be no larger Jordan blocks because the annihilator is squarefree.

Let
$$
r=\dim_kV(2).
$$
Then
$$
\dim_kV(3)=7-r,
$$
with $0\le r\le7$, and the module is
$$
\boxed{
V_r=(k[t]/(t-2))^r
\oplus
(k[t]/(t-3))^{7-r},
\qquad 0\le r\le7.}
$$
The integer $r$ is an isomorphism invariant, so these are exactly the eight
isomorphism classes.
:::

<1>3. Classify the $7\times7$ Jordan matrices with minimal polynomial $(t-2)(t-3)$.
::: proof
A matrix with this minimal polynomial is diagonalizable because the minimal
polynomial has distinct linear factors. Both factors must actually occur, or
the minimal polynomial would omit one of them. Thus the matrix has $r$ copies
of the eigenvalue $2$ and $7-r$ copies of the eigenvalue $3$, where
$$
1\le r\le6.
$$
A complete list of Jordan-form representatives is therefore
$$
\boxed{
J_r=2I_r\oplus3I_{7-r},
\qquad 1\le r\le6.}
$$
These six matrices are pairwise nonconjugate because the multiplicity of the
eigenvalue $2$ is invariant under conjugacy.
:::
:::
