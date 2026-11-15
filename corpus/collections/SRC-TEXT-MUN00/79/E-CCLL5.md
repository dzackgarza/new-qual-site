---
schema: qual/card@1
id: E-CCLL5
kind: problem
title: Normal subgroups and regular coverings
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 3, printed p. 483. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved threads are tmp/sources/mse-4717444-E-CCLL5.md and
    tmp/sources/mse-2920443-E-CCLL5.md, both read whole. Math StackExchange 4717444 is this exercise, asked
    by AlaskaYoung on 2023-06-12; its accepted answer 4717475 by Paul Frost proves one direction, from an
    equivalence carrying any point of the fibre to any other to the normality of H_0, by lifting the
    conjugate loop and pushing the loop at e_1 down with the equivalence. That direction is now recorded on
    the card with its URL, and the card's proof of it is the same argument. Answer 4717455 in the same thread
    only restates the notion of a regular cover. The other thread, 2920443, has answer 2920911 by Andres
    Mejia, which proves the equality p_*pi_1(X,x_0) = p_*pi_1(X,x_1) for a deck transformation carrying x_0 to
    x_1 and the basepoint-change formula, the two steps the card uses; it is recorded with it. Neither writes
    the other direction -- normality to transitivity on the fibre -- which is the first paragraph of the card
    and stays the card's own. Rejected in the search: mse 2739279, the exercise verbatim with no answer.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 3, printed p. 483. The normality of H_0 read off the basepoint-change formula p_* pi_1(E,e) = g^{-1} H_0 g and the classification of connected coverings by subgroups. Checked against Theorem 79.4 and the change-of-basepoint theorem of Section 52. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Let $p: E \to B$ be a covering map; let $p(e_0) = b_0$.
Show that $H_0 = p_*(\pi_1(E, e_0))$ is a normal subgroup of $\pi_1(B, b_0)$ if and only if for every pair of points $e_1, e_2$ of $p^{-1}(b_0)$, there is an equivalence $h: E \to E$ with $h(e_1) = e_2$.
:::

::: {.solution}
Assume $E$ is connected and locally path connected, as in the covering-space classification theorem. Fix $e_0\in p^{-1}(b_0)$ and put
$$
H_0=p_*\pi_1(E,e_0)\le G:=\pi_1(B,b_0).
$$
For any $e\in p^{-1}(b_0)$, choose a path $\lambda$ in $E$ from $e_0$ to $e$, and let
$$
g=[p\lambda]\in G.
$$
Changing basepoint along $\lambda$ gives
$$
p_*\pi_1(E,e)=g^{-1}H_0g
$$
(up to the consistent convention for concatenation; only conjugacy matters below).

Suppose first that $H_0\triangleleft G$. Then for every $e\in p^{-1}(b_0)$,
$$
p_*\pi_1(E,e)=H_0.
$$
Given $e_1,e_2\in p^{-1}(b_0)$, the two pointed coverings $(E,e_1)\to(B,b_0)$ and $(E,e_2)\to(B,b_0)$ therefore have the same associated subgroup. By the equivalence theorem for pointed connected coverings, there is a covering equivalence
$$
h:E\to E,\qquad p\circ h=p,\qquad h(e_1)=e_2.
$$

Conversely, suppose that for every pair $e_1,e_2$ in the fiber there is such an equivalence. For any $g\in G$, lift a representative loop at $b_0$ beginning at $e_0$, and let its endpoint be $e_g$. The basepoint-change formula gives
$$
p_*\pi_1(E,e_g)=g^{-1}H_0g.
$$
By hypothesis there is an equivalence $h:E\to E$ with $h(e_0)=e_g$. Since $p h=p$,
$$
p_*\pi_1(E,e_g)
=p_*h_*\pi_1(E,e_0)
=p_*\pi_1(E,e_0)=H_0.
$$
Thus $g^{-1}H_0g=H_0$ for every $g\in G$. Hence $H_0$ is normal.

That second direction is Paul Frost's, answer 4717475 (https://math.stackexchange.com/a/4717475), posted 2023-06-12 to Math Stack Exchange question 4717444, which is this exercise (https://math.stackexchange.com/questions/4717444, asked by AlaskaYoung on the same day): lift the loop $g^{-1}(p\circ f)g$ from $e_0$, obtaining the point $e_1$, apply the equivalence $h$ carrying $e_1$ to $e_0$, and compute $p_*([h\circ F])=[g]^{-1}[p\circ f][g]$. The same step is Andrés Mejia's answer 2920911 (https://math.stackexchange.com/a/2920911, 2018-09-18) to question 2920443, which also records the basepoint change $p_*\pi_1(E,e_1)=\alpha^{-1}p_*\pi_1(E,e_0)\alpha$ used above. Neither answer writes the first direction, from normality to an equivalence carrying $e_1$ to $e_2$; that needs the classification of connected coverings by their subgroups, and it is the first paragraph of this solution, which is the card's own.
:::
