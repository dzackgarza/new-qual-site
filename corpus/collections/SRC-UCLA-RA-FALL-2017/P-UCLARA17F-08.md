---
schema: qual/card@1
id: P-UCLARA17F-08
kind: problem
title: Uniformly continuous harmonic functions on the disk are Poisson integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Show that a harmonic function $u:\DD\to\RR$ is uniformly continuous if and only if it admits the representation
$$
u(z)=\frac1{2\pi}\int_0^{2\pi}\operatorname{Re}\!\left(\frac{e^{i\theta}+z}{e^{i\theta}-z}\right)f(e^{i\theta})\,d\theta,
\qquad z\in\DD,
$$
with $f:\partial\DD\to\RR$ continuous.
:::

::: {.solution}

For $z\in\DD$ and $\zeta\in\partial\DD$, write
$$
P(z,\zeta)
\coloneqq
\operatorname{Re}\!\left(\frac{\zeta+z}{\zeta-z}\right)
=
\frac{1-\abs{z}^2}{\abs{\zeta-z}^2}.
$$

::: pf

::: {.pf-step #s1}

If $u$ is uniformly continuous on $\DD$, then $u$ has a unique continuous extension $f:\overline{\DD}\to\RR$.


::: pf-proof

Let $\zeta\in\partial\DD$ and choose any sequence $(z_n)$ in $\DD$ with $z_n\to\zeta$. Since $(z_n)$ is Cauchy and $u$ is uniformly continuous, $(u(z_n))$ is Cauchy in $\RR$, hence convergent.

If $(w_n)$ is another sequence in $\DD$ with $w_n\to\zeta$, then $\abs{z_n-w_n}\to0$, so uniform continuity gives $\abs{u(z_n)-u(w_n)}\to0$. Thus the limit depends only on $\zeta$; define it to be $f(\zeta)$, and set $f=u$ on $\DD$.

To prove continuity at a boundary point $\zeta$, fix $\varepsilon>0$ and choose $\delta>0$ from uniform continuity of $u$. If $x\in\overline{\DD}$ and $\abs{x-\zeta}<\delta/2$, choose $x_n\in\DD$ with $x_n\to x$ and $\zeta_n\in\DD$ with $\zeta_n\to\zeta$. For all sufficiently large $n$,
$$
\abs{x_n-\zeta_n}
\le \abs{x_n-x}+\abs{x-\zeta}+\abs{\zeta-\zeta_n}
<\delta.
$$
Hence $\abs{u(x_n)-u(\zeta_n)}<\varepsilon$, and passage to the limit gives $\abs{f(x)-f(\zeta)}\le\varepsilon$. Therefore $f$ is continuous on $\overline{\DD}$. Uniqueness follows because $\DD$ is dense in $\overline{\DD}$.

:::

:::

::: {.pf-step #s2}

Under the hypothesis of step [](#s1){.pf-ref},
$$
u(z)=\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})f(e^{i\theta})\,d\theta
\qquad (z\in\DD).
$$


::: pf-proof

Fix $z=re^{i\varphi}\in\DD$ and choose $R$ with $r<R<1$. Since $u$ is harmonic on the closed disk $\{\abs{w}\le R\}$, the Poisson formula on that disk gives
$$
u(z)
=
\frac1{2\pi}\int_0^{2\pi}
P\!\left(\frac zR,e^{i\theta}\right)
u(Re^{i\theta})\,d\theta.
$$
As $R\uparrow1$, continuity of $f$ on the compact disk $\overline{\DD}$ implies
$$
\sup_{\theta}\abs{u(Re^{i\theta})-f(e^{i\theta})}\longrightarrow0.
$$
Also, because $r<1$ is fixed,
$$
P\!\left(\frac zR,e^{i\theta}\right)
\longrightarrow
P(z,e^{i\theta})
$$
uniformly in $\theta$. Passing to the limit in the integral yields the claimed representation.

:::

:::

::: {.pf-step #s3}

Conversely, suppose that $f:\partial\DD\to\RR$ is continuous and that
$$
u(z)=\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})f(e^{i\theta})\,d\theta.
$$
Then for every $\zeta_0\in\partial\DD$,
$$
\lim_{z\to\zeta_0,\ z\in\DD}u(z)=f(\zeta_0).
$$


