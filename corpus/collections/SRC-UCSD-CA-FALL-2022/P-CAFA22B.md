---
schema: qual/card@1
id: P-CAFA22B
kind: problem
title: The zero of $e^{tz} + z + 1$ in the left half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/FA22_COMPLEX_220ABC.pdf, Problem 2
    (10 points): "Let t < 1. Show that f(z) = e^{tz} + z + 1 has exactly one zero (counting
    multiplicities) in the left halfplane {z : Re z < 0}. Hint: Consider first Re z < eps for
    eps > 0." The card carries the printed hint in its own hint line and restricts t to
    0 <= t < 1, with the remark recording the printed defect for negative t.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Made explicit the Rouché comparison on
    the half-disc: |e^{tz}| <= e^{t eps} because t >= 0 and Re z < eps, and |z+1| >= R - 1 on the
    semicircle, so the inequality holds on the whole boundary for R large, and the count passes to
    the limit over R because every zero of the half-plane lies in some half-disc. The last step now
    argues the point the prose compressed: each half-plane Re z < eps contains exactly one zero,
    none lies on the imaginary axis, so the unique zero of the smaller half-plane is the unique zero
    of the larger one and has negative real part. The remark's counterexample for negative t was
    checked numerically at t = -1: z = -0.605 + 1.788i, -2.053 + 7.718i, -3.285 + 26.618i,
    -3.819 + 45.491i and -4.422 + 83.211i satisfy e^{-z} + z + 1 = 0 to machine precision, with
    their conjugates, and the family continues as the imaginary part grows. A first version of that
    sentence claimed a zero on the negative real axis, which is false: e^{-tX} > X - 1 for every real
    X when t < 0. No
    retained published solution covers this problem.
---

::: {.problem}
Let $0 \leq t < 1$.
Show that $f(z) = e^{tz} + z + 1$ has exactly one zero (counting multiplicities) in the left half-plane $\{z : \operatorname{Re} z < 0\}$.

Hint: Consider first $\operatorname{Re} z < \varepsilon$ for $\varepsilon > 0$.
:::

::: {.remark}
The official Fall 2022 source states only $t<1$. That is false for negative
$t$: for $t\ne0$, the equation is equivalent to
$$
-t(z+1)=W_k(te^{-t}),
$$
and for negative $t$ infinitely many branches give zeros in the left
half-plane. The hypothesis above records the intended nonnegative range.
:::

::: {.solution}
This is Problem 2 (10 points) of the UCSD complex-analysis qualifying exam of Fall 2022 (`assets/attachments/FA22_COMPLEX_220ABC.pdf`), whose hint is to consider $\operatorname{Re}z<\varepsilon$ first. No published solution set is transcribed: the argument is the card's own, by Rouché's theorem.

The paper prints the hypothesis as $t<1$ alone; the statement on this card restricts to $0\leq t<1$, and the remark below records why: for $t<0$ the equation has infinitely many zeros in the left half-plane, with $w=t(z+1)$ the equation is $we^{w}=te^{t}$, whose solutions are $w=W_{k}(te^{t})$ for the branches $W_{k}$ of the Lambert $W$ function, and for large $\abs{k}$ these have $\operatorname{Re}w\approx\log\abs{te^{t}}-\log(2\pi\abs{k})\to-\infty$ with $\operatorname{Im}w\approx2\pi k$, so $z=w/t-1$ has negative real part for every large $k$; for $t=-1$ the zeros include $z\approx-0.605+1.788i$, $-2.053+7.718i$, $-3.285+26.618i$, $-3.819+45.491i$ and $-4.422+83.211i$, with their conjugates.

::: pf

::: {.pf-step #epsilon}
For $0\leq t<1$ there is $\varepsilon>0$ with $e^{t\varepsilon}<1+\varepsilon$.

::: pf-proof
The function $\varphi(\varepsilon)=1+\varepsilon-e^{t\varepsilon}$ has $\varphi(0)=0$ and $\varphi'(0)=1-t>0$, so $\varphi>0$ on some interval $(0,\varepsilon_{0})$; take any $\varepsilon$ there. For $t=0$ the inequality reads $1<1+\varepsilon$, true for every $\varepsilon>0$.
:::
:::

::: {.pf-step #boundary}
On the line $\operatorname{Re}z=\varepsilon$ one has $\abs{e^{tz}}<\abs{z+1}$.

::: pf-proof
Write $z=\varepsilon+iy$. Since $t\geq0$, $\abs{e^{tz}}=e^{t\varepsilon}<1+\varepsilon$ by step [](#epsilon){.pf-ref}, while $\abs{z+1}\geq\operatorname{Re}(z+1)=1+\varepsilon$.
:::
:::

::: {.pf-step #rouche}
$f(z)=e^{tz}+z+1$ has exactly one zero in the half-plane $\operatorname{Re}z<\varepsilon$, counted with multiplicity.

::: pf-proof
Let $D_{R}$ be the half-disc $\theset{\operatorname{Re}z<\varepsilon,\ \abs{z}<R}$ for $R>2$, whose boundary is the vertical segment and the semicircle. On the semicircle $\abs{z}=R\geq R-1\geq1$ and $\abs{z+1}\geq R-1$, while $\abs{e^{tz}}=e^{t\operatorname{Re}z}\leq e^{t\varepsilon}$ because $t\geq0$ and $\operatorname{Re}z<\varepsilon$; so for $R$ large, $\abs{e^{tz}}<\abs{z+1}$ there, and the inequality holds on the vertical segment by step [](#boundary){.pf-ref}. Rouché's theorem on $D_{R}$ gives that $e^{tz}+z+1$ and $z+1$ have the same number of zeros in $D_{R}$, namely one, for every such $R$; letting $R\to\infty$ gives exactly one zero in the half-plane, since every zero there lies in some $D_{R}$.
:::
:::

::: {.pf-step #axis}
$f$ has no zeros on the imaginary axis.

::: pf-proof
If $f(iy)=e^{ity}+iy+1=0$ then $\abs{1+iy}=\abs{e^{ity}}=1$, so $1+y^{2}=1$ and $y=0$; but $f(0)=2\neq0$. Hence no point of the imaginary axis is a zero.
:::
:::

::: {.pf-step #left}
The unique zero of $f$ in $\operatorname{Re}z<\varepsilon$ lies in $\operatorname{Re}z<0$, so $f$ has exactly one zero in the left half-plane, counted with multiplicity.

::: pf-proof
Let $Z$ be the set of zeros of $f$, a discrete subset of $\CC$. Step [](#rouche){.pf-ref} says that for every $\varepsilon>0$ the set $Z\cap\theset{\operatorname{Re}z<\varepsilon}$ has exactly one element, counted with multiplicity. If that element $z_{\varepsilon}$ had $\operatorname{Re}z_{\varepsilon}\geq0$, then, since $z_{\varepsilon}$ is not on the imaginary axis by step [](#axis){.pf-ref}, one would have $\operatorname{Re}z_{\varepsilon}=\delta>0$, and for $0<\varepsilon'<\delta$ the unique zero in $\operatorname{Re}z<\varepsilon'$ would be the same point $z_{\varepsilon'}=z_{\varepsilon}$, which does not lie in that half-plane; the contradiction shows $\operatorname{Re}z_{\varepsilon}<0$. So the single zero in each half-plane $\operatorname{Re}z<\varepsilon$ is a left-half-plane zero, and it is the only one, since any left-half-plane zero lies in $\operatorname{Re}z<\varepsilon$.
:::
:::
:::

:::
