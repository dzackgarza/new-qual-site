---
schema: qual/card@1
id: P-CAF05D
kind: problem
title: "Using Runge-type approximation to separate values outside a compact set"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the
    reciprocal is analytic on the open complement of z_0 because the compact K is
    closed and misses z_0; M is a positive maximum by compactness; h = (z - z_0)g - 1
    is holomorphic on G with h(z_0) = -1 and |h| <= M*eps < 1 on K. Added the empty
    K case, which the prose did not cover and which the stated conclusion needs.
    The collection's provenance is the examination paper only, so no retained
    solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Let $K \subset G \subset \CC$ with $K$ compact and $G$ open.
Suppose that for any $f$ analytic in an open neighborhood of $K$ and any $\epsilon > 0$ there is $g \in H(G)$ so that $\abs{f(z) - g(z)} < \epsilon$ for all $z \in K$.
Let $z_0 \in G \setminus K$ be arbitrary.
Show that there exists $h \in H(G)$ such that $$\abs{h(z_0)} > \sup_{w \in K} \abs{h(w)}.$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step}
It suffices to treat nonempty $K$, since for $K=\emptyset$ the constant function $h\equiv1$ gives $\abs{h(z_0)}=1>0=\sup_{w\in\emptyset}\abs{h(w)}$.

::: pf-proof
$z_0\in G\setminus K$ and $h\equiv1$ is holomorphic on $G$.
:::

:::

::: {.pf-step #reciprocal}
$f(z)\coloneqq\frac{1}{z-z_0}$ is analytic on an open neighbourhood of $K$.

::: pf-proof
$K$ is compact, hence closed, and $z_0\notin K$, so $z_0$ lies in the open set $\CC\setminus K$; thus $K$ is contained in the open set $\CC\setminus\{z_0\}$, on which $f$ is analytic.
:::

:::

::: {.pf-step #bound}
$M\coloneqq\max_{w\in K}\abs{w-z_0}$ is finite and positive.

::: pf-proof
$w\mapsto\abs{w-z_0}$ is continuous and $K$ is compact and nonempty, so the maximum is attained. It is positive because $z_0\notin K$, so no point of $K$ is $z_0$.
:::

:::

::: {.pf-step #approximant}
There is $g\in H(G)$ with
$$
\abs{g(w)-\frac{1}{w-z_0}}<\varepsilon\qquad(w\in K)
$$
for a chosen $\varepsilon$ with $0<\varepsilon<1/M$.

::: pf-proof
Such an $\varepsilon$ exists because $M>0$ by step [](#bound){.pf-ref}. The approximation hypothesis applied to the function $f$ of step [](#reciprocal){.pf-ref}, which is analytic on an open neighbourhood of $K$, produces $g\in H(G)$ with this property.
:::

:::

::: {.pf-step #constructed}
For $h(z)\coloneqq(z-z_0)g(z)-1$ one has $h\in H(G)$, $h(z_0)=-1$, and $\abs{h(w)}\le M\varepsilon<1$ for every $w\in K$.

::: pf-proof
$z\mapsto z-z_0$ and $g$ are holomorphic on $G$, so $h$ is. At $z_0$ the product $(z_0-z_0)g(z_0)$ vanishes, so $h(z_0)=-1$. For $w\in K$,
$$
h(w)=(w-z_0)g(w)-1=(w-z_0)\left(g(w)-\frac{1}{w-z_0}\right),
$$
so by step [](#approximant){.pf-ref} and the definition of $M$,
$$
\abs{h(w)}=\abs{w-z_0}\abs{g(w)-\frac{1}{w-z_0}}\le M\varepsilon<1.
$$
:::

:::

::: {.pf-step}
$\abs{h(z_0)}>\sup_{w\in K}\abs{h(w)}$.

::: pf-proof
$\abs{h(z_0)}=1$ by step [](#constructed){.pf-ref}, and that step bounds $\abs{h}$ by $M\varepsilon<1$ on all of $K$, so $\sup_{w\in K}\abs{h(w)}\le M\varepsilon<1$.
:::

:::

:::

:::
