---
schema: qual/card@1
id: E-MUN-11-4
kind: problem
title: The maximal simply ordered subsets of the plane under $x_0<x_1$ and $y_0\le y_1$
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 4, printed p. 71; the stored
    statement matches, including the three curves and the request to find all maximal
    simply ordered subsets.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.4,
    printed pp. 121-125 (tmp/sources/munkres-solutions-whitman.pdf). His classification is
    the one stated: the graphs of non-decreasing f on an open interval (a,b), unbounded
    above when b is finite and unbounded below when a is finite. The three curve
    verifications and both inclusions of the classification are his, with the case analysis
    compressed here to the three cases his argument turns on.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two maximality claims, the counterexample and the classification, which is what Queue D asks for on this card. The order facts are a step, since every later step quotes them; the curves y = x^3 and y = 2 are separate steps because their maximality has different witnesses, the parabola is the step that exhibits its incomparable pair, and the classification is proved as an if-and-only-if with the two implications as substeps, the second carrying the interval, openness and unboundedness arguments. Statement re-read against Munkres, Topology (2000), §11 Exercise 4, printed pp. 71--72, and the classification and verifications against Dan Whitman's set, Exercise 11.4, printed pp. 121-125. No statement repair.
---

::: {.exercise}

Given two points $(x_0, y_0)$ and $(x_1, y_1)$ of $\RR^2$, define $(x_0, y_0) \prec (x_1, y_1)$ if $x_0 < x_1$ and $y_0 \le y_1$. Show that the curves $y = x^3$ and $y = 2$ are maximal simply ordered subsets of $\RR^2$, and the curve $y = x^2$ is not. Find all maximal simply ordered subsets.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.4, printed pp. 121--125** (`tmp/sources/munkres-solutions-whitman.pdf`); the classification and the verifications below are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §11 Exercise 4, printed pp. 71--72.

::: pf

