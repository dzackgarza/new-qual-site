---
schema: qual/card@1
id: P-ALGS23E
kind: problem
title: "Tensor product of a separable extension with its algebraic closure"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $E/F$ is a separable extension and $[E:F] = n$.
Suppose $\overline{E}$ is an algebraic closure of $E$.
Prove that $$E \otimes_F \overline{E} \simeq \underbrace{\overline{E} \oplus \cdots \oplus \overline{E}}_{n \text{ times}}$$ as rings.
:::

::: {.solution}

::: pf

::: pf-step

Since \(E/F\) is finite and separable, there exists \(\alpha\in E\) such that \(E=F(\alpha)\).

::: pf-proof

This is the primitive element theorem for finite separable extensions.

:::

:::

::: {.pf-step #s2}

Let \(m(x)\in F[x]\) be the minimal polynomial of \(\alpha\). Then \(\deg m=n\) and
\[
E\cong F[x]/(m).
\]

::: pf-proof

Because \(E=F(\alpha)\), one has \([E:F]=\deg m=n\), and evaluation at \(\alpha\) identifies \(F[x]/(m)\) with \(F(\alpha)=E\).

:::

:::

::: {.pf-step #s3}

There is a natural ring isomorphism
\[
E\otimes_F\overline E
\cong
\overline E[x]/(m).
\]

::: pf-proof

Using step [](#s2){.pf-ref} and scalar extension,
\[
(F[x]/(m))\otimes_F\overline E
\cong
\overline E[x]/(m).
\]

:::

:::

::: {.pf-step #s4}

The polynomial \(m\) has exactly \(n\) distinct roots \(\alpha_1,\dots,\alpha_n\) in \(\overline E\), so
\[
m(x)=\prod_{i=1}^n (x-\alpha_i).
\]

::: pf-proof

The polynomial \(m\) is separable because \(E/F\) is separable. Since \(\overline E\) is algebraically closed, \(m\) splits there; separability makes the roots distinct. Its degree is \(n\) by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The ideals \((x-\alpha_i)\subseteq\overline E[x]\) are pairwise comaximal.

::: pf-proof

If \(i\ne j\), then
\[
(x-\alpha_i)-(x-\alpha_j)=\alpha_j-\alpha_i
\]
is a nonzero element of the field \(\overline E\), hence a unit. Therefore the two ideals sum to the whole polynomial ring.

:::

:::

::: {.pf-step #s6}

By the Chinese remainder theorem,
\[
\overline E[x]/(m)
\cong
\prod_{i=1}^n \overline E[x]/(x-\alpha_i)
\cong
\overline E^{\,n}.
\]

::: pf-proof

Use steps [](#s4){.pf-ref} and [](#s5){.pf-ref} for the first isomorphism. Evaluation at \(\alpha_i\) identifies each quotient \(\overline E[x]/(x-\alpha_i)\) with \(\overline E\).

:::

:::

::: pf-step

Hence
\[
E\otimes_F\overline E\cong
\underbrace{\overline E\oplus\cdots\oplus\overline E}_{n\text{ times}}
\]
as rings.

::: pf-proof

Combine steps [](#s3){.pf-ref} and [](#s6){.pf-ref}. For a finite number of factors, the direct product and direct sum have the same underlying ring.

:::

:::

:::

:::
