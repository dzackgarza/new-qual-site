---
schema: qual/card@1
id: E-BB4BN
kind: problem
title: Intervals homeomorphic with the unit interval
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 5, printed p. 111, with the subspace
    topology of §16; the stored statement is the printed sentence, and the card treats a < b
    and a = b separately.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.5, printed p. 181.
    The maps x -> (x-a)/(b-a) and y -> a + y(b-a) and the argument that they are mutually
    inverse continuous bijections are his, as is the remark that [a,a] cannot be
    homeomorphic with [0,1]. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Show that the subspace $(a, b)$ of $\RR$ is homeomorphic with $(0, 1)$ and the subspace $[a, b]$ of $\RR$ is homeomorphic with $[0, 1]$.
:::

::: {.solution}

The maps and the argument are those of **Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.5, manual p. 181, PDF p. 184 (`tmp/sources/munkres-solutions-whitman.pdf`), including his observation on the degenerate case; the statement was checked against Munkres, *Topology* (2000), §18 Exercise 5. Both parts presuppose $a<b$: for $a=b$ the interval $(a,a)$ is empty and $[a,a]$ is a one-point space, so the statement as printed is understood with $a<b$, and the degenerate case is recorded in the last step below.

::: pf

::: {.pf-step #interval-bijection}
Let $a<b$ and let $f\colon(a,b)\to(0,1)$ be given by $f(x)\coloneqq\frac{x-a}{b-a}$. Then $f$ is a bijection.

::: pf-proof
Since $b-a>0$, if $a<x<b$ then $0<\frac{x-a}{b-a}<\frac{b-a}{b-a}=1$, so $f$ takes its values in $(0,1)$. If $f(x)=f(x')$ then $x-a=x'-a$ and $x=x'$, so $f$ is injective. For $t\in(0,1)$ the point $x\coloneqq a+t(b-a)$ satisfies $x-a=t(b-a)$ with $0<t<1$, hence $a<x<b$, and $f(x)=t$; so $f$ is surjective.
:::

:::

::: {.pf-step #open-interval}
$f$ is a homeomorphism of $(a,b)$ onto $(0,1)$.

::: pf-proof
By step [](#interval-bijection){.pf-ref} it is a bijection, with inverse $g(t)\coloneqq a+t(b-a)$. The map $x\mapsto(x-a)/(b-a)$ is linear on $\RR$, hence continuous, and $f$ is its restriction to the subspace $(a,b)$, so $f$ is continuous by Theorem 18.2(d); likewise $g$ is linear and $g=f^{-1}$ is continuous. A continuous bijection with continuous inverse is a homeomorphism.
:::

:::

::: {.pf-step #closed-interval}
For $a<b$, the subspace $[a,b]$ is homeomorphic with $[0,1]$.

::: pf-proof
The same formula $f(x)=\frac{x-a}{b-a}$ maps $[a,b]$ into $[0,1]$ bijectively: if $a\leq x\leq b$ then $0\leq f(x)\leq 1$, and for $t\in[0,1]$ the point $a+t(b-a)$ lies in $[a,b]$ and maps to $t$. Continuity of $f$ and of its inverse $t\mapsto a+t(b-a)$ is again that of the restrictions of the two linear maps, by Theorem 18.2(d).
:::

:::

::: pf-step
Both assertions hold under the stated hypothesis $a<b$, and the degenerate case $a=b$ is excluded.

::: pf-proof
Steps [](#open-interval){.pf-ref} and [](#closed-interval){.pf-ref} give the two homeomorphisms. If $a=b$, then $[a,b]=\theset{a}$ is a one-point space and $(a,a)=\varnothing$; a homeomorphism is a bijection, and neither the empty set nor a one-point set is in bijection with $[0,1]$ or with $(0,1)$, which are infinite, so nothing is lost by reading the exercise with $a<b$.
:::

:::

:::

:::
