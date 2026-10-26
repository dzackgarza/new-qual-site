---
schema: qual/card@1
id: P-TIE-S14-07
kind: problem
title: Analyticity of the gamma function and the reflection formula
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 7.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and labelled the parts against Spring 2014, question 7, pages 7-8 of Questions_from_Tie.pdf, and quoted the formula of question 6 that the statement cites as the previous question.
---

::: {.problem}
For $s > 0$, the **gamma function** is defined by $\Gamma(s) = \int_0^\infty e^{-t} t^{s-1}\,dt$.

(a) Show that the gamma function is analytic in the half-plane $\operatorname{Re}(s) > 0$, and is still given there by the integral formula above.

(b) Apply the formula in the previous question to show that
$$
\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin \pi s}.
$$

Hint: You may need $\Gamma(1-s) = t\int_0^\infty e^{-vt}(vt)^{-s}\,dv$ for $t > 0$.
:::

::: {.remark}
"The formula in the previous question" refers to the question printed immediately before this one in the source (question 6):
$$
\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = \frac{\pi}{n\sin\frac{a\pi}{n}}, \qquad 0 < a < n,\ n \text{ a positive integer}.
$$
With $n = 1$ and $a = 1 - s$ for $0 < s < 1$ it reads $\int_0^\infty \frac{v^{-s}}{1+v}\,dv = \frac{\pi}{\sin \pi s}$, which the hint turns into the reflection formula.
:::

For $t>0$ and complex $s$, write
$$
t^{s-1}\coloneqq e^{(s-1)\log t},
$$
where $\log t$ is the real logarithm.

::: pf

::: {.pf-step #s1-1}

For every compact set
$$
K\subset\{s\in\CC:\operatorname{Re}(s)>0\},
$$
the integral
$$
\int_0^\infty e^{-t}t^{s-1}\,dt
$$
converges uniformly for $s\in K$.


::: pf-proof

Let
$$
\sigma_0\coloneqq\min_{s\in K}\operatorname{Re}(s)>0,
\qquad
\sigma_1\coloneqq\max_{s\in K}\operatorname{Re}(s).
$$
For $0<t\le1$ and $s\in K$,
$$
\abs{e^{-t}t^{s-1}}
=
e^{-t}t^{\operatorname{Re}(s)-1}
\le
t^{\sigma_0-1},
$$
and $t^{\sigma_0-1}$ is integrable on $(0,1]$. For $t\ge1$,
$$
\abs{e^{-t}t^{s-1}}
\le
e^{-t}t^{\sigma_1-1},
$$
which is integrable on $[1,\infty)$. The two bounds are independent of $s\in K$, so the improper integral converges uniformly on $K$ by the Weierstrass criterion for improper integrals.

:::

:::

::: {.pf-step #s1-2}

The function
$$
\Gamma(s)
\coloneqq
\int_0^\infty e^{-t}t^{s-1}\,dt
$$
is analytic on the half-plane $\operatorname{Re}(s)>0$.


::: pf-proof

For $0<\varepsilon<R<\infty$, define
$$
\Gamma_{\varepsilon,R}(s)
\coloneqq
\int_\varepsilon^R e^{-t}e^{(s-1)\log t}\,dt.
$$
On the finite interval $[\varepsilon,R]$, the integrand is entire in $s$ and continuous jointly in $(s,t)$; differentiation under the integral sign gives
$$
\Gamma_{\varepsilon,R}'(s)
=
\int_\varepsilon^R
e^{-t}e^{(s-1)\log t}\log t\,dt,
$$
so $\Gamma_{\varepsilon,R}$ is entire. By step [](#s1-1){.pf-ref}, as $\varepsilon\downarrow0$ and $R\to\infty$, these functions converge uniformly on every compact subset of $\operatorname{Re}(s)>0$ to $\Gamma(s)$. A locally uniform limit of holomorphic functions is holomorphic, so $\Gamma$ is analytic on the half-plane.

:::

:::

::: {.pf-step #s1-3}

For real $s$ with $0<s<1$,
$$
\Gamma(s)\Gamma(1-s)
=
\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
$$


::: pf-proof

For $t>0$, the substitution $u=vt$ in the defining integral for $\Gamma(1-s)$ gives
$$
\Gamma(1-s)
=
t\int_0^\infty e^{-vt}(vt)^{-s}\,dv.
$$
Therefore
$$
\begin{aligned}
\Gamma(s)\Gamma(1-s)
&=
\int_0^\infty
e^{-t}t^{s-1}
\left[
t\int_0^\infty e^{-vt}(vt)^{-s}\,dv
\right]dt\\
&=
\int_0^\infty\int_0^\infty
e^{-(1+v)t}v^{-s}\,dv\,dt.
\end{aligned}
$$
For real $0<s<1$ the integrand is nonnegative, so Tonelli's theorem permits reversing the order:
$$
\begin{aligned}
\Gamma(s)\Gamma(1-s)
&=
\int_0^\infty
v^{-s}
\left(
\int_0^\infty e^{-(1+v)t}\,dt
\right)dv\\
&=
\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For real $0<s<1$,
$$
\Gamma(s)\Gamma(1-s)
=
\frac{\pi}{\sin\pi s}.
$$


::: pf-proof

The formula quoted in the remark, with $n=1$ and $a=1-s$, gives
$$
\int_0^\infty\frac{v^{-s}}{1+v}\,dv
=
\frac{\pi}{\sin\pi(1-s)}
=
\frac{\pi}{\sin\pi s}.
$$
Combine this with step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The reflection formula
$$
\boxed{
\Gamma(s)\Gamma(1-s)
=
\frac{\pi}{\sin\pi s}
}
$$
holds for every $s$ with
$$
0<\operatorname{Re}(s)<1.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, both $\Gamma(s)$ and $\Gamma(1-s)$ are analytic on the strip $0<\operatorname{Re}(s)<1$. The function $\pi/\sin\pi s$ is analytic there as well, because the zeros of $\sin\pi s$ are the integers and no integer lies in the strip. Step [](#s1-4){.pf-ref} shows that the two analytic functions agree for every real $s\in(0,1)$. This set has accumulation points in the strip, so the identity theorem implies equality throughout the strip.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b) on the natural domain where both gamma factors are defined by the integral from part (a).

:::

:::
