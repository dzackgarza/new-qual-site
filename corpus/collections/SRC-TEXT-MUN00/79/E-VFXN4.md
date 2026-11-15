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
    Corollary 60.4 (printed p. 373), Theorem 54.5 (printed p. 345), Theorem 54.6 (printed p. 346) and
    Lemma 58.1 (printed p. 360) named.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 2, printed p. 483. Part (a) from pi_1(P^2) = Z/2, which has no nontrivial map to Z, and the lifting criterion; part (b) the projection onto a factor of the torus. Checked against Corollary 60.4, Theorem 79.1 and Theorem 60.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

(a) Show that every continuous map $f: P^2 \to S^1$ is nulhomotopic.

(b) Find a continuous map of the torus into $S^1$ that is not nulhomotopic.
:::

::: {.solution}

(a) The proof is that of two answers to Math StackExchange question 142987, "Prove every map from the projective plane to the circle is nullhomotopic" (https://math.stackexchange.com/questions/142987, asked by Proton 2012-05-09): answer 143112 by Fredrik Meyer (https://math.stackexchange.com/a/143112), that every homomorphism $\ZZ/2\to\ZZ$ is zero, and answer 143123 by SL2 (https://math.stackexchange.com/a/143123), that a map whose induced homomorphism is zero lifts to the universal cover of $S^1$ and so is nullhomotopic. Both were posted 2012-05-09.

Let $f:P^2\to S^1$. By Corollary 60.4 (printed p. 373) the group $\pi_1(P^2)$ has order $2$, and by Theorem 54.5 (printed p. 345) $\pi_1(S^1)\cong\ZZ$. A homomorphism $h:\ZZ/2\to\ZZ$ satisfies $2h(1)=h(0)=0$, and $\ZZ$ has no element of order $2$, so $h=0$; hence
$$
f_*\pi_1(P^2,x_0)=0 .
$$
Let $p:\RR\to S^1$ be the universal covering. The space $P^2$ is path connected and locally path connected, so the lifting criterion of Theorem 54.6 (printed p. 346) gives $\tilde f:P^2\to\RR$ with $p\circ\tilde f=f$. Since $\RR$ is contractible, $\tilde f$ is homotopic to a constant map, and composing with $p$ gives a nullhomotopy of $f$.

A third answer, 1841392 by user84976 (https://math.stackexchange.com/a/1841392, 2016-06-27) to question 1831470, reaches the same lift without computing $\pi_1(P^2)$: it lifts $f\circ q$ along the quotient $q:S^2\to P^2$, whose domain is simply connected, and shows that the two values of the lift at antipodal points agree, because $x\mapsto\tilde g(x)-\tilde g(-x)$ is continuous, integer valued on the connected space $S^2$, and odd. That route is longer and is not used here; the answer 1840953 in the same thread is the argument above.

(b) The first projection
$$
f:T^2=S^1\times S^1\longrightarrow S^1,\qquad f(x,y)=x,
$$
is not nullhomotopic. Under the isomorphism $\pi_1(T^2)\cong\ZZ\oplus\ZZ$ of Corollary 60.2 (printed p. 372), the induced homomorphism $f_*$ carries $(r,s)$ to $r$; it is onto, and a nullhomotopic map induces the zero homomorphism on fundamental groups (Lemma 58.1, printed p. 348, with the constant map). So $f$ is not nullhomotopic. This part is the card's own: no answer in either saved thread treats part (b).
:::
