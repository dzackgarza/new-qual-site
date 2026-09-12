---
schema: qual/card@1
id: P-GJS7T
kind: problem
title: A square matrix is conjugate to its transpose
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked Linear Algebra 1 on PDF page 2, including the permission to work over C; the proof below works over every field."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nondegeneracy of the coefficient pairing, the matrix identity C-transpose B=BC, and the conjugation formula after rational canonical decomposition."
---

::: problem
Prove that any square matrix is conjugate to its transpose matrix.
(You may prove it over $\mathbb{C}$).
:::

::: solution
We prove the assertion for matrices over any field $F$.

<1>1. The companion matrix $C_f$ of any monic polynomial
$f\in F[t]$ of positive degree is similar to its transpose.

::: proof
Let $d=\deg f$, and regard $C_f$ as multiplication by
$t$ on $E=F[t]/(f)$ in the basis $1,t,\ldots,t^{d-1}$.
Each residue class has a unique representative of degree
less than $d$. Define $\ell:E\to F$ to be the coefficient
of $t^{d-1}$ in that representative, and set
$$
\beta(u,v)=\ell(uv).
$$
This is bilinear. It is nondegenerate: for a nonzero
$u$ represented by a polynomial of degree $k<d$,
take $v=t^{d-1-k}$. The product has degree $d-1$,
so needs no reduction modulo $f$, and $\beta(u,v)$
is the nonzero leading coefficient of $u$.

Commutativity and associativity in $E$ give
$\beta(tu,v)=\ell(tuv)=\beta(u,tv)$.
Let $B_f$ be the matrix of $\beta$ in the indicated
basis. Nondegeneracy makes it invertible, and the
last identity reads
$$
C_f^{\mathsf T} B_f=B_f C_f.
$$
Thus $C_f^{\mathsf T}=B_f C_f B_f^{-1}$.
:::

<1>2. Every square matrix $A$ over $F$ is similar to $A^{\mathsf T}$.

::: proof
Rational canonical form gives an invertible $P$ with
$A=PCP^{-1}$, where $C$ is a direct sum of companion
matrices of monic polynomials [@DF04]. Apply step
<1>1 to each block, and let $B$ be the direct sum
of the resulting invertible matrices $B_f$.
Then $C^{\mathsf T}=BCB^{-1}$.

Put $Q=(P^{-1})^{\mathsf T}BP^{-1}$. It is invertible,
and direct multiplication gives
$$
QAQ^{-1}
=(P^{-1})^{\mathsf T}BCB^{-1}P^{\mathsf T}
=(P^{-1})^{\mathsf T}C^{\mathsf T}P^{\mathsf T}
=A^{\mathsf T}.
$$
This is the required conjugacy, in particular over
$\mathbb C$. The empty matrix, if allowed, is
its own transpose and needs no blocks.
:::
:::
