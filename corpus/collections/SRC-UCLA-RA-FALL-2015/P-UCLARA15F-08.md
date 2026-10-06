---
schema: qual/card@1
id: P-UCLARA15F-08
kind: problem
title: Periodic entire functions of exponential type less than 1 are constant
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 8 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Assume that $f(z)$ is an entire function that is $2\pi$-periodic in the sense that $f(z + 2\pi) = f(z)$, and
\[
|f(x+iy)| \leq C e^{\alpha|y|},
\]
for some $C > 0$, where $0 < \alpha < 1$. Prove that $f$ is constant.
:::

::: {.solution}
For each integer \(n\), define the Fourier coefficient
\[
a_n
=
\frac1{2\pi}
\int_0^{2\pi}
f(x)e^{-inx}\,dx.
\]

<1>1. For every \(y\in\mathbb R\),
\[
\boxed{
a_n
=
\frac1{2\pi}
\int_0^{2\pi}
f(x+iy)e^{-in(x+iy)}\,dx}.
\]

::: {.proof}
Consider the entire function
\[
g_n(z)=f(z)e^{-inz}.
\]
Since \(f\) is \(2\pi\)-periodic and \(n\in\mathbb Z\),
\[
g_n(z+2\pi)
=
f(z+2\pi)e^{-in(z+2\pi)}
=
f(z)e^{-inz}e^{-2\pi in}
=
g_n(z).
\]

Integrate \(g_n\) around the rectangle with vertices
\[
0,\quad 2\pi,\quad 2\pi+iy,\quad iy.
\]
Cauchy's theorem gives total integral \(0\). The two vertical side integrals cancel because of the \(2\pi\)-periodicity of \(g_n\). Hence the bottom and top horizontal integrals are equal:
\[
\int_0^{2\pi}f(x)e^{-inx}\,dx
=
\int_0^{2\pi}
f(x+iy)e^{-in(x+iy)}\,dx.
\]
Divide by \(2\pi\).
:::

<1>2. Therefore
\[
|a_n|
\le
C e^{\alpha|y|}e^{ny}
\]
for every \(y\in\mathbb R\).

::: {.proof}
From step <1>1,
\[
\begin{aligned}
|a_n|
&\le
\frac1{2\pi}
\int_0^{2\pi}
|f(x+iy)|
\,|e^{-in(x+iy)}|
\,dx.
\end{aligned}
\]
Now
\[
|e^{-in(x+iy)}|
=
e^{ny},
\]
and the hypothesis gives
\[
|f(x+iy)|
\le
Ce^{\alpha|y|}.
\]
Thus
\[
|a_n|
\le
Ce^{\alpha|y|}e^{ny}.
\]
:::

## Positive Fourier modes

<1>3. Let
\[
n\ge1.
\]
For \(y<0\),
\[
\boxed{
|a_n|
\le
C e^{(n-\alpha)y}}.
\]

::: {.proof}
When \(y<0\),
\[
|y|=-y.
\]
Hence step <1>2 becomes
\[
|a_n|
\le
C e^{-\alpha y}e^{ny}
=
C e^{(n-\alpha)y}.
\]
:::

<1>4. Since
\[
n-\alpha>0,
\]
letting
\[
y\to-\infty
\]
gives
\[
\boxed{a_n=0}
\]
for every \(n\ge1\).

::: {.proof}
Because \(0<\alpha<1\) and \(n\ge1\),
\[
n-\alpha>0.
\]
Thus
\[
e^{(n-\alpha)y}\to0
\]
as \(y\to-\infty\). Step <1>3 then forces \(|a_n|=0\).
:::

## Negative Fourier modes

<1>5. Let
\[
n\le-1.
\]
For \(y>0\),
\[
\boxed{
|a_n|
\le
C e^{(n+\alpha)y}}.
\]

::: {.proof}
When \(y>0\),
\[
|y|=y.
\]
Thus step <1>2 gives
\[
|a_n|
\le
Ce^{\alpha y}e^{ny}
=
Ce^{(n+\alpha)y}.
\]
:::

<1>6. Since
\[
n+\alpha<0,
\]
letting
\[
y\to+\infty
\]
gives
\[
\boxed{a_n=0}
\]
for every \(n\le-1\).

::: {.proof}
Because \(n\le-1\) and \(\alpha<1\),
\[
n+\alpha\le-1+\alpha<0.
\]
Hence the right-hand side of step <1>5 tends to zero as \(y\to+\infty\).
:::

<1>7. Therefore the only possibly nonzero Fourier coefficient is
\[
\boxed{a_0}.
\]

::: {.proof}
Steps <1>4 and <1>6 kill every coefficient with \(n\ne0\).
:::

Let
\[
h(x)=f(x)-a_0
\]
for real \(x\).

<1>8. Every Fourier coefficient of the continuous \(2\pi\)-periodic function \(h\) is zero.

::: {.proof}
For \(n\ne0\), this follows from step <1>7. For \(n=0\),
\[
\frac1{2\pi}\int_0^{2\pi}h(x)\,dx
=
a_0-a_0
=
0.
\]
:::

<1>9. Hence
\[
\boxed{h(x)=0}
\]
for every real \(x\).

::: {.proof}
A continuous periodic function is uniquely determined by its Fourier coefficients. Equivalently, the Fejér means of its Fourier series converge uniformly to \(h\); since all Fourier coefficients vanish, every Fejér mean is identically zero, so \(h\equiv0\).
:::

<1>10. Thus
\[
\boxed{
f(x)=a_0}
\]
for every real \(x\).

::: {.proof}
This is the definition of \(h\) and step <1>9.
:::

<1>11. Since \(f-a_0\) is entire and vanishes on the real line, it vanishes identically on \(\mathbb C\).

::: {.proof}
The real line has accumulation points in \(\mathbb C\). Apply the identity theorem to the entire function
\[
f-a_0.
\]
:::

<1>12. Therefore
\[
\boxed{f\text{ is constant}.}
\]

::: {.proof}
Step <1>11 gives
\[
f\equiv a_0.
\]
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 is the required conclusion.
:::
:::
