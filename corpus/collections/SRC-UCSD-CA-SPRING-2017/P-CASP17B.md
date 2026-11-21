---
schema: qual/card@1
id: P-CASP17B
kind: problem
title: 'An entire function with $f(z)f(1/z)$ bounded is a monomial'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same argument. The step that the prose compressed is the
    growth estimate: it is now derived from the bound on g with the lower bound |h(z)| >= |h(0)|/2 near 0,
    which is what converts boundedness of g into |f(w)| <= C|w|^m for large |w|. Cauchy's estimate is then
    applied at each k > m with R tending to infinity, which is the step that forces the coefficient to
    vanish, and the order of the zero at 0 is used in the last step to exclude lower-degree terms. No
    published solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $f : \CC \to \CC$ be entire.
Assume that the function $g(z) = f(z) \cdot f\!\left(\frac{1}{z}\right)$ is bounded on $\CC \setminus \{0\}$.
Show that $f(z) = cz^m$.
:::

::: {.solution}

No published solution was located for this examination problem; the argument is the card's own, and it is the standard polynomial-growth argument: boundedness of $g$ near $0$ bounds the growth of $f$ at $\infty$, and Cauchy's estimates then kill every Taylor coefficient past the order of the zero at $0$.

The statement was checked against the Spring 2017 complex-analysis examination collection holding this card. Throughout $f$ is entire, $g(z)\coloneqq f(z)f(1/z)$ is defined on $\CC-\theset{0}$ and bounded there, and $m\coloneqq\operatorname{ord}_{0}(f)$ is the order of the zero of $f$ at $0$, so that $f(z)=z^{m}h(z)$ with $h$ entire and $h(0)\neq0$.

::: pf

::: {.pf-step #zero-case}

If $f\equiv0$ then the conclusion holds with $c\coloneqq0$.

::: pf-proof

The zero function is $0\cdot z^{m}$ for any $m\geq0$, so it has the required form.

:::

:::

::: {.pf-step #factorization}

Otherwise $f(z)=z^{m}h(z)$ with $h$ entire and $h(0)\neq0$, for $m\coloneqq\operatorname{ord}_{0}(f)\geq0$.

::: pf-proof

An entire function not identically zero has a zero of finite order $m$ at $0$ --- the order of vanishing of its power series there --- and factoring out $z^{m}$ leaves an entire $h$ with $h(0)\neq0$. If $f(0)\neq0$ then $m=0$ and $h=f$.

:::

:::

::: {.pf-step #growth}

There are constants $C$ and $R_{0}$ with $\abs{f(w)}\leq C\abs{w}^{m}$ for $\abs{w}>R_{0}$.

::: pf-proof

Let $M$ bound $\abs{g}$ on $\CC-\theset{0}$. Since $h(0)\neq0$ and $h$ is continuous, there is $\rho>0$ with $\abs{h(z)}\geq\abs{h(0)}/2$ for $\abs{z}<\rho$. For $0<\abs{z}<\rho$,
$$
M\geq\abs{g(z)}=\abs{z}^{m}\abs{h(z)}\abs{f(1/z)}\geq\frac{\abs{h(0)}}{2}\abs{z}^{m}\abs{f(1/z)},
$$
so $\abs{f(1/z)}\leq\frac{2M}{\abs{h(0)}}\abs{z}^{-m}$. Putting $w\coloneqq1/z$, for $\abs{w}>1/\rho$ this reads $\abs{f(w)}\leq C\abs{w}^{m}$ with $C\coloneqq2M/\abs{h(0)}$.

:::

:::

::: {.pf-step #polynomial}

$f^{(k)}(0)=0$ for every $k>m$, so $f$ is a polynomial of degree at most $m$.

::: pf-proof

Fix $k>m$ and let $R>1/\rho$. Cauchy's estimate on the circle $\abs{z}=R$ gives $\abs{f^{(k)}(0)}\leq k!\,M_{R}/R^{k}$, where $M_{R}\coloneqq\max_{\abs{z}=R}\abs{f}\leq CR^{m}$ by step [](#growth){.pf-ref}. Hence $\abs{f^{(k)}(0)}\leq k!\,C R^{m-k}$ for every $R>1/\rho$, and $m-k<0$, so the right-hand side tends to $0$ as $R\to\infty$; the left-hand side does not depend on $R$, so it is $0$. A Taylor series with coefficients vanishing past degree $m$ is a polynomial of degree at most $m$.

:::

:::

::: {.pf-step #conclusion}

$f(z)=cz^{m}$ for some constant $c$.

::: pf-proof

By step [](#polynomial){.pf-ref} the function $f$ is a polynomial of degree at most $m$, say $f(z)=\sum_{j=0}^{m}b_{j}z^{j}$. Its zero at $0$ has order exactly $m$, which means $b_{0}=\cdots=b_{m-1}=0$ and $b_{m}\neq0$; so $f(z)=b_{m}z^{m}$.

:::

:::

::: pf-step

Therefore $f(z)=cz^{m}$ for some constant $c$.

::: pf-proof

Steps [](#zero-case){.pf-ref} and [](#conclusion){.pf-ref} cover the two cases, $f$ identically zero and $f$ not; in both the required form holds, with $c=0$ in the first and $c=b_{m}\neq0$ in the second.

:::

:::

:::

:::
