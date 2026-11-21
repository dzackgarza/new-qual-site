---
schema: qual/card@1
id: P-CAF13H
kind: problem
title: "Normal family of holomorphic functions with positive real part and bounded evaluation"
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
    Restructured the prose solution into a Lamport proof and checked it: 1/(f+1) is
    holomorphic with modulus below 1 because Re(f+1) > 1, so Montel applies; the base
    point bound 1/(M+1) keeps the limit from vanishing; Hurwitz (with the counting
    argument written out) makes the limit zero-free; and the reciprocal limit is uniform
    on compacts because the zero-free limit is bounded away from 0 there. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Let $U \subseteq \CC$ be a domain, and let $z_0 \in U$.
For $M > 0$, define $\mathcal{F}_M$ to be the family of functions in $\operatorname{Hol}(U)$ with the properties that $$\abs{f(z_0)} \leq M, \qquad \operatorname{Re} f(z) > 0 \;\forall z \in U.$$ Show that $\mathcal{F}_M$ is a normal family: i.e.\ it is relatively compact in the topology of uniform convergence on compact subsets of $U$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Throughout, $\mathcal F_M$ is the stated family and $h_f\coloneqq\frac{1}{f+1}$ for $f\in\mathcal F_M$.

::: pf

::: {.pf-step #reciprocal}
For every $f\in\mathcal F_M$ the function $h_f=\frac{1}{f+1}$ is holomorphic on $U$ and satisfies $\abs{h_f(z)}<1$ for all $z\in U$.

::: pf-proof
$f$ is holomorphic and $f+1$ never vanishes, because $\operatorname{Re}(f(z)+1)>1>0$; so $h_f$ is holomorphic. Also $\abs{\zeta}\ge\operatorname{Re}\zeta$ for every complex $\zeta$, so $\abs{f(z)+1}\ge\operatorname{Re}(f(z)+1)>1$ and hence $\abs{h_f(z)}<1$.
:::

:::

::: {.pf-step #normal}
The family $\{h_f:f\in\mathcal F_M\}$ is normal in $U$.

::: pf-proof
By step [](#reciprocal){.pf-ref} the family is uniformly bounded on $U$ by $1$; a uniformly bounded family of holomorphic functions is locally bounded, and Montel's theorem makes a locally bounded family of holomorphic functions on the domain $U$ normal.
:::

:::

::: {.pf-step #basepoint}
$\abs{h_f(z_0)}\ge\frac{1}{M+1}$ for every $f\in\mathcal F_M$.

::: pf-proof
By the triangle inequality and $\abs{f(z_0)}\le M$,
$$
\abs{h_f(z_0)}=\frac{1}{\abs{f(z_0)+1}}\ge\frac{1}{\abs{f(z_0)}+1}\ge\frac{1}{M+1}.
$$
:::

:::

::: {.pf-step #limit-zero-free}
If $f_n\in\mathcal F_M$ and $h_{f_n}\to h$ uniformly on compact subsets of $U$, then $h$ is holomorphic, not identically zero, and zero-free on $U$.

::: pf-proof

::: {.pf-step #nonzero-limit}
$h$ is holomorphic on $U$ and $h\not\equiv0$.

::: pf-proof
A locally uniform limit of holomorphic functions is holomorphic. At the base point, step [](#basepoint){.pf-ref} gives $\abs{h_{f_n}(z_0)}\ge\frac{1}{M+1}$ for every $n$, so by continuity of evaluation at the point $z_0$ and convergence there, $\abs{h(z_0)}\ge\frac{1}{M+1}>0$; in particular $h$ is not the zero function.
:::

:::

::: {.pf-step #zero-free}
$h$ has no zeros in $U$.

::: pf-proof
Each $h_{f_n}$ is holomorphic and zero-free, since $h_{f_n}$ is the reciprocal of $f_n+1$, and $h_{f_n}\to h$ locally uniformly with $h\not\equiv0$ by step [](#nonzero-limit){.pf-ref}. Hurwitz's theorem then forces $h$ to be zero-free: if $h$ had a zero of order $m\ge1$ at a point $z_1\in U$, then for all large $n$ the function $h_{f_n}$ would have exactly $m$ zeros in a small disc about $z_1$, contradicting that $h_{f_n}$ has none.
:::

:::

:::

:::

::: {.pf-step #quotient-limit}
In the situation of step [](#limit-zero-free){.pf-ref}, $\frac{1}{h_{f_n}}\to\frac{1}{h}$ uniformly on compact subsets of $U$.

::: pf-proof
Let $K\subset U$ be compact. Since $h$ is continuous and zero-free on $K$, the number $\delta\coloneqq\min_{z\in K}\abs{h(z)}$ is positive. For all large $n$ one has $\abs{h_{f_n}-h}\le\delta/2$ on $K$, hence $\abs{h_{f_n}}\ge\delta/2$ there, and therefore
$$
\abs{\frac{1}{h_{f_n}}-\frac{1}{h}}=\frac{\abs{h-h_{f_n}}}{\abs{h_{f_n}}\abs{h}}\le\frac{2}{\delta^2}\abs{h-h_{f_n}}\longrightarrow0
$$
uniformly on $K$.
:::

:::

::: {.pf-step}
$\mathcal F_M$ is a normal family: every sequence in $\mathcal F_M$ has a subsequence converging uniformly on compact subsets of $U$ to a holomorphic function.

::: pf-proof
Let $f_n\in\mathcal F_M$. By step [](#normal){.pf-ref} the sequence $h_{f_n}$ has a subsequence converging uniformly on compact subsets to a holomorphic $h$; relabel it. By step [](#limit-zero-free){.pf-ref} that $h$ is holomorphic and zero-free, so by step [](#quotient-limit){.pf-ref} the functions
$$
f_n=\frac{1}{h_{f_n}}-1
$$
converge uniformly on compact subsets to $\frac1h-1$, which is holomorphic on $U$. Hence every sequence in $\mathcal F_M$ has a locally uniformly convergent subsequence with holomorphic limit, which is relative compactness of $\mathcal F_M$ in the compact-open topology.
:::

:::

:::
:::
