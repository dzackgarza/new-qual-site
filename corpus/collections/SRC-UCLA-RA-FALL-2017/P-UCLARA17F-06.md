---
schema: qual/card@1
id: P-UCLARA17F-06
kind: problem
title: $L^2$ boundedness of the truncated Riesz potential $\int_{|w-z|\le1}\frac{|f(w)|}{|w-z|}\,dA(w)$
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
Problem 6. Let $f\in L^2(\mathbb C)$. For $z\in\mathbb C$ define
\[
g(z)=\int_{\{w\in\mathbb C:|w-z|\le1\}}\frac{|f(w)|}{|w-z|}\,dA(w),
\]
where $dA$ denotes integration with respect to Lebesgue measure on $\mathbb C\cong\mathbb R^2$. Show that $|g(z)|<\infty$ for almost every $z\in\mathbb C$ and that $g\in L^2(\mathbb C)$.
:::

::: {.solution}
Define
\[
k(u)
=
\frac{\mathbf 1_{\{|u|\le1\}}}{|u|}
\]
on \(\mathbb C\cong\mathbb R^2\).

<1>1. The kernel \(k\) belongs to \(L^1(\mathbb C)\).

::: {.proof}
Using polar coordinates,
\[
\int_{\mathbb C}k(u)\,dA(u)
=
\int_{|u|\le1}\frac{1}{|u|}\,dA(u)
=
\int_0^{2\pi}\int_0^1\frac1r\,r\,dr\,d\theta
=
2\pi.
\]
Thus the integral is finite.
:::

<1>2. More precisely,
\[
\boxed{
\|k\|_1=2\pi}.
\]

::: {.proof}
This is the value computed in step <1>1.
:::

<1>3. After the change of variables
\[
u=w-z,
\]
the function \(g\) can be written as
\[
\boxed{
g(z)
=
\int_{\mathbb C}
|f(z+u)|\,k(u)\,dA(u)}.
\]

::: {.proof}
The condition
\[
|w-z|\le1
\]
becomes
\[
|u|\le1,
\]
and
\[
dA(w)=dA(u).
\]
Thus
\[
\frac{|f(w)|}{|w-z|}
=
|f(z+u)|\,k(u).
\]
:::

<1>4. The function
\[
(z,u)\longmapsto |f(z+u)|k(u)
\]
is measurable on \(\mathbb C\times\mathbb C\).

::: {.proof}
The map
\[
(z,u)\mapsto z+u
\]
is continuous, \(f\) has a measurable representative, and \(k\) is measurable. Products and compositions of measurable functions are measurable.
:::

<1>5. Therefore \(g\) is measurable as an extended-valued nonnegative function.

::: {.proof}
By step <1>4, Tonelli's theorem implies that the integral in \(u\) defines a measurable function of \(z\), possibly taking the value \(+\infty\).
:::

Now apply Minkowski's integral inequality.

<1>6. One has
\[
\|g\|_2
\le
\int_{\mathbb C}
k(u)
\left(
\int_{\mathbb C}
|f(z+u)|^2\,dA(z)
\right)^{1/2}
dA(u).
\]

::: {.proof}
Apply Minkowski's integral inequality to the nonnegative function
\[
H(z,u)=|f(z+u)|k(u):
\]
\[
\left\|
\int H(\cdot,u)\,dA(u)
\right\|_{L^2_z}
\le
\int
\|H(\cdot,u)\|_{L^2_z}
\,dA(u).
\]
Since \(k(u)\) is independent of \(z\),
\[
\|H(\cdot,u)\|_2
=
k(u)
\left(
\int |f(z+u)|^2\,dA(z)
\right)^{1/2}.
\]
:::

<1>7. For every \(u\in\mathbb C\),
\[
\boxed{
\left(
\int_{\mathbb C}
|f(z+u)|^2\,dA(z)
\right)^{1/2}
=
\|f\|_2}.
\]

::: {.proof}
Lebesgue measure is translation invariant. With
\[
w=z+u,
\]
\[
\int_{\mathbb C}|f(z+u)|^2\,dA(z)
=
\int_{\mathbb C}|f(w)|^2\,dA(w).
\]
:::

<1>8. Hence
\[
\|g\|_2
\le
\|f\|_2
\int_{\mathbb C}k(u)\,dA(u).
\]

::: {.proof}
Substitute the constant value from step <1>7 into step <1>6.
:::

<1>9. Using step <1>2,
\[
\boxed{
\|g\|_2
\le
2\pi\|f\|_2}.
\]

::: {.proof}
\[
\int_{\mathbb C}k(u)\,dA(u)
=
2\pi.
\]
:::

<1>10. Therefore
\[
\boxed{
g\in L^2(\mathbb C)}.
\]

::: {.proof}
The right-hand side of step <1>9 is finite because
\[
f\in L^2(\mathbb C).
\]
Thus \(\|g\|_2<\infty\).
:::

<1>11. In particular,
\[
\boxed{
|g(z)|<\infty}
\]
for almost every \(z\in\mathbb C\).

::: {.proof}
An \(L^2\)-function is finite almost everywhere; otherwise the integral of its square would be infinite.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>10 proves \(g\in L^2\), and step <1>11 gives the almost-everywhere finiteness.
:::
:::
