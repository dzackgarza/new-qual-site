---
schema: qual/card@1
id: P-WESTOP03-06
kind: problem
title: Describe the universal cover of the Klein bottle
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Describe the universal covering space of the Klein bottle.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Realize the Klein bottle $K$ as the quotient of the unit square by the identifications
\[
(0,y)\sim(1,y),
\qquad
(x,0)\sim(1-x,1).
\]


::: pf-proof

This is the standard polygonal model of the Klein bottle: one pair of opposite sides is glued preserving orientation and the other pair reversing orientation.

:::

:::

::: pf-step

Define homeomorphisms of $\RR^2$ by
\[
a(x,y)=(x+1,y),
\qquad
b(x,y)=(-x,y+1).
\]
Let $G=\langle a,b\rangle$.


::: pf-proof

Both maps are Euclidean isometries and hence homeomorphisms. Their action reproduces the two edge identifications of the square: $a$ identifies the vertical sides, while $b$ identifies the horizontal sides with reversal in the $x$-coordinate.

:::

:::

::: {.pf-step #s1-3}

The generators satisfy
\[
bab^{-1}=a^{-1}.
\]


::: pf-proof

Since
\[
b^{-1}(x,y)=(-x,y-1),
\]
one computes
\[
bab^{-1}(x,y)
=ba(-x,y-1)
=b(-x+1,y-1)
=(x-1,y)
=a^{-1}(x,y).
\]

:::

:::

::: {.pf-step #s1-4}

Every element of $G$ has the form
\[
a^m b^n,
\qquad m,n\in\ZZ,
\]
and acts by
\[
a^m b^n(x,y)
=\bigl(m+(-1)^n x,\,y+n\bigr).
\]


::: pf-proof

The relation in step [](#s1-3){.pf-ref} allows every word to be rearranged into $a^mb^n$. Since
\[
b^n(x,y)=((-1)^nx,y+n),
\]
applying $a^m$ gives the formula.

:::

:::

::: {.pf-step #s1-5}

The action of $G$ on $\RR^2$ is free.


::: pf-proof

Suppose $a^mb^n(x,y)=(x,y)$. Comparing second coordinates in step [](#s1-4){.pf-ref} gives $n=0$. Then the first coordinate gives $x+m=x$, so $m=0$. Thus only the identity fixes a point.

:::

:::

::: {.pf-step #s1-6}

The action is properly discontinuous.


::: pf-proof

Let $C\subset\RR^2$ be compact. Its $x$- and $y$-coordinates are bounded. If
\[
a^mb^n(C)\cap C\ne\varnothing,
\]
then the formula in step [](#s1-4){.pf-ref} forces $n$ to lie in a bounded set of integers by comparing $y$-coordinates; for each such $n$, comparison of $x$-coordinates forces $m$ into a bounded set of integers. Hence only finitely many group elements move $C$ to meet itself, which is proper discontinuity for this discrete action.

:::

:::

::: {.pf-step #s1-7}

The quotient
\[
\RR^2/G
\]
is homeomorphic to the Klein bottle $K$.


::: pf-proof

The square $[0,1]\times[0,1]$ is a fundamental polygon for the action. The transformation $a$ identifies its two vertical sides as in step [](#s1-1){.pf-ref}, and $b$ identifies its horizontal sides with the reversal $x\mapsto1-x$ after composing with an integral horizontal translation if necessary. Thus the orbit equivalence relation on the fundamental square is exactly the Klein-bottle edge relation.

:::

:::

::: {.pf-step #s1-8}

Therefore the quotient map
\[
p:\RR^2\to K\cong\RR^2/G
\]
is a covering map.


::: pf-proof

A free properly discontinuous action by homeomorphisms has quotient projection a covering map. Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} verify these hypotheses and identify the quotient.

:::

:::

::: {.pf-step #s1-9}

Since $\RR^2$ is simply connected, this covering is universal.


::: pf-proof

The plane is contractible via
\[
H((x,y),t)=((1-t)x,(1-t)y),
\]
so it is simply connected. A connected simply connected covering space is a universal covering space.

:::

:::

::: {.pf-step #s1-10}

Hence the universal covering space of the Klein bottle is
\[
\boxed{\RR^2.}
\]


::: pf-proof

Steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} exhibit $\RR^2$ as a simply connected covering of the Klein bottle.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the requested description.

:::

:::

:::
