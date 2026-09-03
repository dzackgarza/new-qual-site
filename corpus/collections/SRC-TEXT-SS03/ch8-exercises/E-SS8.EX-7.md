---
schema: qual/card@1
id: E-SS8.EX-7
kind: problem
title: "Provide all the details in the proof of the formula for the solution of the Diri"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
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

<1>1. The conformal map $G$ from the strip $\{0 < \operatorname{Im} z < 1\}$ to the unit disk sends $z = iy$ to $G(iy) = r e^{i\theta}$.
::: {.proof}
setup from Section 1.3.
:::

<1>2. $G(iy) = i \frac{\cos \pi y}{1 + \sin \pi y}$.
::: {.proof}
the explicit formula for the strip-to-disk map evaluated on the imaginary axis.
:::

<1>3. For $0 < y \le 1/2$, $\cos \pi y \ge 0$ and $1 + \sin \pi y > 0$, so $G(iy)$ is purely imaginary with positive imaginary part, giving $\theta = \pi/2$.
::: {.proof}
<1>2, reading off the argument.
:::

<1>4. For $1/2 \le y < 1$, $\cos \pi y \le 0$, so $G(iy)$ is purely imaginary with negative imaginary part, giving $\theta = -\pi/2$.
::: {.proof}
<1>2.
:::

<1>5. $r^2 = |G(iy)|^2 = \frac{\cos^2 \pi y}{(1 + \sin \pi y)^2} = \frac{1 - \sin^2 \pi y}{(1 + \sin \pi y)^2} = \frac{1 - \sin \pi y}{1 + \sin \pi y}$.
::: {.proof}
<1>2 and $\cos^2 = 1 - \sin^2$.
:::

<1>6. The Poisson kernel is $P_r(\theta - \varphi) = \frac{1 - r^2}{1 - 2r\cos(\theta - \varphi) + r^2}$.
::: {.proof}
definition of the Poisson kernel.
:::

<1>7. Substituting $r^2 = \frac{1 - \sin \pi y}{1 + \sin \pi y}$ and $\theta = \pm \pi/2$ (so $\cos(\theta - \varphi) = \pm \sin \varphi$), one obtains
$$P_r(\theta - \varphi) = \frac{\sin \pi y}{1 - \cos \pi y \sin \varphi}.$$
::: {.proof}
<1>5 and <1>6, simplifying the resulting expression.
:::

**(b).**

<1>1. The change of variables is $t = F(e^{i\varphi})$, where $F$ is the inverse of the map $t \mapsto \frac{i - e^{\pi t}}{i + e^{\pi t}}$.
::: {.proof}
setup.
:::

<1>2. $e^{i\varphi} = \frac{i - e^{\pi t}}{i + e^{\pi t}}$.
::: {.proof}
given.
:::

<1>3. Taking imaginary parts: $\sin \varphi = \operatorname{Im}\left(\frac{i - e^{\pi t}}{i + e^{\pi t}}\right) = \frac{1}{\cosh \pi t}$.
::: {.proof}
rationalizing the denominator and using $\operatorname{Im}$.
:::

<1>4. Differentiating <1>2 with respect to $t$ and taking imaginary parts gives $\frac{d\varphi}{dt} = \frac{\pi}{\cosh \pi t}$.
::: {.proof}
implicit differentiation of the identity in <1>2.
:::

<1>5. Substituting <1>3 and <1>4 into the integral, and using $\tilde f_0(\varphi) = f_0(t)$,
$$\frac{1}{2\pi}\int_0^\pi P_r(\theta - \varphi)\tilde f_0(\varphi)\,d\varphi = \frac{\sin \pi y}{2}\int_{-\infty}^{\infty} \frac{f_0(t)}{\cosh \pi t - \cos \pi y}\,dt.$$
::: {.proof}
<1>7 (a), <1>3, <1>4, and the change of variables.
:::

**(c).**

<1>1. The same argument with $\theta = -\pi/2$ and $\tilde f_1$ in place of $\tilde f_0$ gives
$$\frac{1}{2\pi}\int_{-\pi}^0 P_r(\theta - \varphi)\tilde f_1(\varphi)\,d\varphi = \frac{\sin \pi y}{2}\int_{-\infty}^{\infty} \frac{f_1(t)}{\cosh \pi t - \cos \pi y}\,dt.$$
::: {.proof}
identical computation to (b), with the lower half of the circle.
:::

<1>2. Q.E.D.
::: {.proof}
<1>5 (a), <1>5 (b), <1>1 (c).
:::
:::
