---
schema: qual/card@1
id: P-AGH2317ZARISKISPACE
kind: problem
title: Zariski spaces, closed points, and stability under specialization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Spaces
  - Noetherian Spaces
  - Generic Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.17 statement and the t(X) construction from II.2.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A topological space $X$ is a **Zariski space** if it is noetherian and every nonempty closed irreducible subset has a unique generic point.

For example, let $R$ be a discrete valuation ring and let $T = \operatorname{sp}(\Spec R)$.
Then $T$ consists of two points: $t_0$, the maximal ideal, and $t_1$, the zero ideal.
The open subsets are $\varnothing$, $\ts{t_1}$, and $T$.
This is an irreducible Zariski space with generic point $t_1$.

a. Show that if $X$ is a noetherian scheme then $\operatorname{sp}(X)$ is a Zariski space.

b. Show that any minimal nonempty closed subset of a Zariski space consists of one point.
We call these closed points.

c. Show that a Zariski space $X$ satisfies the axiom $T_0$: given any two distinct points of $X$, there is an open set containing one but not the other.

d. If $X$ is an irreducible Zariski space, then its generic point is contained in every nonempty open subset of $X$.

e. If $x_0 \in \cl\qty{\ts{x_1}}$, we say $x_0$ is a specialization of $x_1$, or that $x_1$ is a generization of $x_0$.
Now let $X$ be a Zariski space.
Show that the minimal points for the partial ordering determined by $x_1 > x_0$ when $x_0$ is a specialization of $x_1$ are the closed points, and the maximal points are the generic points of the irreducible components of $X$.
Show also that a closed subset contains every specialization of any of its points; we say closed subsets are **stable under specialization**. Similarly, open subsets are stable under generization.

f. Let $t$ be the functor on topological spaces introduced in the proof of Hartshorne II.2.6. If $X$ is a noetherian topological space, show that $t(X)$ is a Zariski space.
Furthermore, $X$ itself is a Zariski space if and only if the map $\alpha: X \to t(X)$ is a homeomorphism.
:::

::: {.solution}
<1>1. If $X$ is a noetherian scheme, then its underlying topological space is a Zariski space.
::: {.proof}
By definition of a noetherian scheme, the underlying space is noetherian.

Let
\[
Z\subseteq X
\]
be a nonempty irreducible closed subset.  Hartshorne II.2.9 shows that every nonempty irreducible closed subset of a scheme has a unique generic point.  Therefore $Z$ has a unique generic point.  This is exactly the definition of a Zariski space.
:::

<1>2. Any minimal nonempty closed subset $Y$ of a Zariski space consists of one point.
::: {.proof}
For any $y\in Y$, the closure
\[
\overline{\{y\}}
\]
is a nonempty closed subset of $Y$.  By minimality,
\[
\overline{\{y\}}=Y.
\]
Thus every point of $Y$ is a generic point of $Y$.

The set $Y$ is irreducible: if
\[
Y=Y_1\cup Y_2
\]
with $Y_i$ closed in $Y$, then every nonempty $Y_i$ is a nonempty closed subset of $X$ contained in $Y$, hence must equal $Y$ by minimality.  So one of $Y_1,Y_2$ equals $Y$.

Since $Y$ is irreducible and the space is Zariski, $Y$ has a unique generic point.  But every point of $Y$ is generic, so $Y$ has exactly one point.
:::

<1>3. A Zariski space satisfies the $T_0$ axiom.
::: {.proof}
Let $x\ne y$.  The closures
\[
\overline{\{x\}},\qquad\overline{\{y\}}
\]
are irreducible closed subsets.  If they were equal, then $x$ and $y$ would both be generic points of the same irreducible closed subset, contradicting uniqueness.

Thus the closures differ.  After interchanging $x$ and $y$ if necessary, assume
\[
y\notin\overline{\{x\}}.
\]
Then
\[
X\setminus\overline{\{x\}}
\]
is an open set containing $y$ but not $x$.  Hence $X$ is $T_0$.
:::

