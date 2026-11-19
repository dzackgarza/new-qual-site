---
schema: qual/card@1
id: P-APAS13L
kind: problem
title: Comaximal ideals, Nullstellensatz, and ideal intersection via an auxiliary variable
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the four parts as the top-level steps and (d) as
    the QED step. Re-checked: $V(I+J)=V(I)\cap V(J)$ and $I(\varnothing)=R$ drive (b) in both
    directions, with $1\in\sqrt{I+J}$ giving $1\in I+J$; the Rabinowitsch trick in (c) is valid in
    both directions because specialising at $t=1$ and $t=0$ maps $IR[t]$ into $I$ and $JR[t]$ into
    $J$; and (d) is the UFD property. Added: the use of algebraic closure in (a), the identification
    of $I(\varnothing)$ with $R$ in (b), and the note that a specialisation of an element of $IR[t]$
    at $t=1$ lies in $I$, which is what makes the second inclusion work. No defect found in the
    statement. The collection's provenance is the Spring 2013 examination paper, so no retained
    solution set covers the problem.
---

::: {.problem}
Let $k$ be an algebraically closed field.

Two ideals $I$ and $J$ of $k[x_1,\ldots,x_n]$ are said to be comaximal if and only if $I+J=k[x_1,\ldots,x_n]$.

(a) State the Weak Nullstellensatz and Hilbert's Nullstellensatz Theorem.

(b) Show that two ideals $I$ and $J$ are comaximal if and only if $V(I)\cap V(J)=\emptyset$.

(c) Show that if $I$ and $J$ are ideals in $k[x_1,\ldots,x_n]$, then
$$
I\cap J=(tI+(1-t)J)\cap k[x_1,\ldots,x_n].
$$

(d) Show that if $I=\langle f\rangle$ and $J=\langle g\rangle$, then $I\cap J=\langle h\rangle$ where $h$ is a least common multiple of $f$ and $g$.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem; the argument is the card's own, and the four parts are the standard consequences of the Nullstellensatz. Write $R=k[x_1,\ldots,x_n]$ with $k$ algebraically closed.

::: pf

::: {.pf-step #statements}
(a) The Weak Nullstellensatz: every maximal ideal of $R$ is $(x_1-a_1,\ldots,x_n-a_n)$ for a unique $a\in k^n$. Hilbert's Nullstellensatz: $I(V(I))=\sqrt I$ for every ideal $I\subseteq R$.

::: pf-proof
These are the two statements in question, with $V(I)=\{a\in k^n:f(a)=0\text{ for all }f\in I\}$ and $I(X)=\{f\in R:f(a)=0\text{ for all }a\in X\}$. The first is the case of the second for maximal ideals, and both use that $k$ is algebraically closed: over a non-algebraically-closed field the maximal ideals of $R$ need not be of that form.
:::

:::

::: {.pf-step #comaximal}
(b) $I+J=R$ if and only if $V(I)\cap V(J)=\varnothing$.

::: pf-proof
First $V(I+J)=V(I)\cap V(J)$, since a point kills $I+J$ exactly when it kills both $I$ and $J$. If $I+J=R$ then $1\in I+J$, so no point kills $I+J$ and $V(I)\cap V(J)=\varnothing$. Conversely if $V(I)\cap V(J)=\varnothing$ then $V(I+J)=\varnothing$, so $\sqrt{I+J}=I(V(I+J))=I(\varnothing)=R$ by the Nullstellensatz, the ideal of the empty set being the whole ring; hence $1\in\sqrt{I+J}$, which means $1^m=1\in I+J$ for some $m\ge1$, so $I+J=R$.
:::

:::

::: {.pf-step #intersection}
(c) $I\cap J=(tI+(1-t)J)\cap R$, inside $R[t]$.

::: pf-proof
Put $K=tI+(1-t)J\subseteq R[t]$. If $f\in I\cap J$ then $f=tf+(1-t)f\in K$ with $f\in R$, so $I\cap J\subseteq K\cap R$. Conversely let $f\in K\cap R$, so $f=ta+(1-t)b$ with $a\in IR[t]$ and $b\in JR[t]$; specialising $t=1$ gives $\restrictionof{f}{t=1}\in I$ and specialising $t=0$ gives $\restrictionof{f}{t=0}\in J$, since $f$ does not involve $t$. Hence $K\cap R\subseteq I\cap J$.
:::

:::

::: {.pf-step}
(d) If $I=(f)$ and $J=(g)$ then $I\cap J=(\operatorname{lcm}(f,g))$.

::: pf-proof
$R$ is a UFD, so a least common multiple $h=\operatorname{lcm}(f,g)$ exists and is unique up to a unit. Since $f\mid h$ and $g\mid h$, $h\in(f)\cap(g)$, giving $(h)\subseteq(f)\cap(g)$. Conversely if $q\in(f)\cap(g)$ then $f\mid q$ and $g\mid q$, and the defining property of the least common multiple gives $h\mid q$, that is $q\in(h)$. Hence $(f)\cap(g)=(h)$. Parts (a), (b) and (c) are steps [](#statements){.pf-ref}, [](#comaximal){.pf-ref} and [](#intersection){.pf-ref}.
:::

:::

:::
:::
