---
schema: qual/card@1
id: P-TIE-F09-07
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 7.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and labelled the parts against Fall 2009, question 7, page 2 of Questions_from_Tie.pdf, and quoted the formula of question 6 that the statement cites as the previous question.
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

::: {.solution}

For $t>0$ and $s\in\CC$, write
$$
t^{s-1}=e^{(s-1)\log t},
$$
where $\log t$ is the real logarithm.

::: pf

::: {.pf-step #s1-1}

For $0<\varepsilon<R<\infty$, the function
$$
\Gamma_{\varepsilon,R}(s)
=
\int_\varepsilon^R e^{-t}t^{s-1}\,dt
$$
is entire in $s$.


::: pf-proof

On the compact interval $[\varepsilon,R]$, the function
$$
(s,t)\longmapsto e^{-t}e^{(s-1)\log t}
$$
is continuous and entire in $s$ for each fixed $t$. On every compact subset of the
$s$-plane, its $s$-derivatives are uniformly bounded on $[\varepsilon,R]$. Hence
differentiation under the finite integral is valid and gives
$$
\Gamma_{\varepsilon,R}'(s)
=
\int_\varepsilon^R e^{-t}t^{s-1}\log t\,dt.
$$
Thus $\Gamma_{\varepsilon,R}$ is entire.

:::

:::

::: {.pf-step #s1-2}

The improper integrals
$$
\int_0^\infty e^{-t}t^{s-1}\,dt
$$
converge uniformly for $s$ in every compact subset of
$$
H=\{s\in\CC:\Re s>0\}.
$$


::: pf-proof

Let $K\subset H$ be compact. Put
$$
\delta=\min_{s\in K}\Re s>0,
\qquad
M=\max_{s\in K}\Re s.
$$
For $0<t\le1$ and $s\in K$,
$$
\abs{e^{-t}t^{s-1}}
\le
t^{\delta-1},
$$
and
$$
\int_0^1 t^{\delta-1}\,dt<\infty.
$$
For $t\ge1$ and $s\in K$,
$$
\abs{e^{-t}t^{s-1}}
\le
e^{-t}t^{M-1},
$$
whose integral over $[1,\infty)$ is finite. The two majorants give uniform control of the
tails at $0$ and at $\infty$, uniformly for $s\in K$.

:::

:::

::: {.pf-step #s1-3}

The function
$$
\boxed{
\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt
}
$$
is analytic on $\Re s>0$.


::: pf-proof

Choose sequences $\varepsilon_j\downarrow0$ and $R_j\uparrow\infty$. By step [](#s1-2){.pf-ref},
$$
\Gamma_{\varepsilon_j,R_j}(s)
\longrightarrow
\int_0^\infty e^{-t}t^{s-1}\,dt
$$
uniformly on every compact subset of $H$. Each truncated function is entire by step [](#s1-1){.pf-ref}.
The locally uniform limit of analytic functions is analytic, so the displayed integral defines
an analytic function on $H$. For real $s>0$ it is the original defining integral, hence this is
the analytic extension of the gamma function.

:::

:::

::: {.pf-step #s1-4}

For real $0<s<1$ and every $t>0$,
$$
\Gamma(1-s)
=
t\int_0^\infty e^{-vt}(vt)^{-s}\,dv.
$$


::: pf-proof

Starting from step [](#s1-3){.pf-ref},
$$
\Gamma(1-s)
=
\int_0^\infty e^{-u}u^{-s}\,du.
$$
Substitute $u=vt$, so $du=t\,dv$. This gives exactly the stated formula.

:::

:::

::: {.pf-step #s1-5}

For real $0<s<1$,
$$
\Gamma(s)\Gamma(1-s)
=
\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
$$


::: pf-proof

Using step [](#s1-4){.pf-ref},
$$
\begin{aligned}
\Gamma(s)\Gamma(1-s)
&=
\int_0^\infty
e^{-t}t^{s-1}
\left(
t\int_0^\infty e^{-vt}(vt)^{-s}\,dv
\right)dt\\
&=
\int_0^\infty\int_0^\infty
e^{-(1+v)t}v^{-s}\,dv\,dt.
\end{aligned}
$$
For real $0<s<1$ the integrand is nonnegative, so Tonelli's theorem permits reversing the
order of integration. Therefore
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

::: {.pf-step #s1-6}

For real $0<s<1$,
$$
\Gamma(s)\Gamma(1-s)
=
\boxed{\frac{\pi}{\sin\pi s}}.
$$


::: pf-proof

The formula quoted from the preceding problem, with $n=1$ and $a=1-s$, gives
$$
\int_0^\infty\frac{v^{-s}}{1+v}\,dv
=
\frac{\pi}{\sin(\pi(1-s))}
=
\frac{\pi}{\sin\pi s}.
$$
Combine this with step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The reflection formula holds for every complex $s$ with
$$
0<\Re s<1.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, both $\Gamma(s)$ and $\Gamma(1-s)$ are analytic on the strip
$0<\Re s<1$. Since $\sin\pi s$ has no zero in this open strip, so is
$$
\frac{\pi}{\sin\pi s}.
$$
Step [](#s1-6){.pf-ref} proves equality on the real interval $(0,1)$, which has accumulation points inside
the strip. The identity theorem therefore gives the equality throughout the strip.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove part (b).

:::

:::

:::
