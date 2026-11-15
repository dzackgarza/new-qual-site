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
---

::: {.exercise}

Give an example to show that the conclusion of the Borsuk lemma need not hold if $f$ is not injective.
:::

::: {.solution}

The Borsuk lemma is Lemma 62.2 (printed p. 382): if $a$ and $b$ are points of $S^2$, $A$ is a compact space, and $f:A\to S^2-\theset{a,b}$ is continuous, injective and nullhomotopic, then $a$ and $b$ lie in the same component of $S^2-f(A)$. The example keeps every hypothesis but injectivity.

Take $a$ and $b$ to be the north and south poles of $S^2$, its centre at the origin, and take $A=[0,2]$, which is compact. Define $g:[0,2]\to S^2$ by
$$
g(t)=\begin{cases}(\cos 2\pi t,\ \sin 2\pi t,\ 0), & 0\le t\le 1,\\ (\cos 2\pi(2-t),\ \sin 2\pi(2-t),\ 0), & 1\le t\le 2,\end{cases}
$$
so that $g(0)=g(1)=g(2)=(1,0,0)$ and $g$ runs once round the equator in one direction on $[0,1]$ and once round it in the other direction on $[1,2]$.

The image of $g$ is the equator, which lies in $S^2-\theset{a,b}$. The two halves of the formula agree at $t=1$, so $g$ is continuous by the pasting lemma (Theorem 18.3, printed p. 108). And $g(0)=g(1)$ with $0\ne1$, so $g$ is not injective. And $g$ is nullhomotopic: $[0,2]$ is contractible, and $H(t,s)=g\bigl((1-s)t\bigr)$ is a homotopy from $g$ to the constant map at $g(0)$, whose values all lie in the image of $g$.

Finally $S^2-g([0,2])$ is the complement of the equator, which is the union of the open northern and southern hemispheres; those are connected, disjoint and open, so they are its two components, and $a$ and $b$ lie in different ones.

So $g$ has compact domain, is continuous, has image in $S^2-\theset{a,b}$, and is nullhomotopic, while $a$ and $b$ lie in different components of $S^2-g(A)$: the conclusion of the Borsuk lemma fails when $f$ is not injective.
:::
