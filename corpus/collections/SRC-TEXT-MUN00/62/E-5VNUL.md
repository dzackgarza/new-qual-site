---
schema: qual/card@1
id: E-5VNUL
kind: problem
title: The Borsuk lemma fails without injectivity
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 1, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Two counterexamples have now been discarded. The
    original took A = [0,1] and f(t) = (cos 2 pi t, sin 2 pi t) with a = 0, b = infinity and claimed f was
    nullhomotopic because A is contractible; a nullhomotopy has to lie in S^2 - a - b, where that loop winds once
    about a, so the hypothesis fails. A first replacement used varphi(theta) = theta on [0, pi] and 2 pi - theta on
    [pi, 2 pi], which takes values in [0, pi] only, so the image was an arc of C rather than C; an arc does not
    separate S^2 (Theorem 63.2, printed p. 389), so the Borsuk conclusion held for it and it proved nothing. The
    map below doubles the parameter on each half, so it runs once round all of C and back, and every step is
    checked: image C, continuity, f(0) = f(2 pi), non-injectivity, and the explicit homotopy. Checked against
    Lemma 62.2 (printed p. 382) and Theorem 61.3 (printed p. 379).
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise (issue #144), and two
    were located, both giving the same construction. (1) Problem (6) of "MATH 4530 - Topology.
    Practice Problems For Final solutions", the course solutions of Cornell's MATH 4530 (Fall 2010),
    https://pi.math.cornell.edu/~matsumura/math4530/2010Fall4530PracticeForFinalSol.pdf, printed
    p. 2 of the file, text at
    tmp/sources/munkres-cornell-math4530-2010-practice-final-solutions.txt: a and b the north and
    south poles, g on [0,2] running once round the equator each way with g(0) = g(1) = g(2) = (1,0,0),
    nullhomotopic, and a and b in different components of S^2 - g([0,2]). (2) Math StackExchange
    answer 1840946 by Jason DeVito to question 1840940, "Show that Borsuk lemma need not hold if f is
    not injective" (2016-06-27), text at tmp/sources/mse-1840940-munkres-62-1.md, which uses a single
    loop on [0,1]. The solution on the card is the Cornell argument transcribed: what the printed
    text leaves implicit is written out, the explicit parametrization of g, continuity by the pasting
    lemma, the nullhomotopy through a contraction of [0,2], and the two hemispheres as the components
    of the complement of the equator. It replaces the card's earlier construction, which ran once
    round a round circle and back and needed Theorem 61.3 to see that the circle separates; that
    theorem is no longer used, and the example is the same one. Checked against Lemma 62.2 (printed
    p. 382) and Theorem 18.3 (printed p. 108).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the retained set now cited in the solution
    section rather than only here: Problem (6) of the Cornell MATH 4530 Fall 2010
    practice-final solutions, printed p. 2, whose construction this is (that text states
    it for Lawson's Borsuk Lemma 13.15(3), so it is used as the argument, not as a
    solution of the Munkres exercise), together with Math StackExchange answer 1840946.
    Checked step by step: [0,2] is compact; the two clauses of g agree at t = 1 so g is
    well defined; g is continuous by the pasting lemma on the two closed halves (Theorem
    18.3, p. 108); g(0) = g(1) exhibits the failure of injectivity; H(t,s) = g((1-s)t)
    takes its values in the equator, hence in S^2 - {a,b}, and contracts g to g(0); and
    S^2 - E is the disjoint union of the open hemispheres, which are connected because
    vertical projection carries them homeomorphically onto the open disc, itself
    homeomorphic to R^2, a finite product of connected spaces (Theorem 23.6, p. 151). One
    citation repaired: the earlier prose justified the connectedness of the hemispheres by
    Corollary 24.2, which is about intervals and rays in R and does not apply to them.
    Lemma 62.2 confirmed as printed (p. 382) and the exercise as printed (p. 384). No
    repair to the statement.
---

::: {.exercise}

Give an example to show that the conclusion of the Borsuk lemma need not hold if $f$ is not injective.
:::

::: {.solution}
The construction is the one in the retained set, **Problem (6) of "MATH 4530 -- Topology. Practice Problems For Final solutions", Cornell MATH 4530 (Fall 2010), printed p. 2** (`tmp/sources/munkres-cornell-math4530-2010-practice-final-solutions.txt`), which states it for Lawson's book; the same construction is given by the Math StackExchange answer 1840946 to question 1840940 (`tmp/sources/mse-1840940-munkres-62-1.md`). Each step below is checked against Munkres' own statement of the lemma, Lemma 62.2, whose hypotheses are that $a,b\in S^2$, that $A$ is compact, that $f:A\to S^2-\{a,b\}$ is continuous and injective, and that $f$ is nullhomotopic, and whose conclusion is that $a$ and $b$ lie in the same component of $S^2-f(A)$. The example keeps every hypothesis except injectivity.

Throughout, $S^2$ is the unit sphere in $\RR^3$ with centre the origin, $a=(0,0,1)$ is the north pole, $b=(0,0,-1)$ is the south pole, $E=\{(x,y,0) \mid x^2+y^2=1\}$ is the equator, and $A=[0,2]$.

::: pf

::: {.pf-step #data}
$A$ is compact, $g:A\to E$ is given by the displayed formula, and $E\subset S^2-\{a,b\}$.

::: pf-proof
$A=[0,2]$ is a closed bounded subset of $\RR$, hence compact (Theorem 27.3). Both clauses of the formula for $g$ are continuous on their intervals because the trigonometric functions are, and at $t=1$ they both take the value $(\cos 2\pi,\sin 2\pi,0)=(1,0,0)$, so $g$ is well defined. Its two clauses trace $E$ and $E$ backwards respectively, so $g(A)=E$. Finally $E\subset\RR^2\times\{0\}$ while $a$ and $b$ have third coordinate $\pm1$, so $E\subset S^2-\{a,b\}$, and $g$ takes values in $S^2$.
:::

:::

::: {.pf-step #continuous}
$g$ is continuous.

::: pf-proof
The closed intervals $[0,1]$ and $[1,2]$ are closed subsets of $A$ with union $A$, and the two clauses of the formula are continuous functions on them agreeing at the single common point $t=1$; by the pasting lemma (Theorem 18.3) their union is a continuous map $A\to\RR^3$, which is $g$.
:::

:::

::: {.pf-step #not-injective}
$g$ is not injective.

::: pf-proof
The points $0$ and $1$ of $A$ are distinct and both are carried to $(\cos 0,\sin 0,0)=(1,0,0)$, since at $t=0$ the first clause gives $(\cos 0,\sin 0,0)$ and at $t=1$ both clauses do. So $g(0)=g(1)$ with $0\ne1$.
:::

:::

::: {.pf-step #null}
$g$ is nullhomotopic as a map into $S^2-\{a,b\}$.

::: pf-proof
Define $H:A\times I\to S^2-\{a,b\}$ by $H(t,s)=g\big((1-s)t\big)$. For $(t,s)\in A\times I$ the number $(1-s)t$ lies in $[0,2]=A$, so $H$ is defined and takes its values in $g(A)=E\subset S^2-\{a,b\}$; it is continuous as a composite of the continuous map $(t,s)\mapsto(1-s)t$ and $g$, using step [](#continuous){.pf-ref}. Moreover $H(t,0)=g(t)$ and $H(t,1)=g(0)$ for every $t$, so $H$ is a homotopy from $g$ to the constant map at $g(0)$ and $g$ is nullhomotopic.
:::

:::

::: {.pf-step}
The points $a$ and $b$ lie in different components of $S^2-g(A)$.

::: pf-proof
By step [](#data){.pf-ref} $g(A)=E$, and $S^2-E$ is the union of the open upper hemisphere $U=\{(x,y,z)\in S^2 \mid z>0\}$ and the open lower hemisphere $L=\{(x,y,z)\in S^2 \mid z<0\}$. These two sets are disjoint, open in $S^2$, and each is connected: vertical projection is a homeomorphism of $U$ onto the open unit disc $D$ of $\RR^2$, the map $x\mapsto x/\sqrt{1+\norm{x}^2}$ is a homeomorphism of $\RR^2$ onto $D$, and $\RR^2=\RR\times\RR$ is connected as a finite product of connected spaces (Theorem 23.6). A separation of $S^2-E$ is thus a pair of disjoint nonempty open sets covering it, so $U$ and $L$ are its two components. Since $a=(0,0,1)\in U$ and $b=(0,0,-1)\in L$, the points $a$ and $b$ lie in different components of $S^2-g(A)$, while the remaining hypotheses of Lemma 62.2 hold by steps [](#data){.pf-ref}, [](#continuous){.pf-ref} and [](#null){.pf-ref} and injectivity fails by step [](#not-injective){.pf-ref}. So the conclusion of the Borsuk lemma does not hold for this $g$, which is the required example.
:::

:::

:::
:::
