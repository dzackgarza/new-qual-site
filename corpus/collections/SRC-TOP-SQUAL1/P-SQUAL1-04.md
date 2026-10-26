---
schema: qual/card@1
id: P-SQUAL1-04
kind: problem
title: Continuous open maps and restrictions to open subspaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
A function $f:X\to Y$ is called **open** if $f(U)$ is open in $Y$ for every open $U\subseteq X$.

1. Give an example of a continuous function that is not open.
2. Let $p:X\to Y$ be continuous and open, and let $A\subseteq X$ be open. Show that the restriction
$$q:A\to p(A)$$
is open, where $p(A)$ has the subspace topology from $Y$.
:::

## Part 1

::: pf

::: pf-step

Let
\[
f:\mathbb R\to\mathbb R
\]
be the constant map
\[
\boxed{f(x)=0}.
\]


::: pf-proof

This gives a concrete function between spaces with the usual topology.

:::

:::

::: pf-step

The map \(f\) is continuous.


::: pf-proof

For any open set \(V\subseteq\mathbb R\),
\[
f^{-1}(V)
=
\begin{cases}
\mathbb R,&0\in V,\\
\varnothing,&0\notin V.
\end{cases}
\]
Both possibilities are open.

:::

:::

::: pf-step

The open set
\[
U=(0,1)
\]
has image
\[
\boxed{f(U)=\{0\}}.
\]


::: pf-proof

The map is constant.

:::

:::

::: pf-step

The singleton \(\{0\}\) is not open in the usual topology on \(\mathbb R\).


::: pf-proof

Every open neighborhood of \(0\) contains points other than \(0\).

:::

:::

::: pf-step

Therefore \(f\) is not an open map.


::: pf-proof

An open map must send every open subset of the domain to an open subset of the codomain. Steps <1>3--<1>4 exhibit an open set whose image is not open.

:::

:::

::: pf-step

Let
\[
U\subseteq A
\]
be open in the subspace topology on \(A\).


::: pf-proof

To prove \(q\) is open, it suffices to show that \(q(U)\) is open in \(p(A)\) for an arbitrary open \(U\subseteq A\).

:::

:::

::: pf-step

Since \(A\) is open in \(X\), the set \(U\) is open in \(X\).


::: pf-proof

Because \(U\) is open in the subspace \(A\), there exists an open set \(V\subseteq X\) such that
\[
U=A\cap V.
\]
Since both \(A\) and \(V\) are open in \(X\), their intersection \(U\) is open in \(X\).

:::

:::

::: pf-step

Since \(p\) is open,
\[
\boxed{p(U)\text{ is open in }Y}.
\]


::: pf-proof

Apply the definition of an open map to the open subset \(U\subseteq X\) from step <1>7.

:::

:::

::: pf-step

One has
\[
\boxed{q(U)=p(U)}.
\]


::: pf-proof

The map \(q\) is simply the restriction of \(p\) to \(A\), and \(U\subseteq A\).

:::

:::

::: pf-step

Since
\[
p(U)\subseteq p(A),
\]
one has
\[
q(U)
=
p(U)
=
p(A)\cap p(U).
\]


::: pf-proof

The first equality is step <1>9. The second follows from the inclusion \(p(U)\subseteq p(A)\).

:::

:::

::: pf-step

Therefore \(q(U)\) is open in the subspace \(p(A)\).


::: pf-proof

By step <1>8, \(p(U)\) is open in \(Y\). Step <1>10 expresses \(q(U)\) as the intersection of \(p(A)\) with an open subset of \(Y\), which is exactly a subspace-open set.

:::

:::

::: pf-step

Hence
\[
\boxed{q:A\to p(A)\text{ is open}.}
\]


::: pf-proof

The open set \(U\subseteq A\) in step <1>6 was arbitrary.

:::

:::

::: pf-qed

Step <1>5 answers part 1, and step <1>12 proves part 2.

:::

:::
