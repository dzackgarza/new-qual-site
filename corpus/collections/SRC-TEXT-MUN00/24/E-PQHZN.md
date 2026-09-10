---
schema: qual/card@1
id: E-PQHZN
kind: problem
title: The long line
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Recall that $S_\Omega$ denotes the minimal uncountable well-ordered set.
Let $L$ denote the ordered set $S_\Omega \times [0, 1)$ in the dictionary order, with its smallest element deleted.
The set $L$ is a classical example in topology called the long line.

Theorem.
The long line is path connected and locally homeomorphic to $\mathbb{R}$, but it cannot be imbedded in $\mathbb{R}$.

(a) Let $X$ be an ordered set; let $a < b < c$ be points of $X$.
Show that $[a, c)$ has the order type of $[0, 1)$ if and only if both $[a, b)$ and $[b, c)$ have the order type of $[0, 1)$.

(b) Let $X$ be an ordered set.
Let $x_0 < x_1 < \cdots$ be an increasing sequence of points of $X$; suppose $b = \sup\ts{x_i}$.
Show that $[x_0, b)$ has the order type of $[0, 1)$ if and only if each interval $[x_i, x_{i+1})$ has the order type of $[0, 1)$.

(c) Let $a_0$ denote the smallest element of $S_\Omega$.
For each element $a$ of $S_\Omega$ different from $a_0$, show that the interval $[a_0 \times 0, a \times 0)$ of $S_\Omega \times [0, 1)$ has the order type of $[0, 1)$.
[Hint: Proceed by transfinite induction. Either $a$ has an immediate predecessor in $S_\Omega$, or there is an increasing sequence $a_i$ in $S_\Omega$ with $a = \sup\ts{a_i}$.]

(d) Show that $L$ is path connected.

(e) Show that every point of $L$ has a neighborhood homeomorphic with an open interval in $\mathbb{R}$.

(f) Show that $L$ cannot be imbedded in $\mathbb{R}$, or indeed in $\mathbb{R}^n$ for any $n$.
[Hint: Any subspace of $\mathbb{R}^n$ has a countable basis for its topology.]
:::

::: {.solution}
Let $a_0$ be the least element of $S_\Omega$.

(a) Suppose first that $[a,c)$ has order type $[0,1)$, and let $t\in(0,1)$ be the image of $b$. Then $[a,b)$ and $[b,c)$ correspond to $[0,t)$ and $[t,1)$, each order-isomorphic to $[0,1)$ by affine rescaling. Conversely, if both pieces have order type $[0,1)$, map them respectively onto
\[
[0,1/2)\qquad\text{and}\qquad[1/2,1)
\]
by order isomorphisms. Their union gives an order isomorphism $[a,c)\cong[0,1)$.

(b) If $[x_0,b)\cong[0,1)$, the images $t_i$ of $x_i$ increase to $1$ because $b=\sup x_i$. Hence each $[x_i,x_{i+1})$ corresponds to $[t_i,t_{i+1})$, which has order type $[0,1)$. Conversely, if every $[x_i,x_{i+1})$ has order type $[0,1)$, map the $i$th piece order-isomorphically onto
\[
[1-2^{-i},\,1-2^{-(i+1)})
\]
(after indexing from $i=0$ in the evident way). These maps concatenate to an order isomorphism $[x_0,b)\cong[0,1)$.

(c) Proceed by transfinite induction on $a\in S_\Omega-\{a_0\}$. If $a$ has immediate predecessor $b$, then
\[
[a_0\times0,a\times0)
=[a_0\times0,b\times0)\cup[b\times0,a\times0),
\]
and the second piece is exactly the fiber $\{b\}\times[0,1)$, so part (a) and the induction hypothesis apply.

If $a$ has no immediate predecessor, its section $S_a$ is countable by minimality of $S_\Omega$. Enumerate a cofinal increasing sequence $a_0'<a_1'<\cdots$ with supremum $a$ (take running maxima of an enumeration of $S_a$). By induction, each interval
\[
[a_i'\times0,a_{i+1}'\times0)
\]
has order type $[0,1)$, so part (b) yields the result for $a$.

(d) The argument in (c), together with (a), shows more generally that every bounded interval in $L$ is order-isomorphic to a real interval. Thus if $p<q$ in $L$, the closed interval $[p,q]$ is homeomorphic to $[0,1]$. Composing such a homeomorphism with the standard path $[0,1]\to[0,1]$ gives a path from $p$ to $q$. Hence $L$ is path connected.

(e) For any $x\in L$, choose $p<x<q$. The same bounded-interval argument shows $(p,q)$ is order-isomorphic, hence homeomorphic, to an open interval of $\mathbb R$. Thus every point has a neighborhood homeomorphic to an open real interval.

(f) The long line is not second countable. For each $a\in S_\Omega$, the vertical interval
\[
\{a\}\times(1/3,2/3)
\]
is a nonempty open subset of $L$, and these sets are pairwise disjoint. A second-countable space can have only countably many pairwise disjoint nonempty open sets, since each contains a distinct element of a fixed countable basis. Therefore $L$ is not second countable.

Every subspace of $\mathbb R^n$ is second countable, because $\mathbb R^n$ has a countable basis and intersections with the subspace form a countable basis. Hence $L$ cannot be embedded in $\mathbb R^n$ for any finite $n$, in particular not in $\mathbb R$.
:::
