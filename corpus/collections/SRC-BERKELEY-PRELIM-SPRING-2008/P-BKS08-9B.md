---
schema: qual/card@1
id: P-BKS08-9B
kind: problem
title: Fourth derivative of x over sine x at zero
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
    Independently checked the Taylor inversion through degree four and the
    resulting fourth derivative against the vendored solution.
---

::: {.problem}
Compute
\[
\lim_{x\to0}\frac{d^4}{dx^4}\left(\frac{x}{\sin x}\right).
\]
:::

::: {.solution}
Let
$$
f(x)=\frac{x}{\sin x}
$$
for $x\ne0$.

<1>1. The singularity of $f$ at $0$ is removable, and the extension
with $f(0)=1$ is analytic near $0$.

::: {.proof}
Write
$$
\frac{\sin x}{x}
=1-\frac{x^2}{6}+\frac{x^4}{120}+O(x^6).
$$
The function $\sin x/x$, extended by the value $1$ at $0$, is
analytic and nonzero in a neighborhood of $0$. Its reciprocal is
therefore analytic there and equals the removable extension of
$x/\sin x$.
:::

<1>2. Near $0$,
$$
f(x)
=1+\frac{x^2}{6}+\frac{7x^4}{360}+O(x^6).
$$

::: {.proof}
Set
$$
u(x)=\frac{x^2}{6}-\frac{x^4}{120}+O(x^6).
$$
Then
$$
\frac{\sin x}{x}=1-u(x),
$$
so
$$
\frac1{1-u}=1+u+u^2+O(u^3).
$$
Since $u=O(x^2)$,
$$
\begin{aligned}
f(x)
&=1+
\left(\frac{x^2}{6}-\frac{x^4}{120}\right)
+\frac{x^4}{36}
+O(x^6)\\
&=1+\frac{x^2}{6}
+\left(\frac1{36}-\frac1{120}\right)x^4
+O(x^6)\\
&=1+\frac{x^2}{6}+\frac{7x^4}{360}+O(x^6).
\end{aligned}
$$
:::

<1>3. The fourth derivative of the analytic extension at $0$ is
$$
f^{(4)}(0)=\frac{7}{15}.
$$

::: {.proof}
For an analytic function, the coefficient of $x^4$ in its Taylor
series at $0$ is $f^{(4)}(0)/4!$. By step <1>2,
$$
\frac{f^{(4)}(0)}{4!}=\frac7{360},
$$
and therefore
$$
f^{(4)}(0)
=24\cdot\frac7{360}
=\frac7{15}.
$$
:::

<1>4. Hence
$$
\boxed{
\lim_{x\to0}\frac{d^4}{dx^4}
\left(\frac{x}{\sin x}\right)
=\frac7{15}.
}
$$

::: {.proof}
By step <1>1, the removable extension of $f$ is analytic near $0$.
Therefore $f^{(4)}$ is continuous at $0$. The required limit is thus
$f^{(4)}(0)$, whose value is given by step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested evaluation.
:::
:::
