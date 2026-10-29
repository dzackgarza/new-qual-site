---
schema: qual/card@1
id: P-UCLARA16S-12
kind: problem
title: Maximum principle for bounded harmonic functions with one exceptional boundary point
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
(a) Find a real-valued harmonic function $v$ defined on the disk $|z|<1$ such that $v(z)>0$ and
\[
\lim_{z\to1}v(z)=\infty.
\]

(b) Let $u$ be a real-valued harmonic function in the disk $|z|<1$ such that $u(z)\le M<\infty$ and
\[
\limsup_{r\to1}u(re^{i\theta})\le0
\]
for all $\theta\in(0,2\pi)$. Show that $u(z)\le0$. The function in part (a) is useful here.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a), define
\[
\boxed{
v(z)
=
-\log\left|\frac{1-z}{2}\right|
}.
\]
Then $v$ is harmonic and strictly positive on $\DD$, and
\[
v(z)\longrightarrow\infty
\qquad
(z\to1).
\]


::: pf-proof

For $z\in\DD$ one has
\[
\operatorname{Re}(1-z)>0,
\]
so the principal logarithm is holomorphic at $(1-z)/2$. Thus
\[
F(z)
\coloneqq
-\Log\left(\frac{1-z}{2}\right)
\]
is holomorphic on $\DD$, and
\[
v=\operatorname{Re}F
\]
is harmonic.

Moreover, for $z\in\DD$,
\[
|1-z|<2,
\]
so
\[
0<
-\log\left|\frac{1-z}{2}\right|
=v(z).
\]
Finally, as $z\to1$,
\[
\left|\frac{1-z}{2}\right|\to0,
\]
and therefore $v(z)\to\infty$.

:::

:::

::: {.pf-step #s2}

Fix $\varepsilon>0$ and set
\[
w_\varepsilon
\coloneqq
u-\varepsilon v.
\]
Then $w_\varepsilon$ is harmonic on $\DD$, bounded above, and for every $\zeta\in\partial\DD$,
\[
\limsup_{r\to1}
w_\varepsilon(r\zeta)
\le0.
\]


::: pf-proof

::: {.pf-step #s2-1}

If $\zeta=e^{i\theta}\ne1$, then
\[
\limsup_{r\to1}w_\varepsilon(re^{i\theta})\le0.
\]


::: pf-proof

The function $v$ extends continuously to every boundary point except $1$, with finite nonnegative value there. By the hypothesis on $u$,
\[
\limsup_{r\to1}
u(re^{i\theta})
\le0.
\]
Hence
\[
\limsup_{r\to1}
w_\varepsilon(re^{i\theta})
\le
-\varepsilon v(e^{i\theta})
\le0.
\]

:::

:::

::: {.pf-step #s2-2}

At the exceptional point $\zeta=1$,
\[
w_\varepsilon(r)\longrightarrow-\infty
\qquad
(r\to1).
\]


::: pf-proof

The hypothesis gives $u(z)\le M$ throughout $\DD$, while step [](#s1){.pf-ref} gives $v(r)\to\infty$ as $r\to1$. Therefore
\[
w_\varepsilon(r)
=
u(r)-\varepsilon v(r)
\le
M-\varepsilon v(r)
\longrightarrow
-\infty.
\]

:::

:::

::: pf-qed

The function $w_\varepsilon$ is harmonic as a linear combination of harmonic functions and satisfies
\[
w_\varepsilon\le u\le M
\]
because $v>0$. Steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref} give the boundary limsup assertion.

:::

:::

:::

::: {.pf-step #s3}

If a harmonic function $w$ on $\DD$ is bounded above and satisfies
\[
\limsup_{r\to1}w(re^{i\theta})\le0
\qquad
(0\le\theta<2\pi),
\]
then
\[
w\le0
\qquad
\text{on }\DD.
\]


::: pf-proof

Fix
\[
z=\rho e^{i\varphi}\in\DD.
\]
For every $R$ with $\rho<R<1$, the Poisson formula on the disk of radius $R$ gives
\[
w(z)
=
\frac1{2\pi}
\int_0^{2\pi}
P_{\rho/R}(\varphi-\theta)
w(Re^{i\theta})\,d\theta,
\]
where
\[
P_s(\alpha)
=
\frac{1-s^2}{1-2s\cos\alpha+s^2}.
\]

Choose any sequence $R_n\uparrow1$. Since $w$ is bounded above, say $w\le A$, and since
\[
\frac{\rho}{R_n}
\longrightarrow
\rho<1,
\]
the kernels $P_{\rho/R_n}$ are uniformly bounded for all sufficiently large $n$. Hence the integrands
\[
P_{\rho/R_n}(\varphi-\theta)
w(R_ne^{i\theta})
\]
have a common integrable upper bound. The reverse Fatou lemma therefore gives
\[
\begin{aligned}
w(z)
&=
\limsup_{n\to\infty}
\frac1{2\pi}
\int_0^{2\pi}
P_{\rho/R_n}(\varphi-\theta)
w(R_ne^{i\theta})\,d\theta\\
&\le
\frac1{2\pi}
\int_0^{2\pi}
\limsup_{n\to\infty}
\left[
P_{\rho/R_n}(\varphi-\theta)
w(R_ne^{i\theta})
\right]d\theta\\
&\le0.
\end{aligned}
\]
For the last inequality, use
\[
P_{\rho/R_n}(\varphi-\theta)
\longrightarrow
P_\rho(\varphi-\theta)>0
\]
together with the assumed radial limsup inequality for $w$.

:::

:::

::: {.pf-step #s4}

For every $\varepsilon>0$ and every $z\in\DD$,
\[
u(z)\le\varepsilon v(z).
\]


::: pf-proof

Apply step [](#s3){.pf-ref} to $w_\varepsilon$ from step [](#s2){.pf-ref}. Then
\[
u(z)-\varepsilon v(z)
=
w_\varepsilon(z)
\le0.
\]

:::

:::

::: {.pf-step #s5}

For every $z\in\DD$,
\[
\boxed{u(z)\le0}.
\]


::: pf-proof

Fix $z\in\DD$. The number $v(z)$ is finite. By step [](#s4){.pf-ref},
\[
u(z)\le\varepsilon v(z)
\]
for every $\varepsilon>0$. Letting $\varepsilon\downarrow0$ gives $u(z)\le0$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} solves part (a), and step [](#s5){.pf-ref} proves part (b).

:::

:::

:::
