---
schema: qual/card@1
id: P-BKS13-8B
kind: problem
title: Average trace of permutation matrices in $S_n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 5 of the retained Spring 2013 solution PDF and independently reviewed the fixed-point count.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the trace/fixed-point identification and the count of permutations fixing a chosen point.
---

::: {.problem}
Consider the symmetric group $\Sigma _ { n }$ in its presentation as $n \times n$ permutation matrices. Define the “expected trace” to be the weighted sum of traces

$$
E _ { n } = { \frac { 1 } { n ! } } \sum _ { g \in \Sigma _ { n } } { \mathrm { T r a c e } } ( g )
$$

Calculate $E _ { n } .$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a permutation
$$
\sigma\in\Sigma_n,
$$
the trace of its permutation matrix equals the number of fixed points of
$\sigma$.

::: pf-proof

The $i$th diagonal entry of the permutation matrix is $1$ exactly when
$$
\sigma(i)=i,
$$
and is $0$ otherwise. Summing the diagonal entries therefore counts fixed
points.

:::

:::

::: {.pf-step #s2}

For each
$$
i\in\{1,\ldots,n\},
$$
exactly
$$
(n-1)!
$$
permutations in $\Sigma_n$ fix $i$.

::: pf-proof

Once $i$ is fixed, the remaining $n-1$ elements may be permuted
arbitrarily. There are $(n-1)!$ such permutations.

:::

:::

::: {.pf-step #s3}

The sum of the traces over all permutation matrices is
$$
\sum_{\sigma\in\Sigma_n}\operatorname{Trace}(\sigma)
=
n!.
$$

::: pf-proof

Using step [](#s1){.pf-ref} and counting fixed points by their position,
$$
\begin{aligned}
\sum_{\sigma\in\Sigma_n}\operatorname{Trace}(\sigma)
&=
\sum_{i=1}^n
\#\{\sigma\in\Sigma_n:\sigma(i)=i\}\\
&=
n(n-1)!\\
&=
n!,
\end{aligned}
$$
by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{E_n=1}.
$$

::: pf-proof

By the definition of $E_n$ and step [](#s3){.pf-ref},
$$
E_n
=
\frac1{n!}
\sum_{\sigma\in\Sigma_n}\operatorname{Trace}(\sigma)
=
\frac{n!}{n!}
=
1.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested value.

:::

:::

:::
