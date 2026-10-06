---
schema: qual/card@1
id: P-PRECALC1-24
kind: problem
title: Limit of $\frac1x\int_0^x(1+\sin 2t)^{1/t}\,dt$ as $x\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Calculate
\[
\lim_{x\to0}\frac1x\int_0^x(1+\sin(2t))^{1/t}\,dt.
\]
:::

::: {.solution}
For \(t\ne0\) near \(0\), define
\[
g(t)
=
(1+\sin(2t))^{1/t}.
\]

<1>1. For \(t\) sufficiently close to \(0\),
\[
\boxed{
1+\sin(2t)>0}.
\]

::: {.proof}
Since
\[
\sin(2t)\to0,
\]
one has
\[
1+\sin(2t)\to1>0.
\]
Therefore the base is positive in some neighborhood of \(0\).
:::

<1>2. Taking logarithms,
\[
\boxed{
\log g(t)
=
\frac{\log(1+\sin(2t))}{t}}.
\]

::: {.proof}
Use
\[
\log(a^{1/t})
=
\frac1t\log a
\]
for the positive base from step <1>1.
:::

<1>3. Factor the logarithmic quotient:
\[
\frac{\log(1+\sin(2t))}{t}
=
\frac{\log(1+\sin(2t))}{\sin(2t)}
\cdot
\frac{\sin(2t)}{2t}
\cdot2.
\]

::: {.proof}
Multiply and divide by \(\sin(2t)\) and \(2t\).
:::

<1>4. One has
\[
\boxed{
\lim_{u\to0}
\frac{\log(1+u)}{u}
=
1}.
\]

::: {.proof}
This is the standard logarithmic limit, equivalently the derivative of
\(\log(1+u)\) at \(u=0\).
:::

<1>5. Therefore
\[
\lim_{t\to0}
\frac{\log(1+\sin(2t))}{\sin(2t)}
=
1.
\]

::: {.proof}
Since
\[
\sin(2t)\to0,
\]
apply step <1>4 with
\[
u=\sin(2t).
\]
:::

<1>6. Also,
\[
\boxed{
\lim_{t\to0}
\frac{\sin(2t)}{2t}
=
1}.
\]

::: {.proof}
This is the standard limit
\[
\frac{\sin u}{u}\to1
\]
with \(u=2t\).
:::

<1>7. Hence
\[
\boxed{
\lim_{t\to0}\log g(t)=2}.
\]

::: {.proof}
Take limits in step <1>3 using steps <1>5--<1>6.
:::

<1>8. Exponentiating,
\[
\boxed{
\lim_{t\to0}g(t)=e^2}.
\]

::: {.proof}
The exponential function is continuous, so step <1>7 gives
\[
g(t)
=
e^{\log g(t)}
\to
e^2.
\]
:::

<1>9. Extend \(g\) continuously to \(t=0\) by defining
\[
\boxed{
g(0)=e^2}.
\]

::: {.proof}
Step <1>8 shows that this removes the singularity at \(t=0\).
:::

<1>10. For \(x\ne0\) sufficiently close to \(0\), the integral mean-value
theorem gives a point \(c_x\) between \(0\) and \(x\) such that
\[
\boxed{
\frac1x\int_0^x g(t)\,dt
=
g(c_x)}.
\]

::: {.proof}
The extended function \(g\) is continuous near \(0\). If \(x>0\), apply the
integral mean-value theorem on \([0,x]\). If \(x<0\), apply it on \([x,0]\):
\[
\int_x^0 g(t)\,dt
=
g(c_x)(0-x),
\]
which is equivalent to the displayed identity after changing signs.
:::

<1>11. As \(x\to0\),
\[
\boxed{c_x\to0}.
\]

::: {.proof}
The point \(c_x\) lies between \(0\) and \(x\), so
\[
|c_x|\le|x|.
\]
:::

<1>12. Therefore
\[
\lim_{x\to0}
\frac1x
\int_0^x
(1+\sin(2t))^{1/t}\,dt
=
e^2.
\]

::: {.proof}
By step <1>10, the quotient equals \(g(c_x)\). By step <1>11,
\[
c_x\to0,
\]
and by continuity of the extension in step <1>9,
\[
g(c_x)\to g(0)=e^2.
\]
:::

<1>13. Hence
\[
\boxed{
\lim_{x\to0}
\frac1x
\int_0^x
(1+\sin(2t))^{1/t}\,dt
=
e^2}.
\]

::: {.proof}
This is step <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the requested limit.
:::
:::
