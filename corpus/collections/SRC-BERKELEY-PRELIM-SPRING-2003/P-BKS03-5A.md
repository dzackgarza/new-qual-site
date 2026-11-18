---
schema: qual/card@1
id: P-BKS03-5A
kind: problem
title: A singular perturbation of a symmetric matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $L$ be a real symmetric $n\times n$ matrix with $0$ as a simple eigenvalue, and let $v\in\RR^n$.

(a) Show that for all sufficiently small $\varepsilon>0$, the equation
$$
Lx+\varepsilon x=v
$$
has a unique solution $x(\varepsilon)$.

(b) Evaluate $\lim_{\varepsilon\to0^+}\varepsilon x(\varepsilon)$ in terms of $v$ and the eigenvectors of $L$.
:::

::: {.solution}

The argument is the card's own: diagonalise $L$ in an orthonormal basis and solve the equation componentwise.

::: pf

::: {.pf-step #basis}

There is an orthonormal basis $e_{1},\dots,e_{n}$ of $\RR^{n}$ of eigenvectors of $L$; write $Le_{i}=\lambda_{i}e_{i}$ with $\lambda_{1}=0$ and $\lambda_{i}\ne0$ for $i\ne1$.

::: pf-proof

A real symmetric matrix is orthogonally diagonalisable (the spectral theorem): there is an orthonormal basis of eigenvectors, and all eigenvalues are real. The hypothesis that $0$ is a simple eigenvalue means exactly that the eigenspace $\ker L$ is one-dimensional, so after reordering exactly one eigenvalue, say $\lambda_{1}$, is $0$ and the others are nonzero.

:::

:::

::: {.pf-step #componentwise}

With $v=\sum_{i}v_{i}e_{i}$ and $x=\sum_{i}x_{i}e_{i}$, the equation $Lx+\varepsilon x=v$ is equivalent to $(\lambda_{i}+\varepsilon)x_{i}=v_{i}$ for every $i$.

::: pf-proof

$Lx=\sum_{i}\lambda_{i}x_{i}e_{i}$ and $\varepsilon x=\sum_{i}\varepsilon x_{i}e_{i}$, so $Lx+\varepsilon x=\sum_{i}(\lambda_{i}+\varepsilon)x_{i}e_{i}$. Since $e_{1},\dots,e_{n}$ is a basis, this equals $v=\sum_{i}v_{i}e_{i}$ exactly when the coordinates agree in each $i$.

:::

:::

::: {.pf-step #unique}

(a) For $0<\varepsilon<\min_{i\ne1}\abs{\lambda_{i}}$ the system has the unique solution $x_{i}(\varepsilon)=v_{i}/(\lambda_{i}+\varepsilon)$.

::: pf-proof

Under the stated bound on $\varepsilon$ every coefficient $\lambda_{i}+\varepsilon$ is nonzero: $\lambda_{1}+\varepsilon=\varepsilon>0$, and $\abs{\lambda_{i}+\varepsilon}\ge\abs{\lambda_{i}}-\varepsilon>0$ for $i\ne1$. So each equation of step [](#componentwise){.pf-ref} has the unique solution $x_{i}=v_{i}/(\lambda_{i}+\varepsilon)$, and the coordinate tuple determines $x(\varepsilon)$:
$$
\boxed{x(\varepsilon)=\sum_{i=1}^{n}\frac{v_{i}}{\lambda_{i}+\varepsilon}\,e_{i}.}
$$

:::

:::

::: {.pf-step #limit}

(b) $\displaystyle\lim_{\varepsilon\to0^{+}}\varepsilon x(\varepsilon)=\inner{v}{e_{1}}e_{1}$.

::: pf-proof

By step [](#unique){.pf-ref},
$$
\varepsilon x(\varepsilon)=\sum_{i=1}^{n}\frac{\varepsilon}{\lambda_{i}+\varepsilon}v_{i}e_{i}.
$$
The first term is $\frac{\varepsilon}{0+\varepsilon}v_{1}e_{1}=v_{1}e_{1}$ for every $\varepsilon>0$, and for $i\ne1$ the coefficient $\frac{\varepsilon}{\lambda_{i}+\varepsilon}\to0$. Since $e_{1}$ is a unit eigenvector and $v=\sum_{i}v_{i}e_{i}$, orthonormality gives $v_{1}=\inner{v}{e_{1}}$, so
$$
\boxed{\lim_{\varepsilon\to0^{+}}\varepsilon x(\varepsilon)=v_{1}e_{1}=\inner{v}{e_{1}}e_{1}.}
$$

:::

:::

:::

:::
