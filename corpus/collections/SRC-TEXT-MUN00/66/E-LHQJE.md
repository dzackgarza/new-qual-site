---
schema: qual/card@1
id: E-LHQJE
kind: problem
title: The winding number as a degree
classification:
  areas:
  - topology
  topics:
  - Winding Number
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §66 Exercise 1, printed p. 406. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Checked against the definition of the winding number
    on printed p. 403 and the degree of a circle map in Exercise 2 of §57 (printed p. 358), which is the
    definition the exercise compares with; the comparison is made through the lifting correspondence of Theorem
    54.3 (printed p. 343) and the standard covering map p: R -> S^1 of Theorem 53.1 (printed p. 335).
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §66 Exercise 1, printed p. 406. Searched outside the checkout for issue #144 on the orchestrator's
    machine, recorded in tmp/sources/mse-searches-144.md; no thread was saved because no question on the exercise
    was found. The queries were "winding number equals degree Munkres", the title query "winding number degree",
    "winding number degree loop", the title query "winding number", q="n(f,a)", and the /similar query "winding
    number of loop equals degree of induced map of circle". Two questions were read and rejected as treating other
    definitions of the winding number, 741880 and 458583; neither is a solution of this exercise and neither was
    saved. Nothing is transcribed and the card keeps its proof, whose closing step identifies n(f,a) with deg h
    through the isomorphism of Theorem 54.5 (printed p. 345). dbFin has no §66 page, Murayama's selection no Chapter
    10, the fourteen GitHub repositories stop at Chapter 3, and the two course pages consulted post no solutions of
    these sections.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The closing step had called both sides "the change in the lift of g", which is the
    book's definition of $n(f,a)$ (printed p. 403) but not of $\deg h$: Exercise 9 of §58 defines the degree by
    $h_*(\gamma(x_0))=d\cdot\gamma(x_1)$. The step now applies the isomorphism
    $[\delta]\mapsto\tilde\delta(1)-\tilde\delta(0)$ of Theorem 54.5 (printed p. 345) at $x_1=h(b_0)$, where it
    carries $[g]=h_*(\gamma(x_0))$ to $\tilde g(1)-\tilde g(0)$ and the preferred generator to $1$, and reads
    off $d$. Two citations of the 2026-11-11 note are corrected: the degree of a circle map is defined in
    Exercise 9 of §58, printed p. 366, and not in "Exercise 2 of §57, printed p. 358", whose Exercise 2 is about
    the surjectivity of maps $S^2\to S^2$; and the lifting correspondence used is Theorem 54.4 with Theorem
    54.5 on printed p. 345, Theorem 54.3 being on printed p. 344 rather than p. 343; and the covering map of
    Theorem 53.1 is on printed p. 337, not p. 335. Not re-read in this pass: the lemmas of §66 after its
    definition.
---

::: {.exercise}

Let $f$ be a loop in $\RR^2 - a$; let $g(s) = [f(s) - a]/\norm{f(s) - a}$.
The map $g$ induces, via the standard quotient map $p: I \to S^1$, a continuous map $h: S^1 \to S^1$.
Show that $n(f, a)$ equals the degree of $h$, as defined in [[E-UU8CC]].
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Lifting and definition of the winding number:

::: pf-proof

::: pf-step

Consider the standard universal covering map $e: \RR \to S^1$ given by $e(t) = (\cos 2\pi t, \sin 2\pi t) = e^{2\pi i t}$.
The normalized loop $g: [0, 1] \to S^1$ is defined by:
$$
g(s) = \frac{f(s) - a}{\norm{f(s) - a}}.
$$

::: pf-proof

definition of radial projection onto $S^1$.

:::

:::

::: pf-step

By the Path Lifting Property for covering spaces, given any choice of $\tilde{g}(0) = t_0 \in e^{-1}(g(0))$, there exists a unique continuous lift $\tilde{g}: [0, 1] \to \RR$ such that $e \circ \tilde{g} = g$.

::: pf-proof

Path Lifting Theorem for covering spaces.

:::

:::

::: pf-step

By definition, the winding number of the loop $f$ around $a$ is the integer change:
$$
n(f, a) = \tilde{g}(1) - \tilde{g}(0).
$$

::: pf-proof

standard definition of winding number via angular lifting.

:::

:::

:::

:::

::: {.pf-step #s2}

Lifting and definition of the degree of $h: S^1 \to S^1$:

::: pf-proof

::: pf-step

The quotient map $p: [0, 1] \to S^1$ is $p(s) = e(s)$.
The continuous map $h: S^1 \to S^1$ satisfies $h(p(s)) = g(s)$ for all $s \in [0, 1]$.

::: pf-proof

definition of the induced map $h$.

:::

:::

::: pf-step

The standard generator of $\pi_1(S^1, 1)$ is the path homotopy class of $\gamma(s) = e(s)$.
The induced homomorphism $h_*: \pi_1(S^1, 1) \to \pi_1(S^1, h(1))$ maps $[\gamma]$ to $[h \circ \gamma] = [g]$.

::: pf-proof

functoriality of the fundamental group.

:::

:::

::: pf-step

Under the isomorphism $\pi_1(S^1,x)\to\ZZ$ that sends the class of a loop $\delta$ at $x$ to $\tilde\delta(1)-\tilde\delta(0)$, the degree of $h$ is
$$
\deg(h) = \tilde{g}(1) - \tilde{g}(0).
$$

::: pf-proof

Exercise 9 of §58 defines the degree as the integer $d$ with $h_*(\gamma(x_0))=d\cdot\gamma(x_1)$, where $\gamma(x)$ is the preferred generator at $x$. Take $x_0=b_0=p(0)$, so that $\gamma(x_0)=\gamma$ and $h_*(\gamma(x_0))=[h\circ\gamma]=[g]$, and put $x_1=h(b_0)$, so that $[g]=d\cdot\gamma(x_1)$. By Theorem 54.5 and change of basepoint, $[\delta]\mapsto\tilde\delta(1)-\tilde\delta(0)$ is an isomorphism $\pi_1(S^1,x)\to\ZZ$ for every $x$, and it carries the preferred generator $\gamma(x)$ to $1$, because $\gamma(x)$ is $\gamma$ transported along a path from $b_0$ to $x$ and the lift difference of $\gamma$ is $1$. Applying it at $x_1$ to $[g]=d\cdot\gamma(x_1)$ gives $\tilde{g}(1)-\tilde{g}(0)=d$. The difference $\tilde{g}(1)-\tilde{g}(0)$ is the same for every lift of $g$.


:::

:::

:::

:::

::: pf-step

Conclusion:
Both definitions coincide with $\tilde{g}(1) - \tilde{g}(0)$, so $n(f, a) = \deg(h)$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
