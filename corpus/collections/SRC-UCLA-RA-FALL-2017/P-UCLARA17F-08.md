---
schema: qual/card@1
id: P-UCLARA17F-08
kind: problem
title: Uniformly continuous harmonic functions on the disk are Poisson integrals
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 8. Show that a harmonic function $u:\mathbb D\to\mathbb R$ is uniformly continuous if and only if it admits the representation
\[
u(z)=\frac1{2\pi}\int_0^{2\pi}\operatorname{Re}\!\left(\frac{e^{i\theta}+z}{e^{i\theta}-z}\right)f(e^{i\theta})\,d\theta,
\qquad z\in\mathbb D,
\]
with $f:\partial\mathbb D\to\mathbb R$ continuous.
:::

For $z\in\mathbb D$ and $\zeta\in\partial\mathbb D$, write
\[
P(z,\zeta)
\coloneqq
\operatorname{Re}\!\left(\frac{\zeta+z}{\zeta-z}\right)
=
\frac{1-|z|^2}{|\zeta-z|^2}.
\]

::: pf

::: pf-step

If $u$ is uniformly continuous on $\mathbb D$, then $u$ has a unique continuous extension $f:\overline{\mathbb D}\to\mathbb R$.


::: pf-proof

Let $\zeta\in\partial\mathbb D$ and choose any sequence $(z_n)$ in $\mathbb D$ with $z_n\to\zeta$. Since $(z_n)$ is Cauchy and $u$ is uniformly continuous, $(u(z_n))$ is Cauchy in $\mathbb R$, hence convergent.

If $(w_n)$ is another sequence in $\mathbb D$ with $w_n\to\zeta$, then $|z_n-w_n|\to0$, so uniform continuity gives $|u(z_n)-u(w_n)|\to0$. Thus the limit depends only on $\zeta$; define it to be $f(\zeta)$, and set $f=u$ on $\mathbb D$.

To prove continuity at a boundary point $\zeta$, fix $\varepsilon>0$ and choose $\delta>0$ from uniform continuity of $u$. If $x\in\overline{\mathbb D}$ and $|x-\zeta|<\delta/2$, choose $x_n\in\mathbb D$ with $x_n\to x$ and $\zeta_n\in\mathbb D$ with $\zeta_n\to\zeta$. For all sufficiently large $n$,
\[
|x_n-\zeta_n|
\le |x_n-x|+|x-\zeta|+|\zeta-\zeta_n|
<\delta.
\]
Hence $|u(x_n)-u(\zeta_n)|<\varepsilon$, and passage to the limit gives $|f(x)-f(\zeta)|\le\varepsilon$. Therefore $f$ is continuous on $\overline{\mathbb D}$. Uniqueness follows because $\mathbb D$ is dense in $\overline{\mathbb D}$.

:::

:::

::: pf-step

Under the hypothesis of step <1>1,
\[
u(z)=\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})f(e^{i\theta})\,d\theta
\qquad (z\in\mathbb D).
\]


::: pf-proof

Fix $z=re^{i\varphi}\in\mathbb D$ and choose $R$ with $r<R<1$. Since $u$ is harmonic on the closed disk $\{|w|\le R\}$, the Poisson formula on that disk gives
\[
u(z)
=
\frac1{2\pi}\int_0^{2\pi}
P\!\left(\frac zR,e^{i\theta}\right)
u(Re^{i\theta})\,d\theta.
\]
As $R\uparrow1$, continuity of $f$ on the compact disk $\overline{\mathbb D}$ implies
\[
\sup_{\theta}|u(Re^{i\theta})-f(e^{i\theta})|\longrightarrow0.
\]
Also, because $r<1$ is fixed,
\[
P\!\left(\frac zR,e^{i\theta}\right)
\longrightarrow
P(z,e^{i\theta})
\]
uniformly in $\theta$. Passing to the limit in the integral yields the claimed representation.

:::

:::

::: pf-step

