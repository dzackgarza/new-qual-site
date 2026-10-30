---
schema: qual/card@1
id: P-UCLARA14S-03
kind: problem
title: Lebesgue criterion for Riemann integrability
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $[a,b]$ be a finite interval and let $f:[a,b]\to\RR$ be bounded and Borel measurable.

(a) Prove that the set of points at which $f$ is continuous is Borel measurable.

(b) Prove that $f$ is Riemann integrable if and only if it is continuous almost everywhere.
:::

::: {.solution}

For $x\in[a,b]$, define the oscillation
$$
\omega_f(x)
\coloneqq
\inf_{\delta>0}
\sup\{
\abs{f(y)-f(z)}:
y,z\in[a,b]\cap(x-\delta,x+\delta)
\}.
$$

::: pf

::: {.pf-step #s1-1}

The function $f$ is continuous at $x$ if and only if
$$
\omega_f(x)=0.
$$


::: pf-proof

If $f$ is continuous at $x$, then for every $\varepsilon>0$ there is $\delta>0$ such that
$$
\abs{f(y)-f(x)}<\frac\varepsilon2
$$
whenever $y\in[a,b]$ and $\abs{y-x}<\delta$. Thus for such $y,z$,
$$
\abs{f(y)-f(z)}
\le
\abs{f(y)-f(x)}+\abs{f(z)-f(x)}
<
\varepsilon,
$$
so $\omega_f(x)=0$.

Conversely, if $\omega_f(x)=0$, then for every $\varepsilon>0$ there is $\delta>0$ such that
$$
\sup\{
\abs{f(y)-f(z)}:
y,z\in[a,b]\cap(x-\delta,x+\delta)
\}
<
\varepsilon.
$$
Taking $z=x$ gives
$$
\abs{f(y)-f(x)}<\varepsilon
$$
whenever $y\in[a,b]$ and $\abs{y-x}<\delta$, so $f$ is continuous at $x$.

:::

:::

::: {.pf-step #s1-2}

For every $n\ge1$, the set
$$
E_n
\coloneqq
\{x\in[a,b]:\omega_f(x)<1/n\}
$$
is open in the relative topology of $[a,b]$.


::: pf-proof

Fix $x\in E_n$. By definition of the infimum, there is $\delta>0$ such that the oscillation of $f$ on
$$
[a,b]\cap(x-\delta,x+\delta)
$$
is strictly less than $1/n$.

If $y\in[a,b]$ and $\abs{y-x}<\delta/2$, then
$$
[a,b]\cap(y-\delta/2,y+\delta/2)
\subset
[a,b]\cap(x-\delta,x+\delta).
$$
Hence the oscillation of $f$ on the smaller neighborhood is also less than $1/n$, so $y\in E_n$. Thus $E_n$ is relatively open.

:::

:::

::: {.pf-step #s1-3}

The set of continuity points of $f$ is Borel measurable.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\{x:f\text{ is continuous at }x\}
=
\bigcap_{n=1}^\infty E_n.
$$
Each $E_n$ is relatively open by step [](#s1-2){.pf-ref}, hence Borel in $[a,b]$. A countable intersection of Borel sets is Borel.

:::

:::

::: pf-step

Choose nested partitions
$$
P_1\subset P_2\subset\cdots
$$
of $[a,b]$ such that
$$
\operatorname{mesh}(P_n)\longrightarrow0,
$$
and
$$
U(f,P_n)\longrightarrow\overline{\int_a^b}f,
\qquad
L(f,P_n)\longrightarrow\underline{\int_a^b}f.
$$


::: pf-proof

For each $n$, choose a partition $Q_n$ with mesh less than $1/n$ and satisfying
$$
U(f,Q_n)
<
\overline{\int_a^b}f+\frac1n,
\qquad
L(f,Q_n)
>
\underline{\int_a^b}f-\frac1n.
$$
Define $P_n$ to be the common refinement of $Q_1,\dots,Q_n$. Refinement decreases upper sums and increases lower sums, while
$$
\operatorname{mesh}(P_n)\le\operatorname{mesh}(Q_n)<1/n.
$$
The asserted limits follow.

:::

:::

::: {.pf-step #s1-5}

For each $n$, define step functions $L_n,U_n$ by taking on each subinterval $I$ of $P_n$ the values
$$
L_n\restrict_I
=
\inf_I f,
\qquad
U_n\restrict_I
=
\sup_I f.
$$
Then, away from partition endpoints,
$$
L_1\le L_2\le\cdots\le f\le\cdots\le U_2\le U_1.
$$


::: pf-proof

Because the partitions are nested, each interval of $P_{n+1}$ lies inside an interval of $P_n$. Infima can only increase under restriction and suprema can only decrease. Also, on every interval $I$ containing $x$,
$$
\inf_I f
\le
f(x)
\le
\sup_I f.
$$
The only ambiguity is at endpoints shared by adjacent intervals; the union of all partition endpoints is countable and therefore null.

:::

:::

::: {.pf-step #s1-6}

The pointwise limits
$$
L(x)=\lim_{n\to\infty}L_n(x),
\qquad
U(x)=\lim_{n\to\infty}U_n(x)
$$
exist almost everywhere, satisfy $L\le f\le U$, and
$$
\int_a^bL
=
\underline{\int_a^b}f,
\qquad
\int_a^bU
=
\overline{\int_a^b}f.
$$


::: pf-proof

The monotonicity from step [](#s1-5){.pf-ref} gives the pointwise limits away from the null set of partition endpoints. Since $f$ is bounded, choose $M$ with
$$
\abs{f}\le M.
$$
Then
$$
\abs{L_n},\abs{U_n}\le M,
$$
so dominated convergence gives
$$
\int_a^bL
=
\lim_{n\to\infty}\int_a^bL_n
=
\lim_{n\to\infty}L(f,P_n)
=
\underline{\int_a^b}f,
$$
and similarly
$$
\int_a^bU
=
\overline{\int_a^b}f.
$$

:::

:::

::: {.pf-step #s1-7}

At every point $x$ that is not an endpoint of any $P_n$,
$$
L(x)=U(x)
$$
if and only if $f$ is continuous at $x$.


::: pf-proof

Let $I_n(x)$ be the unique interval of $P_n$ containing $x$ in its interior. Since the partitions are nested and their mesh tends to zero,
$$
I_{n+1}(x)\subset I_n(x),
\qquad
\operatorname{diam}I_n(x)\to0.
$$
Moreover,
$$
L_n(x)=\inf_{I_n(x)}f,
\qquad
U_n(x)=\sup_{I_n(x)}f.
$$

If $f$ is continuous at $x$, then the oscillation of $f$ on $I_n(x)$ tends to zero, so
$$
U_n(x)-L_n(x)\to0,
$$
hence $L(x)=U(x)$.

Conversely, if $L(x)=U(x)$, then because
$$
L_n(x)\le f(x)\le U_n(x),
$$
the common limit equals $f(x)$, and
$$
U_n(x)-L_n(x)\to0.
$$
Given $\varepsilon>0$, choose $n$ with
$$
U_n(x)-L_n(x)<\varepsilon.
$$
For all $y\in I_n(x)$,
$$
\abs{f(y)-f(x)}
\le
U_n(x)-L_n(x)
<
\varepsilon.
$$
Since $x$ lies in the interior of $I_n(x)$, this gives continuity at $x$.

:::

:::

::: {.pf-step #s1-8}

The function $f$ is Riemann integrable if and only if
$$
L=U
\qquad
\text{almost everywhere}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
\overline{\int_a^b}f
-
\underline{\int_a^b}f
=
\int_a^b(U-L).
$$
Since $U-L\ge0$, this difference is zero if and only if $U-L=0$ almost everywhere. Equality of the upper and lower Riemann integrals is exactly Riemann integrability.

:::

:::

::: {.pf-step #s1-9}

The function $f$ is Riemann integrable if and only if it is continuous almost everywhere.


::: pf-proof

The set of all partition endpoints is countable and hence null. Away from that set, step [](#s1-7){.pf-ref} says
$$
L=U
$$
exactly at the continuity points of $f$. Step [](#s1-8){.pf-ref} therefore identifies Riemann integrability with continuity almost everywhere.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
