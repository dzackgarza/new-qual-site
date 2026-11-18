---
schema: qual/card@1
id: E-QMZO5
kind: problem
title: Dictionary order topology on the plane as a product topology
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 9, printed p. 92; the stored
    statement is the printed one, R_d being R with the discrete topology.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.9, PDF p. 5. Both inclusions are his: {a} x
    (b,d) is a dictionary-open interval, and an interval ((a,b),(c,d)) with a < c is the
    union of {a} x (b,infinity), (a,c) x R and {c} x (-infinity,d), each a union of product
    basis elements. Strictness over the standard topology of R^2 is his witness {0} x (0,1).
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, with both retained sets now cited in the solution
    section. Pages verified: §16 Exercise 9 on printed p. 92; Theorem 16.2 on printed p. 87
    and Lemma 13.2 on printed p. 80, the two results that identify the bases used; and the
    Whitman answer, which the retained PDF shows beginning at the foot of his p. 155 and
    continuing on p. 156, so the citation pp. 155-156 is right. Each step checked: the
    interval ((a,b),(a,d)) is exactly {a} x (b,d), since the two inequalities force x = a and
    b < y < d; an interval with distinct first coordinates splits into the three displayed
    pieces; and the middle piece (a,c) x R is a union of basis elements {t} x (-n,n), which
    replaces the earlier display "union over a<t<c and s<r of {t} x (s,r)", in which the
    indices s, r were not quantified. The comparison with the standard topology is unchanged
    in substance: every rectangle is a union of vertical slices, and {0} x (0,1) is a basis
    element of the product topology that is not standard-open. No repair to the statement.
---

::: {.exercise}

Show that the dictionary order topology on the set $\RR \times \RR$ is the same as the product topology $\RR_d \times \RR$, where $\RR_d$ denotes $\RR$ in the discrete topology.
Compare this topology with the standard topology on $\RR^2$.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.9, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`), restructured into steps; the same argument is in **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.9, printed pp. 155--156**, read in the retained PDF, with one correction to the notation of the middle piece below.

Throughout, $\prec$ is the dictionary order on $\RR\times\RR$, $\mathcal{T}_d$ its order topology, $\mathcal{T}_p$ the product topology of $\RR_d\times\RR$ where $\RR_d$ is $\RR$ discrete, and $\mathcal{T}$ the standard topology of $\RR^2$. The exercise is §16 Exercise 9 (printed p. 92). A basis for $\mathcal{T}_p$ is $\{\{a\}\times(b,d)\}$, since $\{\{a\}\}$ is a basis for $\RR_d$, $\{(b,d)\}$ one for $\RR$, and products of basis elements form a basis for the product (Theorem 16.2, printed p. 87); a basis for $\mathcal{T}_d$ is the collection of open intervals, since $\RR\times\RR$ has no least and no greatest element in the dictionary order.

::: pf

::: {.pf-step #p-in-d}
$\mathcal{T}_p\subset\mathcal{T}_d$.

::: pf-proof
A basis element of $\mathcal{T}_p$ is $\{a\}\times(b,d)$ with $b<d$. A point $(x,y)$ satisfies $(a,b)\prec(x,y)\prec(a,d)$ exactly when $x=a$ and $b<y<d$: the first inequality gives $x>a$, or $x=a$ and $y>b$, and the second gives $x<a$, or $x=a$ and $y<d$. So $\{a\}\times(b,d)$ is the open interval $\big((a,b),(a,d)\big)$ of the dictionary order, hence a basis element of $\mathcal{T}_d$, and every set of $\mathcal{T}_p$ is a union of such sets.
:::

:::

::: {.pf-step #d-in-p}
$\mathcal{T}_d\subset\mathcal{T}_p$, so $\mathcal{T}_d=\mathcal{T}_p$.

::: pf-proof

::: {.pf-step #same-first}
If $a=c$, then $\big((a,b),(a,d)\big)=\{a\}\times(b,d)$, a basis element of $\mathcal{T}_p$.

::: pf-proof
With equal first coordinates the two inequalities of step [](#p-in-d){.pf-ref} read $x=a$ and $b<y<d$.
:::

:::

::: {.pf-step #differing-first}
If $a<c$, then
$$
\big((a,b),(c,d)\big)=\big(\{a\}\times(b,\infty)\big)\cup\big((a,c)\times\RR\big)\cup\big(\{c\}\times(-\infty,d)\big),
$$
and each of the three sets on the right is a union of basis elements of $\mathcal{T}_p$.

::: pf-proof
A point $(x,y)$ lies in the interval when $x$ lies between $a$ and $c$ and is not an endpoint, or $x=a$ and $y>b$, or $x=c$ and $y<d$; these three conditions are exclusive and give the displayed union, the order comparing first coordinates first. For the second claim,
$$
\{a\}\times(b,\infty)=\bigcup_{b<r}\{a\}\times(b,r),\qquad
(a,c)\times\RR=\bigcup_{a<t<c}\{t\}\times\RR=\bigcup_{a<t<c}\ \bigcup_{n\in\ZZ_+}\{t\}\times(-n,n),
$$
$$
\{c\}\times(-\infty,d)=\bigcup_{s<d}\{c\}\times(s,d),
$$
and $\{t\}\times(-n,n)$ is a basis element of $\mathcal{T}_p$ for every $t$ and $n$, so each of the three sets is a union of basis elements. A basis element of $\mathcal{T}_d$ is an interval, and steps [](#same-first){.pf-ref} and this one cover the two cases, so every basis element of $\mathcal{T}_d$ lies in $\mathcal{T}_p$.
:::

:::

:::

:::

::: {.pf-step}
$\mathcal{T}\subset\mathcal{T}_p$, and the inclusion is strict; hence $\mathcal{T}_d=\mathcal{T}_p$ is strictly finer than the standard topology of $\RR^2$.

::: pf-proof
A basis element $(a,b)\times(c,d)$ of the standard topology is $\bigcup_{a<t<b}\{t\}\times(c,d)$, a union of basis elements of $\mathcal{T}_p$. The set $\{0\}\times(0,1)$ is a basis element of $\mathcal{T}_p$, and it is not open in the standard topology: a standard basis element containing $(0,1/2)$ is a rectangle $(a,b)\times(c,d)$ with $a<0<b$, and it contains points whose first coordinate is not $0$. So $\mathcal{T}\subsetneq\mathcal{T}_p$, and by step [](#d-in-p){.pf-ref} the dictionary order topology is strictly finer than the standard one.
:::

:::

:::
:::
