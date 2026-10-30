---
schema: qual/card@1
id: P-SWLWB
kind: problem
title: $\int_0^\infty\frac{dx}{(1+x^n)^2}$, $\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$, $\int_0^\pi\frac{d\theta}{a+\sin\theta}$, $\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}$, $\int_{\abs{z}=2}\frac{dz}{(z^5-1)(z-3)}$, $\int_{-\infty}^{\infty}\frac{\sin(\pi a)\,e^{-ix\xi}}{\cosh(\pi x)+\cos(\pi a)}\,dx$, and $\int_{\abs{z}=1}\cot^2 z\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Part (ii) of the source allows every real a. For a=0 the integral of cos x / x^4 diverges at 0, so part (ii) now assumes a is nonzero.'
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle \int_0^\infty \frac{1}{(1 + x^n)^2} \, dx$, $n \geq 1$

(ii) $\displaystyle \int_0^\infty \frac{\cos x}{(x^2 + a^2)^2} \, dx$, $a \in \RR$, $a\neq0$

(iii) $\displaystyle \int_0^\pi \frac{1}{a + \sin \theta} \, d \theta$, $a>1$

(iv) $\displaystyle \int_0^{\frac{\pi}{2}} \frac{d \theta}{a+ \sin ^2 \theta},$ $a >0$.

(v) $\displaystyle \int_{\abs{z}=2} \frac{1}{(z^{5} -1) (z-3)} \, dz$

(vi) $\displaystyle \int_{- \infty}^{\infty} \frac{\sin \pi a}{\cosh \pi x + \cos \pi a} e^{- i x \xi} \, d x$, $0< a <1$, $\xi \in \RR$

(vii) $\displaystyle \int_{\abs{z} = 1} \cot^2 z \, dz$.
:::

::: {.solution title="(i)"}

::: pf

