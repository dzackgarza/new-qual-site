---
schema: qual/card@1
id: P-O7DMP
kind: problem
title: $\widehat G=\bigl(\frac{\sin\pi\xi}{\pi\xi}\bigr)^2$ for the tent function
  $G$; $\widehat F$; an $L^1$ Fourier transform not in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Define
\[
F(x) &\da \qty{ \sin(\pi x) \over \pi x}^2 \\
G(x) &\da 
\begin{cases}
1 - \abs{x} & \abs{x} \leq 1
\\
0 & \text{else}.
\end{cases}
\]

a. Show that $\fourier{G}(\xi) = F(\xi)$

b. Compute $\fourier{F}$.

c. Give an example of a function $g\not \in L^1(\RR)$ which is the Fourier transform of an $L^1$ function.

*Hint: write \( \fourier{G}(\xi) = H(\xi) + H(-\xi) \)  where*
\[
H(\xi) \da e^{2\pi i \xi} \int_0^1 y e^{2\pi i y \xi }\dy 
.\]
:::
::: {.solution}
Use $\hat g(\xi) = \int g(x)e^{-2\pi i x\xi}\,dx$.

<1>1. $\hat G(\xi) = F(\xi)$.

::: {.proof}
$G$ is even, so the imaginary part of $\int_{-1}^1(1-|x|)e^{-2\pi ix\xi}\,dx$ vanishes and $\hat G(\xi) = 2\int_0^1(1-x)\cos(2\pi x\xi)\,dx$. For $a = 2\pi\xi \neq 0$, integration by parts gives $\int_0^1(1-x)\cos(ax)\,dx = \left[(1-x)\frac{\sin ax}{a}\right]_0^1 + \frac1a\int_0^1\sin(ax)\,dx = \frac{1-\cos a}{a^2}$. With $1 - \cos 2\theta = 2\sin^2\theta$ for $\theta = \pi\xi$, $\hat G(\xi) = \frac{4\sin^2(\pi\xi)}{4\pi^2\xi^2} = F(\xi)$. At $\xi = 0$ both sides equal $1$.
:::

<1>2. $\hat F = G$.

::: {.proof}
$G$ is continuous and in $L^1$, and $\hat G = F \in L^1$ since $F(\xi) \le \min(1, (\pi\xi)^{-2})$. The Fourier inversion theorem gives $G(x) = \int F(\xi)e^{2\pi ix\xi}\,d\xi = \hat F(-x)$ for every $x$. Since $G$ is even, $\hat F = G$.
:::

<1>3. $g(\xi) = \frac{\sin(2\pi\xi)}{\pi\xi}$ is the Fourier transform of $\chi_{[-1,1]} \in L^1$, and $g \notin L^1(\RR)$.

::: {.proof}
$\hat\chi_{[-1,1]}(\xi) = \int_{-1}^1 e^{-2\pi i x\xi}\,dx = \frac{e^{2\pi i\xi} - e^{-2\pi i\xi}}{2\pi i\xi} = \frac{\sin(2\pi\xi)}{\pi\xi}$. For $k \geq 1$ and $\xi \in [k/2 + 1/8, k/2 + 3/8]$, $|\sin 2\pi\xi| \ge 1/\sqrt2$ and $\xi \le k/2 + 1$, so $\int|g| \ge \sum_{k\ge1}\frac{1}{4\sqrt2\,\pi(k/2 + 1)} = \infty$.
:::
:::
