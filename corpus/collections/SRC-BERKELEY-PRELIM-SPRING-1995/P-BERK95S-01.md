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

::: pf

::: {.pf-step #s1}

If $m\ne n$ are positive integers, then
$$
\int_0^{2\pi}
\bigl(\cos(mx)-\cos(nx)\bigr)^2\,dx
=2\pi.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

Distinct members of the sequence satisfy
$$
\norm{f_m-f_n}_{\infty}\ge1.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
2\pi
\le
\int_0^{2\pi}
\norm{f_m-f_n}_{\infty}^2\,dx
=2\pi\norm{f_m-f_n}_{\infty}^2.
$$
Taking square roots gives the result.

:::

:::

::: {.pf-step #s3}

No subsequence of $(f_n)$ converges uniformly on $\RR$.

::: pf-proof

Every uniformly convergent sequence is uniformly Cauchy. But any
subsequence $(f_{n_k})$ consists of functions with distinct indices,
and step [](#s2){.pf-ref} gives
$$
\norm{f_{n_k}-f_{n_\ell}}_{\infty}\ge1
\qquad(k\ne\ell).
$$
Hence no subsequence is uniformly Cauchy.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
