---
schema: qual/card@1
id: P-TIE-F15-12
kind: problem
title: Analytic functions real on a closed curve are constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 12.
---

::: {.problem}
Assume $f(z)$ is analytic in a region $D$ and $\Gamma$ is a rectifiable closed Jordan curve in $D$ whose interior lies in $D$. Prove that if $f(z)$ is real for all $z \in \Gamma$, then $f(z)$ is a constant.
:::

::: {.solution}

Let $\Omega$ denote the interior bounded by $\Gamma$, and write
$$
f=u+iv.
$$

::: pf

::: {.pf-step #s1-1}

The harmonic function $v$ vanishes on $\overline\Omega$.


::: pf-proof

Since $f$ is holomorphic on the region $D$ and $\overline\Omega\subset D$, its imaginary part $v$ is harmonic on a neighborhood of $\overline\Omega$ and continuous there. The hypothesis that $f$ is real on $\Gamma=\partial\Omega$ gives
$$
v=0
$$
on $\partial\Omega$.

By the maximum principle for harmonic functions,
$$
\max_{\overline\Omega}v
=
\max_{\partial\Omega}v
=0.
$$
Applying the same principle to $-v$ gives
$$
\max_{\overline\Omega}(-v)=0.
$$
Thus $v\le0$ and $v\ge0$ on $\Omega$, so
$$
v\equiv0
$$
on $\overline\Omega$.

:::

:::

::: {.pf-step #s1-2}

The function $f$ is constant on $\Omega$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(\Omega)\subset\RR.
$$
If $f$ were nonconstant on the connected open set $\Omega$, the open mapping theorem would imply that $f(\Omega)$ is open in $\CC$. No nonempty subset of $\RR$ is open in $\CC$. Hence $f$ must be constant on $\Omega$.

:::

:::

::: {.pf-step #s1-3}

The function $f$ is constant on all of $D$.


::: pf-proof

Let $c$ be the constant value from step [](#s1-2){.pf-ref}. Then the holomorphic function
$$
f-c
$$
vanishes on the nonempty open subset $\Omega$ of the region $D$. By the identity theorem,
$$
f-c\equiv0
$$
on $D$. Therefore
$$
\boxed{f\equiv c\text{ on }D.}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
