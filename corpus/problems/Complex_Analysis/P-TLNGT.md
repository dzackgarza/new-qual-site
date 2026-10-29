---
schema: qual/card@1
id: P-TLNGT
kind: problem
title: Residue evaluations of seven real and contour integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source labels both the fifth and the sixth integral "(v)" and the seventh "(vi)"; the parts are now labelled (i)-(vii). The source takes $a \in \RR$ in part (ii), where the integral diverges at a = 0; the statement now requires a nonzero.'
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle \int_0^\infty \frac{1}{(1 + x^n)^2} \, dx$, $n \geq 1$.

(ii) $\displaystyle \int_0^\infty \frac{\cos x}{(x^2 + a^2)^2} \, dx$, $a \in \RR$, $a \neq 0$.

(iii) $\displaystyle \int_0^\pi \frac{1}{a + \sin \theta} \, d \theta$, $a>1$.

(iv) $\displaystyle \int_0^{\frac{\pi}{2}} \frac{d \theta}{a+ \sin ^2 \theta}$, $a >0$.

(v) $\displaystyle \int_{\abs{z}=2} \frac{1}{(z^{5} -1) (z-3)} \, dz$.

(vi) $\displaystyle \int_{- \infty}^{\infty} \frac{\sin \pi a}{\cosh \pi x + \cos \pi a} e^{- i x \xi} \, d x$, $0< a <1$, $\xi \in \RR$.

(vii) $\displaystyle \int_{\abs{z} = 1} \cot^2 z \, dz$.
:::

::: {.solution}

::: pf

::: pf-step

(i) $\displaystyle\int_0^\infty\frac{dx}{(1+x^n)^2} = \boxed{\frac{\pi(n-1)}{n^2}\csc\frac\pi n}$ for $n>1$, and the integral equals $\boxed{1}$ for $n=1$.

::: pf-proof

For $n = 1$, $\int_0^\infty (1+x)^{-2}\,dx = 1$. For $n>1$, the substitution $u=x^n$ and the Beta integral $\int_0^\infty u^{s-1}(1+u)^{-s-t}\,du = B(s,t)$ give
$$
\int_0^\infty\frac{dx}{(1+x^n)^2}
=\frac1n B\qty(\frac1n,2-\frac1n)
=\frac1n\qty(1-\frac1n)\Gamma\qty(\frac1n)\Gamma\qty(1-\frac1n)
=\frac{n-1}{n^2}\cdot\frac{\pi}{\sin(\pi/n)},
$$
by $\Gamma(s+1)=s\Gamma(s)$ and the reflection formula.

:::

:::

::: pf-step

(ii) $\displaystyle\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx = \boxed{\frac{\pi e^{-\abs{a}}(\abs{a}+1)}{4\abs{a}^3}}$.

::: pf-proof

Put $A=\abs{a}>0$. The standard residue computation gives $\int_0^\infty \frac{\cos x}{x^2+A^2}\,dx = \frac{\pi}{2A}e^{-A}$. The integrand's $A$-derivative $-2A\cos x/(x^2+A^2)^2$ is dominated by $2A(x^2+A_0^2)^{-2}$ uniformly for $A \geq A_0 > 0$, so differentiation under the integral is valid:
$$
-2A\int_0^\infty\frac{\cos x}{(x^2+A^2)^2}\,dx = \frac{\pi}{2}\frac{d}{dA}\qty(\frac{e^{-A}}{A}) = -\frac{\pi}{2}e^{-A}\qty(\frac1A+\frac1{A^2}).
$$
Dividing by $-2A$ gives the value.

:::

:::

::: pf-step

(iii) $\displaystyle\int_0^\pi\frac{d\theta}{a+\sin\theta} = \boxed{\frac{2}{\sqrt{a^2-1}}\arctan\sqrt{a^2-1}}$.

::: pf-proof

With $t=\tan(\theta/2)$, $\sin\theta = 2t/(1+t^2)$ and $d\theta = 2\,dt/(1+t^2)$, so the integral is $2\int_0^\infty\frac{dt}{at^2+2t+a}$. Completing the square, $at^2+2t+a = a\qty((t+\frac1a)^2+\frac{a^2-1}{a^2})$, and
$$
2\int_0^\infty\frac{dt}{at^2+2t+a} = \frac{2}{\sqrt{a^2-1}}\qty(\frac\pi2-\arctan\frac{1}{\sqrt{a^2-1}}) = \frac{2}{\sqrt{a^2-1}}\arctan\sqrt{a^2-1}.
$$

