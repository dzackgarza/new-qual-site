---
schema: qual/card@1
id: P-AZOFF-D06
kind: problem
title: Fourier transforms of compactly supported continuous functions are entire
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    PDF vector inspection confirms that the source itself prints the
    proper-subset symbol in "for each z subset C". Since z is the variable of
    the function being defined, the intended relation is z in C; the card
    corrects that typographical error.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Restricted the integral to a compact interval containing the support.
    For each z_0, the exponential difference quotient converges uniformly in
    t on that interval to -it e^{-iz_0t}; uniform convergence therefore
    permits passage through the integral and gives a complex derivative at
    every z_0. The source contains no worked solution.
---

::: {.problem}
Suppose that $f$ is a continuous function on $\RR$ which vanishes outside some finite interval and for each $z \in \mathbb { C }$ define

$$
g ( z ) = \int _ { - \infty } ^ { \infty } f ( t ) \exp ( - i z t ) d t .
$$

Show that $g$ is entire.
:::

::: {.solution}
Choose $A>0$ such that
$$
f(t)=0
$$
whenever
$$
\abs t>A.
$$
Then
$$
g(z)
=
\int_{-A}^{A}f(t)e^{-izt}\,dt.
$$

<1>1. Fix $z_0\in\CC$. For $h\neq0$,
$$
\frac{g(z_0+h)-g(z_0)}h
=
\int_{-A}^{A}
f(t)e^{-iz_0t}
\frac{e^{-iht}-1}{h}
\,dt.
$$

::: {.proof}
By the compact-support reduction above,
$$
\begin{aligned}
g(z_0+h)-g(z_0)
&=
\int_{-A}^{A}
f(t)
\bigl(e^{-i(z_0+h)t}-e^{-iz_0t}\bigr)
\,dt\\
&=
\int_{-A}^{A}
f(t)e^{-iz_0t}
\bigl(e^{-iht}-1\bigr)
\,dt.
\end{aligned}
$$
Divide by the nonzero complex number $h$.
:::

<1>2. As $h\to0$,
$$
\frac{e^{-iht}-1}{h}
\longrightarrow
-it
$$
uniformly for
$$
t\in[-A,A].
$$

::: {.proof}
Define the entire function
$$
\Phi(w)
=
\begin{cases}
\dfrac{e^w-1}{w},&w\neq0,\\
1,&w=0.
\end{cases}
$$
Then
$$
\frac{e^{-iht}-1}{h}
=
-it\,\Phi(-iht).
$$
For
$$
\abs t\leq A,
$$
one has
$$
\abs{-iht}\leq A\abs h\longrightarrow0
$$
uniformly in $t$. Since $\Phi$ is continuous at $0$,
$$
\sup_{\abs t\leq A}
\abs{\Phi(-iht)-1}
\longrightarrow0.
$$
Multiplying by $\abs t\leq A$ gives the claimed uniform convergence.
:::

<1>3. The integrands in step <1>1 converge uniformly on $[-A,A]$ to
$$
-it\,f(t)e^{-iz_0t}.
$$

::: {.proof}
The continuous function
$$
t\longmapsto f(t)e^{-iz_0t}
$$
is bounded on the compact interval $[-A,A]$. Multiplying the uniform
convergence from step <1>2 by this bounded factor preserves uniform
convergence.
:::

<1>4. The complex derivative of $g$ exists at $z_0$ and is
$$
g'(z_0)
=
\int_{-A}^{A}
(-it)f(t)e^{-iz_0t}\,dt.
$$

::: {.proof}
Uniform convergence of the integrands in step <1>3 allows the limit to pass
through the Riemann integral in step <1>1. Hence
$$
\begin{aligned}
g'(z_0)
&=
\lim_{h\to0}
\frac{g(z_0+h)-g(z_0)}h\\
&=
\int_{-A}^{A}
(-it)f(t)e^{-iz_0t}\,dt.
\end{aligned}
$$
:::

<1>5. The function $g$ is entire.

::: {.proof}
The point $z_0\in\CC$ was arbitrary. Step <1>4 shows that the complex
derivative exists at every point of $\CC$. Therefore $g$ is entire.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
