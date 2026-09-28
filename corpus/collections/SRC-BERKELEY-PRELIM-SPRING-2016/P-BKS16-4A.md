---
schema: qual/card@1
id: P-BKS16-4A
kind: problem
title: Real-rootedness of real polynomials via the sign of $\operatorname{Im}(p'/p)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the imaginary-part symbols and the prime in p' against Sp16_Exam.pdf page 5 problem 4A.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the logarithmic-derivative factorization for real roots and the local contradiction near an upper-half-plane root in the converse.
---

::: {.problem}
Prove that a monic polynomial $p(z)$ with real coefficients is real-rooted if and only if $\Im(p'(z)/p(z)) < 0$ whenever $\Im(z) > 0$. ($\Im(z)$ denotes the imaginary part of $z$.)
:::

::: {.solution}
<1>1. Suppose first that all roots of $p$ are real. If
$$
p(z)=\prod_{j=1}^d(z-\lambda_j),
\qquad
\lambda_j\in\RR,
$$
with roots repeated according to multiplicity, then for every $z$ in the upper half-plane,
$$
\frac{p'(z)}{p(z)}
=
\sum_{j=1}^d\frac1{z-\lambda_j}.
$$

::: {.proof}
Since every root $\lambda_j$ is real, a point $z$ with $\Im z>0$ is not a root of $p$. Taking the logarithmic derivative of the displayed factorization gives the identity.
:::

<1>2. Under the hypothesis of step <1>1,
$$
\Im\left(\frac{p'(z)}{p(z)}\right)<0
$$
whenever $\Im z>0$.

::: {.proof}
Write
$$
z=x+iy,
\qquad
y>0.
$$
For every real $\lambda_j$,
$$
\frac1{z-\lambda_j}
=
\frac{x-\lambda_j-iy}{(x-\lambda_j)^2+y^2},
$$
so
$$
\Im\left(\frac1{z-\lambda_j}\right)
=
-\frac{y}{(x-\lambda_j)^2+y^2}
<
0.
$$
Summing over $j$ and using step <1>1 gives the claim.
:::

<1>3. Conversely, suppose that $p$ is not real-rooted. Then $p$ has a root
$$
\lambda=a+ib
$$
with $b>0$.

::: {.proof}
Because $p$ has real coefficients, its nonreal roots occur in conjugate pairs. Hence any nonreal root has a conjugate partner, and one of the pair lies in the upper half-plane.
:::

<1>4. Let $m\geq1$ be the multiplicity of $\lambda$, and write
$$
p(z)=(z-\lambda)^m q(z),
\qquad
q(\lambda)\neq0.
$$
Then, away from the roots of $p$,
$$
\frac{p'(z)}{p(z)}
=
\frac{m}{z-\lambda}
+
\frac{q'(z)}{q(z)}.
$$

::: {.proof}
Differentiate the factorization and divide by $(z-\lambda)^mq(z)$.
:::

<1>5. For all sufficiently small $\epsilon>0$, the point
$$
z_\epsilon=\lambda-i\epsilon
$$
lies in the upper half-plane and satisfies
$$
\Im\left(\frac{p'(z_\epsilon)}{p(z_\epsilon)}\right)>0.
$$

::: {.proof}
Since $q(\lambda)\neq0$, there is a neighborhood of $\lambda$ on which $q$ has no zeros. On a sufficiently small closed disk in that neighborhood, the continuous function $q'/q$ is bounded; choose $M>0$ with
$$
\left|\frac{q'(z)}{q(z)}\right|\leq M
$$
there.

Take
$$
0<\epsilon<\min\left(b,\frac{m}{M+1}\right)
$$
small enough that $z_\epsilon$ lies in this disk. Then $\Im z_\epsilon=b-\epsilon>0$, and by step <1>4,
$$
\frac{p'(z_\epsilon)}{p(z_\epsilon)}
=
\frac{m}{-i\epsilon}
+
\frac{q'(z_\epsilon)}{q(z_\epsilon)}
=
\frac{mi}{\epsilon}
+
\frac{q'(z_\epsilon)}{q(z_\epsilon)}.
$$
Therefore
$$
\Im\left(\frac{p'(z_\epsilon)}{p(z_\epsilon)}\right)
\geq
\frac{m}{\epsilon}-M
>
1
>
0.
$$
:::

<1>6. Hence the condition
$$
\Im\left(\frac{p'(z)}{p(z)}\right)<0
\quad\text{whenever }\Im z>0
$$
holds if and only if $p$ is real-rooted.

::: {.proof}
Steps <1>1--<1>2 prove the forward implication. If $p$ were not real-rooted, steps <1>3--<1>5 would produce a point in the upper half-plane where the imaginary part is positive, contradicting the stated condition. Thus the condition implies real-rootedness.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves both directions.
:::
:::
