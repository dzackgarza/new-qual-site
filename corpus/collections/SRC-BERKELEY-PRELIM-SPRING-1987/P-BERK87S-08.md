---
schema: qual/card@1
id: P-BERK87S-08
kind: problem
title: Derivatives preserve a strict half-plane containing all polynomial roots
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Factored p over C. Repeated roots already give derivative roots in the
    same half-plane; away from the roots, p'/p is the sum of reciprocals
    1/(z-lambda_j), each of which has negative real part when Re z <= 0.
---

::: {.problem}
Let $p(z)$ be a nonconstant complex polynomial all of whose roots satisfy
\[
\operatorname{Re}z>0.
\]
Prove that every root of $p'$ also satisfies
\[
\operatorname{Re}z>0.
\]
:::

::: {.solution}
Write
$$
p(z)
=
c\prod_{j=1}^n(z-\lambda_j),
$$
where the roots are listed with multiplicity. By hypothesis,
$$
\operatorname{Re}\lambda_j>0
$$
for every $j$.

::: pf

::: {.pf-step #shared-root-case}
Any root of $p'$ that is also a root of $p$ lies in the half-plane
$\operatorname{Re}z>0$.

::: pf-proof
Every root of $p$ has positive real part by hypothesis. Hence any point that
is simultaneously a root of $p$ and $p'$ already lies in the required
half-plane.
:::

:::

::: {.pf-step #logarithmic-derivative-formula}
If $w$ is not a root of $p$, then
$$
\frac{p'(w)}{p(w)}
=
\sum_{j=1}^n\frac{1}{w-\lambda_j}.
$$

::: pf-proof
Differentiating the factored expression for $p$ gives
$$
p'(z)
=
p(z)
\sum_{j=1}^n\frac{1}{z-\lambda_j}
$$
whenever $p(z)\ne0$. Dividing by $p(w)$ yields the formula.
:::

:::

::: {.pf-step #reciprocal-negative-real-part}
If $\operatorname{Re}w\leq0$, then for every $j$,
$$
\operatorname{Re}\frac{1}{w-\lambda_j}<0.
$$

::: pf-proof
Since $\operatorname{Re}\lambda_j>0$,
$$
\operatorname{Re}(w-\lambda_j)
=
\operatorname{Re}w-\operatorname{Re}\lambda_j
<0.
$$
For any nonzero complex number $u$,
$$
\operatorname{Re}\frac1u
=
\frac{\operatorname{Re}u}{\abs{u}^2}.
$$
Applying this with $u=w-\lambda_j$ gives the claim.
:::

:::

::: {.pf-step #root-boxed}
Every root $w$ of $p'$ satisfies
$$
\boxed{\operatorname{Re}w>0}.
$$

::: pf-proof
Let $p'(w)=0$. If $p(w)=0$, step [](#shared-root-case){.pf-ref} applies. Suppose instead that
$p(w)\ne0$. Then step [](#logarithmic-derivative-formula){.pf-ref} gives
$$
0
=
\frac{p'(w)}{p(w)}
=
\sum_{j=1}^n\frac{1}{w-\lambda_j}.
$$
If $\operatorname{Re}w\leq0$, every summand on the right has strictly
negative real part by step [](#reciprocal-negative-real-part){.pf-ref}, so their sum has strictly negative real
part and cannot equal $0$. Therefore $\operatorname{Re}w>0$.
:::

:::

::: pf-qed
Step [](#root-boxed){.pf-ref} proves the assertion for every zero of $p'$.
:::

:::
:::
