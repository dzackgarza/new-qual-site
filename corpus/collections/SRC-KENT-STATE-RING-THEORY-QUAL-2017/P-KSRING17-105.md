---
schema: qual/card@1
id: P-KSRING17-105
kind: problem
title: Coefficients of a nilpotent polynomial are nilpotent
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 105 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1 and let $f ( x ) \ \in \ R [ x ]$ be nilpotent.
Show that the coefficients of f are nilpotent.
:::

::: {.solution}
Write
$$
f(x)
=
a_0+a_1x+\cdots+a_nx^n.
$$
Assume
$$
f(x)^N=0
$$
for some
$$
N\ge1.
$$

<1>1. Let
$$
\mathfrak p
$$
be any prime ideal of $R$.
Then the image
$$
\overline f(x)
\in
(R/\mathfrak p)[x]
$$
is nilpotent.

::: {.proof}
Apply the quotient homomorphism
$$
R[x]\to(R/\mathfrak p)[x]
$$
coefficientwise.
The relation
$$
f^N=0
$$
maps to
$$
\overline f^{\,N}=0.
$$
Thus
$$
\overline f
$$
is nilpotent.
:::

<1>2. The ring
$$
(R/\mathfrak p)[x]
$$
is an integral domain.

::: {.proof}
Since
$$
\mathfrak p
$$
is prime,
$$
R/\mathfrak p
$$
is an integral domain.
A polynomial ring over an integral domain is again an integral domain.
:::

<1>3. The polynomial
$$
\overline f
$$
is zero in
$$
(R/\mathfrak p)[x].
$$

::: {.proof}
By step <1>1,
$$
\overline f^{\,N}=0.
$$
By step <1>2, the polynomial ring is an integral domain and therefore has no nonzero nilpotent elements.
Hence
$$
\overline f=0.
$$
:::

<1>4. Every coefficient
$$
a_i
$$
belongs to every prime ideal
$$
\mathfrak p
$$
of $R$.

::: {.proof}
The equality
$$
\overline f=0
$$
from step <1>3 means every coefficient of
$$
\overline f
$$
is zero in
$$
R/\mathfrak p.
$$
Thus
$$
a_i+\mathfrak p=0+\mathfrak p,
$$
so
$$
a_i\in\mathfrak p.
$$
The prime ideal $\mathfrak p$ was arbitrary.
:::

<1>5. If an element
$$
a\in R
$$
lies in every prime ideal of $R$, then $a$ is nilpotent.

::: {.proof}
Suppose, for contradiction, that
$$
a
$$
is not nilpotent.
Then the multiplicative set
$$
S
\coloneqq
\{1,a,a^2,a^3,\ldots\}
$$
does not contain $0$.

Consider the set of ideals
$$
\mathcal P
\coloneqq
\{
I\trianglelefteq R:
I\cap S=\varnothing
\},
$$
ordered by inclusion.
It is nonempty because
$$
(0)\cap S=\varnothing.
$$
The union of any chain in $\mathcal P$ is again an ideal disjoint from $S$, so Zorn's lemma gives an ideal
$$
P
$$
maximal among ideals disjoint from $S$.

Such a maximal disjoint ideal is prime.
Indeed, if
$$
xy\in P
$$
with
$$
x,y\notin P,
$$
then both
$$
P+(x)
$$
and
$$
P+(y)
$$
strictly contain $P$, hence meet $S$.
Choose
$$
s=p+rx\in S,
\qquad
t=q+uy\in S
$$
with
$$
p,q\in P.
$$
Then
$$
st
=
pq+puy+rqx+ruxy
\in P,
$$
while
$$
st\in S
$$
because $S$ is multiplicatively closed.
This contradicts
$$
P\cap S=\varnothing.
$$
Thus $P$ is prime.

But
$$
a\in S
$$
and
$$
P\cap S=\varnothing,
$$
so
$$
a\notin P.
$$
Hence $a$ does not lie in every prime ideal, contradiction.
Therefore $a$ is nilpotent.
:::

<1>6. Each coefficient
$$
a_i
$$
of $f$ is nilpotent.

::: {.proof}
By step <1>4,
$$
a_i
$$
lies in every prime ideal of $R$.
Step <1>5 therefore implies that
$$
a_i
$$
is nilpotent.
:::

<1>7. Hence
$$
\boxed{
\text{every coefficient of }f\text{ is nilpotent}.
}
$$

::: {.proof}
Step <1>6 applies to each
$$
i=0,\ldots,n.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
