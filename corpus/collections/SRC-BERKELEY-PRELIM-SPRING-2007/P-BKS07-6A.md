---
schema: qual/card@1
id: P-BKS07-6A
kind: problem
title: Exponential of a complex linear combination of the Pauli matrices
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let
$$
A=\alpha_1\sigma_1+\alpha_2\sigma_2+\alpha_3\sigma_3,
\qquad \alpha_1,\alpha_2,\alpha_3\in\CC,
$$
where
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
Let $\beta\in\CC$ be any square root of $\alpha_1^2+\alpha_2^2+\alpha_3^2$.

(a) Prove that
$$
\exp(A)=\cosh(\beta)I+\frac{\sinh\beta}{\beta}A,
$$
where $\frac{\sinh\beta}{\beta}$ is interpreted as $1$ if $\beta=0$.
(Hint: first show that $A^2$ is a scalar multiple of the identity.)

(b) Evaluate $\exp(A)$ explicitly when $\alpha_1=i\pi$, $\alpha_2=i\pi$, and $\alpha_3=\pi$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$A^2=(\alpha_1^2+\alpha_2^2+\alpha_3^2)I=\beta^2I$.

::: pf-proof

$A=\begin{pmatrix}\alpha_3&\alpha_1-i\alpha_2\\\alpha_1+i\alpha_2&-\alpha_3\end{pmatrix}$. Its square has diagonal entries $\alpha_3^2+(\alpha_1-i\alpha_2)(\alpha_1+i\alpha_2)=\alpha_1^2+\alpha_2^2+\alpha_3^2$ and off-diagonal entries $\alpha_3(\alpha_1\mp i\alpha_2)-\alpha_3(\alpha_1\mp i\alpha_2)=0$.

:::

:::

::: {.pf-step #s2}

Part (a) holds.

::: pf-proof

By step [](#s1){.pf-ref}, $A^{2j}=\beta^{2j}I$ and $A^{2j+1}=\beta^{2j}A$. Hence
$$
\exp(A)=\sum_{j\ge0}\frac{\beta^{2j}}{(2j)!}I+\sum_{j\ge0}\frac{\beta^{2j}}{(2j+1)!}A=\cosh(\beta)I+\frac{\sinh\beta}{\beta}A,
$$
where the second series is $1$ when $\beta=0$, as the convention requires.

:::

:::

::: {.pf-step #s3}

In part (b), $\exp(A)=-I$.

::: pf-proof

Here $\beta^2=-\pi^2-\pi^2+\pi^2=-\pi^2$; take $\beta=i\pi$. Then $\cosh(i\pi)=\cos\pi=-1$ and $\sinh(i\pi)=i\sin\pi=0$, so step [](#s2){.pf-ref} gives $\exp(A)=-I$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} answer parts (a) and (b).

:::

:::

:::
