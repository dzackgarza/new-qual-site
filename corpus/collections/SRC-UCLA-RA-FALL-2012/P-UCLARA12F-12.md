---
schema: qual/card@1
id: P-UCLARA12F-12
kind: problem
title: Maximum principle with finitely many exceptional boundary points
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $M\in\RR$, let $\Omega\subset\CC$ be a bounded open set, and let $u:\Omega\to\RR$ be harmonic.

(a) Show that if
$$
\limsup_{z\to z_0}u(z)\le M
$$
for every $z_0\in\partial\Omega$, then $u(z)\le M$ for every $z\in\Omega$.

(b) Show that if $u$ is bounded above and the condition in part (a) holds for all but finitely many $z_0\in\partial\Omega$, then still $u(z)\le M$ for every $z\in\Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the hypotheses of part (a), for every $\varepsilon>0$ there is an open neighborhood $U$ of $\partial\Omega$ such that
$$
u(z)\le M+\varepsilon
$$
for every $z\in U\cap\Omega$.


::: pf-proof

Fix $\varepsilon>0$. For each $z_0\in\partial\Omega$, the assumption
$$
\limsup_{z\to z_0}u(z)\le M
$$
gives a neighborhood $U_{z_0}$ of $z_0$ such that
$$
u(z)<M+\varepsilon
$$
for $z\in U_{z_0}\cap\Omega$ sufficiently close to $z_0$. The boundary $\partial\Omega$ is compact because $\Omega$ is bounded, so finitely many of these neighborhoods cover it. Their union is the required $U$.

:::

:::

::: {.pf-step #s1-2}

Under the hypotheses of part (a), one has
$$
u(z)\le M+\varepsilon
$$
for every $z\in\Omega$ and every $\varepsilon>0$.


::: pf-proof

Suppose the superlevel set
$$
E_\varepsilon\coloneqq\{z\in\Omega:u(z)>M+\varepsilon\}
$$
were nonempty. By step [](#s1-1){.pf-ref}, its closure is disjoint from a neighborhood of $\partial\Omega$, hence is compactly contained in $\Omega$.

Let $D$ be a connected component of $E_\varepsilon$. Then $u$ is harmonic on $D$, continuous on $\overline D$, and
$$
u=M+\varepsilon
$$
on $\partial D$ by continuity. Since $\overline D$ is compact, $u$ attains its maximum there. The maximum is strictly larger than $M+\varepsilon$ because $D\subset E_\varepsilon$, so it is attained at an interior point of $D$. The maximum principle then forces $u$ to be constant on $D$, contradicting the boundary value $M+\varepsilon$. Thus $E_\varepsilon$ is empty.

:::

:::

::: {.pf-step #s1-3}

Part (a) follows:
$$
\boxed{u(z)\le M\qquad(z\in\Omega).}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives $u(z)\le M+\varepsilon$ for every $\varepsilon>0$. Let $\varepsilon\downarrow0$.

:::

:::

::: {.pf-step #s1-4}

For part (b), let $p_1,\ldots,p_N$ be the exceptional boundary points. Choose $d>0$ so large that
$$
|z-p_j|<d
$$
for every $z\in\Omega$ and every $j$, and define
$$
v(z)
\coloneqq
-\sum_{j=1}^N
\log\frac{|z-p_j|}{d}.
$$
Then $v$ is harmonic and nonnegative on $\Omega$, and
$$
v(z)\to+\infty
$$
as $z\to p_j$ from within $\Omega$.


::: pf-proof

Each point $p_j$ lies on $\partial\Omega$, hence outside $\Omega$. Therefore $z\mapsto\log|z-p_j|$ is harmonic on $\Omega$. By the choice of $d$,
$$
0<\frac{|z-p_j|}{d}<1,
$$
so each summand is nonnegative. As $z\to p_j$, the corresponding logarithm tends to $-\infty$, hence the negative logarithm tends to $+\infty$.

:::

:::

::: {.pf-step #s1-5}

For every $\eta>0$, the harmonic function
$$
u_\eta\coloneqq u-\eta v
$$
satisfies the boundary hypothesis of part (a) with the same constant $M$ at every point of $\partial\Omega$.


::: pf-proof

At a nonexceptional boundary point $z_0$, one has $v\ge0$, so
$$
\limsup_{z\to z_0}u_\eta(z)
\le
\limsup_{z\to z_0}u(z)
\le M.
$$

At an exceptional point $p_j$, the function $u$ is bounded above by hypothesis while $v(z)\to+\infty$ by step [](#s1-4){.pf-ref}. Hence
$$
u_\eta(z)=u(z)-\eta v(z)\to-\infty
$$
as $z\to p_j$, so the required limsup inequality also holds there.

:::

:::

::: {.pf-step #s1-6}

Under the hypotheses of part (b),
$$
\boxed{u(z)\le M\qquad(z\in\Omega).}
$$


::: pf-proof

Apply part (a), proved in step [](#s1-3){.pf-ref}, to $u_\eta$. Step [](#s1-5){.pf-ref} gives
$$
u(z)-\eta v(z)\le M
$$
for every $z\in\Omega$ and every $\eta>0$. For fixed $z$, the number $v(z)$ is finite. Letting $\eta\downarrow0$ gives $u(z)\le M$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
