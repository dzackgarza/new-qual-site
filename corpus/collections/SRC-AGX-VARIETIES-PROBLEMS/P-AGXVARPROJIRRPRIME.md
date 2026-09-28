---
schema: qual/card@1
id: P-AGXVARPROJIRRPRIME
kind: problem
title: A projective variety is irreducible iff its ideal is homogeneous prime
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Homogeneous Ideals
  - Irreducibility
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definition 7.4, Exercises 7.6, and Definition 7.9 in the
    recorded source. Exercise 7.6 supplies the homogeneous witness for
    non-primality, while Definition 7.9 defines projective varieties using
    homogeneous prime ideals.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the circular wording "a projective variety is irreducible iff"
    by the substantive statement for a nonempty projective algebraic set:
    topological irreducibility is equivalent to primality of its homogeneous
    vanishing ideal.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    For irreducible X, used the source's homogeneous witnesses f,g for a
    hypothetical failure of primality to produce a union of two proper
    projective closed subsets. The converse uses the completed forward
    implication P-AGXVARPROJIRR from a homogeneous prime ideal.
---

::: {.problem}
Let
$$
X\subseteq\PP^n_k
$$
be a nonempty projective algebraic set over the algebraically closed ground
field $k$, and let
$$
I(X)\subseteq k[x_0,\ldots,x_n]
$$
be its homogeneous vanishing ideal. Show that
$$
X\text{ is irreducible}
\quad\Longleftrightarrow\quad
I(X)\text{ is prime}.
$$
:::

::: {.solution}
<1>1. Suppose that $X$ is irreducible. Then $I(X)$ is prime.

::: {.proof}
Assume for contradiction that the homogeneous ideal $I(X)$ is not prime.
A homogeneous ideal $I$ is prime if and only if, for all homogeneous $f,g$,
$fg\in I$ implies $f\in I$ or $g\in I$. Hence there exist
homogeneous polynomials
$$
f,g\in k[x_0,\ldots,x_n]
$$
such that
$$
fg\in I(X),
\qquad
f\notin I(X),
\qquad
g\notin I(X).
$$

Because $fg$ vanishes at every point of $X$, for each
$$
p\in X
$$
one has
$$
f(p)g(p)=0.
$$
Since $k$ is a field, either $f(p)=0$ or $g(p)=0$. Therefore
$$
X
=
\bigl(X\intersect V_+(f)\bigr)
\union
\bigl(X\intersect V_+(g)\bigr).
$$
Both terms are Zariski closed in $X$ because $f$ and $g$ are homogeneous.

The first term is proper: since
$$
f\notin I(X),
$$
there is a point of $X$ where $f$ does not vanish. Likewise the second term
is proper because
$$
g\notin I(X).
$$
Thus $X$ is the union of two proper closed subsets, contradicting
irreducibility. Hence $I(X)$ is prime.
:::

<1>2. Suppose that $I(X)$ is prime. Then $X$ is irreducible.

::: {.proof}
Since $X$ is Zariski closed,
$$
X=V_+\bigl(I(X)\bigr).
$$
The ideal $I(X)$ is homogeneous and prime, and $V_+(P)$ is irreducible for
every homogeneous prime $P$ with $V_+(P)$ nonempty [[P-AGXVARPROJIRR]].
Therefore $X$ is irreducible.
:::

<1>3. Therefore
$$
\boxed{
X\text{ is irreducible}
\quad\Longleftrightarrow\quad
I(X)\text{ is a homogeneous prime ideal}.
}
$$

::: {.proof}
Step <1>1 proves the forward implication. Step <1>2 proves the converse.
The ideal $I(X)$ is homogeneous by its projective vanishing-ideal
construction.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required equivalence.
:::
:::
