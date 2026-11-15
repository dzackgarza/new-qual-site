---
schema: qual/card@1
id: E-SADP0
kind: problem
title: Continuous surjections from the interval onto cubes
classification:
  areas:
  - topology
  topics:
  - Compactness
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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §44 Exercise 1 (printed p. 274) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00, and Robert Gardner's ETSU notes on §44
    (faculty.etsu.edu/gardnerr/5357/notes/Munkres-44.pdf) prove only Theorem 44.1, which is the input
    here. The card follows the exercise's own hint. Checked line by line against the book: Theorem 44.1
    gives a continuous surjection p: I -> I^2; if q_k: I -> I^{2^k} is a continuous surjection then
    q_k x q_k: I x I -> I^{2^{k+1}} is one (Theorem 18.4 for continuity of a map into a product, and
    surjectivity coordinatewise), so q_{k+1} = (q_k x q_k) o p is a continuous surjection I -> I^{2^{k+1}},
    beginning at q_0 = id_I; for arbitrary n choose k with n <= 2^k and project onto the first n
    coordinates, which is continuous and surjective. Nothing on the card needed correction.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from the answer 74824 by GEdgar to Math StackExchange 74766, "Is [0,1]^\omega a
    continuous image of [0,1]?" (2011-10-22), https://math.stackexchange.com/questions/74766, text
    at tmp/sources/mse-74766-munkres-44-4b.md: from a continuous surjection f(t) = (u(t), v(t))
    onto I^2, the map t -> (u(t), u(v(t)), v(v(t))) is a continuous surjection onto I^3, and the
    pattern continues. GEdgar gives the n = 3 and n = 4 cases and says that the general case is
    then natural; the card states the general map g_n and proves its surjectivity by choosing
    s_{n-1}, ..., s_1 backwards, which is the induction GEdgar leaves to the reader. The earlier
    note above recording that no published solution was located is superseded.
---

::: {.exercise}

Given $n$, show there is a continuous surjective map $g: I \to I^n$.
[Hint: Consider

$$
f \times f: I \times I \to I^2 \times I^2.]
$$
:::

::: {.solution}

Write $f(t) = (u(t), v(t))$ for the continuous surjection $f: I \to I^2$ of Theorem 44.1, and $v^k$ for the $k$-fold composite of $v$ with itself, $v^0$ being the identity.

::: pf

::: pf-step
For $n \ge 2$ the map $g_n : I \to I^n$ defined by
$$
g_n(t) = \big(u(t),\, u(v(t)),\, \dots,\, u(v^{n-2}(t)),\, v^{n-1}(t)\big)
$$
is continuous.

::: pf-proof
Each coordinate is a composite of the continuous functions $u$ and $v$, hence continuous, and a map into a finite product is continuous when its coordinates are.
:::

:::

::: pf-step
$g_n$ is surjective.

::: pf-proof
Let $(a_1, \dots, a_n) \in I^n$. Since $f$ is surjective, choose $s_{n-1} \in I$ with $u(s_{n-1}) = a_{n-1}$ and $v(s_{n-1}) = a_n$. Having chosen $s_k$ for some $k \ge 2$, choose $s_{k-1} \in I$ with $u(s_{k-1}) = a_{k-1}$ and $v(s_{k-1}) = s_k$. This produces $s_1, \dots, s_{n-1}$ with $u(s_k) = a_k$ for $1 \le k \le n-1$ and $v(s_k) = s_{k+1}$ for $1 \le k \le n-2$. Now choose $t \in I$ with $u(t) = a_1$ and $v(t) = s_1$. Then $v^k(t) = s_k$ for $1 \le k \le n-1$, so $u(v^k(t)) = a_{k+1}$ for $0 \le k \le n-2$ and $v^{n-1}(t) = s_{n-1}$, whose coordinates are $a_{n-1}$ and $a_n$. Hence $g_n(t) = (a_1, \dots, a_n)$.
:::

:::

::: pf-step
For every $n$ there is a continuous surjective map $g: I \to I^n$. $\square$

::: pf-proof
For $n = 1$ the identity of $I$ serves; for $n \ge 2$ the map $g_n$ of step 1 is continuous and surjective by step 2.
:::

:::

:::

:::
