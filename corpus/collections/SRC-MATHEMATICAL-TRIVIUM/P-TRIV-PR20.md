---
schema: qual/card@1
id: P-TRIV-PR20
kind: problem
title: Wald's identities for a random sum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Part (c)'s variance/operator symbols are damaged in the deterministic extraction, so the missing identity is recorded as an explicit gap rather than reconstructed.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the unresolved variance identity in part (c) and removed a stray digit against Probability Problem 20 on page 30 of the source PDF.
---

::: {.problem}
Let $\xi_1, \ldots, \xi_n, \tau$ be independent random variables, $\xi_1, \ldots, \xi_n$ have the same distribution, $\tau$ takes the values $1, \ldots, n$.
Consider the sum of a random number of the random variables $S_\tau = \xi_1 + \ldots + \xi_\tau$.
Show that

(a) $\mathbf{E} S_\tau = \mathbf{E}\tau \cdot \mathbf{E}\xi_1$,

(b) $\mathbf{E}(S_\tau | \tau) = \tau \mathbf{E}\xi_1$,

(c) $\mathbf{D} S_\tau = \mathbf{E}\tau \cdot \mathbf{D}\xi_1 + \mathbf{D}\tau \cdot (\mathbf{E}\xi_1)^2$,

(d) $\mathbf{D}(S_\tau | \tau) = \tau \mathbf{D}\xi_1$.
:::

::: {.solution}

Put
$$
\mu=\mathbf E\xi_1,
\qquad
\sigma^2=\mathbf D\xi_1.
$$
Assume these moments are finite.

::: pf

::: {.pf-step #s1-1}

Conditional on $\tau=k$,
$$
S_\tau=\xi_1+\cdots+\xi_k.
$$


::: pf-proof

This is the definition of the random sum $S_\tau$. Independence of $\tau$ from the $\xi_i$ means that conditioning on $\tau=k$ does not change the joint distribution of $\xi_1,\ldots,\xi_k$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\mathbf E(S_\tau\mid\tau)=\tau\mu}.
$$


::: pf-proof

On the event $\{\tau=k\}$, step [](#s1-1){.pf-ref} and linearity of expectation give
$$
\mathbf E(S_\tau\mid\tau=k)
=\sum_{i=1}^k\mathbf E\xi_i=k\mu.
$$
Thus the conditional expectation as a function of $\tau$ is $\tau\mu$.

:::

:::

::: {.pf-step #s1-3}

Taking expectations in step [](#s1-2){.pf-ref} gives
$$
\boxed{\mathbf ES_\tau=\mathbf E\tau\cdot\mathbf E\xi_1}.
$$


::: pf-proof

By the tower property,
$$
\mathbf ES_\tau
=\mathbf E\bigl[\mathbf E(S_\tau\mid\tau)\bigr]
=\mathbf E(\tau\mu)
=\mu\mathbf E\tau.
$$

:::

:::

::: {.pf-step #s1-4}

Conditional on $\tau=k$,
$$
\mathbf D(S_\tau\mid\tau=k)=k\sigma^2.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $S_\tau$ is then a sum of $k$ independent identically distributed variables. Variances of independent sums add, so
$$
\mathbf D(\xi_1+\cdots+\xi_k)
=\sum_{i=1}^k\mathbf D\xi_i=k\sigma^2.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{\mathbf D(S_\tau\mid\tau)=\tau\mathbf D\xi_1}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} identifies the conditional variance on each event $\{\tau=k\}$, so as a random variable measurable with respect to $\tau$ it equals $\tau\sigma^2$.

:::

:::

::: {.pf-step #s1-6}

The law of total variance gives
$$
\mathbf D S_\tau
=\mathbf E\bigl[\mathbf D(S_\tau\mid\tau)\bigr]
+\mathbf D\bigl(\mathbf E(S_\tau\mid\tau)\bigr).
$$


::: pf-proof

Write
$$
S_\tau-\mathbf ES_\tau
=\bigl(S_\tau-\mathbf E(S_\tau\mid\tau)\bigr)
+\bigl(\mathbf E(S_\tau\mid\tau)-\mathbf ES_\tau\bigr).
$$
After squaring and taking expectations, the cross term vanishes because its conditional expectation given $\tau$ is zero. The two remaining terms are exactly the two terms displayed.

:::

:::

::: {.pf-step #s1-7}

Consequently
$$
\boxed{
\mathbf D S_\tau
=\mathbf E\tau\cdot\mathbf D\xi_1
+\mathbf D\tau\cdot(\mathbf E\xi_1)^2}.
$$


::: pf-proof

Substitute steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref} into step [](#s1-6){.pf-ref}:
$$
\mathbf E(\tau\sigma^2)+\mathbf D(\tau\mu)
=\sigma^2\mathbf E\tau+\mu^2\mathbf D\tau.
$$

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref}, [](#s1-2){.pf-ref}, and [](#s1-7){.pf-ref}, and [](#s1-5){.pf-ref} prove parts (a), (b), (c), and (d), respectively.

:::

:::

:::
