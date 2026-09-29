---
schema: qual/card@1
id: P-BERK96S-13
kind: problem
title: An analytic function with a nontrivial real linear relation between its real and imaginary parts is constant
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the multiplication by a-ib, the Cauchy--Riemann argument, and
    the use of connectedness to conclude constancy.
---

::: {.problem}
Let $f=u+iv$ be analytic on a connected open set $D\subset\mathbb C$. Suppose there are real constants $a,b,c$ with
\[
a^2+b^2\ne0
\]
and
\[
au+bv=c
\]
throughout $D$. Prove that $f$ is constant on $D$.
:::

::: {.solution}
Define
$$
g\coloneqq(a-ib)f.
$$

::: pf

::: {.pf-step #s1}

The function $g$ is analytic on $D$ and has constant real part equal
to $c$.

::: pf-proof

Since $a-ib$ is constant and $f$ is analytic, $g$ is analytic. Also
$$
\begin{aligned}
g
&=
(a-ib)(u+iv)\\
&=
(au+bv)+i(av-bu).
\end{aligned}
$$
By hypothesis,
$$
\Re g=au+bv=c.
$$

:::

:::

::: {.pf-step #s2}

The function $g$ is constant on $D$.

::: pf-proof

Write
$$
g=P+iQ.
$$
By step [](#s1){.pf-ref}, $P=c$, so
$$
P_x=P_y=0.
$$
The Cauchy--Riemann equations give
$$
Q_y=P_x=0,
\qquad
Q_x=-P_y=0.
$$
Thus $Q$ is locally constant. Since $D$ is connected, $Q$ is constant on
$D$. Therefore $g=P+iQ$ is constant on $D$.

:::

:::

::: {.pf-step #s3}

The function $f$ is constant on $D$.

::: pf-proof

The condition
$$
a^2+b^2\neq0
$$
implies
$$
a-ib\neq0.
$$
Hence
$$
f=\frac{g}{a-ib}.
$$
Step [](#s2){.pf-ref} therefore implies that $f$ is constant.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
