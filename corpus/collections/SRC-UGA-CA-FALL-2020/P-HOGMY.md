---
schema: qual/card@1
id: P-HOGMY
kind: problem
title: Iterates of a holomorphic self-map of the disc fixing $0$ converge to $0$ or
  the identity
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Fixed Points
  - Sequences of Functions
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \DD \rightarrow \DD$ is holomorphic and $f(0)=0$.
Let $n \geq 1$, and define the function $f_{n}(z)$ to be the $n$-th composition of $f$ with itself; more precisely, let

$$
f_{1}(z):=f(z), \quad f_{2}(z):=f(f(z)), \quad \text{in general } f_{n}(z):=f\left(f_{n-1}(z)\right).
$$

Suppose that for each $z \in \DD$, $\lim_{n \rightarrow \infty} f_{n}(z)$ exists and equals to $g(z)$.
Prove that either $g(z) \equiv 0$ or $g(z)=z$ for all $z \in \DD$.
:::

::: {.solution}

By the Schwarz lemma, $\abs{f(z)}\le\abs{z}$ on $\DD$, and either $f(z)=e^{i\theta}z$ for some real $\theta$, or $\abs{f(z)}<\abs{z}$ for all $z\neq0$.

::: pf

::: {.pf-step #contract}

If $\abs{f(z)}<\abs{z}$ for all $z\neq0$, then $g\equiv0$.

::: pf-proof

Fix $z\in\DD$ and $r$ with $\abs{z}\le r<1$. The function $f(w)/w$, extended by $f'(0)$ at $0$, is continuous on $\abs{w}\le r$ and has modulus less than $1$ there (at $0$, $\abs{f'(0)}<1$ by the Schwarz lemma). So $c_r\coloneqq\max_{\abs{w}\le r}\abs{f(w)/w}<1$, and $\abs{f(w)}\le c_r\abs{w}$ for $\abs{w}\le r$. Since $\abs{f_n(z)}\le\abs{z}\le r$ for all $n$, induction gives $\abs{f_n(z)}\le c_r^n\abs{z}\to0$.

:::

:::

::: {.pf-step #rotation}

If $f(z)=e^{i\theta}z$, then $g(z)=z$.

::: pf-proof

Here $f_n(z)=e^{in\theta}z$. Take $z\neq0$. Convergence of $f_n(z)$ forces $f_{n+1}(z)-f_n(z)=e^{in\theta}(e^{i\theta}-1)z\to0$, and $\abs{e^{in\theta}(e^{i\theta}-1)z}=\abs{e^{i\theta}-1}\abs{z}$, so $e^{i\theta}=1$. Then $f_n(z)=z$ for all $n$.

:::

:::

::: pf-qed

Steps [](#contract){.pf-ref} and [](#rotation){.pf-ref} cover the two cases of the Schwarz lemma.

:::

:::

:::
