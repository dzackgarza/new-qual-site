---
schema: qual/card@1
id: P-BKF20-6B
kind: problem
title: Hilbert matrix and orthonormal polynomial coefficients
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
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 matrix argument. Expanding
    orthonormality gives PHP^T=I; this identity forces P to be invertible and
    then inversion yields H^{-1}=P^TP.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the entrywise matrix multiplication against the defining
    integrals, the rank argument for invertibility, and the order of factors
    when the identity is inverted.
---

::: {.problem}
Let
\[
H_{ij}=\int_0^1t^it^j\,dt,\qquad0\le i,j\le n,
\]
and let $P_i(t)=\sum_{j=0}^ip_{ij}t^j$ be orthonormal on $[0,1]$. If $P=(p_{ij})$, show that
\[
H^{-1}=P^TP.
\]
:::

::: {.solution}
Extend the coefficients by setting
$$
p_{ij}=0
$$
whenever $j>i$, so that $P=(p_{ij})_{0\le i,j\le n}$ is an
$(n+1)\times(n+1)$ matrix.

::: pf

::: {.pf-step #s1}

For every $0\le i,j\le n$,
$$
(PHP^T)_{ij}
=
\int_0^1P_i(t)P_j(t)\,dt.
$$

::: pf-proof

By matrix multiplication,
$$
\begin{aligned}
(PHP^T)_{ij}
&=
\sum_{\alpha=0}^n\sum_{\beta=0}^n
p_{i\alpha}H_{\alpha\beta}p_{j\beta}\\
&=
\sum_{\alpha=0}^n\sum_{\beta=0}^n
p_{i\alpha}p_{j\beta}
\int_0^1t^\alpha t^\beta\,dt.
\end{aligned}
$$
Because these are finite sums, they may be moved inside the integral:
$$
\begin{aligned}
(PHP^T)_{ij}
&=
\int_0^1
\left(\sum_{\alpha=0}^np_{i\alpha}t^\alpha\right)
\left(\sum_{\beta=0}^np_{j\beta}t^\beta\right)
\,dt\\
&=
\int_0^1P_i(t)P_j(t)\,dt.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The orthonormality hypothesis gives
$$
\boxed{PHP^T=I}.
$$

::: pf-proof

By step [](#s1){.pf-ref} and the assumed orthonormality,
$$
(PHP^T)_{ij}
=
\int_0^1P_i(t)P_j(t)\,dt
=
\delta_{ij}.
$$
Thus every entry of $PHP^T$ agrees with the corresponding entry of
the identity matrix.

:::

:::

::: pf-step

The matrix $P$ is invertible.

::: pf-proof

From step [](#s2){.pf-ref},
$$
n+1
=
\operatorname{rank}(I)
=
\operatorname{rank}(PHP^T)
\le
\operatorname{rank}(P)
\le
n+1.
$$
Hence
$$
\operatorname{rank}(P)=n+1,
$$
so the square matrix $P$ is invertible.

:::

:::

::: {.pf-step #s4}

One has
$$
H=P^{-1}P^{-T},
$$
where
$$
P^{-T}\coloneqq(P^{-1})^T.
$$

::: pf-proof

Multiply the identity
$$
PHP^T=I
$$
from step [](#s2){.pf-ref} on the left by $P^{-1}$ and on the right by
$(P^T)^{-1}=P^{-T}$. This gives
$$
H=P^{-1}P^{-T}.
$$

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{H^{-1}=P^TP}.
$$

::: pf-proof

The right-hand side in step [](#s4){.pf-ref} is a product of invertible matrices,
so $H$ is invertible. Inverting that identity and reversing the order
of factors gives
$$
\begin{aligned}
H^{-1}
&=
(P^{-1}P^{-T})^{-1}\\
&=
(P^{-T})^{-1}(P^{-1})^{-1}\\
&=
P^TP.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required identity.

:::

:::

:::
