---
title: Differentiability
order: 35
topics:
- Differentiation
- Mean Value Theorem
---

# Differentiability

By the mean value theorem, a differentiable function with $\abs{f'}\leq C$ on an interval is $C$-Lipschitz there.
Differentiating a series term by term requires uniform convergence of the series of derivatives and convergence of the series at one point.

[[T-OXNTU]]

[[T-DS4VW]]

[[PR-LTRLV]]

[[FR-EDJWQ]]

[[T-TR526]]

::: {.example title="A bounded differentiable function with unbounded derivative"}
On $[-1,1]$ let
$$
f(x) \coloneqq
\begin{cases}
x^2 \sin\qty{1\over x^2}, & x\neq 0,
\\
0, & x=0.
\end{cases}
$$
Then $\abs f\leq1$, and $f$ is differentiable at $0$ since $\abs{f(h) - f(0)}/\abs h = \abs{ h\sin\qty{h^{-2}}}\leq \abs{h}\to 0$.
For $x\neq0$,
$$
f'(x) = 2x\sin\qty{1\over x^2 } - {2\over x}\cos\qty{1\over x^2}.
$$
For $x_k \coloneqq 1/\sqrt{k\pi}$,
$$
f'(x_k)=-2\sqrt{k\pi}(-1)^k,
\qquad
\abs{f'(x_k)}=2\sqrt{k\pi}\longrightarrow\infty,
$$
so $f'$ is unbounded on $[-1,1]$.

:::
