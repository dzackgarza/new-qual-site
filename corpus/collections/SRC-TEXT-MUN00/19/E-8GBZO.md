---
schema: qual/card@1
id: E-8GBZO
kind: problem
title: The box topology implication in the maps-into-products theorem
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 5, printed p. 118, with Theorem 19.6
    on printed p. 117 and Example 19.2; the stored statement is the printed question and the
    card answers which implication holds.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.5, printed p. 192.
    His is the affirmative half: continuity of f gives continuity of each coordinate
    function, by pulling back the box basis element that is V in one coordinate and the
    whole space elsewhere. The failure of the converse is Munkres's Example 19.2, written
    out on the card with the box-open set whose preimage is the single point 0.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the surviving implication for the box topology
    (the product of V at beta with the other factors gives a box basis element, so f_beta is
    continuous) and the failure of its converse with Example 2 of §19: f(t)=(t,t,t,...) and
    the box-open set prod_n (-1/n,1/n), whose preimage is {0}. Source line repaired: an
    earlier version identified the counterexample as the map (t,2t,3t,...), which is not the
    book's Example 2 and does not occur in Munkres. Whitman, Exercise 19.5, printed p. 192,
    citing Example 19.2.
---

::: {.exercise}

One of the implications stated in Theorem 19.6 holds for the box topology.
Which one?
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.5, printed p. 192** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer and the proof of the surviving implication are his. One source line is repaired: the counterexample is Example 2 of §19 as the book prints it, the map $f(t)=(t,t,t,\dots)$, and not the map $f(t)=(t,2t,3t,\dots)$ with which an earlier version of this card identified it.

Throughout, $f:A\to\prod_{\alpha\in J}X_{\alpha}$ is given by $f(a)=(f_{\alpha}(a))_{\alpha\in J}$ and the product carries the box topology; $\pi_{\beta}$ is the projection.

::: pf

::: {.pf-step #continuous-implies}
If $f$ is continuous, then every coordinate function $f_{\beta}=\pi_{\beta}\circ f$ is continuous.

::: pf-proof
Fix $\beta\in J$ and let $V$ be open in $X_{\beta}$. Put $B_{\alpha}=V$ for $\alpha=\beta$ and $B_{\alpha}=X_{\alpha}$ otherwise, and $B=\prod_{\alpha\in J}B_{\alpha}$. Each $B_{\alpha}$ is open in $X_{\alpha}$, so $B$ is a basis element of the box topology, hence open in the product, and $U=f^{-1}(B)$ is open in $A$ because $f$ is continuous. For $a\in A$,
$$
a\in U\iff f(a)\in B\iff f_{\alpha}(a)\in B_{\alpha}\ \text{for all }\alpha\iff f_{\beta}(a)\in V,
$$
so $U=f_{\beta}^{-1}(V)$. As $V$ was arbitrary, $f_{\beta}$ is continuous, and $\beta$ was arbitrary.
:::

:::

::: {.pf-step #converse-fails}
The converse fails for the box topology: in Example 2 of §19 the map $f:\RR\to\RR^{\omega}$, $f(t)=(t,t,t,\dots)$, has every coordinate function continuous, and $f$ is not continuous for the box topology on $\RR^{\omega}$.

:::: pf-proof

::: {.pf-step #coordinates-continuous}
Every coordinate function $f_{n}(t)=t$ of the example is continuous.

::: pf-proof
Each $f_{n}$ is the identity map of $\RR$, which is continuous.
:::

:::

::: {.pf-step #not-continuous}
$f$ is not continuous for the box topology.

::: pf-proof
The set $B=\prod_{n\in\ZZ_{+}}\big(-\tfrac1n,\tfrac1n\big)$ is a box-open set containing $f(0)=\mathbf{0}$, because each factor is an open interval containing $0$. A real $t$ satisfies $f(t)\in B$ exactly when $\abs{t}<1/n$ for every $n\in\ZZ_{+}$, which forces $t=0$: if $t\ne0$ then the positive integers are unbounded, so some $n$ has $n>1/\abs{t}$, that is $1/n<\abs{t}$. Hence $f^{-1}(B)=\{0\}$. That set is not open in $\RR$, since an interval $(-\delta,\delta)$ about $0$ contains $\delta/2$, which is nonzero and so lies outside $f^{-1}(B)$.
:::

:::

::: {.pf-step}
The converse fails.

::: pf-proof
Steps [](#coordinates-continuous){.pf-ref} and [](#not-continuous){.pf-ref} give a map all of whose coordinate functions are continuous and which is not continuous.
:::

:::

:::

:::

::: {.pf-step}
The implication that holds for the box topology is that a continuous $f$ has every $f_{\alpha}$ continuous; its converse does not hold.

::: pf-proof
Steps [](#continuous-implies){.pf-ref} and [](#converse-fails){.pf-ref} are the two assertions; Theorem 19.6 states that in the product topology both implications hold, and step [](#converse-fails){.pf-ref} shows the second of them does not survive the passage to the box topology.
:::

:::

:::
:::
