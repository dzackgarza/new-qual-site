---
schema: qual/card@1
id: P-CAFA19E
kind: problem
title: "Runge approximation with restricted pole locations"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f = \frac{1}{(z-1)(z-5)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ whose poles can only occur at 2 and 6 such that $$\lim_{n \to \infty} \sup_{3 \leq \abs{z} \leq 4} \abs{f(z) - R_n(z)} = 0.$$

(b) Does there exist a sequence of rational functions $R_n(z)$ whose poles can only occur at 6 such that the above holds?
Justify your answer.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Runge argument for (a) and the contour argument for (b) follow, with the components, the approximation and the obstruction as separate steps.

Let $f(z)=\dfrac{1}{(z-1)(z-5)}$ and $K=\theset{3\le\abs{z}\le4}$.

::: pf

::: {.pf-step #components}
$\CC\setminus K$ has exactly two components, $\abs{z}<3$ and $\abs{z}>4$, containing $2$ and $6$ respectively; $f$ is holomorphic on an open neighbourhood of $K$.

::: pf-proof
$K$ is the closed annulus bounded by the circles of radii $3$ and $4$; its complement is the disjoint union of the open disc $\abs{z}<3$ and the open exterior $\abs{z}>4$, each connected and open. The poles of $f$ are $1$ and $5$, with $\abs{1}=1<3$ and $\abs{5}=5>4$; so $f$ is holomorphic on the annulus $\theset{3/2<\abs{z}<9/2}$, which contains $K$.
:::

:::

::: {.pf-step #part-a}
(a) There are rational functions $R_{n}$ with poles only at $2$ and $6$ such that $R_{n}\to f$ uniformly on $K$.

::: pf-proof
Each component of $\CC\setminus K$ meets the prescribed pole set: $2\in\theset{\abs{z}<3}$ and $6\in\theset{\abs{z}>4}$. Since $f$ is holomorphic on a neighbourhood of $K$ by step [](#components){.pf-ref}, Runge's theorem gives for every $\varepsilon>0$ a rational function $R$ with poles only at $2$ and $6$ and $\sup_{K}\abs{f-R}<\varepsilon$. Taking $\varepsilon=1/n$ gives the sequence $R_{n}$.
:::

:::

::: {.pf-step #part-b}
(b) No such sequence exists with poles only at $6$.

::: pf-proof
Suppose $R_{n}$ has all poles at $6$ and $R_{n}\to f$ uniformly on $K$. Let $\gamma$ be the circle $\abs{z-1}=\tfrac12$; it lies in the disc $\abs{z}<\tfrac32$, hence inside $\CC\setminus K$, and the point $6$ does not lie inside it since $\abs{6-1}=5>\tfrac12$. So every $R_{n}$ is holomorphic on and inside $\gamma$, giving $\int_{\gamma}R_{n}\,dz=0$ by Cauchy's theorem. Next, $f$ has its pole $z=1$ inside $\gamma$ and no other pole inside the disc $\abs{z}<3$, so $\int_{\gamma}f\,dz=2\pi i\operatorname{Res}_{z=1}f=2\pi i\cdot\frac{1}{1-5}=-\frac{\pi i}{2}\ne0$. Also, in the region between $\gamma$ and the circle $\abs{z}=3$ both $f$ and each $R_{n}$ are holomorphic (their poles $1,5$, respectively $6$, lie outside that region), so Cauchy's theorem applied twice gives $\int_{\gamma}f\,dz=\int_{\abs{z}=3}f\,dz$ and $\int_{\gamma}R_{n}\,dz=\int_{\abs{z}=3}R_{n}\,dz$. Finally $\abs{z}=3\subseteq K$ and $R_{n}\to f$ uniformly there, so $\int_{\abs{z}=3}R_{n}\,dz\to\int_{\abs{z}=3}f\,dz$, that is $\int_{\gamma}R_{n}dz\to\int_{\gamma}f\,dz$. This contradicts $0=\int_{\gamma}R_{n}dz$ for all $n$ and $\int_{\gamma}f\,dz=-\pi i/2\ne0$.
:::

:::

::: {.pf-qed}
Part (a) is step [](#part-a){.pf-ref}; part (b) is step [](#part-b){.pf-ref}, and it shows exactly where Runge's hypothesis bites: a pole must be available in each component of the complement of $K$, and the bounded component has no point of $\theset{6}$.
:::

:::

:::
