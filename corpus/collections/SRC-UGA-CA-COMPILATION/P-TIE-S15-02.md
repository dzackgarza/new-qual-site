---
schema: qual/card@1
id: P-TIE-S15-02
kind: problem
title: Locally uniform convergence of analytic functions via $L^1$ convergence on circles
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 2.
---

::: {.problem}
Let $f _ { n } , f$ be analytic functions on the unit disk D. Show that the following are equivalent.

(i) $f _ { n } ( z )$ converges to f(z) uniformly on compact subsets in D.

(ii) $\int _ { \abs{ z } = r } \abs{ f _ { n } ( z ) - f ( z ) } \abs{ d z }$ converges to 0 if $0 < r < 1$
:::

::: {.solution}

Set
$$
h_n\coloneqq f_n-f.
$$

::: pf

::: {.pf-step #s1-1}

Condition (i) implies condition (ii).


::: pf-proof

Fix $0<r<1$. The circle
$$
C_r\coloneqq\{z:\abs{z}=r\}
$$
is a compact subset of the unit disk. By condition (i),
$$
\sup_{\abs{z}=r}\abs{h_n(z)}
\longrightarrow0.
$$
Hence
$$
\begin{aligned}
\int_{\abs{z}=r}\abs{h_n(z)}\,\abs{dz}
&\le
2\pi r
\sup_{\abs{z}=r}\abs{h_n(z)}
\longrightarrow0.
\end{aligned}
$$
Thus condition (ii) holds.

:::

:::

::: {.pf-step #s1-2}

Assume condition (ii). Let $0<\rho<r<1$. Then
$$
\sup_{\abs{z}\le\rho}\abs{h_n(z)}
\le
\frac1{2\pi(r-\rho)}
\int_{\abs{\zeta}=r}
\abs{h_n(\zeta)}\,\abs{d\zeta}.
$$


::: pf-proof

For $\abs{z}\le\rho$, Cauchy's integral formula on the circle $\abs{\zeta}=r$ gives
$$
h_n(z)
=
\frac1{2\pi i}
\int_{\abs{\zeta}=r}
\frac{h_n(\zeta)}{\zeta-z}\,d\zeta.
$$
Since
$$
\abs{\zeta-z}
\ge
\abs{\zeta}-\abs{z}
\ge
r-\rho,
$$
one obtains
$$
\abs{h_n(z)}
\le
\frac1{2\pi(r-\rho)}
\int_{\abs{\zeta}=r}
\abs{h_n(\zeta)}\,\abs{d\zeta}.
$$
The right-hand side is independent of $z$, so taking the supremum over $\abs{z}\le\rho$ gives the stated estimate.

:::

:::

::: {.pf-step #s1-3}

Condition (ii) implies uniform convergence on every closed disk $\abs{z}\le\rho<1$.


::: pf-proof

Fix $\rho<1$ and choose $r$ with
$$
\rho<r<1.
$$
By condition (ii),
$$
\int_{\abs{\zeta}=r}
\abs{h_n(\zeta)}\,\abs{d\zeta}
\longrightarrow0.
$$
Step [](#s1-2){.pf-ref} therefore gives
$$
\sup_{\abs{z}\le\rho}\abs{h_n(z)}
\longrightarrow0.
$$
Since $h_n=f_n-f$, this is uniform convergence of $f_n$ to $f$ on the closed disk.

:::

:::

::: {.pf-step #s1-4}

Condition (ii) implies condition (i).


::: pf-proof

Let $K$ be any compact subset of the unit disk. Then
$$
\rho\coloneqq\max_{z\in K}\abs{z}<1.
$$
Thus
$$
K\subset\{z:\abs{z}\le\rho\}.
$$
Step [](#s1-3){.pf-ref} gives uniform convergence on that closed disk, hence on $K$. Therefore condition (i) holds.

:::

:::

::: {.pf-step #s1-5}

The two conditions are equivalent.


::: pf-proof

Step [](#s1-1){.pf-ref} proves (i)$\Rightarrow$(ii), and step [](#s1-4){.pf-ref} proves (ii)$\Rightarrow$(i).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required equivalence.

:::

:::

:::