<1>4. If $X$ is an irreducible Zariski space with generic point $\eta$, then $\eta$ lies in every nonempty open subset of $X$.
::: {.proof}
Let $U\subseteq X$ be nonempty.  If $\eta\notin U$, then the closed set
\[
X\setminus U
\]
contains $\eta$, hence contains
\[
\overline{\{\eta\}}=X.
\]
This would force $U=\varnothing$, contradiction.
:::

<1>5. Under the specialization order
\[
x_1>x_0
\quad\Longleftrightarrow\quad
x_0\in\overline{\{x_1\}},
\]
the minimal points are exactly the closed points.
::: {.proof}
If $x$ is closed, then
\[
\overline{\{x\}}=\{x\},
\]
so $x$ has no proper specialization and is minimal.

Conversely, if $x$ is minimal, every point of the nonempty closed set
\[
\overline{\{x\}}
\]
is a specialization of $x$.  Minimality therefore forces
\[
\overline{\{x\}}=\{x\},
\]
so $x$ is closed.
:::

<1>6. The maximal points for the specialization order are exactly the generic points of the irreducible components of $X$.
::: {.proof}
Let $x$ be maximal.  The irreducible closed subset
\[
\overline{\{x\}}
\]
is contained in some irreducible component $C$ of $X$.  Let $\eta_C$ be the generic point of $C$.  Then
\[
x\in C=\overline{\{\eta_C\}},
\]
so $\eta_C$ is a generization of $x$.  Maximality gives
\[
x=\eta_C.
\]

Conversely, let $x=\eta_C$ be the generic point of an irreducible component $C$, and suppose $y$ is a generization of $x$.  Then
\[
x\in\overline{\{y\}},
\]
so
\[
C=\overline{\{x\}}\subseteq\overline{\{y\}}.
\]
The right side is irreducible and closed.  Maximality of the irreducible component $C$ forces
\[
\overline{\{y\}}=C.
\]
Thus $y$ and $x$ are both generic points of $C$, and uniqueness gives $y=x$.  Hence $x$ is maximal.
:::

<1>7. Closed subsets are stable under specialization, and open subsets are stable under generization.
::: {.proof}
Let $F\subseteq X$ be closed and let $x\in F$.  If $x_0$ is a specialization of $x$, then
\[
x_0\in\overline{\{x\}}\subseteq F
\]
because $F$ is closed.  Thus $F$ is stable under specialization.

Now let $U$ be open, let $x\in U$, and let $y$ be a generization of $x$.  If $y\notin U$, then the closed complement $X\setminus U$ contains $y$ and therefore all its specializations, including $x$, contradiction.  Hence $y\in U$.
:::

<1>8. Let $X$ be a noetherian topological space.  Recall that $t(X)$ is the set of nonempty irreducible closed subsets of $X$, with closed subsets
\[
t(Y)=\{Z\in t(X):Z\subseteq Y\}
\]
for closed $Y\subseteq X$.  Then $t(X)$ is noetherian.
::: {.proof}
The assignment
\[
Y\longmapsto t(Y)
\]
preserves inclusions and arbitrary intersections.  It also preserves finite unions: if an irreducible closed subset $Z$ is contained in
\[
Y_1\cup Y_2,
\]
then
\[
Z=(Z\cap Y_1)\cup(Z\cap Y_2),
\]
so irreducibility forces $Z\subseteq Y_1$ or $Z\subseteq Y_2$.  Hence
\[
t(Y_1\cup Y_2)=t(Y_1)\cup t(Y_2).
\]
Thus these $t(Y)$ are exactly the closed sets of the topology on $t(X)$.

If
\[
t(Y_1)\supseteq t(Y_2)\supseteq\cdots
\]
is a descending chain of closed subsets of $t(X)$, then
\[
Y_1\supseteq Y_2\supseteq\cdots.
\]
Indeed, if $x\in Y_{n+1}$ then the irreducible closed set $\overline{\{x\}}$ lies in $t(Y_{n+1})\subseteq t(Y_n)$, so $x\in Y_n$.

Since $X$ is noetherian, the chain $Y_n$ stabilizes, hence so does the chain $t(Y_n)$.  Therefore $t(X)$ is noetherian.
:::

