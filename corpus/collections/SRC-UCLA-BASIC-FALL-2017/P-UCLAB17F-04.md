---
schema: qual/card@1
id: P-UCLAB17F-04
kind: problem
title: When the coordinate duals form a basis of the algebraic dual
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $V$ be a real vector space with basis $\{e_i\}_{i\in I}$. Define $e_i^\#\in V^*$ by $e_i^\#(e_j)=\delta_{ij}$.

(a) Show that $\{e_i^\#\}_{i\in I}$ is linearly independent in $V^*$.

(b) Give necessary and sufficient conditions on $V$ for these vectors to form a basis of $V^*$, and prove your claim.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The family
$$
\{e_i^\#\}_{i\in I}
$$
is linearly independent.


::: pf-proof

Consider a finite linear relation
$$
\sum_{i\in F}c_i e_i^\#=0,
$$
where
$$
F\subseteq I
$$
is finite.
Fix
$$
j\in F.
$$
Evaluate the relation at $e_j$:
$$
0
=
\sum_{i\in F}c_i e_i^\#(e_j)
=
\sum_{i\in F}c_i\delta_{ij}
=
c_j.
$$
Since $j$ was arbitrary, every coefficient vanishes.
Thus the family is linearly independent.

:::

:::

::: {.pf-step #s1-2}

If $V$ is finite-dimensional, then
$$
\{e_i^\#\}_{i\in I}
$$
is a basis of $V^*$.


::: pf-proof

If
$$
\dim V=n<\infty,
$$
then the basis index set $I$ has exactly $n$ elements.
The dual space also has dimension $n$.
By step [](#s1-1){.pf-ref}, the $n$ coordinate functionals are linearly independent in $V^*$.
Therefore they form a basis.

:::

:::

::: {.pf-step #s1-3}

Suppose $I$ is infinite.
Define
$$
\varphi:V\to\RR
$$
by
$$
\varphi\left(
\sum_{i\in F}a_i e_i
\right)
=
\sum_{i\in F}a_i,
$$
where $F\subseteq I$ is finite.
Then $\varphi$ is a well-defined linear functional.


::: pf-proof

Every vector in $V$ has a unique finite expansion in the Hamel basis $\{e_i\}_{i\in I}$.
Hence the displayed formula is well-defined.
For vectors with finite coordinate expansions and scalars $\alpha,\beta\in\RR$, summing coefficients shows
$$
\varphi(\alpha v+\beta w)
=
\alpha\varphi(v)+\beta\varphi(w).
$$
Thus
$$
\varphi\in V^*.
$$

:::

:::

::: {.pf-step #s1-4}

For every $j\in I$,
$$
\varphi(e_j)=1.
$$


::: pf-proof

The basis vector $e_j$ has coefficient $1$ at index $j$ and coefficient $0$ at all other indices.
Thus the sum of its coordinates is $1$.

:::

:::

::: {.pf-step #s1-5}

The functional $\varphi$ from step [](#s1-3){.pf-ref} is not in the span of
$$
\{e_i^\#\}_{i\in I}.
$$


::: pf-proof

Any vector in the algebraic span of the family has the form
$$
\psi
=
\sum_{i\in F}c_i e_i^\#
$$
for some finite subset $F\subseteq I$.
Because $I$ is infinite, choose
$$
j\in I\setminus F.
$$
Then
$$
\psi(e_j)
=
\sum_{i\in F}c_i e_i^\#(e_j)
=0.
$$
But step [](#s1-4){.pf-ref} gives
$$
\varphi(e_j)=1.
$$
Hence
$$
\psi\ne\varphi.
$$
So $\varphi$ is not in the span.

:::

:::

::: {.pf-step #s1-6}

If $V$ is infinite-dimensional, the family
$$
\{e_i^\#\}_{i\in I}
$$
does not span $V^*$.


::: pf-proof

An infinite-dimensional vector space has an infinite Hamel basis, so the index set $I$ is infinite.
Then step [](#s1-5){.pf-ref} supplies a functional in $V^*$ outside the span of the coordinate functionals.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\{e_i^\#\}_{i\in I}
\text{ is a basis of }V^*
\iff
\dim V<\infty.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves sufficiency, and step [](#s1-6){.pf-ref} proves necessity.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} proves part (b).

:::

:::

:::
