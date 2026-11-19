---
schema: qual/card@1
id: E-YZ8XN
kind: problem
title: Simple connectedness implies semilocal simple connectedness
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
    Munkres §82 Exercise 1, printed p. 499. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-2364579-E-YZ8XN.md, read whole.
    Math StackExchange 2364579 has one answer, 2365131 by Birch Bryant (2017-07-20), whose last paragraph
    gives the argument for the cone CX on the earring: it is simply connected, so for every neighbourhood U
    the homomorphism i: pi_1(U) -> pi_1(CX) = 0 is trivial, and CX is therefore semilocally simply connected.
    That is this exercise's statement in one instance; the answer does not state it for a general simply
    connected space. It is recorded on the card as that instance, and the card keeps its own proof of the
    general statement. Rejected in the search: nothing else was returned for this exercise.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Exercise 1, printed p. 499. A simply connected space is semilocally simply connected, by taking the neighbourhood itself. Checked against the definition of semilocally simply connected, printed p. 489. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the definition of semilocal simple connectedness is printed on p. 494, not p. 489 as the previous note said; p. 489 carries Corollaries 81.3 and 81.4. The proof now cites the Definition of simple connectedness (printed p. 333) and the Definition of semilocal simple connectedness (printed p. 494), and states the two points the argument needs: that $X$ is a neighbourhood of each of its points, because it is open in itself, and that the induced homomorphism of the inclusion $X\to X$ is the identity of the trivial group, not only a map into a trivial group. What the certificate does not cover: nothing; the exercise has no parts.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct:
    taking U = X at each point makes the induced map the identity of the trivial group pi_1(X,
    x). Added the note that the choice serves under either convention for 'neighbourhood', open
    or not, which the card's sentence covered only for the non-open one. The Math Stack Exchange
    answer cited by the card treats one instance (the cone on the Hawaiian earring) and does not
    state the general case; the card's general argument is its own, as the card says.
---

::: {.exercise}

Show that a simply connected space is semilocally simply connected.

:::

::: {.solution}
$X$ is *simply connected* when it is path connected and $\pi_1(X,x)$ is the trivial group for some, hence every, base point; it is *semilocally simply connected* when for each $b \in X$ there is a neighbourhood $U$ of $b$ such that the homomorphism $i_{*}\colon\pi_1(U,b)\to\pi_1(X,b)$ induced by the inclusion is trivial (Munkres, *Topology* (2000), definitions on printed pp. 333 and 494).

::: pf

::: {.pf-step #neighbourhood}
For $x \in X$ the set $U \coloneqq X$ is a neighbourhood of $x$, and its inclusion into $X$ is the identity map.

::: pf-proof
A neighbourhood of $x$ is a set containing an open set containing $x$, and $X$ itself is open in $X$; the inclusion of $X$ into $X$ is the identity. If the definition in use demands the neighbourhood be open, $X$ is open as well, so the same choice serves.

:::

:::

::: {.pf-step #trivial}
The induced homomorphism $i_{*}\colon\pi_1(U,x)\to\pi_1(X,x)$ is trivial.

::: pf-proof
By step [](#neighbourhood){.pf-ref} the inclusion is the identity of $X$, so $i_{*}$ is the identity homomorphism of $\pi_1(X,x)$. That group is trivial because $X$ is simply connected, so $i_{*}$ is the zero homomorphism, which is what triviality of $i_{*}$ asserts.

:::

:::

::: pf-step
$X$ is semilocally simply connected.

::: pf-proof
The condition of semilocal simple connectedness is that each point $b$ admit a neighbourhood with the property of step [](#trivial){.pf-ref}; taking $U = X$ gives it at every point, so the condition holds at every point of $X$.

:::

:::

:::
:::
