---
schema: qual/card@1
id: P-BERK95S-03
kind: problem
title: A residue integral for $\sin(n\theta)/\sin\theta$
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
---

::: {.problem}
Let $n$ be a positive integer and $0<\theta<\pi$. Prove that
\[
\frac1{2\pi i}\int_{|z|=2}
\frac{z^n}{1-2z\cos\theta+z^2}\,dz
=\frac{\sin(n\theta)}{\sin\theta},
\]
where the circle $|z|=2$ is positively oriented.
:::

::: {.solution}
<1>1. The denominator factors as
$$
1-2z\cos\theta+z^2
=(z-e^{i\theta})(z-e^{-i\theta}).
$$

::: {.proof}
Since
$$
e^{i\theta}+e^{-i\theta}=2\cos\theta,
\qquad
e^{i\theta}e^{-i\theta}=1,
$$
expanding the product gives the denominator. Because
$0<\theta<\pi$, the two roots are distinct. Both have modulus $1$, so
both poles lie inside the contour $\abs z=2$.
:::

<1>2. The sum of the residues inside the contour is
$$
\frac{\sin(n\theta)}{\sin\theta}.
$$

::: {.proof}
At $z=e^{i\theta}$ the residue is
$$
\frac{e^{in\theta}}{e^{i\theta}-e^{-i\theta}}
=
\frac{e^{in\theta}}{2i\sin\theta}.
$$
At $z=e^{-i\theta}$ it is
$$
\frac{e^{-in\theta}}{e^{-i\theta}-e^{i\theta}}
=
-\frac{e^{-in\theta}}{2i\sin\theta}.
$$
Their sum is
$$
\frac{e^{in\theta}-e^{-in\theta}}{2i\sin\theta}
=
\frac{\sin(n\theta)}{\sin\theta}.
$$
:::

<1>3.
$$
\frac1{2\pi i}\int_{\abs z=2}
\frac{z^n}{1-2z\cos\theta+z^2}\,dz
=\frac{\sin(n\theta)}{\sin\theta}.
$$

::: {.proof}
By the residue theorem, the left-hand side is the sum of the residues
inside the positively oriented circle. Step <1>2 computes that sum.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the desired identity.
:::
:::
