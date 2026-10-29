---
schema: qual/card@1
id: P-ALGF20G
kind: problem
title: Galois group and intermediate fields for splitting field of $x^4 - 4x^2 + 1$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 7 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; the polynomial and request for the Galois group and all proper intermediate fields agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that the splitting field is Q(sqrt(2),sqrt(3)), giving Galois group C2 x C2 and exactly the three quadratic intermediate fields.
---

::: {.problem}
Let $K$ be the splitting field over $\QQ$ of $f(x) = x^4 - 4x^2 + 1$.
Find $\mathrm{Gal}(K/\QQ)$, and find all fields $E$ such that $\QQ \subsetneq E \subsetneq K$.
:::

::: {.solution}
Choose the positive real root
\[
\alpha=\sqrt{2+\sqrt3}.
\]

::: pf

::: {.pf-step #s1}

The four roots of $f$ are
\[
\pm\alpha,
\qquad
\pm\alpha^{-1}.
\]

::: pf-proof

Writing $y=x^2$, the equation $f(x)=0$ becomes
\[
y^2-4y+1=0,
\]
whose two roots are
\[
y=2\pm\sqrt3.
\]
Since
\[
(2+\sqrt3)(2-\sqrt3)=1,
\]
we have
\[
\sqrt{2-\sqrt3}=\alpha^{-1}.
\]
Thus the four roots are exactly the displayed elements.

:::

:::

::: {.pf-step #s2}

The splitting field is
\[
K=\QQ(\alpha).
\]

::: pf-proof

The field $\QQ(\alpha)$ contains both $\alpha$ and its inverse $\alpha^{-1}$, hence all four roots from step [](#s1){.pf-ref}. Conversely, every splitting field contains $\alpha$. Therefore $\QQ(\alpha)$ is precisely the splitting field.

:::

:::

::: {.pf-step #s3}

One has
\[
K=\QQ(\sqrt2,\sqrt3).
\]

::: pf-proof

From
\[
\alpha^2+\alpha^{-2}=4
\]
we obtain
\[
(\alpha-\alpha^{-1})^2=2,
\qquad
(\alpha+\alpha^{-1})^2=6.
\]
With the chosen positive real $\alpha>1$, this gives
\[
\alpha-\alpha^{-1}=\sqrt2,
\qquad
\alpha+\alpha^{-1}=\sqrt6.
\]
Hence
\[
\sqrt2\in K,
\qquad
\sqrt3=\frac{\sqrt6}{\sqrt2}\in K,
\]
so
\[
\QQ(\sqrt2,\sqrt3)\subseteq K.
\]

Conversely,
\[
\alpha
=\frac{(\alpha+\alpha^{-1})+(\alpha-\alpha^{-1})}{2}
=\frac{\sqrt6+\sqrt2}{2}
\in\QQ(\sqrt2,\sqrt3).
\]
Together with step [](#s2){.pf-ref} this proves equality.

:::

:::

::: pf-step

The extension $K/\QQ$ has degree $4$ and
\[
\operatorname{Gal}(K/\QQ)\cong C_2\times C_2.
\]

::: pf-proof

The field $\QQ(\sqrt2)$ has degree $2$ over $\QQ$. Also
\[
\sqrt3\notin\QQ(\sqrt2).
\]
Indeed, if $\sqrt3=a+b\sqrt2$ with $a,b\in\QQ$, then squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]
Thus $ab=0$. If $b=0$, then $a^2=3$, impossible for $a\in\QQ$; if $a=0$, then $2b^2=3$, also impossible in $\QQ$. Hence
\[
[K:\QQ]=4.
\]

By step [](#s3){.pf-ref}, independently changing the signs of $\sqrt2$ and $\sqrt3$ defines four $\QQ$-automorphisms of $K$. They exhaust the Galois group because its order is $[K:\QQ]=4$. Each nonidentity sign change has order $2$, so
\[
\operatorname{Gal}(K/\QQ)\cong C_2\times C_2.
\]

:::

:::

::: pf-step

The three proper intermediate fields are
\[
\QQ(\sqrt2),
\qquad
\QQ(\sqrt3),
\qquad
\QQ(\sqrt6).
\]

::: pf-proof

The Klein four group has exactly three nontrivial proper subgroups, each of order $2$. By the Galois correspondence, the proper nontrivial intermediate fields of $K/\QQ$ are exactly their fixed fields.

The automorphism changing the sign of $\sqrt3$ and fixing $\sqrt2$ has fixed field $\QQ(\sqrt2)$. The automorphism changing the sign of $\sqrt2$ and fixing $\sqrt3$ has fixed field $\QQ(\sqrt3)$. Finally, the automorphism changing both signs fixes
\[
\sqrt6=\sqrt2\sqrt3,
\]
so its fixed field is $\QQ(\sqrt6)$. Each of these fields has degree $2$ over $\QQ$, as required for the fixed field of an order-$2$ subgroup. Thus there are no other proper intermediate fields.

:::

:::

:::

:::
