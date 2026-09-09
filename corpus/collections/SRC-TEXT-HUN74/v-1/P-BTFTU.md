---
schema: qual/card@1
id: P-BTFTU
kind: problem
title: Basic divisibility properties of finite field extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent Hungerford chapter-V solutions-manual transcription reproducing V.1.1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $F/K$ be a field extension.
Show that

1. $[F: K] = 1$ iff $F = K$.

2. If $[F: K]$ is prime, then there are no intermediate fields between $F$ and $K$.

3. If $u\in F$ has degree $n$ over $K$, then $n$ divides $[F: K]$.
:::

::: solution
<1>1. One has $[F:K]=1$ if and only if $F=K$.
::: proof
If $F=K$, then $\{1\}$ is a $K$-basis of $F$, so $[F:K]=1$.

Conversely, suppose $[F:K]=1$. Since $1\ne0$, the singleton $\{1\}$ is a
linearly independent subset of the one-dimensional $K$-vector space $F$, hence
is a basis. Therefore every $x\in F$ has the form $x=a\cdot1$ for some $a\in K$,
so $F\subseteq K$. Since $K\subseteq F$ by hypothesis, $F=K$.
:::

<1>2. If $[F:K]$ is prime, there is no proper intermediate field
$K\subsetneq L\subsetneq F$.
::: proof
Let $K\subseteq L\subseteq F$. The tower law gives
\[
[F:K]=[F:L][L:K].
\]
If $[F:K]=p$ is prime, then one of the positive integer factors on the right is
$1$. If $[F:L]=1$, then $F=L$ by <1>1; if $[L:K]=1$, then $L=K$. Thus no
proper intermediate field exists.
:::

<1>3. If $u\in F$ has degree $n$ over $K$, then
\[
[F:K]=[F:K(u)]\,n.
\]
::: proof
By definition of the degree of an algebraic element,
\[
[K(u):K]=n.
\]
Applying the tower law to
\[
K\subseteq K(u)\subseteq F
\]
gives
\[
[F:K]=[F:K(u)][K(u):K]=[F:K(u)]n.
\]
In particular, when $[F:K]$ is finite, this says in the usual integer sense that
$n$ divides $[F:K]$; the displayed equality is the corresponding general degree
factorization.
:::
:::
