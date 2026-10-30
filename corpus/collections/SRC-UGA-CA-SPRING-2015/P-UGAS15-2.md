---
schema: qual/card@1
id: P-UGAS15-2
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx$ for $0<a<n$
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
Suppose $n$ is an integer and $a$ is a real number satisfying $0<a<n$. Compute the integral
$$
\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx.
$$
:::

::: {.solution}
Since $0<a<n$, the integer $n$ is positive. Write $I$ for the integral, put $\omega=e^{i\pi/n}$, and let $z^{a-1}=\exp((a-1)\log z)$ with the branch of $\log z$ whose argument lies in $(0,2\pi)$ on $\CC\setminus[0,\infty)$. On the edge $\arg z=0$ take the boundary values from above, $z^{a-1}=x^{a-1}$.

::: pf

::: {.pf-step #conv}
The integral $I$ converges absolutely.

::: pf-proof
Near $0$ the integrand is at most $x^{a-1}$, which is integrable because $a>0$. For $x\ge1$ it is at most $x^{a-1-n}$, which is integrable because $a<n$.
:::

:::

::: {.pf-step #contour}
For $0<\varepsilon<1<R$, let $\Gamma$ be the boundary of the sector $\{z:\varepsilon<\abs{z}<R,\ 0<\arg z<2\pi/n\}$, oriented positively. Then
$$
\oint_\Gamma\frac{z^{a-1}}{1+z^n}\,dz=-\frac{2\pi i}{n}\,\omega^{a}.
$$

::: pf-proof
The zeros of $1+z^n$ are $\omega^{2k+1}$, and the only one with argument in $(0,2\pi/n)$ is $\omega$. It is a simple zero, and $\omega^n=-1$, so the residue is
$$
\frac{\omega^{a-1}}{n\omega^{n-1}}=\frac{\omega^{a}}{n\omega^n}=-\frac{\omega^a}{n}.
$$
For $n\ge2$ the integrand is holomorphic on a neighborhood of the closed sector, because the closed sector minus $0$ lies in $\CC\setminus[0,\infty)$ except for the edge $\arg z=0$, and there the branch extends holomorphically across $(0,\infty)$ from above. For $n=1$ the sector is the keyhole region, and the displayed identity is the limit of the residue theorem on keyhole contours whose edges approach $(0,\infty)$ from above and from below. In both cases the residue theorem gives the identity.
:::

:::

::: {.pf-step #edges}
The two straight edges of $\Gamma$ contribute
$$
\bigl(1-e^{2\pi ia/n}\bigr)\int_\varepsilon^R\frac{x^{a-1}}{1+x^n}\,dx.
$$

::: pf-proof
On the edge $\arg z=0$ the integrand is $x^{a-1}/(1+x^n)$, traversed from $\varepsilon$ to $R$. On the edge $\arg z=2\pi/n$ put $z=te^{2\pi i/n}$. Then $z^n=t^n$, $z^{a-1}\,dz=e^{2\pi i a/n}t^{a-1}\,dt$, and the edge is traversed from $R$ to $\varepsilon$.
:::

:::

::: {.pf-step #arcs}
The integrals over the arcs $\abs{z}=R$ and $\abs{z}=\varepsilon$ tend to $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: pf-proof
Each arc has length at most $2\pi\abs{z}$. On $\abs{z}=R$ the integrand is at most $R^{a-1}/(R^n-1)$, so the integral is at most $2\pi R^a/(R^n-1)\to0$ because $a<n$. On $\abs{z}=\varepsilon$ the integrand is at most $\varepsilon^{a-1}/(1-\varepsilon^n)$, so the integral is at most $2\pi\varepsilon^a/(1-\varepsilon^n)\to0$ because $a>0$.
:::

:::

::: pf-step
$$
\boxed{I=\frac{\pi}{n\sin(\pi a/n)}}.
$$

::: pf-proof
Let $\varepsilon\to0$ and $R\to\infty$ in step [](#contour){.pf-ref}. Steps [](#conv){.pf-ref}, [](#edges){.pf-ref} and [](#arcs){.pf-ref} give
$$
\bigl(1-e^{2\pi ia/n}\bigr)I=-\frac{2\pi i}{n}e^{i\pi a/n}.
$$
Since $0<a/n<1$, the factor $1-e^{2\pi ia/n}$ is not $0$. Divide by $-e^{i\pi a/n}$:
$$
\bigl(e^{i\pi a/n}-e^{-i\pi a/n}\bigr)I=\frac{2\pi i}{n},
\qquad\text{that is,}\qquad
2i\sin(\pi a/n)\,I=\frac{2\pi i}{n}.
$$
:::

:::

:::

:::

::: remark
One printing takes $n=3$.
:::
