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

::: problem
Suppose $E/F$ is a separable extension and $[E:F] = n$.
Suppose $\overline{E}$ is an algebraic closure of $E$.
Prove that $$E \otimes_F \overline{E} \simeq \underbrace{\overline{E} \oplus \cdots \oplus \overline{E}}_{n \text{ times}}$$ as rings.
:::


::: {.solution}
<1>1. Since \(E/F\) is finite and separable, there exists \(\alpha\in E\) such that \(E=F(\alpha)\).
::: {.proof}
This is the primitive element theorem for finite separable extensions.
:::

<1>2. Let \(m(x)\in F[x]\) be the minimal polynomial of \(\alpha\). Then \(\deg m=n\) and
\[
E\cong F[x]/(m).
\]
::: {.proof}
Because \(E=F(\alpha)\), one has \([E:F]=\deg m=n\), and evaluation at \(\alpha\) identifies \(F[x]/(m)\) with \(F(\alpha)=E\).
:::

<1>3. There is a natural ring isomorphism
\[
E\otimes_F\overline E
\cong
\overline E[x]/(m).
\]
::: {.proof}
Using <1>2 and scalar extension,
\[
(F[x]/(m))\otimes_F\overline E
\cong
\overline E[x]/(m).
\]
:::

<1>4. The polynomial \(m\) has exactly \(n\) distinct roots \(\alpha_1,\dots,\alpha_n\) in \(\overline E\), so
\[
m(x)=\prod_{i=1}^n (x-\alpha_i).
\]
::: {.proof}
The polynomial \(m\) is separable because \(E/F\) is separable. Since \(\overline E\) is algebraically closed, \(m\) splits there; separability makes the roots distinct. Its degree is \(n\) by <1>2.
:::

<1>5. The ideals \((x-\alpha_i)\subseteq\overline E[x]\) are pairwise comaximal.
::: {.proof}
If \(i\ne j\), then
\[
(x-\alpha_i)-(x-\alpha_j)=\alpha_j-\alpha_i
\]
is a nonzero element of the field \(\overline E\), hence a unit. Therefore the two ideals sum to the whole polynomial ring.
:::

<1>6. By the Chinese remainder theorem,
\[
\overline E[x]/(m)
\cong
\prod_{i=1}^n \overline E[x]/(x-\alpha_i)
\cong
\overline E^{\,n}.
\]
::: {.proof}
Use <1>4 and <1>5 for the first isomorphism. Evaluation at \(\alpha_i\) identifies each quotient \(\overline E[x]/(x-\alpha_i)\) with \(\overline E\).
:::

<1>7. Hence
\[
E\otimes_F\overline E\cong
\underbrace{\overline E\oplus\cdots\oplus\overline E}_{n\text{ times}}
\]
as rings.
::: {.proof}
Combine <1>3 and <1>6. For a finite number of factors, the direct product and direct sum have the same underlying ring.
:::
:::