<1>9. Every nonempty irreducible closed subset of $t(X)$ has a unique generic point.
::: {.proof}
Let
\[
t(Y)\subseteq t(X)
\]
be nonempty and irreducible.  If $Y$ were reducible,
\[
Y=Y_1\cup Y_2
\]
with proper closed subsets $Y_i$, then
\[
t(Y)=t(Y_1)\cup t(Y_2)
\]
would be reducible.  Hence $Y$ is irreducible.

Thus $Y$ itself is a point of $t(X)$.  Its closure in $t(X)$ is
\[
\overline{\{Y\}}=t(Y),
\]
because a closed set $t(F)$ contains the point $Y$ exactly when $Y\subseteq F$, and then it contains every irreducible closed subset of $Y$.
So $Y$ is a generic point of $t(Y)$.

If another point $Z\in t(X)$ had the same closure, then
\[
t(Z)=t(Y).
\]
Since $Z\in t(Z)=t(Y)$, one has $Z\subseteq Y$, and similarly $Y\subseteq Z$.  Thus $Z=Y$.  The generic point is unique.
:::

<1>10. Hence $t(X)$ is a Zariski space.
::: {.proof}
Step <1>8 gives noetherianity and <1>9 gives unique generic points for nonempty irreducible closed subsets.
:::

<1>11. Define
\[
\alpha:X\longrightarrow t(X),
\qquad
x\longmapsto\overline{\{x\}}.
\]
Then $\alpha$ is continuous and
\[
\alpha^{-1}(t(Y))=Y
\]
for every closed subset $Y\subseteq X$.
::: {.proof}
For $x\in X$,
\[
\alpha(x)\in t(Y)
\iff
\overline{\{x\}}\subseteq Y.
\]
Because $Y$ is closed, this is equivalent to $x\in Y$.  Thus the inverse image of the closed set $t(Y)$ is the closed set $Y$, proving continuity and the formula.
:::

<1>12. If $X$ is a Zariski space, then $\alpha:X\to t(X)$ is a bijection.
::: {.proof}
Every point of $t(X)$ is an irreducible closed subset $Y\subseteq X$.  Since $X$ is a Zariski space, $Y$ has a generic point $y$, and
\[
\alpha(y)=\overline{\{y\}}=Y.
\]
Thus $\alpha$ is surjective.

If $\alpha(x)=\alpha(y)$, then $x$ and $y$ are both generic points of the same irreducible closed subset.  Uniqueness gives $x=y$.  Thus $\alpha$ is injective.
:::

<1>13. If $X$ is a Zariski space, then $\alpha$ is a homeomorphism.
::: {.proof}
By <1>12, $\alpha$ is bijective, and by <1>11 it is continuous.

Let $Y\subseteq X$ be closed.  For every irreducible closed subset $Z\subseteq Y$, the Zariski-space property gives a generic point $z\in Z\subseteq Y$, and
\[
\alpha(z)=Z.
\]
Hence
\[
\alpha(Y)=t(Y),
\]
which is closed in $t(X)$.  Therefore $\alpha$ is a closed continuous bijection and hence a homeomorphism.
:::

<1>14. Conversely, if $X$ is noetherian and $\alpha:X\to t(X)$ is a homeomorphism, then $X$ is a Zariski space.
::: {.proof}
By <1>10, $t(X)$ is a Zariski space.  The property of being noetherian with a unique generic point for every nonempty irreducible closed subset is topological and is preserved by homeomorphism.  Hence $X$ is a Zariski space.
:::

<1>15. Therefore, for a noetherian space $X$,
\[
\boxed{
X\text{ is a Zariski space}
\iff
\alpha:X\xrightarrow{\sim}t(X)\text{ is a homeomorphism}.}
\]
::: {.proof}
Steps <1>13 and <1>14 prove the two implications.
:::

<1>16. Q.E.D.
::: {.proof}
Steps <1>1--<1>7 prove parts (a)--(e), and steps <1>8--<1>15 prove part (f).
:::
:::
