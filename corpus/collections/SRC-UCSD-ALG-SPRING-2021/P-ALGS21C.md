---
schema: qual/card@1
id: P-ALGS21C
kind: problem
title: 'Galois group of $x^6-5$ over $\QQ(\sqrt5)$'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
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
Let $f = x^6 - 5$.
Let $K$ be the splitting field of $f$ over $F = \mathbb{Q}(\sqrt{5})$.
Find the Galois group $\operatorname{Gal}(K/F)$ and show it is isomorphic to a familiar group.
:::

::: {.solution}

::: pf

::: pf-step

Let \(\alpha=5^{1/6}>0\) and let \(\zeta=\zeta_3\) be a primitive cube root of unity. Since \(\alpha^3=\sqrt5\in F\), the roots of \(x^6-5\) are
\[
\pm\alpha,\quad \pm\zeta\alpha,\quad \pm\zeta^2\alpha,
\]
so \(K=F(\alpha,\zeta)\).

::: pf-proof

The six roots are \(\alpha\) times the sixth roots of unity. Because \(-1\in F\), adjoining \(\zeta_3\) supplies all sixth roots of unity. Conversely, a splitting field contains \(\alpha\) and the quotient \((\zeta\alpha)/\alpha=\zeta\).

:::

:::

::: {.pf-step #s2}

The polynomial \(x^3-\sqrt5\) is irreducible over \(F\). Hence \([F(\alpha):F]=3\).

::: pf-proof

A reducible cubic has a root in the base field. If \(u\in F\) satisfied \(u^3=\sqrt5\), then taking norms from \(F=\mathbb Q(\sqrt5)\) to \(\mathbb Q\) would give
\[
N_{F/\mathbb Q}(u)^3=N_{F/\mathbb Q}(\sqrt5)=-5,
\]
impossible because \(-5\) is not a cube in \(\mathbb Q\). Thus the cubic has no root in \(F\) and is irreducible.

:::

:::

::: {.pf-step #s3}

The field \(F(\alpha)\) is real, while \(\zeta\notin\mathbb R\). Therefore
\[
[K:F(\alpha)]=2,
\qquad
[K:F]=6.
\]

::: pf-proof

Both \(F\) and \(\alpha\) are real, so \(F(\alpha)\subseteq\mathbb R\). The nonreal element \(\zeta\) satisfies \(x^2+x+1\), hence has degree \(2\) over \(F(\alpha)\). Now multiply degrees using step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Define \(F\)-automorphisms \(r,s\) of \(K\) by
\[
r(\alpha)=\zeta\alpha,\quad r(\zeta)=\zeta,
\]
\[
s(\alpha)=\alpha,\quad s(\zeta)=\zeta^{-1}.
\]
Then \(r^3=s^2=1\) and \(srs=r^{-1}\).

::: pf-proof

The map \(r\) preserves \(\alpha^3=\sqrt5\), and \(s\) is complex conjugation, which fixes the real field \(F(\alpha)\). Thus both are \(F\)-automorphisms. Their orders are \(3\) and \(2\), and
\[
srs(\alpha)=sr(\alpha)=s(\zeta\alpha)=\zeta^{-1}\alpha=r^{-1}(\alpha),
\]
while both sides agree on \(\zeta\).

:::

:::

::: pf-step

The six elements \(1,r,r^2,s,sr,sr^2\) are distinct, so they form all of \(\operatorname{Gal}(K/F)\).

::: pf-proof

They are distinct from their actions on \(\alpha\) and \(\zeta\). Since \([K:F]=6\) by step [](#s3){.pf-ref} and \(K/F\) is a splitting field in characteristic zero, its Galois group has exactly six elements.

:::

:::

::: pf-step

Therefore
\[
\operatorname{Gal}(K/F)\cong S_3\cong D_6.
\]

::: pf-proof

The relations \(r^3=s^2=1\) and \(srs=r^{-1}\) give the standard presentation of \(S_3\), equivalently the dihedral group of order \(6\).

:::

:::

:::

:::
