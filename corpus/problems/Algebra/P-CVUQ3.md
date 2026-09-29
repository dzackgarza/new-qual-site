---
schema: qual/card@1
id: P-CVUQ3
kind: problem
title: Galois group of $x^{15}+2$ over $\QQ$ is a semidirect product of a Sylow $2$-subgroup with $\ZZ/15\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Semidirect Products
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $L$ be the splitting field of $x^{15}+2$ over $\QQ$. Prove that
\[
\operatorname{Gal}(L/\QQ)
\cong
\ZZ/15\ZZ\semidirect (\ZZ/15\ZZ)^\times
\cong
C_{15}\semidirect(C_4\times C_2),
\]
and identify the right factor as a Sylow $2$-subgroup.
:::

::: {.solution}
Let $\alpha$ be a root of $x^{15}+2$, so $\alpha^{15}=-2$, and let $\zeta=\zeta_{15}$ be a primitive $15$th root of unity.

::: pf

::: pf-step

The splitting field is
\[
L=\QQ(\alpha,\zeta).
\]

::: pf-proof

The roots of $x^{15}+2$ are
\[
\alpha,\zeta\alpha,\dots,\zeta^{14}\alpha.
\]
Hence adjoining $\alpha$ and $\zeta$ gives every root, and any splitting field contains both $\alpha$ and the quotient $(\zeta\alpha)/\alpha=\zeta$.

:::

:::

::: {.pf-step #s2}

One has
\[
[\QQ(\alpha):\QQ]=15,
\qquad
[\QQ(\zeta):\QQ]=\varphi(15)=8,
\]
and therefore
\[
\QQ(\alpha)\cap\QQ(\zeta)=\QQ.
\]

::: pf-proof

The polynomial $x^{15}+2$ is Eisenstein at $2$, so it is irreducible over $\QQ$ and $[\QQ(\alpha):\QQ]=15$. The cyclotomic degree is $\varphi(15)=8$.

The degree of the intersection divides both extension degrees, hence divides $\gcd(15,8)=1$. Therefore the intersection is $\QQ$.

:::

:::

::: {.pf-step #s3}

Hence
\[
[L:\QQ]=120.
\]

::: pf-proof

Since the two finite extensions in step [](#s2){.pf-ref} have relatively prime degrees, they are linearly disjoint over $\QQ$. Thus
\[
[L:\QQ]
=[\QQ(\alpha):\QQ]\,[\QQ(\zeta):\QQ]
=15\cdot8=120.
\]

:::

:::

::: pf-step

The subgroup
\[
N=\operatorname{Gal}(L/\QQ(\zeta))
\]
is cyclic of order $15$.

::: pf-proof

By step [](#s3){.pf-ref},
\[
[L:\QQ(\zeta)]=15.
\]
Because $\zeta\in\QQ(\zeta)$, every map
\[
\sigma_a:\alpha\mapsto\zeta^a\alpha,
\qquad
\zeta\mapsto\zeta,
\qquad a\in\ZZ/15\ZZ,
\]
is an automorphism of $L$ fixing $\QQ(\zeta)$. These give $15$ distinct automorphisms, so
\[
N\cong\ZZ/15\ZZ.
\]
Since $N$ is the kernel of restriction
\[
\operatorname{Gal}(L/\QQ)\to\operatorname{Gal}(\QQ(\zeta)/\QQ),
\]
it is normal.

:::

:::

::: pf-step

The cyclotomic Galois group
\[
H\cong(\ZZ/15\ZZ)^\times
\]
embeds in $\operatorname{Gal}(L/\QQ)$ as the subgroup fixing $\alpha$.

::: pf-proof

Because $\QQ(\alpha)\cap\QQ(\zeta)=\QQ$, every automorphism of $\QQ(\zeta)/\QQ$ extends uniquely to the compositum while acting trivially on $\QQ(\alpha)$. Thus for each
\[
b\in(\ZZ/15\ZZ)^\times
\]
there is an automorphism
\[
\tau_b:\alpha\mapsto\alpha,
\qquad
\zeta\mapsto\zeta^b.
\]
These form a subgroup
\[
H\cong\operatorname{Gal}(\QQ(\zeta)/\QQ)
\cong(\ZZ/15\ZZ)^\times.
\]
Since
\[
(\ZZ/15\ZZ)^\times\cong C_4\times C_2,
\]
this subgroup has order $8$ and is therefore a Sylow $2$-subgroup of the group of order $120$.

:::

:::

::: {.pf-step #s6}

Conjugation gives the natural multiplicative action
\[
\tau_b\sigma_a\tau_b^{-1}=\sigma_{ba}.
\]

::: pf-proof

It suffices to evaluate both sides on $\alpha$ and $\zeta$. Since $\tau_b^{-1}$ fixes $\alpha$,
\[
\tau_b\sigma_a\tau_b^{-1}(\alpha)
=
\tau_b(\zeta^a\alpha)
=
\zeta^{ba}\alpha
=
\sigma_{ba}(\alpha),
\]
and both automorphisms fix $\zeta$ after the full conjugation.

:::

:::

::: pf-step

Therefore
\[
\operatorname{Gal}(L/\QQ)
\cong
C_{15}\semidirect(C_4\times C_2).
\]

::: pf-proof

The subgroups $N$ and $H$ have orders $15$ and $8$, have trivial intersection, and
\[
|NH|=15\cdot8=120=|\operatorname{Gal}(L/\QQ)|.
\]
Thus the full group is their internal semidirect product. By step [](#s6){.pf-ref} the action of the complement $H\cong(\ZZ/15\ZZ)^\times$ on $N\cong\ZZ/15\ZZ$ is multiplication modulo $15$.

:::

:::

:::

:::
