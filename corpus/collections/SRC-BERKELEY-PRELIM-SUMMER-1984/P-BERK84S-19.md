---
schema: qual/card@1
id: P-BERK84S-19
kind: problem
title: Asymptotic forced response of a damped oscillator
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 19 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the sinusoidal particular solution, phase-amplitude conversion, and exponential decay of the homogeneous transient.
---

::: {.problem}
Let $x ( t )$ be the solution of the differential equation

$$
x ^ { \prime \prime } ( t ) + 8 x ^ { \prime } ( t ) + 2 5 x ( t ) = 2 \cos t
$$

with initial conditions $x ( 0 ) = 0$ and $x ^ { \prime } ( 0 ) = 0$ . Show that for suitable constants α and $\delta$

$$
\operatorname* { l i m } _ { t  \infty } ( x ( t ) - \alpha \cos ( t - \delta ) ) = 0 .
$$
:::

::: {.solution}
<1>1. A particular solution is
\[
x_p(t)=\frac{3}{40}\cos t+\frac1{40}\sin t.
\]
::: {.proof}
Seek a particular solution of the form
\[
x_p(t)=A\cos t+B\sin t.
\]
Then
\[
x_p'(t)=-A\sin t+B\cos t,
\qquad
x_p''(t)=-A\cos t-B\sin t.
\]
Substitution into
\[
x''+8x'+25x=2\cos t
\]
gives
\[
(24A+8B)\cos t+(24B-8A)\sin t=2\cos t.
\]
Hence
\[
24A+8B=2,
\qquad
24B-8A=0.
\]
The second equation gives $B=A/3$; substituting into the first yields $A=3/40$, hence $B=1/40$.
:::

<1>2. Every solution differs from $x_p$ by an exponentially decaying function.
::: {.proof}
The characteristic equation of the homogeneous equation is
\[
r^2+8r+25=0,
\]
whose roots are
\[
r=-4\pm3i.
\]
Thus every homogeneous solution has the form
\[
x_h(t)=e^{-4t}(C\cos3t+D\sin3t)
\]
for real constants $C,D$.
The prescribed initial conditions determine some particular values of $C$ and $D$, but their values are irrelevant for the limit.
Since $\cos3t$ and $\sin3t$ are bounded,
\[
\lim_{t\to\infty}x_h(t)=0.
\]
Therefore
\[
\lim_{t\to\infty}\bigl(x(t)-x_p(t)\bigr)=0.
\]
:::

<1>3. Write the steady-state term in amplitude-phase form.
::: {.proof}
Choose
\[
\alpha=\sqrt{\left(\frac3{40}\right)^2+\left(\frac1{40}\right)^2}
=\frac{\sqrt{10}}{40}
\]
and choose $\delta$ with
\[
\cos\delta=\frac3{\sqrt{10}},
\qquad
\sin\delta=\frac1{\sqrt{10}};
\]
for example $\delta=\arctan(1/3)$.
Then
\[
\alpha\cos(t-\delta)
=\alpha(\cos t\cos\delta+\sin t\sin\delta)
=\frac3{40}\cos t+\frac1{40}\sin t
=x_p(t).
\]
Combining this with <1>2 gives
\[
\boxed{\lim_{t\to\infty}\left(x(t)-\alpha\cos(t-\delta)\right)=0}.
\]
:::
:::
