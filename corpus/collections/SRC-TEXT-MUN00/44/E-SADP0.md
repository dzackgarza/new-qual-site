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
    same device gives I^4. GEdgar then goes on to the infinite product, writing
    f_infinity(t) = (u(t), u(v(t)), u(v(v(t))), ...) on I^omega, and does not state a general
    finite case; the card states the general map g_n and proves its surjectivity by choosing
    s_{n-2}, ..., s_0 backwards, which GEdgar leaves to the reader. The earlier note above
    recording that no published solution was located is superseded.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The display of g_n ended with u(v^(n-2)) and v(v^(n-2)) after an ellipsis that began at the
    second coordinate, so that at n = 3 it read as five coordinates with the first two repeated,
    and the sentence after it described the first n-2 coordinates as the u-terms. The map is now
    given by its coordinates: the k-th is u composed with v to the k-1 for k at most n-1, and the
    last is v composed with v to the n-2, which is GEdgar's f_3 = (u, u o v, v o v) at n = 3 and
    f at n = 2; the surjectivity step is worded in the same coordinates.
---

::: {.exercise}

Given $n$, show there is a continuous surjective map $g: I \to I^n$.
[Hint: Consider

$$
f \times f: I \times I \to I^2 \times I^2.]
$$
:::

::: {.solution}

Write $f(t) = (u(t), v(t))$ for the continuous surjection $f: I \to I^2$ of Theorem 44.1, and $v^k$ for the $k$-fold composite of $v$ with itself, $v^0$ being the identity. For $n \ge 2$ let $g_n : I \to I^n$ be the map
$$
g_n(t) = \big(u(t),\, u(v(t)),\, \dots,\, u(v^{n-2}(t)),\, v(v^{n-2}(t))\big),
$$
whose $k$-th coordinate is $u(v^{k-1}(t))$ for $1 \le k \le n-1$ and whose last coordinate is $v(v^{n-2}(t))$: the ellipsis in the display stands for the coordinates between the second and the $(n-1)$-st, so that $g_2 = f$ and $g_3(t) = (u(t), u(v(t)), v(v(t)))$.

::: pf

::: pf-step
For $n \ge 2$ the map $g_n : I \to I^n$ is continuous.

::: pf-proof
Each coordinate is a composite of the continuous functions $u$ and $v$, hence continuous, and a map into a finite product is continuous when its coordinates are.
:::

:::

::: pf-step
$g_n$ is surjective.

::: pf-proof
Let $(a_1, \dots, a_n) \in I^n$. Since $f$ is surjective, choose $s_{n-2} \in I$ with $u(s_{n-2}) = a_{n-1}$ and $v(s_{n-2}) = a_n$. Having chosen $s_k$ for some $k$ with $1 \le k \le n-2$, choose $s_{k-1} \in I$ with $u(s_{k-1}) = a_k$ and $v(s_{k-1}) = s_k$. This produces $s_0, \dots, s_{n-2}$ with $u(s_k) = a_{k+1}$ for $0 \le k \le n-2$ and $v(s_k) = s_{k+1}$ for $0 \le k \le n-3$. Put $t = s_0$; then $v^k(t) = s_k$ for $0 \le k \le n-2$, so the $k$-th coordinate of $g_n(t)$ is $u(v^{k-1}(t)) = u(s_{k-1}) = a_k$ for $1 \le k \le n-1$, and its last coordinate is $v(v^{n-2}(t)) = v(s_{n-2}) = a_n$. Hence $g_n(t) = (a_1, \dots, a_n)$.
:::

:::

::: pf-step
For every $n$ there is a continuous surjective map $g: I \to I^n$. $\square$

::: pf-proof
For $n = 1$ the identity of $I$ serves, for $n = 2$ the map $f$ of Theorem 44.1 does, and for $n \ge 3$ the map $g_n$ of step 1 is continuous and surjective by step 2.
:::

:::

:::

:::
