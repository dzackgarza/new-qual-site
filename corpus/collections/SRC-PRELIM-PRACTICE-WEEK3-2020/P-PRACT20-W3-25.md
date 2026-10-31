---
schema: qual/card@1
id: P-PRACT20-W3-25
kind: problem
title: The integrals $\int_0^{\pi/2}(a\cos^2x+b\sin^2x)^{-n}\,dx$ by differentiating in parameters
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Differentiation Under the Integral
relations: []
review: draft
---

::: {.problem}
For $a, b > 0$ and $n \in \NN$, define
$$
I_{n}(a, b) = \int_{0}^{\pi/2} \frac{dx}{(a \cos^{2}(x) + b \sin^{2}(x))^{n}}.
$$
(a) Show that
$$
\frac{\partial I_{n}}{\partial a} + \frac{\partial I_{n}}{\partial b} + n I_{n+1} = 0.
$$

(b) Evaluate $I_{1}(a, b)$ explicitly, and use (a) to evaluate $I_{2}(a, b)$.
:::

::: {.solution}
The denominator is at least $\min(a,b)^n>0$ on $[0,\pi/2]$, so the integrand and its partial derivatives in $a,b$ are continuous on $[0,\pi/2]\times(0,\infty)^2$. Differentiating under the integral sign (Leibniz rule), we find

$$
\frac{\partial I_n}{\partial a}(a,b)=-\int_0^{\pi/2}\frac{n\cos^2x\,dx}{(a\cos^2x+b\sin^2x)^{n+1}},\qquad\frac{\partial I_n}{\partial b}(a,b)=-\int_0^{\pi/2}\frac{n\sin^2x\,dx}{(a\cos^2x+b\sin^2x)^{n+1}},
$$

and so

$$
\frac{\partial I_n}{\partial a}+\frac{\partial I_n}{\partial b}=-n\int_0^{\pi/2}\frac{\cos^2x+\sin^2x}{(a\cos^2x+b\sin^2x)^{n+1}}\,dx=-nI_{n+1}.
$$

To evaluate $I_1(a,b)$, divide numerator and denominator by $\cos^2(x)$ and substitute $u = \tan(x)$:

$$
\begin{aligned}
I_1(a,b) &= \int_0^{\pi/2} \frac{dx}{a\cos^2(x) + b\sin^2(x)}
= \int_0^{\pi/2} \frac{\sec^2(x)\,dx}{a + b\tan^2(x)}
= \int_0^\infty \frac{du}{a + bu^2} \\
&= \frac{1}{a}\int_0^\infty \frac{du}{1 + \frac{b}{a}u^2}
= \frac{1}{a}\sqrt{\frac{a}{b}}\,\arctan\left(u\sqrt{\frac{b}{a}}\right)\evalfrom_{u=0}^{u\to\infty}
= \frac{\pi}{2\sqrt{ab}}.
\end{aligned}
$$

Then

$$
I_2(a,b)=-\frac{\partial I_1}{\partial a}(a,b)-\frac{\partial I_1}{\partial b}(a,b)=\frac{\pi}{4a\sqrt{ab}}+\frac{\pi}{4b\sqrt{ab}}=\frac{\pi}{4\sqrt{ab}}\left(\frac1a+\frac1b\right).
$$
:::
