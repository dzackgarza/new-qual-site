---
schema: qual/card@1
id: P-UCLARA18F-09
kind: problem
title: Residues and Taylor coefficients of $\pi z\cot\pi z$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 9. Consider the meromorphic function
\[
g(z)=-\pi z\cot(\pi z)
\]
on the entire plane $\CC$.

(a) Find all poles of $g$ and determine the residue of $g$ at each pole.

(b) In the Taylor series representation
\[
g(z)=\sum_{k=0}^{\infty}a_kz^k
\]
about $z=0$, show that for each $k\ge1$,
\[
a_{2k}=\sum_{n\ge1}\frac{2}{n^{2k}}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The poles of \(g\) are precisely the nonzero integers, every pole is simple, and for each \(n\in\ZZ\setminus\{0\}\),
\[
\boxed{\operatorname{Res}(g,n)=-n}.
\]


::: pf-proof

Since
\[
g(z)=-\pi z\,\frac{\cos(\pi z)}{\sin(\pi z)},
\]
the only possible poles are the zeros of \(\sin(\pi z)\), namely the integers. If \(n\ne0\), then
\[
\sin(\pi n)=0,
\qquad
\frac{d}{dz}\sin(\pi z)\bigg|_{z=n}=\pi\cos(\pi n)=\pi(-1)^n\ne0,
\]
while the numerator at \(n\) is \(-\pi n(-1)^n\ne0\). Thus \(n\) is a simple pole, and
\[
\operatorname{Res}(g,n)
=\frac{-\pi n\cos(\pi n)}{\pi\cos(\pi n)}
=-n.
\]
At \(z=0\),
\[
\lim_{z\to0}g(z)
=-\lim_{z\to0}\frac{\pi z\cos(\pi z)}{\sin(\pi z)}
=-1,
\]
so the singularity at \(0\) is removable rather than a pole.

:::

:::

::: {.pf-step #s1-2}

For \(z\notin\ZZ\),
\[
\pi\cot(\pi z)
=\frac1z+2z\sum_{m=1}^{\infty}\frac1{z^2-m^2}.
\]


::: pf-proof

Euler's product for the sine function is
\[
\frac{\sin(\pi z)}{\pi z}
=\prod_{m=1}^{\infty}\left(1-\frac{z^2}{m^2}\right).
\]
Taking the logarithmic derivative on a compact set avoiding the integers gives
\[
\pi\cot(\pi z)-\frac1z
=\sum_{m=1}^{\infty}
\frac{-2z/m^2}{1-z^2/m^2}
=2z\sum_{m=1}^{\infty}\frac1{z^2-m^2},
\]
which is the claimed identity.

:::

:::

::: {.pf-step #s1-3}

For \(|z|<1\),
\[
g(z)=-1+2\sum_{m=1}^{\infty}\frac{z^2}{m^2-z^2}.
\]


::: pf-proof

Multiplying the identity in step [](#s1-2){.pf-ref} by \(-z\) gives
\[
g(z)
=-1-2z^2\sum_{m=1}^{\infty}\frac1{z^2-m^2}
=-1+2\sum_{m=1}^{\infty}\frac{z^2}{m^2-z^2}.
\]
The restriction \(|z|<1\) avoids every nonzero integer and is the disc of convergence relevant to the Taylor expansion about \(0\).

:::

:::

::: {.pf-step #s1-4}

For every integer \(k\ge1\), the Taylor coefficient of \(z^{2k}\) is
\[
a_{2k}=\boxed{2\sum_{m=1}^{\infty}\frac1{m^{2k}}}.
\]


::: pf-proof

Fix \(0<r<1\). For \(|z|\le r\) and every \(m\ge1\), the geometric-series expansion gives
\[
\frac{z^2}{m^2-z^2}
=\sum_{k=1}^{\infty}\frac{z^{2k}}{m^{2k}}.
\]
Moreover,
\[
\sum_{m=1}^{\infty}\sum_{k=1}^{\infty}
2\frac{|z|^{2k}}{m^{2k}}
\le
2\left(\sum_{m=1}^{\infty}\frac1{m^2}\right)
\left(\sum_{k=1}^{\infty}r^{2k}\right)
<\infty.
\]
Thus the double series is uniformly absolutely convergent on \(|z|\le r\), so step [](#s1-3){.pf-ref} may be rearranged as
\[
\begin{aligned}
g(z)
&=-1+2\sum_{m=1}^{\infty}\sum_{k=1}^{\infty}\frac{z^{2k}}{m^{2k}}\\
&=-1+\sum_{k=1}^{\infty}
\left(2\sum_{m=1}^{\infty}\frac1{m^{2k}}\right)z^{2k}.
\end{aligned}
\]
Since \(r<1\) was arbitrary, this is the Taylor expansion of \(g\) throughout \(|z|<1\), and comparison of coefficients gives the claimed formula.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-4){.pf-ref} proves part (b).

:::

:::

:::
