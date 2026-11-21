---
schema: qual/card@1
id: P-CAFA25E
kind: problem
title: 'If $\theset{f(nz)}$ is a normal family on an annulus, then $f$ is constant'
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Entire Functions
  - Montel
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function, and define $f_n(z) = f(nz)$.
Suppose that $\mathcal{F} = \{f_n : n \geq 1\}$ is a normal family on the annulus $\{1 < \abs{z} < 2\}$.
Show that $f$ is constant.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Laurent-coefficient argument follows, with the subsequence, the coefficient limits and the vanishing of the higher coefficients as separate steps.

Let $f(w)=\sum_{m\ge0}a_{m}w^{m}$ be entire, $f_{n}(z)=f(nz)$ and $A=\theset{1<\abs{z}<2}$.

::: pf

::: {.pf-step #subsequence}
Normality gives a strictly increasing sequence $n_{j}$ and a holomorphic $g$ on $A$ with $f_{n_{j}}\to g$ uniformly on compact subsets of $A$.

::: pf-proof
A normal family is one from which every sequence has a subsequence converging uniformly on compact subsets of the domain to a holomorphic limit; apply this to the sequence $(f_{n})$, and pass to a further subsequence if necessary so that $n_{j}$ increases.
:::

:::

::: {.pf-step #coefficients}
Writing $g(z)=\sum_{m\in\ZZ}b_{m}z^{m}$ on the annulus, one has $a_{m}n_{j}^{m}\to b_{m}$ for $m\ge0$ and $b_{m}=0$ for $m<0$.

::: pf-proof
Fix $r$ with $1<r<2$. On the circle $\abs{z}=r$, inside $A$, the functions $f_{n_{j}}$ converge uniformly to $g$, hence in $L^{2}$ of the circle. The Laurent coefficient functional $h\mapsto\frac{1}{2\pi i}\oint_{\abs{z}=r}h(z)z^{-m-1}dz$ is continuous for uniform convergence, so the coefficients converge: for $m\ge0$ the coefficient of $z^{m}$ in $f_{n_{j}}$ is $a_{m}n_{j}^{m}$ because $f_{n_{j}}$ is entire, so $a_{m}n_{j}^{m}\to b_{m}$; for $m<0$ that coefficient is $0$, so $b_{m}=0$.
:::

:::

::: {.pf-step #vanish}
$a_{m}=0$ for every $m\ge1$.

::: pf-proof
Fix $m\ge1$. By step [](#coefficients){.pf-ref} the numbers $a_{m}n_{j}^{m}$ converge, hence are bounded, say by $C$; but $n_{j}^{m}\to\infty$ because $n_{j}$ is strictly increasing. So $\abs{a_{m}}\le Cn_{j}^{-m}\to0$, giving $a_{m}=0$.
:::

:::

::: {.pf-qed}
All Taylor coefficients of $f$ of positive order vanish by step [](#vanish){.pf-ref}, so $f=a_{0}$ is constant.
:::

:::

:::
