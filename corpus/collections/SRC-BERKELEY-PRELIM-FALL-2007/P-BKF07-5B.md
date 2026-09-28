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

<1>1. For every $r\ge R_0$,
$$
\int_{\abs{z}=r}g(z)\,dz
=2\pi i\sum_{j=1}^n\operatorname{Res}_{z=a_j}g(z).
$$

::: {.proof}
The function $g=1/f$ is meromorphic on $\CC$, with poles precisely at
the zeros $a_1,\ldots,a_n$ of $f$. For $r\ge R_0$, all of these poles
lie inside the circle $\abs{z}=r$, and there are no poles on or outside
that circle. The residue theorem therefore gives the displayed identity.
:::

<1>2. For every $r\ge R_0$,
$$
\left|\int_{\abs{z}=r}g(z)\,dz\right|
\le 2\pi r^{1-\alpha}.
$$

::: {.proof}
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

<1>3. The contour integrals in step <1>1 tend to $0$ as
$r\to\infty$.

::: {.proof}
Since $\alpha>1$, the exponent $1-\alpha$ is negative. Hence
$2\pi r^{1-\alpha}\to0$, and step <1>2 gives the claim.
:::

<1>4. The sum of residues satisfies
$$
\sum_{j=1}^n\operatorname{Res}_{z=a_j}\frac1{f(z)}
=\boxed{0}.
$$

::: {.proof}
By step <1>1, for every $r\ge R_0$ the contour integral equals
$2\pi i$ times the displayed sum, which is independent of $r$.
Step <1>3 shows that the left-hand side tends to $0$ as $r\to\infty$.
Therefore the constant residue sum must be $0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required identity.
:::
:::
