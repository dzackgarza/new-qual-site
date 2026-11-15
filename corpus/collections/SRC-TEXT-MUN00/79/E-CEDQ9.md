---
schema: qual/card@1
id: E-CEDQ9
kind: problem
title: Maps of higher spheres into the circle are nullhomotopic
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
    Corrected the lifting citation. The solution cited Theorem 54.6 for the lifting criterion; Theorem 54.6
    (printed p. 346) is the strengthened lifting correspondence, not the existence theorem for lifts of
    maps, and the printed hint's "lifting lemma" is Lemma 79.1, the general lifting lemma (printed p. 478),
    which is what the argument uses. Lemma 79.1 also assumes that the base points correspond, f(y_0) = p(e_0),
    and the card had written p_* pi_1(R, 0) with no reason for 0 to lie over f(x_0); it now chooses x_0 in S^n,
    puts b_0 = f(x_0) and takes e_0 in p^{-1}(b_0). Checked on the page images: the statements of Lemma 79.1
    (printed p. 478) and of Theorem 54.6 (printed p. 346), and that S^n is simply connected for n > 1 and R is
    contractible, which are the two facts the argument needs. Not covered: nothing of the exercise's statement
    changes, and the proof of Lemma 79.1 is the book's and is cited rather than reproduced.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 1, printed p. 483. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved threads are tmp/sources/mse-2813729-E-CEDQ9.md and
    tmp/sources/mse-783766-E-CEDQ9.md, both read whole. Math StackExchange 2813729, "Show that a continuous
    map f: S^n -> S^1 is nullhomotopic" (asked 2018-06-09), has one answer, 2813771 by the account posting as
    user113529 (2018-06-09), which proves the exercise for every n > 1: f_*(pi_1(S^n)) = 0 inside
    p_*(pi_1(R)) = 0, so f lifts to the universal cover R by the lifting criterion, and R is contractible.
    That proof is transcribed in the solution block with its URL and replaces the card's own proof of the same
    argument, which is now written with the book's Theorem 53.1 (printed p. 337) and Lemma 79.1, the general
    lifting lemma (printed p. 478), named, together with the choice of e_0 over f(x_0) that Lemma 79.1
    requires. The second saved thread, 783766, proves the case n = 2 only, as answer 783783 by Giorgio
    Mossa, and adds nothing to it.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 1, printed p. 483. The lifting criterion for S^n simply connected, then the contraction of R. Checked against Theorem 79.1 (the lifting criterion) and Theorem 59.3. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Show that if $n > 1$, every continuous map $f: S^n \to S^1$ is nullhomotopic.
[Hint: Use the lifting lemma.]
:::

::: {.solution}

The proof below is that of Math StackExchange answer 2813771 (https://math.stackexchange.com/a/2813771), posted 2018-06-09 by the account posting as user113529 to question 2813729, "Show that a continuous map $f: S^n \to S^1$ is nullhomotopic" (https://math.stackexchange.com/questions/2813729), asked by Greywhite on the same day, and it is the argument the printed hint asks for. The same argument for $n = 2$ alone is answer 783783 by Giorgio Mossa (https://math.stackexchange.com/a/783783), posted 2014-05-06 to question 783766, with nothing added.

Let $n>1$ and let $f:S^n\to S^1$ be continuous. Choose $x_0\in S^n$ and let
$$
p:\RR\longrightarrow S^1,\qquad p(t)=e^{2\pi i t},
$$
be the universal covering map of Theorem 53.1 (printed p. 337). Put $b_0=f(x_0)$ and choose $e_0\in p^{-1}(b_0)$, which exists because $p$ is onto; then $p(e_0)=b_0=f(x_0)$, which is the hypothesis Lemma 79.1 puts on the base points. The sphere $S^n$ is path connected and locally path connected, and simply connected for $n>1$, so
$$
f_*\pi_1(S^n,x_0)=0\subseteq p_*\pi_1(\RR,e_0)=0,
$$
and Lemma 79.1, the general lifting lemma (printed p. 478), applied with $Y=S^n$ and $y_0=x_0$, gives a lift $\tilde f:S^n\to\RR$ with $p\circ\tilde f=f$ and $\tilde f(x_0)=e_0$.

The real line is contractible, so $\tilde f$ is homotopic to a constant map $c:S^n\to\RR$; composing that homotopy with $p$ gives a homotopy from $f=p\circ\tilde f$ to the constant map $p\circ c$. Hence $f$ is nullhomotopic.
:::
