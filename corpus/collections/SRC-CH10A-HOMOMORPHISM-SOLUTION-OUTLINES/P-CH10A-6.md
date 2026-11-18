---
schema: qual/card@1
id: P-CH10A-6
kind: problem
title: Antidifferentiation as a homomorphism of the additive group of real polynomials
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Replaced the garbled 'R f' with the integral sign and restored math delimiters, per page 1 of Ch10PtASltns.pdf.
---

::: {.problem}
Let $G$ be the group of all polynomials with real coefficients under addition.
For each $f$ in $G$ let $\int f$ denote the antiderivative of $f$ that passes through the point $(0, 0)$.
Show that the mapping $f \mapsto \int f$ from $G$ to $G$ is a homomorphism.
What is the kernel of this mapping?
Is this mapping a homomorphism if $\int f$ denotes the antiderivative of $f$ that passes through $(0, 1)$?
:::

::: {.solution}

The argument is the card's own: the antiderivative with zero constant term is additive in the coefficients, and the version through $(0,1)$ fails additivity at the constant term.

::: pf

::: {.pf-step #formula}

$\phi(f)=a_{0}x+\frac{a_{1}}{2}x^{2}+\cdots+\frac{a_{n}}{n+1}x^{n+1}$ for $f=a_{0}+a_{1}x+\cdots+a_{n}x^{n}$.

::: pf-proof

The antiderivative of $a_{k}x^{k}$ is $\frac{a_{k}}{k+1}x^{k+1}$, and the one passing through $(0,0)$ is the one whose value at $0$ is $0$, which holds for this expression since every term vanishes at $0$. Uniqueness of the antiderivative up to an additive constant makes this the only such polynomial.

:::

:::

::: {.pf-step #additive}

$\phi(f+g)=\phi(f)+\phi(g)$.

::: pf-proof

Addition in $\RR[x]$ is coefficientwise, so the coefficients of $f+g$ are $a_{k}+b_{k}$ where those are the coefficients of $f$ and $g$. By step [](#formula){.pf-ref}, $\phi(f+g)=\sum_{k}\frac{a_{k}+b_{k}}{k+1}x^{k+1}=\sum_{k}\frac{a_{k}}{k+1}x^{k+1}+\sum_{k}\frac{b_{k}}{k+1}x^{k+1}=\phi(f)+\phi(g)$. Hence $\phi$ is a homomorphism of the additive group $G=\RR[x]$.

:::

:::

::: {.pf-step #kernel}

$\ker\phi=\{0\}$.

::: pf-proof

$\phi(f)=0$ means every coefficient $\frac{a_{k}}{k+1}$ vanishes, and a field of characteristic $0$ has $k+1\ne0$, so $a_{k}=0$ for all $k$ and $f$ is the zero polynomial. Conversely $\phi(0)=0$. So the kernel is trivial.

:::

:::

::: {.pf-step #shifted}

The map taking $f$ to the antiderivative through $(0,1)$ is not a homomorphism.

::: pf-proof

That antiderivative is $\psi(f)=\phi(f)+1$, so $\psi(f+g)=\phi(f)+\phi(g)+1$ while $\psi(f)+\psi(g)=\phi(f)+\phi(g)+2$; these differ by the constant $1$, and $1\ne0$ in $\RR[x]$. Equivalently $\psi(0)=1\ne0$, and a homomorphism must send $0$ to $0$:
$$
\boxed{\ker\phi=\{0\},\qquad \psi(f)=\phi(f)+1\ \text{is not a homomorphism because } \psi(0)=1.}
$$

:::

:::

:::

:::
