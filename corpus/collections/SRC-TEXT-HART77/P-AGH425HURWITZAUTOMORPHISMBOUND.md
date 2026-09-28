---
schema: qual/card@1
id: P-AGH425HURWITZAUTOMORPHISMBOUND
kind: problem
title: A curve of genus $g \geq 2$ has at most $84(g-1)$ automorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Curves
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.5. The proof below derives the branch-fibre
    contribution from the Galois quotient and proves the numerical minimum
    by an exhaustive case analysis of the possible quotient genus and branch
    indices.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Prove the theorem of Hurwitz that a curve $X$ of genus $g \geq 2$ over a field of characteristic 0 has at most $84(g-1)$ automorphisms.

We will see later (Ex.
5.2) or (V, Ex.
1.11) that the group $G=\Aut X$ is finite.
So let $G$ have order $n$.
Then $G$ acts on the function field $K(X)$.
Let $L$ be the fixed field.
Then the field extension $L \subseteq K(X)$ corresponds to a finite morphism of curves $f: X \to Y$ of degree $n$.

a. If $P \in X$ is a ramification point, and $e_P=r$, show that $f^{-1} f(P)$ consists of exactly $n / r$ points, each having ramification index $r$.
Let $P_1, \ldots, P_s$ be a maximal set of ramification points of $X$ lying over distinct points of $Y$, and let $e_{P_i}=r_i$.
Then show that Hurwitz's theorem implies that
$$
{2 g-2 \over n } =2 g(Y)-2+\sum_{i=1}^s\left(1- {1\over r_i}\right)
$$

b. Since $g \geq 2$, the left hand side of the equation is $>0$.
Show that if $g(Y) \geq 0$, $s \geq 0$, $r_i \geq 2$, $i=1, \ldots, s$ are integers such that
$$
2g(Y)-2+\sum_{i=1}^s\left(1- {1\over r_i}\right)>0,
$$
then the minimum value of this expression is $1/42$.
Conclude that $n \leq 84(g-1)$.

See (Ex.
5.7) for an example where this maximum is achieved.
It is known that this maximum is achieved for infinitely many values of $g$ (Macbeath).
Over a field of characteristic $p>0$, the same bound holds, provided $p>g+1$, with one exception, namely the hyperelliptic curve $y^2=x^p-x$, which has $p=2g+1$ and $2p(p^2-1)$ automorphisms (Roquette).
:::

::: {.solution}
Let
$$
G=\Aut X,
\qquad
n=\size G.
$$

<1>1. It is enough to prove the bound after replacing the ground field by
its algebraic closure.

::: {.proof}
Base change to an algebraic closure preserves the genus.  Every
$k$-automorphism of $X$ induces an automorphism of the base-changed curve,
and this map on automorphism groups is injective.  Thus a bound for the
geometric automorphism group also bounds $\Aut_kX$.

We may therefore assume from now on that $k$ is algebraically closed.  In
particular every closed point of the curves below has residue field $k$.
:::

<1>2. If
$$
f:X\longrightarrow Y=X/G
$$
is the quotient map and $P\in X$ has ramification index $e_P=r$, then
$$
f^{-1}(f(P))
$$
has exactly $n/r$ points, and every one of them has ramification index $r$.

::: {.proof}
The extension of function fields
$$
k(Y)=k(X)^G\subseteq k(X)
$$
is Galois with group $G$.  Hence $G$ acts transitively on the points of $X$
lying over a fixed point of $Y$.

Let
$$
G_P=\{\sigma\in G:\sigma(P)=P\}
$$
be the stabilizer.  For a Galois extension of function fields, $G_P$ is the
decomposition group at $P$.  Because the residue field extension is trivial
over the algebraically closed field $k$, the decomposition group equals the
inertia group.  Its order is therefore the ramification index:
$$
\size G_P=e_P=r.
$$

Orbit--stabilizer now gives
$$
\size(G\cdot P)=\frac nr.
$$
This orbit is the whole fibre.  Stabilizers of points in the same orbit are
conjugate, so they all have order $r$ and hence all points of the fibre have
ramification index $r$.
:::

<1>3. If $P_1,\ldots,P_s$ lie over the distinct branch points of $Y$ and
$$
r_i=e_{P_i},
$$
then
$$
\boxed{
\frac{2g-2}{n}
=
2g(Y)-2
+
\sum_{i=1}^s\left(1-\frac1{r_i}\right).
}
$$

::: {.proof}
Characteristic $0$ ramification is tame, so Riemann--Hurwitz for the
degree-$n$ morphism $f$ gives
$$
2g-2
=
n\bigl(2g(Y)-2\bigr)
+
\sum_{P\in X}(e_P-1).
$$