::: pf-proof

::: {.pf-step #s3-1}

For every $z\in\DD$,
$$
\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})\,d\theta=1.
$$


::: pf-proof

The Poisson kernel is the harmonic extension of the constant boundary function $1$, so the Poisson formula applied to the constant harmonic function $1$ gives the identity.

:::

:::

::: pf-step

Fix $\varepsilon>0$. There is an open arc $I\subset\partial\DD$ containing $\zeta_0$ such that
$$
\abs{f(\zeta)-f(\zeta_0)}<\varepsilon
\qquad (\zeta\in I).
$$


::: pf-proof

This is continuity of $f$ at $\zeta_0$.

:::

:::

::: {.pf-step #s3-3}

If $J=\partial\DD\setminus I$, then
$$
\sup_{\zeta\in J}P(z,\zeta)\longrightarrow0
\qquad\text{as }z\to\zeta_0, z\in\DD.
$$


::: pf-proof

The compact set $J$ does not contain $\zeta_0$, so
$$
d\coloneqq\min_{\zeta\in J}\abs{\zeta-\zeta_0}>0.
$$
For $\abs{z-\zeta_0}<d/2$ and $\zeta\in J$,
$$
\abs{\zeta-z}
\ge \abs{\zeta-\zeta_0}-\abs{z-\zeta_0}
\ge d/2.
$$
Therefore
$$
0\le P(z,\zeta)
=\frac{1-\abs{z}^2}{\abs{\zeta-z}^2}
\le \frac{4(1-\abs{z}^2)}{d^2},
$$
and the right-hand side tends to $0$ as $z\to\zeta_0$.

:::

:::

::: {.pf-step #s3-4}

$u(z)\to f(\zeta_0)$ as $z\to\zeta_0$ within $\DD$.


::: pf-proof

Let
$$
M\coloneqq\max_{\zeta\in\partial\DD}\abs{f(\zeta)-f(\zeta_0)}.
$$
Using step [](#s3-1){.pf-ref} and splitting the boundary integral over $I$ and $J$,
$$
\begin{aligned}
\abs{u(z)-f(\zeta_0)}
&\le
\frac1{2\pi}\int_I
P(z,\zeta)\abs{f(\zeta)-f(\zeta_0)}\,\abs{d\zeta} \\
&\qquad+
\frac1{2\pi}\int_J
P(z,\zeta)\abs{f(\zeta)-f(\zeta_0)}\,\abs{d\zeta} \\
&\le
\varepsilon+
M\sup_{\zeta\in J}P(z,\zeta).
\end{aligned}
$$
By step [](#s3-3){.pf-ref} the second term tends to $0$. Hence
$$
\limsup_{z\to\zeta_0}\abs{u(z)-f(\zeta_0)}\le\varepsilon.
$$
Since $\varepsilon>0$ was arbitrary, the limit is $0$.

:::

:::

::: pf-qed

Step [](#s3-4){.pf-ref} proves the claim of step [](#s3){.pf-ref}.

:::

:::

:::

::: {.pf-step #s4}

Under the hypothesis of step [](#s3){.pf-ref}, $u$ is uniformly continuous on $\DD$.


::: pf-proof

Define $\widetilde u$ on $\overline{\DD}$ by $\widetilde u=u$ on $\DD$ and $\widetilde u=f$ on $\partial\DD$. The function $u$ is continuous in $\DD$, and step [](#s3){.pf-ref} shows that $\widetilde u$ is continuous at every boundary point. Thus $\widetilde u$ is continuous on the compact set $\overline{\DD}$, hence uniformly continuous there. Its restriction $u$ to $\DD$ is therefore uniformly continuous.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the forward implication, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the converse.

:::

:::

:::
