---
schema: qual/card@1
id: P-JWOJ5
kind: problem
title: "The integral of the log of the chord length over the circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Mean Value Property
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, with (a) and (b) as sub-blocks of two top-level
    steps and the equivalence as the QED step. Re-checked: $1-rz$ lies in the disc of radius $1$
    about $1$ for $\abs z<1$, so the holomorphic logarithm given by $-\sum(rz)^n/n$ exists and has
    real part $\log\abs{1-rz}$; the mean value property of the harmonic real part at the centre gives
    the vanishing integral; and the limit $r\uparrow1$ is justified by an explicit domination, for
    which the card now proves $\abs{1-re^{i\theta}}^2=(1-r)^2+4r\sin^2(\theta/2)\ge2\sin^2(\theta/2)$
    for $r\ge\tfrac12$ and uses $\sin(\theta/2)\ge(2/\pi)\min(\theta/2,(2\pi-\theta)/2)$ to bound
    the negative part by an integrable function. For (b): $\abs{1-e^{i\theta}}=2\sin(\theta/2)$, the
    substitution $x=\theta/(2\pi)$, and the logarithmic integrability at the endpoints, which makes
    the steps reversible. Added: the domination details and the integrability clause, which the
    earlier text asserted in one sentence. No defect found in the statement. Not claimed: a printed
    solution, the collection recording no provenance.
---

::: {.problem}
(a) Show, without using the identity in part (b), that
$$
\int_0^{2\pi} \log\abs{1 - e^{i\theta}}~d\theta = 0
$$

(b) Show that this identity is equivalent to
$$
\int_0^1 \log(\sin(\pi x)) ~dx = -\log 2
.$$
:::

::: {.solution}
The collection records no provenance and retains no solution set, so the argument is the card's own.

::: pf

::: {.pf-step #harmonic-mean-value}
For $0<r<1$ one has $\int_0^{2\pi}\log\abs{1-re^{i\theta}}\,d\theta=0$.

:::: pf-proof

::: {.pf-step #branch}
The function $z\mapsto\log(1-rz)$ is holomorphic on the unit disc, with real part $\log\abs{1-rz}$.

::: pf-proof
For $\abs z<1$ and $0<r<1$ one has $\abs{rz}<1$, so $1-rz$ lies in the disc of radius $1$ about $1$, where a holomorphic logarithm exists; it is given by its power series $-\sum_{n\ge1}(rz)^n/n$ at $0$, and its real part is $\log\abs{1-rz}$ because $\log w=\log\abs w+i\arg w$ for that branch.
:::

:::

::: {.pf-step}
$\frac1{2\pi}\int_0^{2\pi}\log\abs{1-re^{i\theta}}\,d\theta=\log\abs{1}=0$.

::: pf-proof
The real part of a holomorphic function is harmonic, and a harmonic function satisfies the mean value property: its value at the centre $0$ of the disc is the average of its boundary values on every circle $\abs z=\rho$ with $\rho<1$. Taking $\rho\to1$ gives the displayed identity for the boundary circle, the integrand being continuous in $\theta$ for fixed $r$.
:::

:::

:::

:::

::: {.pf-step #limit}
$\int_0^{2\pi}\log\abs{1-e^{i\theta}}\,d\theta=0$.

::: pf-proof
Let $r\uparrow1$. For each $\theta\in(0,2\pi)$ the numbers $1-re^{i\theta}$ tend to $1-e^{i\theta}\ne0$, so the logarithms tend to $\log\abs{1-e^{i\theta}}$. For $r\ge\tfrac12$,
$$
\abs{1-re^{i\theta}}^2=(1-r)^2+4r\sin^2(\theta/2)\ge2\sin^2(\theta/2),
$$
so $\log\abs{1-re^{i\theta}}\ge\tfrac12\log2+\log\sin(\theta/2)$, while $\abs{1-re^{i\theta}}\le2$ gives the upper bound $\log2$. Since $\sin(\theta/2)\ge(2/\pi)\min(\theta/2,(2\pi-\theta)/2)$ on $(0,2\pi)$, the negative part is dominated by a constant plus $\abs{\log\theta}+\abs{\log(2\pi-\theta)}$, which is integrable on $(0,2\pi)$, and the positive part by the constant $\log2$; so dominated convergence applies to the functions $\log\abs{1-re^{i\theta}}$ and the limit of the integrals is the integral of the limit, which is $0$ by step [](#harmonic-mean-value){.pf-ref}.
:::

:::

::: {.pf-step #equivalence}
(b) Part (a) is equivalent to $\int_0^1\log(\sin \pi x)\,dx=-\log2$.

::: pf-proof
For $0<\theta<2\pi$ one has $\abs{1-e^{i\theta}}=2\sin(\theta/2)>0$, so part (a) reads $\int_0^{2\pi}\bigl(\log2+\log\sin(\theta/2)\bigr)d\theta=0$, that is $2\pi\log2+\int_0^{2\pi}\log\sin(\theta/2)\,d\theta=0$. Substituting $x=\theta/(2\pi)$, so that $d\theta=2\pi\,dx$ and $\sin(\theta/2)=\sin(\pi x)$, gives $2\pi\log2+2\pi\int_0^1\log(\sin\pi x)\,dx=0$, which is $\int_0^1\log(\sin\pi x)\,dx=-\log2$. Each step is an identity between integrals of functions integrable on the interval — the singularities of $\log\sin$ at the endpoints being logarithmic — and the substitution is a bijection of $(0,1)$ onto $(0,2\pi)$ up to the factor $2\pi$, so the two statements are equivalent. Part (a) is step [](#limit){.pf-ref}.
:::

:::

:::
:::
