---
schema: qual/card@1
id: E-SMI-8000E-CY1
kind: problem
title: Conjugates of cycles in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000e cycles problem 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Verified the conjugated permutation on every point in and outside the support of the cycle."
---

::: {.exercise}
Prove: if $s$ is any permutation in $S_n$, and $(a_1\,a_2\,\cdots\,a_k)$ is the cycle taking $a_1$ to $a_2$, etc., then
\[
s(a_1\,a_2\,\cdots\,a_k)s^{-1} = \bigl(s(a_1)\,s(a_2)\,\cdots\,s(a_k)\bigr).
\]
:::

::: {.solution}
Let
$$
c=(a_1\,a_2\,\cdots\,a_k)
$$
and
$$
d=\bigl(s(a_1)\,s(a_2)\,\cdots\,s(a_k)\bigr).
$$
We show that the permutations $scs^{-1}$ and $d$ agree on every element of
$\{1,\ldots,n\}$.

::: pf

::: {.pf-step #s1}

Compute the action on the support of the conjugated cycle.

::: pf-proof

For $1\le i<k$,
$$
\begin{aligned}
(scs^{-1})(s(a_i))
&=s(c(a_i))\\
&=s(a_{i+1}).
\end{aligned}
$$
Similarly,
$$
(scs^{-1})(s(a_k))
=s(c(a_k))
=s(a_1).
$$
Thus $scs^{-1}$ acts on the points
$$
s(a_1),\ldots,s(a_k)
$$
exactly as the cycle $d$ does.

:::

:::

::: {.pf-step #s2}

Both permutations fix every point outside that support.

::: pf-proof

Let $x$ be different from each $s(a_i)$. Since $s$ is bijective,
$s^{-1}(x)$ is different from every $a_i$. Hence $c$ fixes $s^{-1}(x)$,
and therefore
$$
(scs^{-1})(x)
=s(s^{-1}(x))
=x.
$$
The cycle $d$ also fixes $x$ by definition.

:::

:::

::: pf-step

Conclude the equality of permutations.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that $scs^{-1}$ and $d$ have the same value on
every point. Hence
$$
\boxed{
s(a_1\,a_2\,\cdots\,a_k)s^{-1}
=\bigl(s(a_1)\,s(a_2)\,\cdots\,s(a_k)\bigr).}
$$

:::

:::

:::

:::
