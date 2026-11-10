---
schema: qual/card@1
id: E-ZHWI8
kind: problem
title: The set where f is at most g is closed
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Order Topology
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 8, printed pp. 111-112, with the
    pasting lemma on printed p. 108; both parts are stored as printed, including the
    bracketed hint to (b).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.8, PDF p. 12. From them: the two cases for the
    openness of {g < f}, according to whether an element lies between g(a) and f(a) or f(a)
    is its immediate successor, and the pasting of f on {f <= g} with g on {g <= f}. Their
    second case needs the observation that g(x) <= g(a) < f(a) <= f(x), which the card
    supplies; their union is indexed by Y and not by X. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Let $Y$ be an ordered set in the order topology.
Let $f, g: X \to Y$ be continuous.

(a) Show that the set $\theset{x \mid f(x) \leq g(x)}$ is closed in $X$.

(b) Let $h: X \to Y$ be the function

$$
h(x) = \min\theset{f(x), g(x)}.
$$

Show that $h$ is continuous.
[Hint: Use the pasting lemma.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.8, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two cases of (a) and the pasting argument of (b) are theirs, with one step of their second case supplied, and one index set corrected: their union is over $c\in Y$, not $c\in X$. Whitman, printed pp. 184--185, proves (a) with the set of elements having an immediate successor and the same two cases, and (b) by the same pasting lemma.

(a) Put $C=\{x\mid f(x)\le g(x)\}$; we show that $U=X-C=\{x\mid g(x)<f(x)\}$ is open. Let $a\in U$, so $g(a)<f(a)$.

If some $c\in Y$ satisfies $g(a)<c<f(a)$, then
$$
a\in g^{-1}\big((-\infty,c)\big)\cap f^{-1}\big((c,+\infty)\big),
$$
an open set, and any $x$ in that set has $g(x)<c<f(x)$, hence lies in $U$.

If there is no element strictly between $g(a)$ and $f(a)$, then $f(a)$ is the immediate successor of $g(a)$, and
$$
a\in g^{-1}\big((-\infty,f(a))\big)\cap f^{-1}\big((g(a),+\infty)\big),
$$
again an open set. For $x$ in it we have $g(x)<f(a)$ and $f(x)>g(a)$; since $f(a)$ is the immediate successor of $g(a)$, the first inequality gives $g(x)\le g(a)$ and the second gives $f(x)\ge f(a)$. Hence $g(x)\le g(a)<f(a)\le f(x)$ and $x\in U$.

So every point of $U$ has a neighbourhood inside $U$, $U$ is open, and $C$ is closed.

(b) Let $A=\{x\mid f(x)\le g(x)\}$ and $B=\{x\mid g(x)\le f(x)\}$. Both are closed by (a) (applied to the pair $f,g$ and to the pair $g,f$), $A\cap B=\{x\mid f(x)=g(x)\}$, and $A\cup B=X$ because for each $x$ one of $f(x)\le g(x)$, $g(x)\le f(x)$ holds. The restrictions $f\restrict_{A}$ and $g\restrict_{B}$ are continuous, so by the pasting lemma (Theorem 18.3, printed p. 108) the map
$$
h:X\to Y,\qquad h(x)=\begin{cases}f(x),&x\in A,\\ g(x),&x\in B,\end{cases}
$$
is well defined and continuous. For $x\in A$ we have $f(x)\le g(x)$, so $h(x)=f(x)=\min\{f(x),g(x)\}$; for $x\in B$ similarly $h(x)=g(x)=\min\{f(x),g(x)\}$. Hence $h=\min\{f,g\}$ is continuous.
:::
