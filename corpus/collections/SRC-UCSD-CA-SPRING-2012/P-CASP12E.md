---
schema: qual/card@1
id: P-CASP12E
kind: problem
title: "Boundary behavior of the Poisson integral on arcs of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $f(e^{it})$ be a piecewise continuous, real-valued function on $\circlegroup$, and consider the harmonic function in the unit disk $\DD$ given by $$u(z) := \frac{1}{2\pi}\int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it})\,dt,$$ where $P_r(\theta)$ denotes the Poisson kernel and $z = re^{i\theta}$.
Suppose that $A \subset \circlegroup$ is an open sub-arc on which $f$ is continuous.
Show that $$\lim_{z \to a} u(z) = f(a)$$ for every $a = e^{i\theta} \in A$.
:::

::: {.solution}

The argument is the card's own, splitting the Poisson integral into an arc of continuity and its complement; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f$ be piecewise continuous and real valued on the unit circle $\circlegroup$ and continuous on an open sub-arc $A$; for $z=re^{i\theta}$ put
$$
u(z)=\frac{1}{2\pi}\int_{-\pi}^{\pi}P_{r}(\theta-t)f(e^{it})\,dt,\qquad P_{r}(\varphi)=\frac{1-r^{2}}{1-2r\cos\varphi+r^{2}}.
$$

::: pf

::: {.pf-step #identity}
$\displaystyle u(z)-f(a)=\frac{1}{2\pi}\int_{-\pi}^{\pi}P_{r}(\theta-t)\big(f(e^{it})-f(a)\big)\,dt$ for every $z=re^{i\theta}$ and every $a\in\circlegroup$.

::: pf-proof
$P_{r}\ge0$ and $\frac{1}{2\pi}\int_{-\pi}^{\pi}P_{r}(\theta-t)\,dt=1$ for $0\le r<1$, since the Poisson kernel is the real part of the Poisson–Cauchy kernel and its integral is normalised to $2\pi$. Multiplying $f(a)$ by that identity and subtracting from the definition of $u(z)$ gives the display.
:::

:::

::: {.pf-step #small-arc}
For every $\varepsilon>0$ there is an open arc $J_{0}$ about $a$ with $\abs{f(e^{it})-f(a)}<\varepsilon$ on $J_{0}$ and $\displaystyle\abs{\frac{1}{2\pi}\int_{J_{0}}P_{r}(\theta-t)\big(f(e^{it})-f(a)\big)dt}\le\varepsilon$ for all $r<1$ and all $\theta$.

::: pf-proof
$A$ is open and $a\in A$, so there is a closed arc $J$ whose interior contains $a$ and which is contained in $A$; the half-width of $J$ is some $\eta>0$. Continuity of $f$ at $a$ along the circle gives an open arc $J_{0}$ about $a$, of half-width $0<\eta_{0}<\eta$, with $\abs{f(e^{it})-f(a)}<\varepsilon$ there. Then, $P_{r}\ge0$ and the total integral of $P_{r}$ being $2\pi$,
$$
\abs{\int_{J_{0}}P_{r}(\theta-t)\big(f(e^{it})-f(a)\big)dt}\le\varepsilon\int_{J_{0}}P_{r}(\theta-t)\,dt\le2\pi\varepsilon .
$$
:::

:::

::: {.pf-step #complement}
If $z_{n}=r_{n}e^{i\theta_{n}}\to a=e^{i\theta_{0}}$ with $r_{n}<1$, then $\displaystyle\int_{\circlegroup\setminus J_{0}}P_{r_{n}}(\theta_{n}-t)\big(f(e^{it})-f(a)\big)dt\longrightarrow0$.

::: pf-proof
$f$ is bounded on the circle by some $M$, being piecewise continuous there, so $\abs{f(e^{it})-f(a)}\le2M$ for all $t$. Since $J_{0}$ is an arc of half-width $\eta_{0}$ about $\theta_{0}$ and $\theta_{n}\to\theta_{0}$, for all large $n$ and all $t\notin J_{0}$ one has $\abs{\theta_{n}-t}\ge\eta_{0}/2=:\eta'$ (modulo $2\pi$), a fixed positive angular distance. On that range
$$
0\le P_{r_{n}}(\theta_{n}-t)=\frac{1-r_{n}^{2}}{1-2r_{n}\cos(\theta_{n}-t)+r_{n}^{2}}\le\frac{1-r_{n}^{2}}{1-2r_{n}\cos\eta'+r_{n}^{2}}\longrightarrow0,
$$
the denominator tending to $2(1-\cos\eta')>0$ as $r_{n}\to1$. Hence the integral is bounded by $2M\cdot2\pi\cdot\sup_{t\notin J_{0}}P_{r_{n}}(\theta_{n}-t)\to0$.
:::

:::

::: {.pf-step #limit}
$\displaystyle\lim_{z\to a}u(z)=f(a)$ for every $a\in A$.

::: pf-proof
Let $\varepsilon>0$ and take $J_{0}$ as in step [](#small-arc){.pf-ref}. By steps [](#identity){.pf-ref} and [](#small-arc){.pf-ref},
$$
\abs{u(z)-f(a)}\le\varepsilon+\abs{\frac{1}{2\pi}\int_{\circlegroup\setminus J_{0}}P_{r}(\theta-t)\big(f(e^{it})-f(a)\big)dt}
$$
for every $z=re^{i\theta}$, and step [](#complement){.pf-ref} makes the second term less than $\varepsilon$ once $z$ is close enough to $a$ with $r<1$. So $\abs{u(z)-f(a)}<2\varepsilon$ eventually, and $\varepsilon$ was arbitrary.
:::

:::

:::
:::
