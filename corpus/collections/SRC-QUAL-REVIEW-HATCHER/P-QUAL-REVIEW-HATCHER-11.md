---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-11
kind: problem
title: Realize the Klein bottle as a quotient of the plane
classification:
  areas: [topology]
  topics:
  - Klein Bottle
  - Group Actions
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 11 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Find a subgroup
$$
\Gamma\subseteq\operatorname{Aut}(\RR^2)
$$
such that
$$
\RR^2/\Gamma
$$
is homeomorphic to the Klein bottle.
:::

::: {.solution}

Define homeomorphisms of $\RR^2$ by
$$
\boxed{
a(x,y)=(x+1,y)}
$$
and
$$
\boxed{
b(x,y)=(-x,y+1)}.
$$

Let
$$
\Gamma=\langle a,b\rangle
\subseteq\operatorname{Aut}(\RR^2).
$$

::: pf

::: pf-step

The inverse of $b$ is
$$
\boxed{
b^{-1}(x,y)=(-x,y-1)}.
$$


::: pf-proof

Indeed,
$$
b(-x,y-1)
=
(x,y).
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
bab^{-1}=a^{-1}}.
$$


::: pf-proof

For $(x,y)\in\RR^2$,
$$
\begin{aligned}
bab^{-1}(x,y)
&=
ba(-x,y-1)\\
&=
b(1-x,y-1)\\
&=
(x-1,y)\\
&=
a^{-1}(x,y).
\end{aligned}
$$

:::

:::

::: pf-step

Every element of $\Gamma$ can be written in the form
$$
\boxed{
a^m b^n}
$$
with
$$
m,n\in\ZZ.
$$


::: pf-proof

The relation
$$
ba=a^{-1}b
$$
from step [](#s1-2){.pf-ref} allows every occurrence of $b$ to be moved to the right of every occurrence of $a$, at the cost of inverting powers of $a$.

:::

:::

::: {.pf-step #s1-4}

For $n=2k$,
$$
\boxed{
b^{2k}(x,y)=(x,y+2k)}.
$$


::: pf-proof

Since
$$
b^2(x,y)
=
b(-x,y+1)
=
(x,y+2),
$$
the formula follows by iteration.

:::

:::

::: {.pf-step #s1-5}

For $n=2k+1$,
$$
\boxed{
b^{2k+1}(x,y)=(-x,y+2k+1)}.
$$


::: pf-proof

Apply one additional $b$ after step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence every element of $\Gamma$ has one of the two forms
$$
(x,y)\longmapsto(x+m,y+2k)
$$
or
$$
(x,y)\longmapsto(-x+m,y+2k+1).
$$


::: pf-proof

Compose $a^m$ with the formulas in steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

The action of $\Gamma$ on $\RR^2$ is free.


::: pf-proof

Suppose a group element fixes $(x,y)$.

For an element of the first type,
$$
(x+m,y+2k)=(x,y)
$$
forces
$$
m=0,\qquad k=0,
$$
so the element is the identity.

For an element of the second type,
$$
(-x+m,y+2k+1)=(x,y)
$$
would force
$$
2k+1=0,
$$
which is impossible for integer $k$.

:::

:::

::: pf-step

The action is properly discontinuous.


::: pf-proof

Let $K\subset\RR^2$ be compact. It is contained in a rectangle
$$
[-M,M]\times[-M,M].
$$
If
$$
\gamma K\cap K\ne\varnothing,
$$
then the translation component in the $y$-direction of $\gamma$ must have absolute value at most $2M$, so only finitely many integers $k$ are possible in step [](#s1-6){.pf-ref}. For each such $k$, the $x$-translation parameter $m$ must also lie in a bounded interval, so only finitely many $m$ occur. Thus only finitely many $\gamma\in\Gamma$ meet $K$.

:::

:::

::: {.pf-step #s1-9}

Every $\Gamma$-orbit meets the closed unit square
$$
Q=[0,1]\times[0,1].
$$


::: pf-proof

Given $(x,y)\in\RR^2$, first use a suitable power of $b$ or $b^2$ to move the $y$-coordinate into $[0,1]$. Then use a suitable power of $a$ to move the $x$-coordinate into $[0,1]$.

:::

:::

::: {.pf-step #s1-10}

The vertical edges of $Q$ are identified by $a$:
$$
\boxed{
(0,y)\sim(1,y)}.
$$


::: pf-proof

$$
a(0,y)=(1,y).
$$

:::

:::

::: {.pf-step #s1-11}

The bottom and top edges are identified by $b$, modulo the vertical-edge identification:
$$
\boxed{
(x,0)\sim(1-x,1)}.
$$


::: pf-proof

One has
$$
b(x,0)=(-x,1).
$$
Using the relation
$$
(u,1)\sim(u+1,1)
$$
coming from $a$, the point $(-x,1)$ is equivalent to
$$
(1-x,1).
$$

:::

:::

::: {.pf-step #s1-12}

Therefore the quotient of $Q$ induced by the $\Gamma$-action has the standard Klein-bottle edge identifications:
$$
(0,y)\sim(1,y),
\qquad
(x,0)\sim(1-x,1).
$$


::: pf-proof

These are exactly the identifications from steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Hence
$$
\boxed{
\RR^2/\Gamma
\cong
K}
$$
where $K$ is the Klein bottle.


::: pf-proof

By step [](#s1-9){.pf-ref}, $Q$ is a fundamental region for the action. Step [](#s1-12){.pf-ref} identifies its boundary exactly by the standard polygon presentation of the Klein bottle.

:::

:::

::: {.pf-step #s1-14}

Thus one valid choice is
$$
\boxed{
\Gamma
=
\left\langle
(x,y)\mapsto(x+1,y),\,
(x,y)\mapsto(-x,y+1)
\right\rangle}.
$$


::: pf-proof

This is the group constructed above, and step [](#s1-13){.pf-ref} proves its quotient is the Klein bottle.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} gives the required subgroup of $\operatorname{Aut}(\RR^2)$.

:::

:::

:::
