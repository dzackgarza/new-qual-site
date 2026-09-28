---
schema: qual/card@1
id: P-BKS08-6B
kind: problem
title: An orthogonality condition forced by a decaying ODE solution
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the exact derivative identity and the boundary-term
    limit giving the source's orthogonality condition.
---

::: {.problem}
Let $y:[0,\infty)\to\mathbb R$ be smooth and satisfy
$$
y''-y=f(x)\qquad(x>0),
$$
with
$$
y(0)=y'(0)=0,
$$
and suppose $y(x)\to0$ and $y'(x)\to0$ as $x\to\infty$. Here $f$ is continuous on $[0,\infty)$ and vanishes for $x>1$.

Find a nonzero function $g$, independent of $y$ and $f$, such that
$$
\int_0^1 f(x)g(x)\,dx=0.
$$
:::

::: {.solution}
Take
$$
\boxed{g(x)=e^{-x}}.
$$

<1>1. For every $x>0$,
$$
\frac{d}{dx}\left(e^{-x}(y'(x)+y(x))\right)
=e^{-x}f(x).
$$

::: {.proof}
Using the differential equation,
$$
\begin{aligned}
\frac{d}{dx}\left(e^{-x}(y'+y)\right)
&=-e^{-x}(y'+y)+e^{-x}(y''+y')\\
&=e^{-x}(y''-y)\\
&=e^{-x}f.
\end{aligned}
$$
:::

<1>2. For every $L>0$,
$$
\int_0^L e^{-x}f(x)\,dx
=e^{-L}(y'(L)+y(L)).
$$

::: {.proof}
Integrate the identity in step <1>1 from $0$ to $L$. The lower
boundary term is
$$
y'(0)+y(0)=0
$$
by the initial conditions.
:::

<1>3. One has
$$
\int_0^\infty e^{-x}f(x)\,dx=0.
$$

::: {.proof}
By hypothesis,
$$
y(L)\longrightarrow0
\qquad\text{and}\qquad
y'(L)\longrightarrow0.
$$
Hence the right-hand side of step <1>2 tends to $0$ as
$L\to\infty$. Taking the limit gives the displayed identity.
:::

<1>4. Since $f(x)=0$ for $x>1$,
$$
\boxed{
\int_0^1 f(x)e^{-x}\,dx=0.
}
$$

::: {.proof}
The integral in step <1>3 equals the integral over $[0,1]$ because
$f$ vanishes on $(1,\infty)$.
:::

<1>5. The function $g(x)=e^{-x}$ is nonzero and is independent of
$y$ and $f$.

::: {.proof}
The exponential $e^{-x}$ is positive for every $x\ge0$ and was chosen
without reference to either $y$ or $f$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4--<1>5 give the required function and orthogonality identity.
:::
:::