Conversely, suppose that $f:\partial\mathbb D\to\mathbb R$ is continuous and that
\[
u(z)=\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})f(e^{i\theta})\,d\theta.
\]
Then for every $\zeta_0\in\partial\mathbb D$,
\[
\lim_{z\to\zeta_0,\ z\in\mathbb D}u(z)=f(\zeta_0).
\]


::: pf-proof

::: pf-step

For every $z\in\mathbb D$,
\[
\frac1{2\pi}\int_0^{2\pi}P(z,e^{i\theta})\,d\theta=1.
\]


::: pf-proof

The Poisson kernel is the harmonic extension of the constant boundary function $1$, so the Poisson formula applied to the constant harmonic function $1$ gives the identity.

:::

:::

::: pf-step

Fix $\varepsilon>0$. There is an open arc $I\subset\partial\mathbb D$ containing $\zeta_0$ such that
\[
|f(\zeta)-f(\zeta_0)|<\varepsilon
\qquad (\zeta\in I).
\]


::: pf-proof

This is continuity of $f$ at $\zeta_0$.

:::

:::

::: pf-step

If $J=\partial\mathbb D\setminus I$, then
\[
\sup_{\zeta\in J}P(z,\zeta)\longrightarrow0
\qquad\text{as }z\to\zeta_0, z\in\mathbb D.
\]


::: pf-proof

The compact set $J$ does not contain $\zeta_0$, so
\[
d\coloneqq\min_{\zeta\in J}|\zeta-\zeta_0|>0.
\]
For $|z-\zeta_0|<d/2$ and $\zeta\in J$,
\[
|\zeta-z|
\ge |\zeta-\zeta_0|-|z-\zeta_0|
\ge d/2.
\]
Therefore
\[
0\le P(z,\zeta)
=\frac{1-|z|^2}{|\zeta-z|^2}
\le \frac{4(1-|z|^2)}{d^2},
\]
and the right-hand side tends to $0$ as $z\to\zeta_0$.

:::

:::

::: pf-step

$u(z)\to f(\zeta_0)$ as $z\to\zeta_0$ within $\mathbb D$.


::: pf-proof

Let
\[
M\coloneqq\max_{\zeta\in\partial\mathbb D}|f(\zeta)-f(\zeta_0)|.
\]
Using step <2>1 and splitting the boundary integral over $I$ and $J$,
\[
\begin{aligned}
|u(z)-f(\zeta_0)|
&\le
\frac1{2\pi}\int_I
P(z,\zeta)|f(\zeta)-f(\zeta_0)|\,|d\zeta| \\
&\qquad+
\frac1{2\pi}\int_J
P(z,\zeta)|f(\zeta)-f(\zeta_0)|\,|d\zeta| \\
&\le
\varepsilon+
M\sup_{\zeta\in J}P(z,\zeta).
\end{aligned}
\]
By step <2>3 the second term tends to $0$. Hence
\[
\limsup_{z\to\zeta_0}|u(z)-f(\zeta_0)|\le\varepsilon.
\]
Since $\varepsilon>0$ was arbitrary, the limit is $0$.

:::

:::

::: pf-qed

Step <2>4 proves the claim of step <1>3.

:::

:::

:::

::: pf-step

Under the hypothesis of step <1>3, $u$ is uniformly continuous on $\mathbb D$.


::: pf-proof

Define $\widetilde u$ on $\overline{\mathbb D}$ by $\widetilde u=u$ on $\mathbb D$ and $\widetilde u=f$ on $\partial\mathbb D$. The function $u$ is continuous in $\mathbb D$, and step <1>3 shows that $\widetilde u$ is continuous at every boundary point. Thus $\widetilde u$ is continuous on the compact set $\overline{\mathbb D}$, hence uniformly continuous there. Its restriction $u$ to $\mathbb D$ is therefore uniformly continuous.

:::

:::

::: pf-qed

Steps <1>1 and <1>2 prove the forward implication, and steps <1>3 and <1>4 prove the converse.

:::

:::
