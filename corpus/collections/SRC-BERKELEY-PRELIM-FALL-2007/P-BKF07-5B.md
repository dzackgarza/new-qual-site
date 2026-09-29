---
schema: qual/card@1
id: P-BKF07-5B
kind: problem
title: Sum of residues of the reciprocal of a rapidly growing entire function
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the large-circle residue identity and the decay
    estimate from the growth hypothesis against the vendored solution.
---

::: {.problem}
Let \(f\) be entire and let \(a_1,\ldots,a_n\) be all of its zeros in \(\mathbb C\). Suppose there exist \(R>0\) and \(\alpha>1\) such that
\[
|f(z)|\ge |z|^\alpha
\]
for every \(|z|\ge R\). Prove that
\[
\sum_{j=1}^n \operatorname{Res}_{z=a_j}\frac1{f(z)}=0.
\]
:::

::: {.solution}

Set
$$
g(z)\coloneqq\frac1{f(z)}.
$$
Choose $R_0>R$ so large that every zero
$a_1,\ldots,a_n$ lies in the disk $\abs{z}<R_0$.

::: pf

::: {.pf-step #contour-integral-residue-sum}
For every $r\ge R_0$,
$$
\int_{\abs{z}=r}g(z)\,dz
=2\pi i\sum_{j=1}^n\operatorname{Res}_{z=a_j}g(z).
$$

::: pf-proof
The function $g=1/f$ is meromorphic on $\CC$, with poles precisely at
the zeros $a_1,\ldots,a_n$ of $f$. For $r\ge R_0$, all of these poles
lie inside the circle $\abs{z}=r$, and there are no poles on or outside
that circle. The residue theorem therefore gives the displayed identity.
:::

:::

::: {.pf-step #integral-bound}
For every $r\ge R_0$,
$$
\left|\int_{\abs{z}=r}g(z)\,dz\right|
\le 2\pi r^{1-\alpha}.
$$

::: pf-proof
On the circle $\abs{z}=r$, the hypothesis gives
$$
\abs{g(z)}
=\frac1{\abs{f(z)}}
\le\frac1{r^\alpha}.
$$
The circle has length $2\pi r$, so the ML estimate yields
$$
\left|\int_{\abs{z}=r}g(z)\,dz\right|
\le 2\pi r\cdot r^{-\alpha}
=2\pi r^{1-\alpha}.
$$
:::

:::

::: {.pf-step #integral-tends-to-zero}
The contour integrals in step [](#contour-integral-residue-sum){.pf-ref} tend to $0$ as
$r\to\infty$.

::: pf-proof
Since $\alpha>1$, the exponent $1-\alpha$ is negative. Hence
$2\pi r^{1-\alpha}\to0$, and step [](#integral-bound){.pf-ref} gives the claim.
:::

:::

::: {.pf-step #residue-sum-zero}
The sum of residues satisfies
$$
\sum_{j=1}^n\operatorname{Res}_{z=a_j}\frac1{f(z)}
=\boxed{0}.
$$

::: pf-proof
By step [](#contour-integral-residue-sum){.pf-ref}, for every $r\ge R_0$ the contour integral equals
$2\pi i$ times the displayed sum, which is independent of $r$.
Step [](#integral-tends-to-zero){.pf-ref} shows that the left-hand side tends to $0$ as $r\to\infty$.
Therefore the constant residue sum must be $0$.
:::

:::

::: pf-qed
Step [](#residue-sum-zero){.pf-ref} is the required identity.
:::

:::

:::
