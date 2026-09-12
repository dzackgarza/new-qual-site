---
schema: qual/card@1
id: P-ALGS09G
kind: problem
title: "Factorization in Noetherian domains, integral closure of UFDs, and non-UFD examples"
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
  date: 2026-09-08
  note: Compared with Problem 7 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Proved atomicity by ACC on principal ideals, integral closure of UFDs by a coprime denominator argument, and non-UFD Noetherianity of Z[sqrt(-5)] using the multiplicative norm.
---

::: problem
(a) Show that a commutative Noetherian domain $R$ has the following property: given any nonzero, nonunit $x \in R$ one has $x = z_1 z_2 \cdots z_m$ for some irreducible elements $z_i \in R$.

(b) Prove that any UFD is integrally closed in its field of fractions.

(c) Give, with proof, an example of a domain $R$ which is Noetherian, but not a UFD.
:::

::: {.solution}
<1>1. Every nonzero nonunit in a Noetherian domain is a finite product of irreducibles.
::: {.proof}
Assume, for contradiction, that some nonzero nonunit $x_0\in R$ is not a finite product of irreducibles.
Then $x_0$ is not irreducible, so
\[
x_0=x_1y_1
\]
with $x_1,y_1$ nonunits.
If both $x_1$ and $y_1$ were finite products of irreducibles, then so would be $x_0$.
Hence at least one factor is again a nonzero nonunit that is not a finite product of irreducibles; rename it $x_1$.

Since $x_0=x_1y_1$,
\[
(x_0)\subseteq(x_1).
\]
This inclusion is strict.
Indeed, if $(x_0)=(x_1)$, then $x_1=x_0r=x_1y_1r$ for some $r\in R$.
Because $R$ is a domain and $x_1\ne0$,
\[
1=y_1r,
\]
contradicting that $y_1$ is a nonunit.

Repeating the construction gives an infinite strictly ascending chain
\[
(x_0)\subsetneq(x_1)\subsetneq(x_2)\subsetneq\cdots.
\]
But a Noetherian ring satisfies the ascending chain condition on ideals.
This contradiction proves that every nonzero nonunit factors into finitely many irreducibles.
:::

<1>2. Every UFD is integrally closed in its field of fractions.
::: {.proof}
Let $R$ be a UFD with fraction field $K$, and suppose
\[
\alpha=\frac ab\in K
\]
is integral over $R$, where $a,b\in R$, $b\ne0$, and $a,b$ have no common irreducible factor.
Since $\alpha$ is integral, there are $c_0,\ldots,c_{n-1}\in R$ such that
\[
\alpha^n+c_{n-1}\alpha^{n-1}+\cdots+c_1\alpha+c_0=0.
\]
Multiplying by $b^n$ gives
\[
a^n+c_{n-1}a^{n-1}b+\cdots+c_1ab^{n-1}+c_0b^n=0.
\]
Hence
\[
b\mid a^n.
\]
If $b$ were not a unit, some irreducible $q$ would divide $b$.
Then $q\mid a^n$.
In a UFD every irreducible is prime, so $q\mid a$, contradicting the choice of $a,b$ with no common irreducible factor.
Therefore $b$ is a unit, and
\[
\alpha\in R.
\]
Thus $R$ is integrally closed in $K$.
:::

<1>3. The domain
\[
R=\mathbb Z[\sqrt{-5}]
\]
is Noetherian.
::: {.proof}
As a $\mathbb Z$-module,
\[
R=\mathbb Z\oplus\mathbb Z\sqrt{-5},
\]
so $R$ is finitely generated over the Noetherian ring $\mathbb Z$.
Hence $R$ is a Noetherian $\mathbb Z$-module.
Every ideal of $R$ is, in particular, a $\mathbb Z$-submodule of $R$.
Therefore every ascending chain of ideals of $R$ stabilizes, so $R$ is a Noetherian ring.
It is a domain because it is a subring of $\mathbb C$.
:::

<1>4. The ring $\mathbb Z[\sqrt{-5}]$ is not a UFD.
::: {.proof}
For
\[
z=a+b\sqrt{-5}\in R,
\]
define
\[
N(z)=z\overline z=a^2+5b^2\in\mathbb Z_{\ge0}.
\]
The norm is multiplicative:
\[
N(zw)=N(z)N(w).
\]
The only units have norm $1$.
There are no elements of norm $2$ or $3$, since
\[
a^2+5b^2=2
\quad\text{or}\quad
3
\]
has no integer solutions.

Now
\[
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
\]
The elements $2$ and $3$ are irreducible: a nontrivial factorization of $2$ would force a factor of norm $2$, and a nontrivial factorization of $3$ would force a factor of norm $3$.
Likewise
\[
N(1\pm\sqrt{-5})=6,
\]
so a nontrivial factorization of either element would force factors of norms $2$ and $3$; these do not exist.
Thus all four displayed factors are irreducible.

The two factorizations are inequivalent up to units and ordering.
Indeed associates have the same norm, whereas
\[
N(2)=4,
\qquad
N(3)=9,
\qquad
N(1\pm\sqrt{-5})=6.
\]
Hence neither $2$ nor $3$ is associate to either $1+\sqrt{-5}$ or $1-\sqrt{-5}$.
Therefore $R$ does not have unique factorization.
:::

<1>5. Consequently $\mathbb Z[\sqrt{-5}]$ is a Noetherian domain that is not a UFD.
::: {.proof}
Combine <1>3 and <1>4.
:::
:::
