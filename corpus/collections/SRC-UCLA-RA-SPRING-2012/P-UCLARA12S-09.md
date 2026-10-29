---
schema: qual/card@1
id: P-UCLARA12S-09
kind: problem
title: Jordan lemma on a quarter circle
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
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Prove Jordan's lemma: if $f:\CC\to\CC$ is meromorphic, $R>0$, and $k>0$, then
$$
\left|\int_\Gamma f(z)e^{ikz}\,dz\right|\le \frac{100}{k}\sup_{z\in\Gamma}|f(z)|,
$$
where $\Gamma$ is the quarter-circle $z=Re^{i\theta}$, $0\le\theta\le\pi/2$.
:::

::: {.solution}

Set
$$
M\coloneqq\sup_{z\in\Gamma}\abs{f(z)}.
$$
If $M<\infty$, then $f$ has no pole on the compact arc $\Gamma$, so the line integral is well defined.

::: pf

::: {.pf-step #s1-1}

Parametrizing $\Gamma$ by $z(\theta)=Re^{i\theta}$ gives
$$
\abs{f(z(\theta))e^{ikz(\theta)}z'(\theta)}
\le
RM e^{-kR\sin\theta}.
$$


::: pf-proof

Since
$$
z'(\theta)=iRe^{i\theta},
$$
we have $\abs{z'(\theta)}=R$. Also
$$
\abs{e^{ikRe^{i\theta}}}
=
\abs{e^{ikR\cos\theta-kR\sin\theta}}
=
e^{-kR\sin\theta}.
$$
Combining these estimates with $\abs{f(z(\theta))}\le M$ proves the claim.

:::

:::

::: {.pf-step #s1-2}

The integral satisfies the sharper estimate
$$
\abs{\int_\Gamma f(z)e^{ikz}\,dz}
\le
\boxed{\frac{\pi}{2k}M}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{\int_\Gamma f(z)e^{ikz}\,dz}
\le
RM\int_0^{\pi/2}e^{-kR\sin\theta}\,d\theta.
$$
The concavity of $\sin\theta$ on $[0,\pi/2]$ gives the chord bound
$$
\sin\theta\ge\frac{2}{\pi}\theta.
$$
Hence
$$
\begin{aligned}
\abs{\int_\Gamma f(z)e^{ikz}\,dz}
&\le
RM\int_0^{\pi/2}e^{-(2kR/\pi)\theta}\,d\theta\\
&\le
RM\int_0^\infty e^{-(2kR/\pi)\theta}\,d\theta\\
&=
\frac{\pi}{2k}M.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The required Jordan-lemma bound holds:
$$
\boxed{
\abs{\int_\Gamma f(z)e^{ikz}\,dz}
\le
\frac{100}{k}\sup_{z\in\Gamma}\abs{f(z)} }.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the same inequality with constant $\pi/2$, and $\pi/2<100$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required estimate.

:::

:::

:::
