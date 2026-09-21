---
schema: qual/card@1
id: P-AZOFF-A03
kind: problem
title: A differentiable function with discontinuous derivative
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Verified directly that the piecewise function x^2 sin(1/x^2), extended by
    0 at the origin, is differentiable at 0 with derivative 0. Away from 0
    its derivative is explicit, and along x_n=(2 pi n)^(-1/2) the derivative
    tends to negative infinity, proving discontinuity at 0. The source
    compilation contains no worked solution for this problem.
---

::: {.problem}
Give an example of a function $f:\mathbb R\to\mathbb R$ that is differentiable everywhere but whose derivative $f'$ is not continuous at $0$.
:::

::: {.solution}
Define
$$
f(x)=
\begin{cases}
x^2\sin(1/x^2),&x\neq0,\\
0,&x=0.
\end{cases}
$$

<1>1. The function $f$ is differentiable at every $x\neq0$, with
$$
f'(x)
=
2x\sin(1/x^2)
-
\frac{2}{x}\cos(1/x^2).
$$

::: {.proof}
On $\RR\sm\{0\}$, the function is a product and composition of differentiable
functions. The product and chain rules give
$$
\begin{aligned}
f'(x)
&=
2x\sin(1/x^2)
+
x^2\cos(1/x^2)\left(-\frac{2}{x^3}\right)\\
&=
2x\sin(1/x^2)
-
\frac{2}{x}\cos(1/x^2).
\end{aligned}
$$
:::

<1>2. The function $f$ is differentiable at $0$, and
$$
f'(0)=0.
$$

::: {.proof}
By the definition of the derivative,
$$
\frac{f(h)-f(0)}{h}
=
h\sin(1/h^2)
$$
for $h\neq0$. Since
$$
\abs{h\sin(1/h^2)}
\leq
\abs h
\longrightarrow
0,
$$
we obtain
$$
f'(0)
=
\lim_{h\to0}\frac{f(h)-f(0)}h
=
0.
$$
:::

<1>3. The derivative $f'$ is not continuous at $0$.

::: {.proof}
For $n\geq1$, put
$$
x_n=\frac{1}{\sqrt{2\pi n}}.
$$
Then $x_n\to0$ and
$$
\frac{1}{x_n^2}=2\pi n.
$$
By step <1>1,
$$
\begin{aligned}
f'(x_n)
&=
2x_n\sin(2\pi n)
-
\frac{2}{x_n}\cos(2\pi n)\\
&=
-\frac{2}{x_n}.
\end{aligned}
$$
Thus
$$
f'(x_n)\longrightarrow-\infty,
$$
whereas step <1>2 gives $f'(0)=0$. Hence $f'(x_n)$ does not converge to
$f'(0)$, so $f'$ is not continuous at $0$.
:::

<1>4. The displayed $f$ is an everywhere differentiable function whose
derivative is discontinuous at $0$.

::: {.proof}
Steps <1>1--<1>2 prove differentiability on all of $\RR$, and step <1>3 proves
the required discontinuity.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies the requested example.
:::
:::
