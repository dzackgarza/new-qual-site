---
schema: qual/card@1
id: P-CASP19D
kind: problem
title: "Growth bound for the derivative of a conformal map via distance to boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Riemann Mapping Theorem
  - Derivative Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: $r$ is the distance from $a$ to the
    complement, so $D(a,r)\subseteq\Omega$ and $F(\zeta)=f(a+r\zeta)$ maps $\DD$ to $\DD$ fixing $0$
    with derivative $rf'(a)$, giving $r\le1/f'(a)$; and for $R<\infty$ the exterior of
    $\overline{D(a,R)}$ is connected and disjoint from $\partial\Omega$, so either it lies in
    $\Omega$ or $\Omega\subseteq\overline{D(a,R)}$ — the first alternative makes $\CC\setminus\Omega$
    compact hence $\hat\CC\setminus\Omega$ disconnected, against simple connectivity. Then
    $G=(g-a)/R$ maps $\DD$ into the closed disc with $G(0)=0$, so Schwarz gives $1/f'(a)\le R$.
    Repaired: the earlier text concluded $\Omega\subset D(a,R)$ with strict containment, which the
    argument does not give — a domain may touch the circle $|z-a|=R$ — and the card now states
    $\Omega\subseteq\overline{D(a,R)}$ and uses Schwarz's lemma in the closed-disc form, which is
    the form that applies. Added: the reason $D(a,r)\subseteq\Omega$, the connectedness of the
    exterior, and the derivative of the inverse under the inverse function theorem. The collection's
    provenance is the Spring 2019 examination paper, so no retained solution set covers the problem.
---

::: {.problem}
Let $\Omega \neq \CC$ be a simply connected region with $a \in \Omega$ and $f$ a one-to-one analytic function from $\Omega$ onto $\DD$.
Assume $f(a) = 0$ and $f'(a) > 0$.
Prove that
$$
\inf_{z \in \partial \Omega} \abs{z - a} \leq \frac{1}{f'(a)} \leq \sup_{z \in \partial \Omega} \abs{z - a}.
$$
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own; both inequalities are Schwarz's lemma applied to $f$ rescaled and to $f^{-1}$ rescaled. Put $r=\inf_{z\in\partial\Omega}\abs{z-a}$ and $R=\sup_{z\in\partial\Omega}\abs{z-a}$, in $[0,\infty]$ and $(0,\infty]$ respectively.

::: pf

::: {.pf-step #lower}
$r\le 1/f'(a)$.

::: pf-proof
$r$ is the distance from $a$ to the complement of $\Omega$, so the disc $D(a,r)$ is contained in $\Omega$: were a point of distance less than $r$ outside $\Omega$, a segment from $a$ to it would meet $\partial\Omega$ at distance less than $r$. Hence $F(\zeta)=f(a+r\zeta)$ is defined and holomorphic on $\DD$, takes values in $\DD$, and satisfies $F(0)=f(a)=0$ and $F'(0)=rf'(a)$. Schwarz's lemma gives $\abs{F'(0)}\le1$, that is $rf'(a)\le1$; since $f'(a)>0$, this is $r\le1/f'(a)$.
:::

:::

::: {.pf-step #containment}
If $R<\infty$ then $\Omega\subseteq\overline{D(a,R)}$.

::: pf-proof
Suppose $\Omega$ meets the exterior $E=\CC\setminus\overline{D(a,R)}$. The set $E$ is connected and disjoint from $\partial\Omega$, every boundary point having distance at most $R$ from $a$; a connected set disjoint from the boundary of $\Omega$ lies entirely in $\Omega$ or entirely in its complement, so $E\subseteq\Omega$. Then $\CC\setminus\Omega$ is a nonempty subset of the compact set $\overline{D(a,R)}$, hence compact and bounded away from $\infty$; so the complement of $\Omega$ in the Riemann sphere is $(\CC\setminus\Omega)\cup\{\infty\}$, a disjoint union of two nonempty relatively closed sets, which is disconnected. That contradicts the characterization of simply connected proper plane domains as those whose complement in the sphere is connected. Hence $\Omega\cap E=\varnothing$, that is $\Omega\subseteq\overline{D(a,R)}$.
:::

:::

::: {.pf-step #upper}
$1/f'(a)\le R$.

::: pf-proof
If $R=\infty$ there is nothing to prove. Otherwise step [](#containment){.pf-ref} gives $\Omega\subseteq\overline{D(a,R)}$. Let $g=f^{-1}\colon\DD\to\Omega$, which is holomorphic with $g(0)=a$ and $g'(0)=1/f'(a)$ by the inverse function theorem. Then
$$
G(\zeta)=\frac{g(\zeta)-a}{R}
$$
is holomorphic on $\DD$, satisfies $G(0)=0$ and $\abs{G(\zeta)}\le1$ because $g(\zeta)\in\overline{D(a,R)}$, and has $G'(0)=1/(Rf'(a))$. Schwarz's lemma, in the form that a holomorphic map of $\DD$ into the closed unit disc fixing $0$ has derivative at $0$ of modulus at most $1$, gives $1/(Rf'(a))\le1$, hence $1/f'(a)\le R$.
:::

:::

::: {.pf-step}
$\boxed{\inf_{z\in\partial\Omega}\abs{z-a}\le\dfrac{1}{f'(a)}\le\sup_{z\in\partial\Omega}\abs{z-a}}$.

::: pf-proof
The two inequalities are steps [](#lower){.pf-ref} and [](#upper){.pf-ref}: $r\le1/f'(a)\le R$. Both bounds are attained as equalities exactly when the corresponding Schwarz lemma is an equality, that is when $F$ or $G$ is a rotation, so when $\Omega$ is a disc centred at $a$; the statement only asserts the inequalities.
:::

:::

:::
:::
