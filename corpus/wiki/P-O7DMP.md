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

::: problem
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
<1>1. (a) $\hat G(\xi) = F(\xi)$ where $G(x) = (1-|x|)^+$ (the tent function) and $F(\xi) = \left(\frac{\sin \pi \xi}{\pi \xi}\right)^2$.
    <2>1. $G$ is even, so $\hat G(\xi) = \int_{-1}^1 (1-|x|)e^{-2\pi i x\xi}\,dx = 2\int_0^1 (1-x)\cos(2\pi x\xi)\,dx$.
        Proof: the sine (imaginary) part of the integral vanishes by oddness.
    <2>2. $\int_0^1 (1-x)\cos(2\pi x\xi)\,dx = \dfrac{1 - \cos(2\pi\xi)}{(2\pi\xi)^2}$.
        Proof: integrate by parts with $a = 2\pi\xi$: $\int_0^1(1-x)\cos(ax)\,dx = \left[(1-x)\frac{\sin ax}{a}\right]_0^1 + \frac{1}{a}\int_0^1\sin(ax)\,dx = 0 + \frac{1}{a}\cdot\frac{1-\cos a}{a}$.
    <2>3. $\hat G(\xi) = 2\cdot\frac{1-\cos(2\pi\xi)}{(2\pi\xi)^2} = \frac{2\cdot 2\sin^2(\pi\xi)}{4\pi^2\xi^2} = \left(\frac{\sin\pi\xi}{\pi\xi}\right)^2 = F(\xi)$.
        Proof: $1 - \cos 2\theta = 2\sin^2\theta$ with $\theta = \pi\xi$.

<1>2. (b) $\hat F = G$.
    Proof: by (a), $\hat G = F$ with $G$ continuous and compactly supported; the Fourier inversion theorem gives $\check F = G$ everywhere, and with the symmetric normalization ($\hat{\hat g}(x) = g(-x)$, since the kernel $e^{-2\pi i x\xi}$ is its own conjugate-transpose) $\hat F(\xi) = \hat{\hat G}(\xi) = G(-\xi) = G(\xi)$ (evenness of $G$).

<1>3. (c) Example of $g \notin L^1(\RR)$ which is the Fourier transform of an $L^1$ function: $g(\xi) = \dfrac{\sin(2\pi\xi)}{\pi\xi} = \hat\chi_{[-1,1]}(\xi)$.
    <2>1. $\chi_{[-1,1]} \in L^1(\RR)$.
        Proof: bounded, compact support.
    <2>2. $\hat\chi_{[-1,1]}(\xi) = \int_{-1}^1 e^{-2\pi i x\xi}\,dx = \frac{e^{-2\pi i\xi} - e^{2\pi i\xi}}{-2\pi i\xi} = \frac{\sin(2\pi\xi)}{\pi\xi}$.
        Proof: direct integration ($\sin$ over the symmetric interval).
    <2>3. $g \notin L^1(\RR)$: $|g(\xi)| \sim \frac{1}{\pi|\xi|}$ at infinity, and $\int \frac{d\xi}{|\xi|}$ diverges.
        Proof: for $|\xi| \ge 1$, $|\sin(2\pi\xi)| \ge c$ on a positive fraction of the line... more simply $|g(\xi)| \ge \frac{|\sin(2\pi\xi)|}{\pi|\xi|}$, and $\int_1^\infty \frac{|\sin(2\pi\xi)|}{\xi}\,d\xi = \infty$ (the average of $|\sin|$ over periods is $2/\pi > 0$, so the integral diverges logarithmically).

<1>4. Q.E.D.
    Proof: <1>1, <1>2, <1>3 settle (a), (b), (c). (Note: the tent function's transform $F$ IS integrable, so it is not a valid example for (c); the sinc function $\sin(2\pi\xi)/\pi\xi$ is the standard one.)
:::
