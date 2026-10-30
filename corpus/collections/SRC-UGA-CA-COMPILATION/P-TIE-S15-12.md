---
schema: qual/card@1
id: P-TIE-S15-12
kind: problem
title: Casorati--Weierstrass for accumulating poles
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 12.
---

::: {.problem}
(1) Let f be analytic in $\Omega : 0 < \abs{ z - a } < r$except at a sequence of poles$a _ { n } \in \Omega$with$\operatorname* { l i m } _ { n \to \infty } a _ { n } = a$.
Show that for any w$\in \CC$, there exists a sequence$z _ { n } \in \Omega$such that$\operatorname* { l i m } _ { n \to \infty } f ( z _ { n } ) = w$

(2) Explain the similarity and difference between the above assertion and the Weierstrass-Casorati theorem.
:::

::: {.solution}

We prove the stronger statement that the sequence in part (1) may be chosen so that
$$
z_n\longrightarrow a.
$$

::: pf

::: {.pf-step #s1-1}

Fix $w\in\CC$. If there were no sequence $z_n\to a$ with $f(z_n)\to w$, then there would exist $\varepsilon>0$ and $\delta>0$ such that
$$
\abs{f(z)-w}\ge\varepsilon
$$
whenever
$$
0<\abs{z-a}<\delta
$$
and $z$ is not a pole of $f$.


::: pf-proof

Suppose the asserted uniform lower bound failed for every positive $\varepsilon$ and $\delta$. Taking
$$
\varepsilon=\delta=\frac1n
$$
would produce points $z_n$ with
$$
0<\abs{z_n-a}<\frac1n
$$
and
$$
\abs{f(z_n)-w}<\frac1n.
$$
Then $z_n\to a$ and $f(z_n)\to w$, contrary to the assumption. Hence such $\varepsilon$ and $\delta$ must exist.

:::

:::

::: {.pf-step #s1-2}

Under the assumption of step [](#s1-1){.pf-ref}, the function
$$
g(z)\coloneqq\frac1{f(z)-w}
$$
extends holomorphically across every pole $a_n$ lying in
$$
0<\abs{z-a}<\delta,
$$
with
$$
g(a_n)=0.
$$


::: pf-proof

Let $a_n$ be a pole of order $m$. Near $a_n$,
$$
f(z)
=
\frac{c_{-m}}{(z-a_n)^m}
+\cdots,
\qquad
c_{-m}\ne0.
$$
Equivalently,
$$
(z-a_n)^m(f(z)-w)
$$
extends holomorphically near $a_n$ with nonzero value $c_{-m}$ at $a_n$. Therefore
$$
\frac1{f(z)-w}
=
\frac{(z-a_n)^m}
{(z-a_n)^m(f(z)-w)}
$$
extends holomorphically across $a_n$ and has a zero there of order $m$.

:::

:::

::: {.pf-step #s1-3}

The extended function $g$ is bounded on the punctured disk
$$
0<\abs{z-a}<\delta.
$$


::: pf-proof

At non-pole points, step [](#s1-1){.pf-ref} gives
$$
\abs{g(z)}
=
\frac1{\abs{f(z)-w}}
\le
\frac1\varepsilon.
$$
At each filled-in pole $a_n$, step [](#s1-2){.pf-ref} gives $g(a_n)=0$, so the same bound holds. Thus $g$ is bounded throughout the punctured disk after the removable extensions at the poles.

:::

:::

::: {.pf-step #s1-4}

The point $a$ is a removable singularity of $g$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, $g$ is holomorphic and bounded on
$$
0<\abs{z-a}<\delta.
$$
Riemann's removable singularity theorem therefore extends $g$ holomorphically to the full disk
$$
\abs{z-a}<\delta.
$$

:::

:::

::: {.pf-step #s1-5}

The assumption in step [](#s1-1){.pf-ref} is impossible.


::: pf-proof

There are infinitely many poles $a_n\to a$. By step [](#s1-2){.pf-ref}, the holomorphic extension of $g$ from step [](#s1-4){.pf-ref} satisfies
$$
g(a_n)=0
$$
for all sufficiently large $n$. These zeros accumulate at the interior point $a$ of the extended domain. The identity theorem therefore gives
$$
g\equiv0
$$
on the disk.

This is impossible: away from the poles,
$$
g(z)=\frac1{f(z)-w},
$$
which is never zero. Hence the assumption of step [](#s1-1){.pf-ref} cannot hold.

:::

:::

::: {.pf-step #s1-6}

For every $w\in\CC$, there exists a sequence $z_n\in\Omega$ such that
$$
\boxed{
z_n\to a,
\qquad
f(z_n)\to w.
}
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, for every positive integer $n$ there is a non-pole point $z_n$ satisfying
$$
0<\abs{z_n-a}<\frac1n
$$
and
$$
\abs{f(z_n)-w}<\frac1n.
$$
These inequalities give the two asserted limits.

:::

:::

::: {.pf-step #s1-7}

The conclusion is analogous to the Casorati--Weierstrass theorem because every finite complex number is a cluster value of $f$ at $a$.


::: pf-proof

Casorati--Weierstrass says that if $a$ is an isolated essential singularity of a holomorphic function, then the image of every punctured neighborhood of $a$ is dense in $\CC$. Equivalently, for every $w\in\CC$ there is a sequence $z_n\to a$ with
$$
f(z_n)\to w.
$$
Step [](#s1-6){.pf-ref} gives exactly this cluster-value conclusion in the present setting.

:::

:::

::: {.pf-step #s1-8}

The difference is that here $a$ is not an isolated singularity of $f$.


::: pf-proof

In Casorati--Weierstrass, $f$ is holomorphic on some full punctured disk
$$
0<\abs{z-a}<\rho,
$$
and $a$ is the only singular point there. In the present problem, every punctured neighborhood of $a$ contains poles $a_n$ of $f$. Thus $f$ is not holomorphic on any deleted neighborhood of $a$, and $a$ is an accumulation point of singularities rather than an isolated essential singularity.

Moreover, the poles themselves show that $\infty$ is also a spherical cluster value at $a$. Thus the spherical cluster set in the present situation is all of the Riemann sphere.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (1) in the stronger form $z_n\to a$, and steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give the requested comparison with Casorati--Weierstrass.

:::

:::

:::
