---
schema: qual/card@1
id: P-UCLARA14F-01
kind: problem
title: Borel measurability of $L^2\cap L^3$ in $L^3(\RR)$
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 1 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Show that
$$
A \coloneqq \left\{ f \in L^3(\RR) : \int_{\RR} |f(x)|^2\,dx < \infty \right\}
$$
is a Borel subset of $L^3(\RR)$.
:::

::: {.solution}

For each $n\in\NN$, define
$$
\phi_n:L^3(\RR)\to[0,\infty),
\qquad
\phi_n(f)=\int_{-n}^{n}|f(x)|^2\,dx.
$$

::: pf

::: {.pf-step #s1-1}

For every measurable $h$ on $[-n,n]$,
$$
\|h\|_{L^2([-n,n])}
\le
(2n)^{1/6}\|h\|_{L^3([-n,n])}.
$$


::: pf-proof

Apply Hölder's inequality with exponents
$$
\frac32
\qquad\text{and}\qquad
3
$$
to $|h|^2$ and $1$:
$$
\int_{-n}^{n}|h|^2
\le
\left(\int_{-n}^{n}|h|^3\right)^{2/3}
\left(\int_{-n}^{n}1^3\right)^{1/3}.
$$
Thus
$$
\|h\|_2^2
\le
\|h\|_3^2(2n)^{1/3},
$$
and taking square roots gives the claim.

:::

:::

::: {.pf-step #s1-2}

For every $f,g\in L^3(\RR)$,
$$
|\phi_n(f)-\phi_n(g)|
\le
(2n)^{1/3}
\|f-g\|_3
\bigl(\|f\|_3+\|g\|_3\bigr).
$$


::: pf-proof

On $[-n,n]$,
$$
\bigl||f|^2-|g|^2\bigr|
\le
|f-g|(|f|+|g|).
$$
Hence Cauchy--Schwarz gives
$$
\begin{aligned}
|\phi_n(f)-\phi_n(g)|
&\le
\|f-g\|_{L^2([-n,n])}
\bigl(
\|f\|_{L^2([-n,n])}
+\|g\|_{L^2([-n,n])}
\bigr).
\end{aligned}
$$
Apply step [](#s1-1){.pf-ref} to each $L^2$ norm and use
$$
\|h\|_{L^3([-n,n])}\le\|h\|_{L^3(\RR)}.
$$
The resulting factor is
$$
(2n)^{1/6}(2n)^{1/6}
=(2n)^{1/3},
$$
which yields the displayed estimate.

:::

:::

::: {.pf-step #s1-3}

Each functional
$$
\phi_n:L^3(\RR)\to\RR
$$
is continuous.


::: pf-proof

Fix $f\in L^3(\RR)$ and let $g\to f$ in $L^3$. Then
$$
\|g\|_3
\le
\|f\|_3+\|g-f\|_3,
$$
so the factor
$$
\|f\|_3+\|g\|_3
$$
remains bounded near $f$. Step [](#s1-2){.pf-ref} then implies
$$
|\phi_n(g)-\phi_n(f)|\to0.
$$

:::

:::

::: {.pf-step #s1-4}

For every $f\in L^3(\RR)$,
$$
\int_{\RR}|f(x)|^2\,dx
=
\lim_{n\to\infty}\phi_n(f)
$$
in $[0,\infty]$.


::: pf-proof

The nonnegative functions
$$
|f|^2\chi_{[-n,n]}
$$
increase pointwise to $|f|^2$. The monotone convergence theorem therefore
gives the equality.

:::

:::

::: {.pf-step #s1-5}

The set $A$ has the representation
$$
\boxed{
A
=
\bigcup_{m=1}^{\infty}
\bigcap_{n=1}^{\infty}
\{f\in L^3(\RR):\phi_n(f)\le m\}}.
$$


::: pf-proof

If
$$
\int_{\RR}|f|^2<\infty,
$$
choose an integer $m$ larger than this integral. Then by step [](#s1-4){.pf-ref},
$$
\phi_n(f)\le m
$$
for every $n$, so $f$ belongs to the right-hand side.

Conversely, if there is $m$ such that
$$
\phi_n(f)\le m
$$
for every $n$, then step [](#s1-4){.pf-ref} gives
$$
\int_{\RR}|f|^2
=
\lim_{n\to\infty}\phi_n(f)
\le m<\infty.
$$
Thus $f\in A$.

:::

:::

::: {.pf-step #s1-6}

The set $A$ is Borel in $L^3(\RR)$.


::: pf-proof

By step [](#s1-3){.pf-ref}, each set
$$
\{f:\phi_n(f)\le m\}
=
\phi_n^{-1}((-\infty,m])
$$
is closed, hence Borel. Step [](#s1-5){.pf-ref} expresses $A$ using only countable
intersections and a countable union of these Borel sets. Therefore $A$ is
Borel.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