By step <1>2, the fibre over the branch point represented by $P_i$ contains
$n/r_i$ points, each with ramification index $r_i$.  Its total contribution
to the ramification sum is therefore
$$
\frac n{r_i}(r_i-1)
=
n\left(1-\frac1{r_i}\right).
$$
Summing over all branch fibres and dividing by $n$ gives the displayed
formula.
:::

<1>4. Put
$$
E
=
2g(Y)-2
+
\sum_{i=1}^s\left(1-\frac1{r_i}\right),
\qquad
r_i\ge2.
$$
If $E>0$ and $g(Y)\ge1$, then
$$
E\ge\frac12.
$$

::: {.proof}
If $g(Y)\ge2$, then already
$$
2g(Y)-2\ge2.
$$

If $g(Y)=1$, the genus term is $0$.  Positivity then forces at least one
branch point, and every summand satisfies
$$
1-\frac1{r_i}\ge\frac12.
$$
Thus $E\ge1/2$ in the only remaining case.
:::

<1>5. Suppose $g(Y)=0$.  If $E>0$, then $s\ge3$.  For $s\ge4$, one has
$$
E\ge\frac16.
$$

::: {.proof}
For $g(Y)=0$,
$$
E
=
-2+s-\sum_{i=1}^s\frac1{r_i}.
$$
If $s\le2$, this is negative, so $s\ge3$.

If $s\ge5$, then $1-1/r_i\ge1/2$ gives
$$
E\ge-2+\frac s2\ge\frac12.
$$

If $s=4$, then
$$
E=2-\sum_{i=1}^4\frac1{r_i}.
$$
The choice $(2,2,2,2)$ gives $E=0$.  Subject to $E>0$, the reciprocal sum
is maximized by changing just one denominator from $2$ to the next possible
integer $3$.  Hence
$$
\sum_{i=1}^4\frac1{r_i}
\le
\frac12+\frac12+\frac12+\frac13
=
\frac{11}{6},
$$
and therefore
$$
E\ge\frac16.
$$
:::

<1>6. Suppose $g(Y)=0$ and $s=3$.  Then the smallest positive value of $E$
is
$$
\frac1{42},
$$
attained for
$$
(r_1,r_2,r_3)=(2,3,7)
$$
up to permutation.

::: {.proof}
Reorder the indices so that
$$
2\le r_1\le r_2\le r_3.
$$
Now
$$
E
=
1-left(\frac1{r_1}+\frac1{r_2}+\frac1{r_3}\right),
$$
so we must maximize the reciprocal sum subject to it being strictly less
than $1$.

If $r_1\ge4$, then the sum is at most $3/4$.

Suppose $r_1=3$.  If $r_2=3$, positivity excludes $r_3=3$, so
$r_3\ge4$ and the reciprocal sum is at most
$$
\frac13+\frac13+\frac14
=
\frac{11}{12}.
$$
If $r_2\ge4$, it is at most
$$
\frac13+\frac14+\frac14
=
\frac56.
$$

It remains to take $r_1=2$.  The case $r_2=2$ cannot give a positive $E$.
If $r_2=3$, positivity requires
$$
\frac12+\frac13+\frac1{r_3}<1,
$$
so $r_3\ge7$.  The largest possible reciprocal sum is therefore
$$
\frac12+\frac13+\frac17
=
\frac{41}{42}.
$$
If $r_2=4$, positivity excludes $r_3=4$, so $r_3\ge5$ and the sum is at
most
$$
\frac12+\frac14+\frac15
=
\frac{19}{20}.
$$
Finally, if $r_2\ge5$, the sum is at most
$$
\frac12+\frac15+\frac15
=
\frac9{10}.
$$

Among all cases the largest reciprocal sum strictly below $1$ is therefore
$41/42$, attained at $(2,3,7)$.  Hence the least positive value of $E$ is
$$
1-\frac{41}{42}=\frac1{42}.
$$
:::

<1>7. One has
$$
\boxed{\size\Aut X\le84(g-1).}
$$

::: {.proof}
Since $g\ge2$, step <1>3 gives
$$
E=\frac{2g-2}{n}>0.
$$
Steps <1>4--<1>6 show that every positive value of $E$ is at least $1/42$.
Therefore
$$
\frac{2g-2}{n}\ge\frac1{42},
$$
so
$$
n\le42(2g-2)=84(g-1).
$$
This is Hurwitz's bound.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>2--<1>3 prove part (a), steps <1>4--<1>6 prove the numerical
minimum in part (b), and step <1>7 gives the required automorphism bound.
:::
:::
