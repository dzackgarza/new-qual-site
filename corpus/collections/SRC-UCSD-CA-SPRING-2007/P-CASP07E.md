---
schema: qual/card@1
id: P-CASP07E
kind: problem
title: 'Convergence and zeros of $\prod_n\qty{1-\alpha_n z^n}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\{\alpha_n\}_{n=1}^{\infty}$ be positive numbers such that $\limsup_{n \to \infty} \alpha_n^{1/n} = \lambda$.
Define $q_n(z) := 1 - \alpha_n z^n$ and $r = 1/\lambda$.
Show that the infinite product $\prod_{n=1}^{\infty} q_n(z)$ converges in $\mathcal{O}(B(0, r))$ to an analytic function whose zeros (counting multiplicities) inside $B(0, r)$ are precisely those of the $q_n(z)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own normal-convergence argument follows, with the choice of $q$, the termwise bound and the convergence theorem as separate steps.

Let $\alpha_{n}>0$ with $\limsup_{n}\alpha_{n}^{1/n}=\lambda$, $q_{n}(z)=1-\alpha_{n}z^{n}$ and $r=1/\lambda$ (with $r=\infty$ if $\lambda=0$).

::: pf

::: {.pf-step #choice}
For $0<\rho<r$ there is $q$ with $\lambda\rho<q<1$, and then $\alpha_{n}^{1/n}\rho\le q$ for all large $n$.

::: pf-proof
$\rho<1/\lambda$ gives $\lambda\rho<1$, so some $q\in(\lambda\rho,1)$ exists. Since $\lambda<\frac q\rho$ and $\limsup\alpha_{n}^{1/n}=\lambda$, all sufficiently large $n$ satisfy $\alpha_{n}^{1/n}<\frac q\rho$, that is $\alpha_{n}^{1/n}\rho<q$.
:::

:::

::: {.pf-step #bound}
For $\abs{z}\le\rho$ and $n$ large, $\abs{\alpha_{n}z^{n}}\le q^{n}$; hence $\sum_{n}\sup_{\abs z\le\rho}\abs{\alpha_{n}z^{n}}<\infty$.

::: pf-proof
$\abs{\alpha_{n}z^{n}}=(\alpha_{n}^{1/n}\abs z)^{n}\le(\alpha_{n}^{1/n}\rho)^{n}\le q^{n}$ by step [](#choice){.pf-ref}. The finitely many remaining $n$ contribute finitely many finite suprema, and $\sum q^{n}<\infty$ since $q<1$.
:::

:::

::: {.pf-step #product}
$\prod_{n}(1-\alpha_{n}z^{n})$ converges uniformly on $\abs z\le\rho$, for every $\rho<r$, to a holomorphic function $F$ with $F(0)=1$.

::: pf-proof
By step [](#bound){.pf-ref} the series $\sum_{n}\sup_{\abs z\le\rho}\abs{\alpha_{n}z^{n}}$ converges, so the product converges normally on $\abs z\le\rho$ to a holomorphic function, uniformly on compact subsets of $B(0,r)$ since $\rho<r$ was arbitrary; and $F(0)=\prod_{n}1=1$ with the product converging uniformly to it, so $F$ is not identically zero.
:::

:::

::: {.pf-step #zeros}
The zeros of $F$ in $B(0,r)$, with multiplicities, are exactly the zeros of the individual $q_{n}$ there.

::: pf-proof
For a normally convergent product $\prod(1+f_{n})$ with $\sum\sup_{\abs z\le\rho}\abs{f_{n}}<\infty$, the zero set of the limit inside $\abs z<\rho$ is the union of the zero sets of the partial products, and the multiplicity at any point is the sum of the multiplicities of the factors: on a small disc around a point $z_{0}$ where the number of vanishing factors is finite and the others are bounded away from $0$, the product is a finite product times a nonvanishing normally convergent product. Finally $q_{n}(z)=1-\alpha_{n}z^{n}$ has the $n$ simple zeros $z^{n}=1/\alpha_{n}$, all of modulus $\alpha_{n}^{-1/n}$; a zero of $q_{n}$ lying in $B(0,r)$ is a zero of $F$ there with the multiplicity contributed by that factor, and no other point of $B(0,r)$ is a zero of $F$.
:::

:::

::: {.pf-qed}
Steps [](#product){.pf-ref} and [](#zeros){.pf-ref} give the statement: the product converges in $\mathcal O(B(0,1/\lambda))$ to a holomorphic function whose zeros, with multiplicity, are those of the factors $q_{n}$.
:::

:::

:::
