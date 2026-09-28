---
schema: qual/card@1
id: P-C3CRT
kind: problem
title: If $I+J=R$ then $IJ = I \cap J$ and $R/(IJ) \cong R/I \oplus R/J$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Chinese Remainder Theorem
  - Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared June 2012 Rings 3 on PDF page 10, including the section's convention that rings have an identity."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both ideal inclusions, the explicit lift of arbitrary residues, and the well-defined inverse on quotient classes, including an ideal equal to R."
---

::: {.problem}
Suppose that $R$ is a commutative ring with identity and $I$ and $J$ are ideals of $R$.
Suppose that $I + J = R$.

a. Prove that $IJ = I \cap J$.

b. Prove that $R/(IJ)$ is isomorphic to $R/I \oplus R/J$.
(This is the Chinese Remainder Theorem).
:::

::: {.solution}
Choose $u\in I$ and $v\in J$ such that $u+v=1$.
The finite direct sum in the statement carries componentwise
addition and multiplication, so it is the product ring $R/I\times R/J$.

<1>1. The ideals $IJ$ and $I\cap J$ are equal.

::: {.proof}
Every product $ij$, with $i\in I$ and $j\in J$, belongs to
both ideals. Their intersection is closed under finite sums,
so $IJ\subseteq I\cap J$.

Conversely, for $z\in I\cap J$ one has $z=zu+zv$.
Since $u\in I$, $z\in J$, and $R$ is commutative,
$zu\in IJ$. Since $z\in I$ and $v\in J$, also $zv\in IJ$.
Thus $z\in IJ$, proving the reverse inclusion.
:::

<1>2. The map
$$
\phi:R\longrightarrow R/I\times R/J,\qquad
r\longmapsto(r+I,r+J)
$$
is a surjective ring homomorphism with kernel $IJ$.

::: {.proof}
Both components are quotient homomorphisms, so $\phi$ preserves
addition, multiplication, and the identity. Its kernel is
$I\cap J$, which equals $IJ$ by step <1>1.

For arbitrary representatives $a,b\in R$, put $r=av+bu$.
Then $r-a=u(b-a)\in I$ and $r-b=v(a-b)\in J$.
Consequently $\phi(r)=(a+I,b+J)$, proving surjectivity.
:::

<1>3. The required isomorphism and its inverse are
$$
\begin{aligned}
\overline\phi:R/(IJ)&\longrightarrow R/I\times R/J,
&r+IJ&\longmapsto(r+I,r+J),\\
\psi:R/I\times R/J&\longrightarrow R/(IJ),
&(a+I,b+J)&\longmapsto av+bu+IJ.
\end{aligned}
$$

::: {.proof}
The map $\overline\phi$ is well defined because $IJ\subseteq I\cap J$.
It is a ring homomorphism. Changing $a$ by an element $i\in I$
changes $av+bu$ by $iv\in IJ$; changing $b$ by $j\in J$
changes it by $ju\in IJ$. Thus $\psi$ is also well defined.

The residue computation in step <1>2 gives
$\overline\phi\psi(a+I,b+J)=(a+I,b+J)$.
In the other direction,
$\psi\overline\phi(r+IJ)=r(v+u)+IJ=r+IJ$.
Therefore $\overline\phi$ is a bijective ring homomorphism
and hence the desired ring isomorphism. The argument does
not require $I$ or $J$ to be proper.
:::
:::