:::

:::

::: pf-step

(iv) $\displaystyle\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta} = \boxed{\frac{\pi}{2\sqrt{a(a+1)}}}$.

::: pf-proof

With $t=\tan\theta$, $\sin^2\theta = t^2/(1+t^2)$ and $d\theta = dt/(1+t^2)$, so the integral is
$$
\int_0^\infty\frac{dt}{a+(a+1)t^2} = \frac{1}{\sqrt{a(a+1)}}\cdot\frac\pi2.
$$

:::

:::

::: pf-step

(v) $\displaystyle\int_{\abs{z}=2}\frac{dz}{(z^5-1)(z-3)} = \boxed{-\frac{\pi i}{121}}$.

::: pf-proof

Let $F(z)=\frac1{(z^5-1)(z-3)}$. The five roots of $z^5-1$ lie inside $\abs{z}=2$ and $z=3$ lies outside. Since $F(z) = O(z^{-6})$ at infinity, the sum of all residues of $F$ in $\CC$ is zero. As $\Res(F;3)=\frac1{3^5-1}=\frac1{242}$, the residues inside the contour sum to $-\frac1{242}$, and the integral is $2\pi i\cdot\qty(-\frac1{242})$.

:::

:::

::: pf-step

(vi) $\displaystyle\int_{-\infty}^{\infty}\frac{\sin(\pi a)e^{-ix\xi}}{\cosh(\pi x)+\cos(\pi a)}\,dx = \boxed{\frac{2\sinh(a\xi)}{\sinh\xi}}$ for $\xi\neq0$, and $\boxed{2a}$ for $\xi=0$.

::: pf-proof

Substituting $u=\pi x$ and writing $k=\xi/\pi$, the integral is $\frac{\sin\pi a}{\pi}I$ with $I=\int_{-\infty}^\infty h(u)\,du$, $h(u)=\frac{e^{-iku}}{\cosh u+\cos\pi a}$. Integrate $h$ over the boundary of the rectangle $[-R,R]\times[0,2\pi]$. On the vertical sides $\abs{\cosh u+\cos\pi a}\geq \frac12 e^{R}-2$ while $\abs{e^{-iku}} \leq e^{2\pi\abs{k}}$, so those integrals tend to $0$. Since $h(u+2\pi i)=e^{2\pi k}h(u)$,
$$
(1-e^{2\pi k})\,I = 2\pi i\sum\Res h.
$$
The poles in the strip are the solutions of $\cosh u = \cos(\pi-\pi a)$, namely $u_1=i\pi(1-a)$ and $u_2=i\pi(1+a)$, both simple, with $\sinh u_1 = i\sin\pi a$ and $\sinh u_2 = -i\sin\pi a$. Hence
$$
\sum\Res h = \frac{e^{k\pi(1-a)}-e^{k\pi(1+a)}}{i\sin\pi a} = \frac{-2e^{k\pi}\sinh(k\pi a)}{i\sin\pi a}.
$$
For $k\neq0$, $1-e^{2\pi k} = -2e^{\pi k}\sinh(\pi k)$, so $I = \frac{2\pi\sinh(\pi k a)}{\sin(\pi a)\sinh(\pi k)}$ and the integral is $\frac{2\sinh(\pi k a)}{\sinh(\pi k)} = \frac{2\sinh(a\xi)}{\sinh\xi}$. The integral is continuous in $\xi$ by dominated convergence, so its value at $\xi=0$ is the limit $2a$.

:::

:::

::: pf-step

(vii) $\displaystyle\int_{\abs{z}=1}\cot^2z\,dz = \boxed{0}$.

::: pf-proof

The poles of $\cot^2 z$ are the multiples of $\pi$, so only $z=0$ lies inside $\abs{z}=1$. From $\cot z=\frac1z-\frac z3+O(z^3)$ we get $\cot^2z=\frac1{z^2}-\frac23+O(z^2)$, so the residue at $0$ is zero.

:::

:::

:::

:::
