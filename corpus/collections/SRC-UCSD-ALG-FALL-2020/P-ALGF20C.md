---
schema: qual/card@1
id: P-ALGF20C
kind: problem
title: 'Unique factorization in $\mathbb{Z}[2\sqrt{2}]$, $\mathbb{Z}[x,y]$, and $\mathbb{Z}+x\mathbb{Q}[x]$'
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; all three rings and the hint about x agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified non-normality of Z[2sqrt(2)], Gauss-lemma UFD closure for Z[x,y], and failure of atomic factorization for x in Z+xQ[x].
---

::: problem
Determine if each of the following rings is a unique factorization domain.
For each case, you need give only a short justification or line of argument.

(1) $\mathbb{Z}[2\sqrt{2}]$.

(2) $\mathbb{Z}[x,y]$.

(3) $\mathbb{Z} + x\mathbb{Q}[x] := \{ a_0 + a_1 x + \cdots + a_n x^n \mid a_0 \in \mathbb{Z},\; a_1,\ldots,a_n \in \mathbb{Q},\; n \in \mathbb{Z}^+ \}$ (hint: consider the element $x$).
:::

::: {.solution}
<1>1. The ring $\mathbb Z[2\sqrt2]$ is not a UFD.
::: {.proof}
Put
\[
R=\mathbb Z[2\sqrt2]
=\{a+2b\sqrt2:a,b\in\mathbb Z\}.
\]
Its fraction field contains
\[
\sqrt2=\frac{2\sqrt2}{2},
\]
and $\sqrt2$ is integral over $R$ because it satisfies the monic polynomial
\[
t^2-2\in R[t].
\]
However $\sqrt2\notin R$: an equality
\[
\sqrt2=a+2b\sqrt2
\]
with $a,b\in\mathbb Z$ would force $a=0$ and $2b=1$.

Every UFD is integrally closed. Indeed, if a reduced fraction $a/b$ in the fraction field of a UFD satisfies a monic equation of degree $d$, multiplying by $b^d$ shows that $b$ divides $a^d$; coprimeness of $a$ and $b$ then forces $b$ to be a unit. Thus the existence of the integral element $\sqrt2\notin R$ proves that $R$ is not a UFD.
:::

<1>2. The ring $\mathbb Z[x,y]$ is a UFD.
::: {.proof}
The integers form a UFD. Gauss's lemma says that if $A$ is a UFD, then the polynomial ring $A[t]$ is again a UFD: contents factor uniquely in $A$, while primitive factorizations are the same as factorizations in $\operatorname{Frac}(A)[t]$ up to units. Applying this first to
\[
A=\mathbb Z
\]
and then to
\[
A=\mathbb Z[x]
\]
gives
\[
\mathbb Z[x,y]=\mathbb Z[x][y]
\]
as a UFD.
:::

<1>3. Let
\[
S=\mathbb Z+x\mathbb Q[x].
\]
The only units of $S$ are $\pm1$.
::: {.proof}
If $uv=1$ in $S$, then the same equality holds in the polynomial ring $\mathbb Q[x]$. Hence both $u$ and $v$ have degree $0$. The constant elements of $S$ are precisely the integers, whose only units are $\pm1$.
:::

<1>4. The element $x\in S$ has no factorization into irreducibles.
::: {.proof}
Suppose, toward a contradiction, that
\[
x=u p_1\cdots p_r
\]
with $u$ a unit and each $p_i$ irreducible in $S$. Degrees computed in $\mathbb Q[x]$ add, so exactly one factor, say $p_j$, has degree $1$ and every other $p_i$ has degree $0$.

Since the degree-zero elements of $S$ are integers, the equality shows that
\[
p_j=\pm\frac{x}{d}
\]
for some nonzero integer $d$. But
\[
\frac{x}{d}
=2\cdot\frac{x}{2d},
\]
and both factors lie in $S$ and are nonunits by <1>3. Thus $x/d$, and hence $p_j$, is reducible, a contradiction.
:::

<1>5. Therefore $S=\mathbb Z+x\mathbb Q[x]$ is not a UFD.
::: {.proof}
A UFD requires every nonzero nonunit to factor as a finite product of irreducibles. By <1>4, the nonzero nonunit $x$ has no such factorization. Hence $S$ is not a UFD.
:::

Thus the answers are: (1) no, (2) yes, and (3) no.
:::
