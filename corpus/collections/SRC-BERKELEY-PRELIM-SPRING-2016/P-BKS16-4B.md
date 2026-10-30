---
schema: qual/card@1
id: P-BKS16-4B
kind: problem
title: Contour integral of $(6z^5+1)/(z^6+z+1)$ over $\abs{z}=2$
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
  note: Restored the contour integral of (6z^5+1)/(z^6+z+1) over C against Sp16_Exam.pdf page 15 problem 4B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2016 solution and verified the zero count by Rouché's theorem.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the strict Rouché inequality on $\abs{z}=2$ and the argument-principle evaluation.
---

::: {.problem}
Compute

$$
\int_C \frac{6z^5 + 1}{z^6 + z + 1} \, dz,
$$

where $C$ is the circle centered at the origin with radius 2, oriented counterclockwise.
:::

::: {.solution}

Put
$$
P(z)\coloneqq z^6+z+1.
$$
Then $P'(z)=6z^5+1$.

::: pf

::: {.pf-step #s1-1}

The polynomial $P$ has exactly six zeros inside $C$ and no zeros on $C$.


::: pf-proof

On $C$, one has $\abs{z}=2$, so
$$
\abs{z+1}\leq \abs{z}+1=3<64=\abs{z^6}.
$$
By Rouché's theorem, $z^6$ and
$$
P(z)=z^6+(z+1)
$$
have the same number of zeros inside $C$, counted with multiplicity. Since $z^6$ has six zeros there, so does $P$. The strict inequality also implies that $P$ has no zero on $C$.

:::

:::

::: {.pf-step #s1-2}

The integral equals
$$
\boxed{12\pi i}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the argument principle applies to $P$ on $C$. Since $P$ is a polynomial and has six zeros inside $C$, counted with multiplicity,
$$
\int_C\frac{P'(z)}{P(z)}\,dz
=
2\pi i\cdot6
=
12\pi i.
$$
Substituting $P'(z)=6z^5+1$ gives the integral in the problem.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested value.

:::

:::

:::
