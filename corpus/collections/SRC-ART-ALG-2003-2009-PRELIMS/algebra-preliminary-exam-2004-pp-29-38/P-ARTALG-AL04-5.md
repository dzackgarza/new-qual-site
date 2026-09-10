---
schema: qual/card@1
id: P-ARTALG-AL04-5
kind: problem
title: Euclidean domains and failures of the converse factorization implications
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three requested examples with 2004 Rings 1 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked Euclidean division, the nonprincipal ideal (2,x), multiplicativity of the quadratic norm, and irreducibility and nonassociation of every factor of 6."
---

::: problem
Give an example of each of the following:

(a) A Euclidean domain.

(b) A Unique Factorization Domain that is not a PID.

(c) An integral domain that is not a Unique Factorization Domain.
:::

::: solution
Examples are, respectively, $\mathbb Z$, $\mathbb Z[x]$, and
$\mathbb Z[\sqrt{-5}]$.

<1>1. The ring $\mathbb Z$ is Euclidean.

::: proof
Use the Euclidean function $d(b)=|b|$ for $b\ne0$. For integers
$a,b$ with $b\ne0$, integer division gives $a=qb+r$ with
$0\leq r<|b|$. Thus $r=0$ or $d(r)<d(b)$, as required.
:::

<1>2. The ring $\mathbb Z[x]$ is a unique factorization domain
but not a principal ideal domain.

::: proof
Unique prime factorization makes $\mathbb Z$ a unique factorization
domain. Gauss's lemma implies that a polynomial ring in one variable
over a unique factorization domain is again a unique factorization
domain [@DF04]. Hence $\mathbb Z[x]$ has that property.

Its ideal $J=(2,x)$ is not principal. Every element of $J$ has
even constant coefficient, so $1\notin J$ and $J$ is proper.
If $J=(f)$, then $2=fg$ for some $g\in\mathbb Z[x]$. Degrees
of nonzero polynomials add, so $f$ is a constant integer dividing
$2$: it is $1,-1,2$, or $-2$. The first two possibilities would
give the whole ring. The last two give $(2)$, which does not contain
$x$ because its coefficient of $x$ is odd. No generator is possible.
:::

<1>3. The integral domain $R=\mathbb Z[\sqrt{-5}]$ is not a
unique factorization domain.

::: proof
The ring embeds in $\mathbb C$, so it is a domain. For
$z=a+b\sqrt{-5}$ define
$$
N(z)=z\overline z=a^2+5b^2.
$$
This is a nonnegative integer, is positive when $z\ne0$, and
satisfies $N(zw)=N(z)N(w)$ by multiplication and conjugation.
A unit must have norm $1$; conversely norm $1$ gives inverse
$\overline z\in R$. Solving $a^2+5b^2=1$ shows that the only
units are $\pm1$. There is no element of norm $2$ or $3$:
if $b\ne0$ the norm is at least $5$, and if $b=0$ it is a
square integer.

Now
$$
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
$$
The element $2$, of norm $4$, is irreducible: a factorization
into two nonunits would require both factors to have norm $2$.
Similarly $3$, of norm $9$, would require factors of norm $3$.
Each element $1\pm\sqrt{-5}$ has norm $6$, so a factorization
into nonunits would require norms $2$ and $3$. All these
possibilities have been excluded.

Associates have the same norm because units have norm $1$.
The norms $4$ and $9$ of the factors on the left differ from
the norm $6$ of either factor on the right. Thus no rearrangement
and multiplication by units can identify the two irreducible
factorizations. This disproves unique factorization in $R$.
:::
:::
