---
schema: qual/card@1
id: E-SS8.EX-7
kind: problem
title: The solution of the Dirichlet problem in a strip
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
7. Provide all the details in the proof of the formula for the solution of the Dirichlet problem in a strip discussed in Section 1.3. Recall that it sufices to compute the solution at the points $z = i y$ with $0 < y < 1$

(a) Show that if $r e ^ { i \theta } = G ( i y )$ , then

$$
r e ^ {i \theta} = i \frac {\cos \pi y}{1 + \sin \pi y}.
$$

This leads to two separate cases: either $0 < y \le 1 / 2$ and $\theta = \pi / 2$ , or $1 / 2 \leq$

$y < 1$ and $\theta = - \pi / 2$ . In either case, show that

$$
r ^ {2} = \frac {1 - \sin \pi y}{1 + \sin \pi y} \quad \mathrm{and} \quad P _ {r} (\theta - \varphi) = \frac {\sin \pi y}{1 - \cos \pi y \sin \varphi}.
$$

(b) In the integral $\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } P _ { r } ( \theta - \varphi ) \tilde { f } _ { 0 } ( \varphi ) d \varphi } \end{array}$ make the change of variables $t =$ $F ( e ^ { i \varphi } )$ . Observe that

$$
e ^ {i \varphi} = \frac {i - e ^ {\pi t}}{i + e ^ {\pi t}},
$$

and then take the imaginary part and diferentiate both sides to establish the two identities

$$
\sin \varphi = \frac {1}{\cosh \pi t} \quad \mathrm{and} \quad \frac {d \varphi}{d t} = \frac {\pi}{\cosh \pi t}.
$$

Hence deduce that

$$
\begin{array}{r} \frac {1}{2 \pi} \int_ {0} ^ {\pi} P _ {r} (\theta - \varphi) \tilde {f} _ {0} (\varphi) d \varphi = \frac {1}{2 \pi} \int_ {0} ^ {\pi} \frac {\sin \pi y}{1 - \cos \pi y \sin \varphi} \tilde {f} _ {0} (\varphi) d \varphi \\ = \frac {\sin \pi y}{2} \int_ {- \infty} ^ {\infty} \frac {f _ {0} (t)}{\cosh \pi t - \cos \pi y} d t. \end{array}
$$

(c) Use a similar argument to prove the formula for the integra $\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { 0 } P _ { r } ( \theta - \varphi ) \tilde { f } _ { 1 } ( \varphi ) d \varphi . } \end{array}$
:::

::: {.solution}
**(a).**

::: pf

::: pf-step
The conformal map $G$ from the strip $\{0 < \operatorname{Im} z < 1\}$ to the unit disk sends $z = iy$ to $G(iy) = r e^{i\theta}$.

::: pf-proof
setup from Section 1.3.
:::

:::

::: {.pf-step #p1-s2}
$G(iy) = i \frac{\cos \pi y}{1 + \sin \pi y}$.

::: pf-proof
the explicit formula for the strip-to-disk map evaluated on the imaginary axis.
:::

:::

::: pf-step
For $0 < y \le 1/2$, $\cos \pi y \ge 0$ and $1 + \sin \pi y > 0$, so $G(iy)$ is purely imaginary with positive imaginary part, giving $\theta = \pi/2$.

::: pf-proof
Step [](#p1-s2){.pf-ref}, reading off the argument.
:::

:::

::: pf-step
For $1/2 \le y < 1$, $\cos \pi y \le 0$, so $G(iy)$ is purely imaginary with negative imaginary part, giving $\theta = -\pi/2$.

::: pf-proof
Step [](#p1-s2){.pf-ref}.
:::

:::

::: {.pf-step #p1-s5}
$r^2 = |G(iy)|^2 = \frac{\cos^2 \pi y}{(1 + \sin \pi y)^2} = \frac{1 - \sin^2 \pi y}{(1 + \sin \pi y)^2} = \frac{1 - \sin \pi y}{1 + \sin \pi y}$.

::: pf-proof
Step [](#p1-s2){.pf-ref} and $\cos^2 = 1 - \sin^2$.
:::

:::

::: {.pf-step #p1-s6}
The Poisson kernel is $P_r(\theta - \varphi) = \frac{1 - r^2}{1 - 2r\cos(\theta - \varphi) + r^2}$.

::: pf-proof
definition of the Poisson kernel.
:::

:::

::: {.pf-step #p1-s7}
Substituting $r^2 = \frac{1 - \sin \pi y}{1 + \sin \pi y}$ and $\theta = \pm \pi/2$ (so $\cos(\theta - \varphi) = \pm \sin \varphi$), one obtains
$$P_r(\theta - \varphi) = \frac{\sin \pi y}{1 - \cos \pi y \sin \varphi}.$$

::: pf-proof
Step [](#p1-s5){.pf-ref} and step [](#p1-s6){.pf-ref}, simplifying the resulting expression.
:::

:::

:::

**(b).**

::: pf

::: pf-step
The change of variables is $t = F(e^{i\varphi})$, where $F$ is the inverse of the map $t \mapsto \frac{i - e^{\pi t}}{i + e^{\pi t}}$.

::: pf-proof
setup.
:::

:::

::: {.pf-step #p2-s2}
$e^{i\varphi} = \frac{i - e^{\pi t}}{i + e^{\pi t}}$.

::: pf-proof
given.
:::

:::

::: {.pf-step #p2-s3}
Taking imaginary parts: $\sin \varphi = \operatorname{Im}\left(\frac{i - e^{\pi t}}{i + e^{\pi t}}\right) = \frac{1}{\cosh \pi t}$.

::: pf-proof
rationalizing the denominator and using $\operatorname{Im}$.
:::

:::

::: {.pf-step #p2-s4}
Differentiating step [](#p2-s2){.pf-ref} with respect to $t$ and taking imaginary parts gives $\frac{d\varphi}{dt} = \frac{\pi}{\cosh \pi t}$.

::: pf-proof
implicit differentiation of the identity in step [](#p2-s2){.pf-ref}.
:::

:::

::: {.pf-step #p2-s5}
Substituting step [](#p2-s3){.pf-ref} and step [](#p2-s4){.pf-ref} into the integral, and using $\tilde f_0(\varphi) = f_0(t)$,
$$\frac{1}{2\pi}\int_0^\pi P_r(\theta - \varphi)\tilde f_0(\varphi)\,d\varphi = \frac{\sin \pi y}{2}\int_{-\infty}^{\infty} \frac{f_0(t)}{\cosh \pi t - \cos \pi y}\,dt.$$

::: pf-proof
Step [](#p1-s7){.pf-ref} (a), step [](#p2-s3){.pf-ref}, step [](#p2-s4){.pf-ref}, and the change of variables.
:::

:::

:::

**(c).**

::: pf

::: {.pf-step #p3-s1}
The same argument with $\theta = -\pi/2$ and $\tilde f_1$ in place of $\tilde f_0$ gives
$$\frac{1}{2\pi}\int_{-\pi}^0 P_r(\theta - \varphi)\tilde f_1(\varphi)\,d\varphi = \frac{\sin \pi y}{2}\int_{-\infty}^{\infty} \frac{f_1(t)}{\cosh \pi t - \cos \pi y}\,dt.$$

::: pf-proof
identical computation to (b), with the lower half of the circle.
:::

:::

::: pf-qed
Step [](#p1-s5){.pf-ref} (a), step [](#p2-s5){.pf-ref} (b), step [](#p3-s1){.pf-ref} (c).
:::

:::

:::
