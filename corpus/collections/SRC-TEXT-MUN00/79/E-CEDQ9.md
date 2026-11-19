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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the lift exists by Lemma 79.1 with
    the base points made to correspond, $S^n$ being simply connected for $n>1$ and $\RR$
    contractible; the contraction is exhibited as the explicit homotopy $H(t,y)=(1-t)y$; and
    composing with $p$ gives the nullhomotopy. Added: the explicit contraction of $\RR$ and the
    statement that the composed homotopy is constant in the space variable at time $1$, which the
    prose left to the reader. The source is a Stack Exchange answer, a user post and not a
    publication, and the card says so; the earlier events already record that no published solution
    of §79 Exercise 1 was located. No defect found in the statement, printed p. 483.
---

::: {.exercise}

Show that if $n > 1$, every continuous map $f: S^n \to S^1$ is nullhomotopic.
[Hint: Use the lifting lemma.]
:::

::: {.solution}
The argument is that of Math StackExchange answer 2813771, posted 2018-06-09 to question 2813729, and it is the argument the printed hint asks for. The same argument for $n=2$ alone is answer 783783, posted 2014-05-06 to question 783766, with nothing added. Take the universal covering $p\colon\RR\to S^1$, $p(t)=e^{2\pi it}$, of Theorem 53.1 (printed p. 337).

::: pf

::: {.pf-step #lift}
For $n>1$ and continuous $f\colon S^n\to S^1$, there is a continuous $\tilde f\colon S^n\to\RR$ with $p\circ\tilde f=f$.

::: pf-proof
Choose $x_0\in S^n$ and put $b_0=f(x_0)$; since $p$ is onto, choose $e_0\in p^{-1}(b_0)$, so that $p(e_0)=f(x_0)$, which is the base-point condition of Lemma 79.1. The sphere $S^n$ is path connected, locally path connected and, for $n>1$, simply connected, so $f_*\pi_1(S^n,x_0)=0$; and $\RR$ is contractible, so $p_*\pi_1(\RR,e_0)=0$. Hence $f_*\pi_1(S^n,x_0)\subseteq p_*\pi_1(\RR,e_0)$, and Lemma 79.1, the general lifting lemma (printed p. 478), applied with $Y=S^n$ and $y_0=x_0$, produces the lift with $\tilde f(x_0)=e_0$.
:::

:::

::: {.pf-step #contract}
$\tilde f$ is homotopic to a constant map $c\colon S^n\to\RR$.

::: pf-proof
$\RR$ is contractible: the map $H(t,y)=(1-t)y$ is a homotopy from the identity of $\RR$ to the constant map at $0$, so $H\circ(\operatorname{id}\times\tilde f)$ is a homotopy from $\tilde f$ to the constant map at $0$.
:::

:::

::: {.pf-step}
$\boxed{\text{Every continuous }f\colon S^n\to S^1\text{ with }n>1\text{ is nullhomotopic}}$.

::: pf-proof
Let $G\colon S^n\times[0,1]\to\RR$ be the homotopy of step [](#contract){.pf-ref} from $\tilde f$ to a constant map. Then $p\circ G\colon S^n\times[0,1]\to S^1$ is continuous, agrees with $p\circ\tilde f=f$ at time $0$ by step [](#lift){.pf-ref}, and is constant in the space variable at time $1$; so $f$ is homotopic to the constant map $p\circ c$, that is, $f$ is nullhomotopic.
:::

:::

:::
:::
