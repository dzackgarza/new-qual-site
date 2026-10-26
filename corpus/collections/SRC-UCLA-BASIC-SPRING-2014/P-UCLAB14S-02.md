---
schema: qual/card@1
id: P-UCLAB14S-02
kind: problem
title: Images of two linear maps and their composition
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 2. Suppose that $S,T\in\operatorname{Hom}(V,V)$, where $V$ is a finite-dimensional vector space over $\mathbb R$.
Let $\operatorname{im}S$ be the image of $S$ and $\ker S$ the kernel of $S$.
Show that
\[
\dim(\operatorname{im}S)+\dim(\operatorname{im}T)
\leq \dim(\operatorname{im}(S\circ T))+\dim V.
\]
:::

::: pf

::: pf-step

Restrict $S$ to $\operatorname{im}T$:
\[
S|_{\operatorname{im}T}:\operatorname{im}T\to V.
\]
Its image is $\operatorname{im}(S\circ T)$.


::: pf-proof

An element of the image is $S(Tv)$ for some $v\in V$, and conversely every $(S\circ T)(v)$ has this form.

:::

:::

::: pf-step

The kernel of the restriction is
\[
\ker S\cap\operatorname{im}T.
\]


::: pf-proof

For $y\in\operatorname{im}T$, the equation $S(y)=0$ is equivalent to $y\in\ker S\cap\operatorname{im}T$.

:::

:::

::: pf-step

Rank--nullity for the restriction gives
\[
\dim(\operatorname{im}T)
=\dim(\ker S\cap\operatorname{im}T)
+\dim(\operatorname{im}(S\circ T)).
\]


::: pf-proof

Apply rank--nullity using steps <1>1 and <1>2.

:::

:::

::: pf-step

Therefore
\[
\dim(\operatorname{im}T)
\leq\dim(\ker S)+\dim(\operatorname{im}(S\circ T)).
\]


::: pf-proof

The inclusion $\ker S\cap\operatorname{im}T\subseteq\ker S$ bounds the first term on the right side of step <1>3.

:::

:::

::: pf-step

Rank--nullity for $S:V\to V$ gives
\[
\dim(\ker S)=\dim V-\dim(\operatorname{im}S).
\]


::: pf-proof

Rearrange $\dim V=\dim(\ker S)+\dim(\operatorname{im}S)$.

:::

:::

::: pf-step

Substitution into step <1>4 gives
\[
\dim(\operatorname{im}T)
\leq\dim V-\dim(\operatorname{im}S)
+\dim(\operatorname{im}(S\circ T)).
\]


::: pf-proof

Substitute the equality from step <1>5.

:::

:::

::: pf-step

Hence
\[
\boxed{
\dim(\operatorname{im}S)+\dim(\operatorname{im}T)
\leq\dim(\operatorname{im}(S\circ T))+\dim V.}
\]


::: pf-proof

Add $\dim(\operatorname{im}S)$ to both sides of step <1>6.

:::

:::

::: pf-qed

Step <1>7 is the required inequality.

:::

:::
