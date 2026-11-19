---
schema: qual/card@1
id: E-2STPW
kind: problem
title: Nulhomotopic maps of the circle have fixed and antipodal points
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 55: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-55-retractions-and-fixed-points/problem-2-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-2-solution.txt), and against Munkres,
    Topology (2000), Section 55 Exercise 2, printed p. 353. dbFin uses Lemma 55.3 and Theorem 55.6: a nullhomotopic $h$ extends over $B^2$, the extension composed with the inclusion has a fixed point $x$ in $S^1$, which is a fixed point of $h$, and composing with the half-turn gives the antipodal point. The card instead argues with the winding number: if $h$ has no fixed point the straight-line homotopy makes $h$ homotopic to the antipodal map, and if it misses the antipodes it makes $h$ homotopic to the identity, either of which contradicts $\deg h=0$ for a nullhomotopic map, the degree being the class in $\pi_1(S^1)$ under Theorem 54.5. Both proofs are correct; the card's uses the degree, which is the class in $\pi_1(S^1)$ and so is available after Section 54.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution on 2026-11-19. Its first step had no proof block at all,
    its next two carried run-in titles and "Proof:" labels over unlabelled
    substeps, and the solution ended with a paragraph outside the proof citing
    "steps s2 and s3", two labels that did not exist — the gates could not see
    that reference, since the paragraph sat outside the pf block. The proof is
    now the published one, transcribed: a nullhomotopic map of S^1 extends over
    B^2 (Lemma 55.3), and Brouwer applied to the extension, then to the map
    followed by the half-turn, gives the fixed point and the antipodal point. The
    card had been proved by the winding number instead, and its event of
    2026-11-11 records that both routes are correct; the transcribed route is now
    the one on the card. Read for this repair in
    tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-2-solution.txt
    (read 2026-11-11) and checked against
    tmp/sources/munkres-2000-topology.md and the retained PDF: the exercise on
    printed p. 353 (PDF p. 368, printed page = PDF page - 15), Lemma 55.3 with its
    three equivalent conditions on printed p. 349 (PDF p. 364), and Theorem 55.6
    on printed p. 351 (PDF p. 366). No statement changes.

---

::: {.exercise}

Show that if $h: S^1 \to S^1$ is nulhomotopic, then $h$ has a fixed point and $h$ maps some point $x$ to its antipode $-x$.
:::

::: {.solution}
The argument is that of the published solution of dbFin, "Section 55: Problem 2 Solution": a nullhomotopic map of the circle extends over the disc, Brouwer's theorem applied to that extension gives the fixed point, and the same theorem applied to the map followed by the half-turn gives the point sent to its antipode. The exercise is Munkres, *Topology* (2000), Section 55, Exercise 2, printed p. 353; the extension lemma is Lemma 55.3, printed p. 349, and Brouwer's fixed-point theorem for the disc is Theorem 55.6, printed p. 351.

Let $j\colon S^1\to B^2$ be the inclusion, and $\tau\colon S^1\to S^1$ the half-turn $\tau(x)=-x$.

::: pf

::: {.pf-step #extension}
A nullhomotopic map $u\colon S^1\to S^1$ extends to a continuous map $B^2\to S^1$, and $\tau\circ u$ is nullhomotopic.

::: pf-proof
The first clause is the equivalence of (1) and (2) in Lemma 55.3, printed p. 349: a continuous $u\colon S^1\to X$ is nullhomotopic exactly when it extends to a continuous $k\colon B^2\to X$. For the second, if $H\colon S^1\times I\to S^1$ is a homotopy from $u$ to a constant map, then $\tau\circ H$ is a homotopy from $\tau\circ u$ to a constant map.
:::

:::

::: {.pf-step #fixed}
Every nullhomotopic map $u\colon S^1\to S^1$ has a fixed point.

::: pf-proof
By step [](#extension){.pf-ref} let $k\colon B^2\to S^1$ extend $u$. The composite $j\circ k\colon B^2\to B^2$ is continuous, so by Theorem 55.6, printed p. 351, there is $x\in B^2$ with $(j\circ k)(x)=x$. Then $x=j(k(x))$ lies in $j(S^1)=S^1$, and on $S^1$ the map $k$ agrees with $u$, so $x=u(x)$.
:::

:::

::: {.pf-step #antipode}
Some $x\in S^1$ satisfies $h(x)=-x$.

::: pf-proof
By step [](#extension){.pf-ref} the composite $\tau\circ h$ is nullhomotopic, so by step [](#fixed){.pf-ref} there is $x\in S^1$ with $(\tau\circ h)(x)=x$, that is $-h(x)=x$.
:::

:::

:::

:::
