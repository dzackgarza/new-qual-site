---
schema: qual/card@1
id: P-BERK95S-01
kind: problem
title: The sequence $\cos(nx)$ has no uniformly convergent subsequence on $\RR$
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
For each positive integer $n$, define
\[
f_n(x)=\cos(nx),
\qquad x\in\mathbb R.
\]
Prove that the sequence $(f_n)$ has no uniformly convergent subsequence.
:::

::: {.solution}
<1>1. If $m\ne n$ are positive integers, then
$$
\int_0^{2\pi}
\bigl(\cos(mx)-\cos(nx)\bigr)^2\,dx
=2\pi.
$$

::: {.proof}
The standard trigonometric orthogonality relations give
$$
\int_0^{2\pi}\cos^2(mx)\,dx
=
\int_0^{2\pi}\cos^2(nx)\,dx
=\pi
$$
and, because $m\ne n$,
$$
\int_0^{2\pi}\cos(mx)\cos(nx)\,dx=0.
$$
Expanding the square proves the claim.
:::

<1>2. Distinct members of the sequence satisfy
$$
\norm{f_m-f_n}_{\infty}\ge1.
$$

::: {.proof}
By step <1>1,
$$
2\pi
\le
\int_0^{2\pi}
\norm{f_m-f_n}_{\infty}^2\,dx
=2\pi\norm{f_m-f_n}_{\infty}^2.
$$
Taking square roots gives the result.
:::

<1>3. No subsequence of $(f_n)$ converges uniformly on $\RR$.

::: {.proof}
Every uniformly convergent sequence is uniformly Cauchy. But any
subsequence $(f_{n_k})$ consists of functions with distinct indices,
and step <1>2 gives
$$
\norm{f_{n_k}-f_{n_\ell}}_{\infty}\ge1
\qquad(k\ne\ell).
$$
Hence no subsequence is uniformly Cauchy.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
