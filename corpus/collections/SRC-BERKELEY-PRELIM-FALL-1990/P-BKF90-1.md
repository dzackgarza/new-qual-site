---
schema: qual/card@1
id: P-BKF90-1
kind: problem
title: Integer solutions of $a^b=b^a$ with $a<b$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Reduced by the gcd to coprime factors, which forces the smaller coprime
    factor to be one, then solved the remaining equation a^(y-1)=y.
---

::: {.problem}
Find all pairs of integers $a,b$ satisfying
\[
0<a<b,
\qquad
a^b=b^a.
\]
:::

::: {.solution}

::: pf

::: pf-step

Write
$$
d\coloneqq\gcd(a,b),
\qquad
a=dx,
\qquad
b=dy,
$$
where $x,y$ are coprime positive integers with $x<y$.

::: pf-proof

This is the standard decomposition by the greatest common divisor. Since $0<a<b$, one has $x<y$.

:::

:::

::: {.pf-step #s2}

One has $x=1$.

::: pf-proof

The equation $a^b=b^a$ becomes
$$
(dx)^{dy}=(dy)^{dx}.
$$
Both sides are positive, so taking the $d$th root gives
$$
(dx)^y=(dy)^x.
$$
Hence
$$
d^{y-x}x^y=y^x.
$$
In particular $x^y$ divides $y^x$. Since $x$ and $y$ are coprime, $x^y$ is coprime to $y^x$. Therefore $x^y=1$, so $x=1$.

:::

:::

::: {.pf-step #s3}

If $y=b/a$, then
$$
a^{y-1}=y.
$$

::: pf-proof

By step [](#s2){.pf-ref}, $a=d$ and $b=dy=ay$. Substituting into $a^b=b^a$ gives
$$
a^{ay}=(ay)^a.
$$
Taking the positive $a$th root yields
$$
a^y=ay,
$$
and division by $a>0$ gives the claim.

:::

:::

::: {.pf-step #s4}

The only possibility is $y=2$ and $a=2$.

::: pf-proof

Since $y>1$, step [](#s3){.pf-ref} rules out $a=1$, so $a\ge2$. If $y\ge3$, then
$$
y=a^{y-1}\ge2^{y-1}>y,
$$
a contradiction. The last strict inequality holds for $y=3$ and then inductively, since doubling a number larger than $y$ gives a number larger than $y+1$.

Thus $y=2$. Step [](#s3){.pf-ref} then gives
$$
a=a^{2-1}=2.
$$

:::

:::

::: {.pf-step #s5}

The complete solution is
$$
\boxed{(a,b)=(2,4)}.
$$

::: pf-proof

By step [](#s4){.pf-ref}, $a=2$ and $y=2$, so $b=ay=4$. Conversely,
$$
2^4=16=4^2,
$$
so this pair satisfies the equation and the inequality $0<a<b$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives all pairs satisfying the stated conditions.

:::

:::

:::
