---
schema: qual/card@1
id: P-UCLARA14F-11
kind: problem
title: Harnack inequality for nonnegative harmonic functions
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 11 on page 2 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\Omega \subset \CC$ be open, bounded, and simply connected. Let $u$ be harmonic in $\Omega$ and assume that $u \geq 0$. Show the following: for each compact set $K \subset \Omega$, there exists a constant $C_K > 0$ such that
\[
\sup_{x \in K} u(x) \leq C_K \inf_{x \in K} u(x).
\]
:::

::: {.solution}

::: pf

::: pf-step

By the Riemann mapping theorem, there is a conformal bijection
\[
\phi:\DD\longrightarrow\Omega.
\]


::: pf-proof

The domain $\Omega$ is open, connected, simply connected, and bounded, hence
is a proper simply connected domain in $\CC$. The Riemann mapping
theorem therefore applies.

:::

:::

::: pf-step

The function
\[
v=u\circ\phi
\]
is nonnegative and harmonic on $\DD$.


::: pf-proof

A conformal change of variable preserves harmonicity in the plane. Since
$u\ge0$ on $\Omega$ and $\phi(\DD)=\Omega$, one also has
\[
v\ge0.
\]

:::

:::

::: pf-step

The set
\[
L=\phi^{-1}(K)
\]
is compact in $\DD$, so there is $r\in(0,1)$ such that
\[
L\subseteq\overline{D(0,r)}.
\]


::: pf-proof

The inverse $\phi^{-1}$ is continuous, so the preimage of the compact set
$K$ is compact. Since $L$ is compact and contained in the open unit disk,
\[
\max_{z\in L}|z|<1.
\]
Choose $r$ strictly between this maximum and $1$.

:::

:::

::: {.pf-step #s1-4}

For every $z$ with $|z|\le r$, Harnack's inequality gives
\[
\frac{1-r}{1+r}v(0)
\le
v(z)
\le
\frac{1+r}{1-r}v(0).
\]


::: pf-proof

For a nonnegative harmonic function on the unit disk, Harnack's inequality
states that
\[
\frac{1-|z|}{1+|z|}v(0)
\le
v(z)
\le
\frac{1+|z|}{1-|z|}v(0).
\]
If $|z|\le r$, monotonicity of the two rational factors gives the displayed
uniform bounds.

:::

:::

::: {.pf-step #s1-5}

One has
\[
v(0)
\le
\frac{1+r}{1-r}
\inf_{z\in L}v(z).
\]


::: pf-proof

The left-hand inequality in step [](#s1-4){.pf-ref} gives, for every $z\in L$,
\[
v(z)
\ge
\frac{1-r}{1+r}v(0).
\]
Taking the infimum over $L$ and rearranging gives the claim.

:::

:::

::: {.pf-step #s1-6}

For every $z\in L$,
\[
v(z)
\le
\left(\frac{1+r}{1-r}\right)^2
\inf_{\zeta\in L}v(\zeta).
\]


::: pf-proof

The right-hand inequality in step [](#s1-4){.pf-ref} gives
\[
v(z)
\le
\frac{1+r}{1-r}v(0).
\]
Substitute the upper bound for $v(0)$ from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
\sup_{x\in K}u(x)
\le
C_K
\inf_{x\in K}u(x)}
\]
with
\[
\boxed{
C_K
=
\left(\frac{1+r}{1-r}\right)^2}.
\]


::: pf-proof

Since $\phi:L\to K$ is a bijection,
\[
\sup_{x\in K}u(x)
=
\sup_{z\in L}v(z)
\]
and
\[
\inf_{x\in K}u(x)
=
\inf_{z\in L}v(z).
\]
Taking the supremum in step [](#s1-6){.pf-ref} gives the asserted inequality.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} supplies the required constant for the arbitrary compact set $K$.

:::

:::

:::
