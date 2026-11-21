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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, one per move of the argument, each carrying a `pf-proof`; the claims are
    the prose's own and the closing provenance paragraph is kept verbatim outside the proof.
    Cited by number only: Munkres Theorem 79.4 for the classification of pointed connected
    coverings by their subgroups, and the path-lifting property of a covering. Checked: that
    the basepoint-change formula conjugates by $[p\lambda]$ with the same convention on both
    sides, that $h_*\pi_1(E,e_0)=\pi_1(E,e_g)$ for a homeomorphism carrying $e_0$ to $e_g$, and
    that $p\circ h=p$ gives $p_*h_*=p_*$.
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

::: pf

::: pf-step

For any $e\in p^{-1}(b_0)$, choosing a path $\lambda$ in $E$ from $e_0$ to $e$ and putting $g=[p\lambda]\in G$, the basepoint-change formula gives
$$
p_*\pi_1(E,e)=g^{-1}H_0g
$$
(up to the convention for concatenation; only conjugacy is used below).

::: pf-proof

$E$ is path connected, being connected and locally path connected, so a path $\lambda$ from $e_0$ to $e$ exists. Changing the basepoint of $\pi_1(E,\cdot)$ along $\lambda$ conjugates $\pi_1(E,e_0)$ to $\pi_1(E,e)$ in $\pi_1(E,e_0)$'s own terms, and $p_*$ carries that conjugation to conjugation by $p_*[\lambda]=[p\lambda]=g$: for a loop $\mu$ at $e_0$, the loop $\bar\lambda\mu\lambda$ at $e$ maps to $\overline{p\lambda}\,(p\mu)\,(p\lambda)$, whose class is $g^{-1}[p\mu]g$. Hence $p_*\pi_1(E,e)=g^{-1}H_0g$. The reversed convention would replace $g$ by $g^{-1}$, which changes nothing about conjugacy.

:::

:::

::: pf-step

If $H_0\triangleleft G$, then $p_*\pi_1(E,e)=H_0$ for every $e\in p^{-1}(b_0)$.

::: pf-proof

By step 1, $p_*\pi_1(E,e)=g^{-1}H_0g$ for some $g\in G$; normality gives $g^{-1}H_0g=H_0$.

:::

:::

::: pf-step

In that case, for $e_1,e_2\in p^{-1}(b_0)$ the pointed coverings $(E,e_1)\to(B,b_0)$ and $(E,e_2)\to(B,b_0)$ have the same associated subgroup, so there is a covering equivalence
$$
h:E\to E,\qquad p\circ h=p,\qquad h(e_1)=e_2.
$$

::: pf-proof

A pointed covering of the connected, locally path connected base $(B,b_0)$ corresponds to the subgroup $p_*\pi_1(E,e)$ of $G$, and two pointed connected coverings are equivalent over $(B,b_0)$ exactly when the subgroups agree (the classification theorem for covering spaces, Munkres Theorem 79.4). By step 2 both subgroups equal $H_0$, so the equivalence exists and carries $e_1$ to $e_2$; being an equivalence of coverings it satisfies $p\circ h=p$, and being a homeomorphism it is the required $h$.

:::

:::

::: pf-step

Conversely, suppose that for every pair $e_1,e_2$ in the fibre there is such an equivalence. For $g\in G$, lift a representative loop at $b_0$ beginning at $e_0$, and let its endpoint be $e_g$; then
$$
p_*\pi_1(E,e_g)=g^{-1}H_0g.
$$

::: pf-proof

The path-lifting property lifts the loop representing $g$ to a path in $E$ starting at $e_0$; its endpoint $e_g$ lies over $b_0$, and $g=[p\lambda]$ for that lifted path $\lambda$, so step 1 applies with $e=e_g$.

:::

:::

::: pf-step

By hypothesis there is an equivalence $h:E\to E$ with $h(e_0)=e_g$, and since $p\circ h=p$,
$$
p_*\pi_1(E,e_g)=p_*h_*\pi_1(E,e_0)=p_*\pi_1(E,e_0)=H_0.
$$

::: pf-proof

$e_0$ and $e_g$ are both in $p^{-1}(b_0)$, so the hypothesis provides $h$ with $h(e_0)=e_g$. Then $h_*\pi_1(E,e_0)=\pi_1(E,e_g)$ because $h$ is a homeomorphism, and $p\circ h=p$ gives $p_*h_*=p_*$ on homotopy groups.

:::

:::

::: pf-step

Thus $g^{-1}H_0g=H_0$ for every $g\in G$, so $H_0$ is normal in $G$.

::: pf-proof

Steps 4 and 5 compute $g^{-1}H_0g=p_*\pi_1(E,e_g)=H_0$. The element $g\in G$ was arbitrary, which is the definition of normality.

:::

:::

::: pf-step

The two implications give the equivalence: $H_0=p_*\pi_1(E,e_0)$ is normal in $\pi_1(B,b_0)$ if and only if for every pair $e_1,e_2\in p^{-1}(b_0)$ there is an equivalence $h:E\to E$ with $h(e_1)=e_2$.

::: pf-proof

Steps 2 and 3 prove the implication from normality to transitivity on the fibre, and steps 4--6 the converse. Together they are the assertion of the exercise.

:::

:::

:::

That second direction is Paul Frost's, answer 4717475 (https://math.stackexchange.com/a/4717475), posted 2023-06-12 to Math Stack Exchange question 4717444, which is this exercise (https://math.stackexchange.com/questions/4717444, asked by AlaskaYoung on the same day): lift the loop $g^{-1}(p\circ f)g$ from $e_0$, obtaining the point $e_1$, apply the equivalence $h$ carrying $e_1$ to $e_0$, and compute $p_*([h\circ F])=[g]^{-1}[p\circ f][g]$. The same step is Andrés Mejia's answer 2920911 (https://math.stackexchange.com/a/2920911, 2018-09-18) to question 2920443, which also records the basepoint change $p_*\pi_1(E,e_1)=\alpha^{-1}p_*\pi_1(E,e_0)\alpha$ used above. Neither answer writes the first direction, from normality to an equivalence carrying $e_1$ to $e_2$; that needs the classification of connected coverings by their subgroups, and it is the first paragraph of this solution, which is the card's own.
:::
