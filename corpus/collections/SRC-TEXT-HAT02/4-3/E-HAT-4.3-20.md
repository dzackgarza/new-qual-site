---
schema: qual/card@1
id: E-HAT-4.3-20
kind: problem
title: "Postnikov towers for $\\Omega X$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof repaired: the card displayed the three-term sequence Omega X_{n+1} -> Omega X_n -> Omega X_{n-1} and called it principal with an Eilenberg--MacLane loop space as fibre. In the book's indexing that is misaligned: AT.txt:20426-20430 has the Postnikov fibration K(pi_{n+1}X, n+1) -> X_{n+1} -> X_n, whose loop is K(pi_{n+1}X, n) -> Omega X_{n+1} -> Omega X_n, whereas the fibre of Omega X_n -> Omega X_{n-1} is K(pi_n X, n-1). The display now names the correct spaces.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.3 Exercise 20, printed
    p. 420 (PDF p. 429), and against the Postnikov theory of pp. 410-412. Each step re-read:
    looping preserves Hurewicz fibrations; $\pi_i(\Omega X_n)=\pi_{i+1}(X_n)$ makes $\Omega X_n$ the
    $(n-1)$-st stage of $\Omega X$; $X_n\to X_{n-1}$ is principal as the pullback of the path-loop
    fibration over $K(\pi_n X,n+1)$ along the k-invariant; and looping that pullback gives the
    pullback of the path-loop fibration of $K(\pi_n X,n)$ along $\Omega k_n$. A slip of my own in
    the first draft is repaired here: the fibre of $\Omega X_n\to\Omega X_{n-1}$ is the loop of the
    fibre of $p_n$, that is $K(\pi_n X,n-1)$, not $\Omega K(\pi_n X,n+1)$; the step now says so and
    matches the conclusion. Not claimed: any statement about Moore-Postnikov towers or about
    non-connected $X$.
---

::: {.problem}
Show that by applying the loop space functor to a Postnikov tower for $X$ one obtains a Postnikov tower of principal fibrations for $\Omega X$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.3 Exercise 20. It is checked against Hatcher, Algebraic Topology, Section 4.3 Exercise 20, printed p. 420, and against the Postnikov tower theory of pp. 410--412 and Theorem 4.69 there.

::: pf

::: {.pf-step #tower}
Let $\cdots\to X_n\to X_{n-1}\to\cdots$ be a Postnikov tower for $X$: each $p_n:X_n\to X_{n-1}$ is a fibration, $X_n$ has $\pi_i(X_n)=\pi_i(X)$ for $i\le n$ and $\pi_i(X_n)=0$ for $i>n$, and $X\to X_n$ induces these isomorphisms and a surjection on $\pi_{n+1}$.

::: pf-proof
This is Hatcher's definition of a Postnikov tower; the last condition is what makes $X_n$ the $n$-th stage of $X$ rather than merely a space with the right truncated groups.
:::

:::

::: {.pf-step #loop}
Looping gives a tower $\cdots\to\Omega X_n\to\Omega X_{n-1}\to\cdots$ of fibrations.

::: pf-proof
The loop space functor carries a Hurewicz fibration $p:E\to B$ to a Hurewicz fibration $\Omega p:\Omega E\to\Omega B$: a homotopy $F:Z\times I\to\Omega B$ lifting a map $Z\to\Omega E$ is a map $Z\times I\times I\to B$ whose restriction to $Z\times\{0\}\times I$ lifts, and the homotopy lifting property of $p$ applied to $Z\times I\times I$ lifts it. Hence each $\Omega p_n$ is a fibration.
:::

:::

::: {.pf-step #stages}
$\Omega X_n$ is the $(n-1)$-st Postnikov stage of $\Omega X$.

::: pf-proof
$\pi_i(\Omega X_n)=\pi_{i+1}(X_n)$. For $i+1\le n$, that is $\pi_{i+1}(X)=\pi_i(\Omega X)$; for $i+1>n$, that is $0$. So $\pi_i(\Omega X_n)=\pi_i(\Omega X)$ for $i\le n-1$ and $\pi_i(\Omega X_n)=0$ for $i\ge n$, which is exactly the truncation required of the $(n-1)$-st stage of $\Omega X$. The maps $\Omega X\to\Omega X_n$ induce these isomorphisms, since they are the loops of maps that are isomorphisms on the relevant groups.
:::

:::

::: {.pf-step #principal}
Each fibration $p_n:X_n\to X_{n-1}$ is principal: it is the pullback of a path--loop fibration along a $k$-invariant $k_n:X_{n-1}\to K(\pi_nX,n+1)$, with fibre $K(\pi_nX,n)$.

::: pf-proof
This is the sense in which a Postnikov tower of a connected CW complex is a tower of principal fibrations (Theorem 4.69): the fibration $X_n\to X_{n-1}$ is classified up to fibre homotopy equivalence by the class $k_n\in H^{n+1}(X_{n-1};\pi_nX)$, and a fibration over $X_{n-1}$ with fibre $K(\pi_nX,n)$ and classifying class $k_n$ is the pullback of the path--loop fibration $PK(\pi_nX,n+1)\to K(\pi_nX,n+1)$ along $k_n$.
:::

:::

::: {.pf-step #loopprincipal}
Looping a pullback square produces a pullback square, so $\Omega p_n:\Omega X_n\to\Omega X_{n-1}$ is the pullback of the path--loop fibration over $K(\pi_nX,n+1)$ along $\Omega k_n$.

::: pf-proof
Looping is a right adjoint of the suspension functor and preserves limits, in particular pullbacks, so the looped square exhibits $\Omega X_n\to\Omega X_{n-1}$ as the pullback along $\Omega k_n$ of the loop of the path--loop fibration $PK(\pi_nX,n+1)\to K(\pi_nX,n+1)$ (written $PK$ for the contractible path space). That loop is a fibration with contractible total space over $\Omega K(\pi_nX,n+1)=K(\pi_nX,n)$, that is the path--loop fibration of $K(\pi_nX,n)$, whose fibre is $\Omega K(\pi_nX,n)=K(\pi_nX,n-1)$. Hence the looped fibration is principal, classified by $\Omega k_n$, with fibre
$$
\Omega K(\pi_nX,n)=K(\pi_nX,n-1).
$$
Note the shift: the fibre here is the loop of the *fibre* $K(\pi_nX,n)$ of $p_n$, not the loop of its base.
:::

:::

::: {.pf-step #conclusion}
Looping a Postnikov tower for $X$ gives a Postnikov tower of principal fibrations for $\Omega X$.

::: pf-proof
Steps [](#loop){.pf-ref} and [](#stages){.pf-ref} show that the looped tower is a Postnikov tower for $\Omega X$, with stages $\Omega X_n$ indexed so that $\Omega X_n$ is the $(n-1)$-st stage. Step [](#loopprincipal){.pf-ref} shows that each fibration in it is principal, with fibre the Eilenberg--MacLane loop space $K(\pi_nX,n)=\Omega K(\pi_nX,n+1)$. Hence
$$
\boxed{\text{looping a Postnikov tower for }X\text{ gives a Postnikov tower of principal fibrations for }\Omega X.}
$$
The indexing shifts by one, which is why the fibre of $\Omega X_n\to\Omega X_{n-1}$ is $K(\pi_nX,n-1)$: the group is $\pi_{n-1}(\Omega X)=\pi_n(X)$.
:::

:::

:::
:::
