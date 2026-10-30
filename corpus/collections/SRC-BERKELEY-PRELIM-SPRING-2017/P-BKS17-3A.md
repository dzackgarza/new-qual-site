---
schema: qual/card@1
id: P-BKS17-3A
kind: problem
title: Positive functions satisfying $\int_x^y f(x)f(y)/f(t)^2\,dt=\sin(y-x)$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 4 problem 3A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 solution and filled in the deduction from the three-point identity to the sine form.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the interval-additivity identity, the sine/cosine linear-combination argument, positivity at both endpoint limits, and direct substitution of all solutions.
---

::: {.problem}
Suppose we have a continuous positive function $f : (0, \pi) \to (0, \infty)$ such that for all $x, y \in (0, \pi)$ we have

$$
\int_x^y \frac{f(x) f(y)}{f^2(t)} \, dt = \sin(y - x).
$$

(a) Show that $\sin(z - x) f(y) = \sin(y - x) f(z) + \sin(z - y) f(x)$.

(b) Find all possibilities for $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $u,v\in(0,\pi)$,
$$
\int_u^v\frac{dt}{f(t)^2}
=
\frac{\sin(v-u)}{f(u)f(v)}.
$$


::: pf-proof

This is the given identity divided by the positive number $f(u)f(v)$.

:::

:::

::: {.pf-step #s1-2}

For every $x,y,z\in(0,\pi)$,
$$
\sin(z-x)f(y)
=
\sin(y-x)f(z)
+
\sin(z-y)f(x).
$$


::: pf-proof

By additivity of the integral and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\frac{\sin(z-x)}{f(x)f(z)}
&=
\int_x^z\frac{dt}{f(t)^2}\\
&=
\int_x^y\frac{dt}{f(t)^2}
+
\int_y^z\frac{dt}{f(t)^2}\\
&=
\frac{\sin(y-x)}{f(x)f(y)}
+
\frac{\sin(z-y)}{f(y)f(z)}.
\end{aligned}
$$
Multiplying by the positive product $f(x)f(y)f(z)$ gives the displayed identity.

:::

:::

::: {.pf-step #s1-3}

There exist constants $A,B\in\RR$ such that
$$
f(y)=A\sin y+B\cos y
$$
for every $y\in(0,\pi)$.


::: pf-proof

Choose distinct $x,z\in(0,\pi)$. Since $0<\abs{z-x}<\pi$,
$$
\sin(z-x)\ne0.
$$
Solving the identity in step [](#s1-2){.pf-ref} for $f(y)$ and expanding the two sine differences gives
$$
\begin{aligned}
f(y)
&=
\frac{f(z)\sin(y-x)+f(x)\sin(z-y)}{\sin(z-x)}\\
&=
\frac{f(z)\cos x-f(x)\cos z}{\sin(z-x)}\sin y
+
\frac{f(x)\sin z-f(z)\sin x}{\sin(z-x)}\cos y.
\end{aligned}
$$
The two coefficients are constants independent of $y$; call them $A$ and $B$.

:::

:::

::: {.pf-step #s1-4}

Positivity of $f$ forces
$$
B=0
\qquad\text{and}\qquad
A>0.
$$


::: pf-proof

The formula in step [](#s1-3){.pf-ref} extends continuously to the endpoints. Since $f(y)>0$ for every $0<y<\pi$,
$$
\lim_{y\downarrow0}f(y)=B\geq0.
$$
Likewise,
$$
\lim_{y\uparrow\pi}f(y)=-B\geq0.
$$
Thus $B=0$. Then
$$
f(y)=A\sin y.
$$
Since $\sin y>0$ on $(0,\pi)$ and $f$ is positive there, one must have $A>0$.

:::

:::

::: {.pf-step #s1-5}

Every function
$$
f(y)=a\sin y,
\qquad a>0,
$$
satisfies the given integral identity.


::: pf-proof

For $x,y\in(0,\pi)$,
$$
\begin{aligned}
\int_x^y\frac{f(x)f(y)}{f(t)^2}\,dt
&=
\sin x\sin y\int_x^y\csc^2t\,dt\\
&=
\sin x\sin y\,[ -\cot t ]_x^y\\
&=
\cos x\sin y-\sin x\cos y\\
&=
\sin(y-x).
\end{aligned}
$$
The constant $a$ cancels from the quotient.

:::

:::

::: {.pf-step #s1-6}

The complete set of possibilities is
$$
\boxed{f(y)=a\sin y\quad(a>0)}.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} show that every solution has this form, and step [](#s1-5){.pf-ref} shows that every such function is a solution.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
