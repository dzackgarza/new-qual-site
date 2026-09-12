---
schema: qual/card@1
id: P-JHUMAY11ANA
kind: problem
title: Entire functions with unit modulus on the unit circle are monomials
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2011 problem 1 on PDF page 24; preserved the entire-plane hypothesis and request for an exhaustive explicit classification."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked finiteness and multiplicities of interior zeros, the nonvanishing quotient on the closed disk, and the polynomial identity that excludes nonzero Blaschke zeros for an entire function."
---

1. Find all entire functions f such that $| f ( z ) | = 1$ whenever $| z | = 1$ . Give explicit formulas for the functions and give a proof for your answer.
   (An entire function is a holomorphic function on C.)

::: solution
The functions are exactly
$$
\boxed{f(z)=\alpha z^n,\qquad |\alpha|=1,\quad n=0,1,2,\ldots.}
$$

<1>1. Removing all zeros in the unit disk leaves a constant-modulus quotient.

::: proof
The boundary condition implies that $f$ is not identically
zero and has no zero on the unit circle. It has finitely
many zeros in the closed unit disk: otherwise compactness
would give an accumulation point in $\mathbb C$, contradicting
the identity theorem [@SS03]. List its interior zeros
as $a_1,\ldots,a_n$, repeated according to multiplicity.
The list may be empty. Define
$$
P(z)=\prod_{j=1}^n(z-a_j),\qquad
Q(z)=\prod_{j=1}^n(1-\overline{a_j}z),
$$
with empty products equal to one. Since $|a_j|<1$, the
polynomial $Q$ has no zero in the closed unit disk.
The quotient
$$
H(z)=\frac{f(z)Q(z)}{P(z)}
$$
extends holomorphically across every $a_j$, because $P$
has exactly the same multiplicity there as $f$.
The extended values are nonzero. Thus $H$ is holomorphic
and nonzero on a neighborhood of the closed unit disk.

For $|z|=1$, direct expansion gives
$|z-a_j|=|1-\overline{a_j}z|$. Hence $|P(z)|=|Q(z)|$
there, and $|H(z)|=1$. Apply the maximum modulus principle
to both $H$ and $1/H$: throughout the disk, $|H|\leq1$
and $|1/H|\leq1$, so $|H|=1$ [@SS03]. The same principle
makes $H$ a constant $\alpha$ with $|\alpha|=1$.
Consequently $fQ=\alpha P$ on the disk, and then on all
of $\mathbb C$ by the identity theorem.
:::

<1>2. The entire-plane hypothesis forces every $a_j$ to be zero.

::: proof
If some $a_j\ne0$, the point $b=1/\overline{a_j}$
is a zero of $Q$ with $|b|>1$. But every zero of $P$
has modulus less than one, so $P(b)\ne0$. Evaluating
the entire identity $fQ=\alpha P$ at $b$ would give
$0=\alpha P(b)\ne0$, a contradiction.

Thus all $a_j$ are zero. It follows that $P(z)=z^n$
and $Q(z)=1$, so $f(z)=\alpha z^n$ everywhere.
Conversely every such monomial is entire and has modulus
one on the unit circle. This proves both necessity and
sufficiency, including the constant case $n=0$.
:::
:::