::: {.pf-step #order}
$\prec$ is a strict partial order on $\RR^2$, and two points of $\RR^2$ are comparable exactly when their $x$-coordinates differ and the point with the smaller $x$-coordinate has the smaller-or-equal $y$-coordinate. In particular two points with equal $x$-coordinate are never comparable.

::: pf-proof
Irreflexivity is $x<x$ being false, and transitivity is the conjunction of $x_0<x_1<x_2$ and $y_0\le y_1\le y_2$. Since the order on $\RR$ is simple, for points with $x_0\ne x_1$ exactly one of $x_0<x_1$, $x_1<x_0$ holds, and comparability is then decided by the corresponding inequality between the $y$-coordinates; for $x_0=x_1$ neither conjunct can hold.
:::

:::

::: {.pf-step #cubic}
The curve $y=x^3$ is a maximal simply ordered subset of $\RR^2$ under $\prec$.

::: pf-proof
For $u<v$ one has $u<v$ and $u^3<v^3$, so the curve is simply ordered by step [](#order){.pf-ref}. If $(x,y)$ is a point off the curve, then $(x,x^3)$ lies on it and has the same $x$-coordinate as $(x,y)$, so the two are incomparable by step [](#order){.pf-ref}; hence no proper superset of the curve is simply ordered.
:::

:::

::: {.pf-step #horizontal}
The line $y=2$ is a maximal simply ordered subset of $\RR^2$.

::: pf-proof
For $u<v$ the points $(u,2)$ and $(v,2)$ satisfy $u<v$ and $2\le2$, so the line is simply ordered. A point $(x,y)$ with $y\ne2$ is incomparable with $(x,2)$, which lies on the line, because the two share their $x$-coordinate; so no proper superset is simply ordered.
:::

:::

::: {.pf-step #parabola}
The curve $y=x^2$ is not a simply ordered subset.

::: pf-proof
The points $(-1,1)$ and $(0,0)$ both lie on the curve. The first has the smaller $x$-coordinate but the larger $y$-coordinate, since $1>0$, so the pair violates the comparability condition of step [](#order){.pf-ref}; and the reverse comparison fails because $0<-1$ is false. Hence the curve is not simply ordered, and in particular not maximal.
:::

:::

::: {.pf-step #classification}
A subset of $\RR^2$ is a maximal simply ordered subset if and only if it is
$$
A_f=\{(x,f(x))\mid x\in(a,b)\}
$$
for a non-decreasing $f:(a,b)\to\RR$ on an open interval $-\infty\le a<b\le+\infty$ that is unbounded above when $b<+\infty$ and unbounded below when $a>-\infty$.

::: pf-proof

::: {.pf-step #graphs-are-maximal}
Every such $A_f$ is maximal simply ordered.

::: pf-proof
$A_f$ is simply ordered because $f$ is non-decreasing. Let $(x,y)\notin A_f$. If $a<x<b$ then $y\ne f(x)$ and $(x,f(x))\in A_f$ shares the $x$-coordinate with $(x,y)$, so the two are incomparable. If $b<+\infty$ and $x\ge b$, choose $t\in(a,b)$ with $f(t)>y$, which the unboundedness above provides; then $t<x$, so $(t,f(t))\prec(x,y)$ would need $f(t)\le y$, which fails, and $(x,y)\prec(t,f(t))$ would need $x<t$, which fails: the two are incomparable. If $a>-\infty$ and $x\le a$, choose $t\in(a,b)$ with $f(t)<y$; then $(x,y)\prec(t,f(t))$ would need $y\le f(t)$, which fails, and the reverse comparison needs $t<x$, which fails. So every point outside $A_f$ is incomparable with a point of $A_f$, and $A_f$ is maximal.
:::

:::

::: {.pf-step #maximal-is-graph}
Every maximal simply ordered subset of $\RR^2$ is some $A_f$.

::: pf-proof
Let $B$ be maximal simply ordered. Distinct points of $B$ have distinct $x$-coordinates by step [](#order){.pf-ref}, so $B$ is the graph of a function $f$ on its domain $D=\{x\mid (x,y)\in B\text{ for some }y\}$. The domain is an interval: if $x_1<x<x_2$ with $x_i\in D$, then $(x,f(x_1))$ is comparable with every $(t,f(t))\in B$ — for $t\le x_1$ we have $t<x$ and $f(t)\le f(x_1)$ because $B$ is simply ordered, for $x_1<t<x$ we have $t<x$ and $f(t)\le f(x_1)$ likewise, and for $x\le t$ we have $x<t$ and $f(x_1)\le f(t)$ — so by maximality $(x,f(x_1))\in B$ and $x\in D$. On $D$ the function $f$ is non-decreasing, since $x<x'$ with $x,x'\in D$ makes $(x,f(x))$ and $(x',f(x'))$ comparable, which gives $f(x)\le f(x')$. If $D$ had a least element $a>-\infty$, then $(a-1,f(a)-1)$ would be comparable with every point of $B$, because $a-1<t$ and $f(a)-1<f(a)\le f(t)$ for every $t\in D$; maximality would put it in $B$ with first coordinate outside $D$, which is impossible. So $D$ has no least element, and symmetrically no greatest element; being an interval, $D$ is then an open interval $(a,b)$ with $-\infty\le a<b\le+\infty$. Finally, if $b<+\infty$ and $f$ were bounded above by $M$, then $(b,M+1)$ would be comparable with every point of $B$, since $t<b$ and $f(t)\le M<M+1$ for $t\in D$, and maximality would put it in $B$ with first coordinate $b\notin D$; so $f$ is unbounded above when $b<+\infty$, and symmetrically unbounded below when $a>-\infty$. Hence $B=A_f$ for such an $f$.
:::

:::

Steps [](#graphs-are-maximal){.pf-ref} and [](#maximal-is-graph){.pf-ref} give the two implications, so the maximal simply ordered subsets are exactly the sets $A_f$ described in the claim; this is the classification the exercise asks for.
:::

:::

:::
:::
