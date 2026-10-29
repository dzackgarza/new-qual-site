---
schema: qual/card@1
id: E-CLMEK
kind: problem
title: Differentiable contractions are uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is a differentiable contraction, $f$ is uniformly continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #mobius-in-aut}
Every map $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\neq0$ lies in $\Aut(\CP^1)$.

::: pf-proof
Let $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\GL_2(\CC)$.
The linear automorphism $A$ of $\CC^2$ descends to the holomorphic map $[z_0:z_1]\mapsto[az_0+bz_1:cz_0+dz_1]$ of $\CP^1$, which on the affine chart $z=[z:1]$ is $z\mapsto\frac{az+b}{cz+d}$.
Its inverse is the map induced by $A^{-1}$, which is also holomorphic.
:::

:::

::: pf-step
$\Aut(\CP^1)$ is exactly the set of maps $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\neq0$.

::: pf-proof

::: {.pf-step #rational}
Let $f\in\Aut(\CP^1)$. Then $f=p/q$ for coprime polynomials $p,q$, not both constant.

::: pf-proof
A meromorphic function on $\CP^1$ is rational, and $f$ is not constant because it is bijective.
:::

:::

::: {.pf-step #fiber-count}
Let $n=\max\{\deg p,\deg q\}$.
For all but finitely many $w\in\CC$, the fiber $f^{-1}(w)$ consists of the $n$ roots, counted with multiplicity, of the degree-$n$ polynomial $p-wq$.

::: pf-proof
Since $p$ and $q$ are coprime, $f(z)=w$ is equivalent to $p(z)-wq(z)=0$ for $z\in\CC$.
The coefficient of $z^n$ in $p-wq$ is nonzero except for at most one value of $w$, and $\infty$ lies in the fiber of only one value $f(\infty)$.
:::

:::

::: {.pf-step #unramified}
Every root in step [](#fiber-count){.pf-ref} is simple.

::: pf-proof
The inverse of $f$ is holomorphic, so $(f^{-1})'(f(z))f'(z)=1$ in local coordinates, and $f'$ has no zeros.
A root $z_0$ of $p-wq$ of multiplicity at least two with $q(z_0)\neq0$ would be a zero of $f'=\frac{(p-wq)'q-(p-wq)q'}{q^2}$.
:::

:::

::: pf-step
$n=1$, and $f(z)=\frac{az+b}{cz+d}$ with $ad-bc\neq0$.

::: pf-proof
By step [](#fiber-count){.pf-ref} and step [](#unramified){.pf-ref}, a generic fiber of $f$ has exactly $n$ points, and $f$ is injective, so $n=1$.
Hence $p(z)=az+b$ and $q(z)=cz+d$.
If $ad-bc=0$, the two linear polynomials are proportional and $f$ is constant, which step [](#rational){.pf-ref} excludes.
Together with step [](#mobius-in-aut){.pf-ref}, this proves the equality of the two sets.
:::

:::

:::

:::

:::

:::
