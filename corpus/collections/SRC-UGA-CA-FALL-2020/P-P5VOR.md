---
schema: qual/card@1
id: P-P5VOR
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^3}\,dx$ for $0<a<3$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Let $a \in \RR$ with $0<a<3$. Evaluate 
$$
\int_{0}^{\infty} \frac{x^{a-1}}{1+x^{3}} d x
.$$

:::

::: {.solution}

Let $I$ be the integral; it converges because $0<a<3$. Let $z^{a-1}=\exp((a-1)\log z)$ with $\arg z\in(-\pi/2,3\pi/2)$, and let $f(z)=z^{a-1}/(1+z^3)$. Put $\omega=e^{i\pi/3}$. For $0<\varepsilon<1<R$, let $\Gamma$ be the boundary of the sector $\{\varepsilon<\abs{z}<R,\ 0<\arg z<2\pi/3\}$, oriented positively.

::: pf

::: {.pf-step #res}

$\displaystyle\int_\Gamma f\,dz=2\pi i\operatorname{Res}_{z=\omega}f=-\frac{2\pi i}{3}e^{i\pi a/3}$.

::: pf-proof

The zeros of $1+z^3$ are $\omega,-1,\overline\omega$, and only $\omega$ lies inside the sector. It is a simple zero, so the residue is $\omega^{a-1}/(3\omega^2)=\omega^{a-3}/3=-e^{i\pi a/3}/3$, because $\omega^3=-1$.

:::

:::

::: {.pf-step #arcs}

The integrals over the arcs $\abs{z}=R$ and $\abs{z}=\varepsilon$ tend to $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: pf-proof

On $\abs{z}=R$, $\abs{f}\le R^{a-1}/(R^3-1)$, and the arc has length $2\pi R/3$, so the integral is $O(R^{a-3})\to0$. On $\abs{z}=\varepsilon$, $\abs{f}\le\varepsilon^{a-1}/(1-\varepsilon^3)$, and the arc has length $2\pi\varepsilon/3$, so the integral is $O(\varepsilon^{a})\to0$.

:::

:::

::: {.pf-step #ray}

The integral over the ray $\arg z=2\pi/3$, from $Re^{2\pi i/3}$ to $\varepsilon e^{2\pi i/3}$, tends to $-e^{2\pi ia/3}I$.

::: pf-proof

With $z=te^{2\pi i/3}$, $z^{a-1}=t^{a-1}e^{2\pi i(a-1)/3}$, $z^3=t^3$ and $dz=e^{2\pi i/3}dt$, so the integral is $-e^{2\pi ia/3}\int_\varepsilon^R\frac{t^{a-1}}{1+t^3}\,dt$.

:::

:::

::: pf-qed

On $[\varepsilon,R]$ the integrand is $x^{a-1}/(1+x^3)$. By Steps [](#res){.pf-ref}, [](#arcs){.pf-ref} and [](#ray){.pf-ref}, $(1-e^{2\pi ia/3})I=-\frac{2\pi i}{3}e^{i\pi a/3}$. Since $1-e^{2\pi ia/3}=-2ie^{i\pi a/3}\sin(\pi a/3)$,
$$
\boxed{\int_0^\infty\frac{x^{a-1}}{1+x^3}\,dx=\frac{\pi}{3\sin(\pi a/3)}}.
$$

:::

:::

:::