::: {.pf-step #beta}

$\displaystyle\int_0^\infty\frac{dx}{(1+x^n)^2}=\frac1nB\left(\frac1n,2-\frac1n\right)$.

::: pf-proof

Substitute $u=x^n$, so $dx=\frac1nu^{1/n-1}\,du$, and use $B(p,q)=\int_0^\infty\frac{u^{p-1}}{(1+u)^{p+q}}\,du$.

:::

:::

::: pf-step

$\displaystyle\int_0^\infty\frac{dx}{(1+x^n)^2}=\boxed{\frac{\pi(n-1)}{n^2\sin(\pi/n)}}$ for $n>1$, and the integral is $\boxed{1}$ for $n=1$.

::: pf-proof

By $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$, $\Gamma(2)=1$, $\Gamma(2-\frac1n)=(1-\frac1n)\Gamma(1-\frac1n)$ and Euler's reflection formula, step [](#beta){.pf-ref} equals
$$
\frac1n\cdot\frac{n-1}n\,\Gamma\!\left(\tfrac1n\right)\Gamma\!\left(1-\tfrac1n\right)=\frac{\pi(n-1)}{n^2\sin(\pi/n)}.
$$
For $n=1$, $B(1,1)=1$.

:::

:::

:::

:::

::: {.solution title="(ii)"}
Put $A=\abs a>0$ and $J(A)\coloneqq\int_0^\infty\frac{\cos x}{(x^2+A^2)^2}\,dx$.

::: pf

::: {.pf-step #base}

$\displaystyle I(A)\coloneqq\int_0^\infty\frac{\cos x}{x^2+A^2}\,dx=\frac{\pi}{2A}e^{-A}$.

::: pf-proof

$2I(A)=\Re\int_{-\infty}^\infty\frac{e^{ix}}{x^2+A^2}\,dx$. Close in the upper half-plane; by Jordan's lemma the arc contributes nothing in the limit, and the only enclosed pole is $iA$, with residue $e^{-A}/(2iA)$. So $2I(A)=2\pi i\cdot e^{-A}/(2iA)=\pi e^{-A}/A$.

:::

:::

::: pf-step

$J(A)=\boxed{\dfrac{\pi e^{-\abs a}(\abs a+1)}{4\abs a^3}}$.

::: pf-proof

Differentiation under the integral sign is justified on $A\ge A_0>0$ by the integrable bound $2A/(x^2+A_0^2)^2$, and gives $I'(A)=-2AJ(A)$. By step [](#base){.pf-ref},
$$
I'(A)=-\frac{\pi e^{-A}(A+1)}{2A^2},
$$
so $J(A)=\pi e^{-A}(A+1)/(4A^3)$.

:::

:::

:::

:::

::: {.solution title="(iii)"}

::: pf

::: {.pf-step #weier}

$\displaystyle\int_0^\pi\frac{d\theta}{a+\sin\theta}=2\int_0^\infty\frac{dt}{at^2+2t+a}$.

::: pf-proof

Substitute $t=\tan(\theta/2)$, so $\sin\theta=2t/(1+t^2)$ and $d\theta=2\,dt/(1+t^2)$, and $t$ runs over $(0,\infty)$.

:::

:::

::: pf-step

$\displaystyle\int_0^\pi\frac{d\theta}{a+\sin\theta}=\boxed{\frac2{\sqrt{a^2-1}}\arctan\sqrt{a^2-1}}$.

::: pf-proof

Write $c=\sqrt{a^2-1}$, so $at^2+2t+a=a\bigl[(t+\frac1a)^2+\frac{c^2}{a^2}\bigr]$. Then
$$
\int_0^\infty\frac{dt}{at^2+2t+a}=\frac1c\left[\frac\pi2-\arctan\frac1c\right]=\frac1c\arctan c,
$$
and step [](#weier){.pf-ref} doubles this.

:::

:::

:::

:::

::: {.solution title="(iv)"}

::: pf

::: pf-step

$\displaystyle\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}=\boxed{\frac{\pi}{2\sqrt{a(a+1)}}}$.

::: pf-proof

Substitute $t=\tan\theta$, so $\sin^2\theta=t^2/(1+t^2)$ and $d\theta=dt/(1+t^2)$:
$$
\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}=\int_0^\infty\frac{dt}{a+(a+1)t^2}=\frac1{\sqrt{a(a+1)}}\cdot\frac\pi2.
$$

:::

:::

:::

:::

::: {.solution title="(v)"}
Let $F(z)=\dfrac1{(z^5-1)(z-3)}$.

::: pf

::: {.pf-step #total}

The sum of the residues of $F$ at all its poles in $\CC$ is $0$.

::: pf-proof

$F(z)=O(z^{-6})$ as $z\to\infty$, so $\oint_{\abs z=R}F\,dz\to0$, while for $R>3$ this integral is $2\pi i$ times the sum of all residues.

:::

:::

::: pf-step

$\displaystyle\int_{\abs z=2}F(z)\,dz=\boxed{-\frac{\pi i}{121}}$.

::: pf-proof

The circle $\abs z=2$ encloses the five roots of $z^5-1$ and not $3$. By step [](#total){.pf-ref}, their residues sum to $-\Res(F;3)=-\frac1{3^5-1}=-\frac1{242}$, and $2\pi i\cdot(-\frac1{242})=-\frac{\pi i}{121}$.

:::

:::

:::

:::

::: {.solution title="(vi)"}
Put $A=\pi a\in(0,\pi)$, substitute $y=\pi x$, and let $k=\xi/\pi$. The integral equals $\frac{\sin A}{\pi}J(k)$, where
$$
J(k)\coloneqq\int_{-\infty}^{\infty}\frac{e^{-iky}}{\cosh y+\cos A}\,dy,
\qquad
F(z)\coloneqq\frac{e^{-ikz}}{\cosh z+\cos A}.
$$
Since $J(-k)=J(k)$, first take $k>0$, and let $\Gamma_R$ be the clockwise boundary of the rectangle with vertices $-R,R,R-2\pi i,-R-2\pi i$.

::: pf

::: {.pf-step #res}

The poles of $F$ in $-2\pi<\Im z<0$ are $z_1=-i(\pi-A)$ and $z_2=-i(\pi+A)$, and their residues sum to $\dfrac{2ie^{-\pi k}\sinh(Ak)}{\sin A}$.

::: pf-proof

$\cosh(-it)=\cos t$, so the zeros of $\cosh z+\cos A$ in this strip are where $\cos t=-\cos A$ with $t\in(0,2\pi)$, that is, $t=\pi\mp A$. There $\sinh z_1=-i\sin A$ and $\sinh z_2=i\sin A$, so
$$
\Res(F;z_1)=\frac{e^{-k(\pi-A)}}{-i\sin A},
\qquad
\Res(F;z_2)=\frac{e^{-k(\pi+A)}}{i\sin A},
$$
and their sum is $ie^{-\pi k}(e^{Ak}-e^{-Ak})/\sin A$.

:::

:::

::: {.pf-step #edges}

As $R\to\infty$, $\oint_{\Gamma_R}F\,dz\to(1-e^{-2\pi k})J(k)$.

::: pf-proof

The denominator has period $2\pi i$ and $e^{-ik(x-2\pi i)}=e^{-2\pi k}e^{-ikx}$, so the lower side, traversed from right to left, contributes $-e^{-2\pi k}J(k)$ in the limit. On the vertical sides $\abs{e^{-ikz}}\le1$ and $\abs{\cosh z+\cos A}\ge\sinh R-1$, so they contribute nothing in the limit.

:::

:::

::: {.pf-step #j}

$J(k)=\dfrac{2\pi\sinh(Ak)}{\sin A\,\sinh(\pi k)}$ for $k\neq0$, and $J(0)=\dfrac{2A}{\sin A}$.

::: pf-proof

For the clockwise contour, $\oint_{\Gamma_R}F\,dz=-2\pi i$ times the sum of the enclosed residues. Steps [](#res){.pf-ref} and [](#edges){.pf-ref} give
$$
(1-e^{-2\pi k})J(k)=\frac{4\pi e^{-\pi k}\sinh(Ak)}{\sin A},
$$
which is the claim for $k>0$; evenness gives $k<0$. $J$ is continuous at $0$ by dominated convergence, so $J(0)$ is the limit $2\pi A/(\pi\sin A)$.

:::

:::

::: pf-step

$\displaystyle\int_{-\infty}^{\infty}\frac{\sin(\pi a)\,e^{-ix\xi}}{\cosh(\pi x)+\cos(\pi a)}\,dx=\boxed{\frac{2\sinh(a\xi)}{\sinh\xi}}$ for $\xi\ne0$, and $\boxed{2a}$ for $\xi=0$.

::: pf-proof

Multiply step [](#j){.pf-ref} by $\frac{\sin A}{\pi}$, and use $Ak=a\xi$ and $\pi k=\xi$.

:::

:::

:::

:::

::: {.solution title="(vii)"}

::: pf

::: {.pf-step #laurent}

The only pole of $\cot^2z$ in $\abs z\le1$ is $0$, and $\cot^2z=\dfrac1{z^2}-\dfrac23+O(z^2)$ there.

::: pf-proof

The poles of $\cot z$ are $k\pi$, $k\in\ZZ$, and $\pi>1$. From $\cot z=\frac1z-\frac z3+O(z^3)$, squaring gives the expansion.

:::

:::

::: pf-step

$\displaystyle\int_{\abs z=1}\cot^2z\,dz=\boxed{0}$.

::: pf-proof

By step [](#laurent){.pf-ref}, the residue at $0$ is $0$.

:::

:::

:::

:::
