---
schema: qual/card@1
id: E-0EZ4U
kind: problem
title: Seifert-van Kampen with trivial intersection homomorphism
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Seifert-van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §70 Exercise 1, printed p. 433. A published solution is "Solutions to exercises for Mathematics
    205A", University of California, Riverside, Part 9 (Fall 2014), §70 Exercise 1, the set's printed p. 6,
    which proves that the square with the two quotients is a pushout. The card proves the same thing in the
    form the exercise's own hint asks for, Theorem 70.1 used to build a left inverse of h, having checked that
    the pushout form and the left-inverse form are the same statement; the sheet's content is the existential
    half of step 3 below. Checked against Theorem 70.1 (printed p. 426), the extension condition for free products (Lemma 68.3, printed p. 418) and §59 for the generation of pi_1(X) by the two images. Nothing on the sheet
    needed correction; its one gap is that it does not say why the free-product generators lie in the image of
    h, which step 2 records.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §70 Exercise 1, printed p. 433. Searched outside the checkout for issue #144; the questions the
    throttled address could not open were read from the orchestrator's machine, recorded in
    tmp/sources/mse-searches-144.md, thread tmp/sources/mse-2546862-E-0EZ4U.md. Math StackExchange 2546862, "Munkres
    Exercise 70.1" (asked 2017-12-02), answer 4686314 by user497021 (2023-04-25), read whole, proves both parts:
    pi_1(U cup V) is the pushout of pi_1(V) <- pi_1(U cap V) -> pi_1(U), which is Theorem 70.1 in its pushout form,
    and the pushout of the two composites through the quotients is the free product, both composites being trivial.
    Its five diagrams are lost (the answer links images it could not embed), two displayed arrows read q_2 i_2 where
    q_1 i_1 is meant, and the closing step, that a pushout over trivial maps is the free product, is stated without
    proof. What it proves is the statement of the published solution the card already cites, the Riverside Part 9
    sheet's §70 Exercise 1 at its printed p. 6, so nothing is transcribed from it and the card keeps the proof in
    the exercise's own hint form. dbFin has no §70 page, Murayama's selection none, the fourteen repositories stop
    at Chapter 3. The card was re-read against Theorem 70.1 (printed p. 426) and the extension condition for free
    products (Lemma 68.3, printed p. 418).
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Two defects reported by a reader of this card, checked against §70 (exercises printed p. 433) before
    changing anything. (a) The exercise stands under the section's printed sentence "In the following
    exercises, assume the hypotheses of the Seifert-van Kampen theorem", which the card's statement omitted;
    the statement now opens with it. (b) Step 3 read "q_1 i_1(gamma) lies in N_1", which compares an element of
    the quotient pi_1(U)/N_1 with a subgroup of pi_1(U); what the argument needs is that i_1(gamma) lies in N_1
    for every gamma, by definition of N_1, so that q_1 i_1(gamma) is the identity of the quotient, and the step
    now says that (and the same for q_2 i_2). The rest of the proof was re-read and kept.
---

::: {.exercise}

Assume the hypotheses of the Seifert–van Kampen theorem (Theorem 70.1, printed p. 426).

Suppose that the homomorphism $i_*$ induced by inclusion $i: U \cap V \to X$ is trivial.

(a) Show that $j_1$ and $j_2$ induce an epimorphism

$$
h: (\pi_1(U, x_0)/N_1) * (\pi_1(V, x_0)/N_2) \to \pi_1(X, x_0),
$$

where $N_1$ is the least normal subgroup of $\pi_1(U, x_0)$ containing image $i_1$, and $N_2$ is the least normal subgroup of $\pi_1(V, x_0)$ containing image $i_2$.

(b) Show that $h$ is an isomorphism.
[Hint: Use Theorem 70.1 to define a left inverse for $h$.]
:::

::: {.solution}

Keep the notation of Theorem 70.1 (printed p. 426): $i_1:\pi_1(U\cap V)\to\pi_1(U)$, $i_2:\pi_1(U\cap V)\to\pi_1(V)$, $j_1:\pi_1(U)\to\pi_1(X)$, $j_2:\pi_1(V)\to\pi_1(X)$, the maps induced by inclusion. Put $q_1:\pi_1(U)\to\pi_1(U)/N_1$ and $q_2:\pi_1(V)\to\pi_1(V)/N_2$ for the quotient maps and $J_1,J_2$ for the injections of the two quotients into their free product.

::: pf

::: pf-step

The homomorphisms $j_i$ carry $N_i$ to the identity, so they induce $h$.

::: pf-proof

$j_1\circ i_1=j_2\circ i_2=i$ is trivial by hypothesis, so $i_1(\pi_1(U\cap V))\subseteq\ker j_1$; since $N_1$ is the least normal subgroup containing that image and $\ker j_1$ is normal, $N_1\subseteq\ker j_1$. Likewise $N_2\subseteq\ker j_2$. Hence $j_i$ factors through $q_i$, and the two resulting maps of the quotients extend, by the extension condition for free products (Lemma 68.3, printed p. 418), to a homomorphism $h$ of the free product.

:::

:::

::: pf-step

$h$ is onto.

::: pf-proof

By §59 the images of $j_1$ and $j_2$ generate $\pi_1(X,x_0)$; each is in the image of $h$, since $h(J_1(q_1(g)))=j_1(g)$ and $h(J_2(q_2(g)))=j_2(g)$. A group generated by a set contained in the image of $h$ is the image of $h$.

:::

:::

::: pf-step

$h$ has a left inverse $\Phi$.

::: pf-proof

Take $H=\pi_1(U)/N_1 * \pi_1(V)/N_2$ and $\phi_i=J_i\circ q_i$ in Theorem 70.1. Their composites with $i_1,i_2$ agree because $i$ is trivial and $q_1 i_1$, $q_2 i_2$ both land in the identity: $i_1(\gamma)$ lies in $N_1$ for every $\gamma$, by definition of $N_1$, so $q_1i_1(\gamma)$ is the identity of $\pi_1(U)/N_1$, and likewise $q_2i_2(\gamma)$ is the identity of $\pi_1(V)/N_2$. Theorem 70.1 then gives $\Phi:\pi_1(X,x_0)\to H$ with $\Phi\circ j_i=J_iq_i$.

:::

:::

::: pf-step

$\Phi\circ h=\mathrm{id}$.

::: pf-proof

For $g\in\pi_1(U)$, $\Phi h J_1q_1(g)=\Phi j_1(g)=J_1q_1(g)$; likewise for $g\in\pi_1(V)$. The elements $J_1q_1(g)$ and $J_2q_2(g)$ generate the free product, so $\Phi h$ agrees with the identity on a generating set, hence everywhere.

:::

:::

::: pf-qed

$h$ is onto by step 2 and has a left inverse by steps 3--4, so $h$ is an isomorphism.

:::

:::
:::
