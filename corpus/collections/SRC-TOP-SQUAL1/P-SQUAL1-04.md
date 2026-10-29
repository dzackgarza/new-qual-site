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

::: {.solution}

## Part 1

::: pf

::: pf-step

Let
\[
f:\RR\to\RR
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

For any open set \(V\subseteq\RR\),
\[
f^{-1}(V)
=
\begin{cases}
\RR,&0\in V,\\
\varnothing,&0\notin V.
\end{cases}
\]
Both possibilities are open.

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

The singleton \(\{0\}\) is not open in the usual topology on \(\RR\).


::: pf-proof

Every open neighborhood of \(0\) contains points other than \(0\).

:::

:::

::: {.pf-step #s1-5}

Therefore \(f\) is not an open map.


::: pf-proof

An open map must send every open subset of the domain to an open subset of the codomain. Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} exhibit an open set whose image is not open.

:::

:::

::: {.pf-step #s1-6}

Let
\[
U\subseteq A
\]
be open in the subspace topology on \(A\).


::: pf-proof

To prove \(q\) is open, it suffices to show that \(q(U)\) is open in \(p(A)\) for an arbitrary open \(U\subseteq A\).

:::

:::

::: {.pf-step #s1-7}

Since \(A\) is open in \(X\), the set \(U\) is open in \(X\).


::: pf-proof

Because \(U\) is open in the subspace \(A\), there exists an open set \(V\subseteq X\) such that
\[
U=A\cap V.
\]
Since both \(A\) and \(V\) are open in \(X\), their intersection \(U\) is open in \(X\).

:::

:::

::: {.pf-step #s1-8}

Since \(p\) is open,
\[
\boxed{p(U)\text{ is open in }Y}.
\]


::: pf-proof

Apply the definition of an open map to the open subset \(U\subseteq X\) from step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
\[
\boxed{q(U)=p(U)}.
\]


::: pf-proof

The map \(q\) is simply the restriction of \(p\) to \(A\), and \(U\subseteq A\).

:::

:::

::: {.pf-step #s1-10}

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

The first equality is step [](#s1-9){.pf-ref}. The second follows from the inclusion \(p(U)\subseteq p(A)\).

:::

:::

::: pf-step

Therefore \(q(U)\) is open in the subspace \(p(A)\).


::: pf-proof

By step [](#s1-8){.pf-ref}, \(p(U)\) is open in \(Y\). Step [](#s1-10){.pf-ref} expresses \(q(U)\) as the intersection of \(p(A)\) with an open subset of \(Y\), which is exactly a subspace-open set.

:::

:::

::: {.pf-step #s1-12}

Hence
\[
\boxed{q:A\to p(A)\text{ is open}.}
\]


::: pf-proof

The open set \(U\subseteq A\) in step [](#s1-6){.pf-ref} was arbitrary.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers part 1, and step [](#s1-12){.pf-ref} proves part 2.

:::

:::

:::
