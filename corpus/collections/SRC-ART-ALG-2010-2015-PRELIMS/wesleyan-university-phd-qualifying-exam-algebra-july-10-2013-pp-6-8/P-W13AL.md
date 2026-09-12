---
schema: qual/card@1
id: P-W13AL
kind: problem
title: Algebraic elements form a subfield, and the minimal polynomial of $2\sqrt{2}-\sqrt{3}$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked both parts of July 2013 Fields 3 on PDF page 8, including the coefficient 2 and the minus sign in the radical expression."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the finite-dimensional subring argument for inverses and algebraicity, the biquadratic degree, and recovery of both radicals from the proposed generator."
---

::: problem
a. Suppose $K/F$ is a field extension.
Prove that the elements of $K$ that are algebraic over $F$ form a subfield of $K$.

b. Find the minimal polynomial of $2\sqrt{2} - \sqrt{3}$ over $\mathbb{Q}$.
:::

::: solution
<1>1. The elements algebraic over $F$ form a subfield of $K$.

::: proof
Every element of $F$ is algebraic over $F$, being a root of
a linear polynomial. Suppose $\alpha,\beta\in K$ are
algebraic over $F$, with monic annihilating polynomials of
degrees $m,n$, respectively. Reduction by these equations
shows that the subring $A=F[\alpha,\beta]\subseteq K$ is
spanned over $F$ by
$$
\{\alpha^i\beta^j:0\leq i<m,\ 0\leq j<n\}.
$$
Thus $A$ is a finite-dimensional $F$-vector space.
For $0\ne a\in A$, multiplication by $a$ is an injective
$F$-linear endomorphism of $A$, since $A$ is a subring of
a field. An injective endomorphism of a finite-dimensional
space is surjective, so $ab=1$ for some $b\in A$.
Therefore $A$ is itself a field.

Each $z\in A$ is algebraic over $F$: if $d=\dim_F A$,
the $d+1$ powers $1,z,\ldots,z^d$ are linearly dependent,
yielding a nonzero annihilating polynomial in $F[T]$.
In particular $\alpha-\beta$, $\alpha\beta$, and
$\alpha^{-1}$ when $\alpha\ne0$ are algebraic. Together
with containment of $F$, these closure properties prove the
subfield assertion.
:::

<1>2. The field $E=\mathbb Q(\sqrt2,\sqrt3)$ has degree $4$
over $\mathbb Q$.

::: proof
A square of a nonzero rational number has an even exponent
at every prime in its factorization. Hence $2$ is not a
rational square, and $1,\sqrt2$ are a basis of
$\mathbb Q(\sqrt2)$ over $\mathbb Q$.
If $(a+b\sqrt2)^2=3$ for $a,b\in\mathbb Q$, comparison
of these two basis coefficients gives
$a^2+2b^2=3$ and $2ab=0$.
For $b=0$ this gives $a^2=3$, impossible because the
exponent of $3$ is odd. For $a=0$ it gives $b^2=3/2$,
also impossible because the exponent of $3$ is odd.
Thus $T^2-3$ has no root in $\mathbb Q(\sqrt2)$ and is
irreducible over that field. Adjoining $\sqrt3$ has degree
$2$, and the tower law gives $[E:\mathbb Q]=2\cdot2=4$.
:::

<1>3. The minimal polynomial in part (b) is
$$
\boxed{T^4-22T^2+25}.
$$

::: proof
Put $\gamma=2\sqrt2-\sqrt3$. One has
$\gamma^2=11-4\sqrt6$, so
$(\gamma^2-11)^2=96$. Expanding gives
$\gamma^4-22\gamma^2+25=0$.

To prove minimality, rather than just annihilation, note that
$$
(2\sqrt2-\sqrt3)(2\sqrt2+\sqrt3)=8-3=5.
$$
Thus $\gamma\ne0$ and $5/\gamma=2\sqrt2+\sqrt3$.
Consequently
$$
\sqrt2=\frac{\gamma+5/\gamma}{4},\qquad
\sqrt3=\frac{5/\gamma-\gamma}{2}.
$$
Both radicals belong to $\mathbb Q(\gamma)$, so this field
equals $E$. Step <1>2 shows that $\gamma$ has degree $4$.
Its minimal polynomial is therefore the monic degree-four
annihilating polynomial displayed above.
:::
:::
