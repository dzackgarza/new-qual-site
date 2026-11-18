---
schema: qual/card@1
id: E-VFXN4
kind: problem
title: Maps of the projective plane and the torus into the circle
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Corrected two citations. Part (a) cited Theorem 54.6 (printed p. 346) for the lifting criterion; that
    theorem is the lifting correspondence, and the passage needed is Lemma 79.1, the general lifting lemma
    (printed p. 478), whose base-point hypothesis f(y_0) = p(e_0) the card had not met: it now chooses
    x_0 in P^2, puts b_0 = f(x_0) and takes e_0 in p^{-1}(b_0) before using p_* pi_1(R, e_0). Part (b) cited
    Lemma 58.1 (printed p. 360) for the triviality of the induced homomorphism of a nullhomotopic map; Lemma
    58.1 needs a homotopy that fixes the base point throughout, and the homotopy from f to a constant map
    moves it, so the correct citation is Corollary 58.6 (printed p. 364), of which that triviality is the
    whole statement. Checked on the page images: Lemma 79.1 (printed p. 478), Lemma 58.1 (printed p. 360) and
    Corollary 58.6 (printed p. 364); and that both parts of the exercise, including part (b)'s projection onto
    a factor, are unchanged. Not covered: the triviality of pi_1(R) and the contractibility of R are cited,
    not reproved.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 2, printed p. 483. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved threads are tmp/sources/mse-142987-E-VFXN4.md and
    tmp/sources/mse-1831470-E-VFXN4.md, both read whole. Part (a) is proved in both: Math StackExchange
    142987 has 143112 by Fredrik Meyer and 143123 by SL2 (both 2012-05-09), and 1831470 has 1840953 by Max
    and 1841392 by user84976 (both 2016-06-27), the first of the four giving the same route, the second a
    route through S^2 that avoids pi_1(P^2). Part (a) is now transcribed from 143112 and 143123 with their
    URLs, and the S^2 route is recorded with the reason it is not used. Part (b) is answered nowhere in
    either thread and stays the card's own: the projection of the torus onto a factor is not nullhomotopic
    because it induces a surjection on pi_1. The card's former proof was a pf chain whose pf-proofs were
    one-line citations ("the only homomorphism Z/2 -> Z is the zero map"); it is now written out, with
    Corollary 60.4 (printed p. 373), Theorem 54.5 (printed p. 345), Lemma 79.1 (printed p. 478) with the
    point e_0 chosen over f(x_0) and Corollary 58.6 (printed p. 364) named; before the correction recorded in
    the first event of this list the two last were cited as Theorem 54.6 and Lemma 58.1.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 2, printed p. 483. Part (a) from pi_1(P^2) = Z/2, which has no nontrivial map to Z, and the lifting criterion; part (b) the projection onto a factor of the torus. Checked against Corollary 60.4, Theorem 79.1 and Theorem 60.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) that pi_1(P^2) has order 2 and every
    homomorphism to Z is zero, that the lifting criterion then gives a lift to the universal
    cover of S^1, and that contractibility of R gives the nullhomotopy; (b) that the first
    projection induces (r,s) -> r, which is nonzero, against Corollary 58.6. Part (a) is
    Meyer's and SL2's answers to MSE 142987; part (b) is the card's own. No repair needed.
---

::: {.exercise}

(a) Show that every continuous map $f: P^2 \to S^1$ is nulhomotopic.

(b) Find a continuous map of the torus into $S^1$ that is not nulhomotopic.
:::

::: {.solution}
Part (a) is the argument of two answers to Math Stack Exchange question 142987, "Prove every map from the projective plane to the circle is nullhomotopic" (asked 2012-05-09): answer 143112 by Fredrik Meyer (every homomorphism $\ZZ/2\to\ZZ$ is zero) and answer 143123 by SL2 (a map whose induced homomorphism is zero lifts to the universal cover of $S^{1}$ and so is nullhomotopic), both posted 2012-05-09. Part (b) is the card's own; no answer in the saved threads treats it.

::: pf

::: {.pf-step #induced-zero}
(a) For every continuous $f:P^{2}\to S^{1}$ the induced homomorphism $f_{*}:\pi_{1}(P^{2},x_{0})\to\pi_{1}(S^{1},f(x_{0}))$ is zero.

::: pf-proof
$\pi_{1}(P^{2},x_{0})$ has order $2$ (Corollary 60.4, printed p. 373) and $\pi_{1}(S^{1})\cong\ZZ$ (Theorem 54.5, printed p. 345). In the identification $\pi_{1}(P^{2},x_{0})=\ZZ/2$, a homomorphism $h$ into $\ZZ$ satisfies $2h(1)=h(0)=0$, and $\ZZ$ has no element of order $2$, so $h(1)=0$ and $h$ is the zero homomorphism.
:::

:::

::: {.pf-step #lift}
(a) $f$ lifts to $\tilde f:P^{2}\to\RR$ along the universal covering $p:\RR\to S^{1}$, and is therefore nulhomotopic.

::: pf-proof
$P^{2}$ is path connected and locally path connected. Let $p:\RR\to S^{1}$ be the universal covering, put $b_{0}=f(x_{0})$ and choose $e_{0}\in p^{-1}(b_{0})$. Since $f_{*}\pi_{1}(P^{2},x_{0})=0\subset p_{*}\pi_{1}(\RR,e_{0})$, the general lifting lemma (Lemma 79.1, printed p. 478) applies with $Y=P^{2}$ and gives a continuous $\tilde f:P^{2}\to\RR$ with $p\circ\tilde f=f$. The space $\RR$ is contractible, so $\tilde f$ is homotopic to the constant map at $\tilde f(x_{0})$; composing that homotopy with $p$ gives a homotopy from $f$ to the constant map at $b_{0}$.
:::

:::

::: {.pf-step #torus}
(b) The first projection $f:T^{2}\to S^{1}$, $f(x,y)=x$, is not nulhomotopic.

::: pf-proof
Under the isomorphism $\pi_{1}(T^{2})\cong\ZZ\oplus\ZZ$ (Corollary 60.2, printed p. 372) the induced homomorphism $f_{*}$ carries the class of a loop with winding numbers $(r,s)$ to $r$; in particular $f_{*}$ is onto $\ZZ$ and not the zero homomorphism. A nulhomotopic map induces the trivial homomorphism on fundamental groups (Corollary 58.6, printed p. 364), so $f$ is not nulhomotopic.
:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Steps [](#induced-zero){.pf-ref} and [](#lift){.pf-ref} prove (a), and step [](#torus){.pf-ref} proves (b).
:::

:::

:::
:::
