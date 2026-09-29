---
schema: qual/card@1
id: E-HAT-3.2-16
kind: problem
title: Torsion in products of CW complexes
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that if $X$ and $Y$ are finite CW complexes such that $H^*(X; \mathbb{Z})$ and $H^*(Y; \mathbb{Z})$ contain no elements of order a power of a given prime $p$, then the same is true for $X \times Y$.
[Apply Theorem 3.15 with coefficients in various fields.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a finite CW complex $Z$, $H^*(Z;\ZZ)$ has no $p$-torsion iff $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ)$ for all $n$.

::: pf-proof

::: {.pf-step #s1-1}

By the universal coefficient theorem, $H^n(Z;\FF_p) \cong H^n(Z;\ZZ) \otimes \FF_p \oplus \operatorname{Tor}(H^{n+1}(Z;\ZZ), \FF_p)$.

::: pf-proof

UCT for cohomology.

:::

:::

::: {.pf-step #s1-2}

$\operatorname{Tor}(H^{n+1}(Z;\ZZ), \FF_p)$ is the $p$-torsion of $H^{n+1}(Z;\ZZ)$.

::: pf-proof

$\operatorname{Tor}(A, \FF_p) \cong \{a \in A : pa = 0\}$.

:::

:::

::: {.pf-step #s1-3}

$\dim_{\FF_p}(H^n(Z;\ZZ) \otimes \FF_p) = \operatorname{rank} H^n(Z;\ZZ) = \dim_{\QQ} H^n(Z;\QQ)$.

::: pf-proof

tensoring a finitely generated abelian group with $\FF_p$ kills the torsion and keeps the free part; the rank equals the rational Betti number.

:::

:::

::: {.pf-step #s1-4}

Hence $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ) + \dim_{\FF_p}(p\text{-torsion of } H^{n+1}(Z;\ZZ))$.

::: pf-proof

Steps [](#s1-1){.pf-ref}, [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

Therefore the equality $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ)$ for all $n$ holds iff $H^*(Z;\ZZ)$ has no $p$-torsion.

::: pf-proof

Step [](#s1-4){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s2}

By hypothesis, $\dim_{\FF_p} H^i(X;\FF_p) = \dim_{\QQ} H^i(X;\QQ)$ and $\dim_{\FF_p} H^j(Y;\FF_p) = \dim_{\QQ} H^j(Y;\QQ)$ for all $i, j$.

::: pf-proof

Step [](#s1){.pf-ref} applied to $X$ and $Y$.

:::

:::

::: {.pf-step #s3}

$\dim_{\FF_p} H^n(X \times Y;\FF_p) = \sum_{i+j=n} \dim_{\FF_p} H^i(X;\FF_p) \cdot \dim_{\FF_p} H^j(Y;\FF_p)$.

::: pf-proof

Künneth theorem (Theorem 3.15) with field coefficients $\FF_p$; the Tor term vanishes over a field.

:::

:::

::: {.pf-step #s4}

$\dim_{\QQ} H^n(X \times Y;\QQ) = \sum_{i+j=n} \dim_{\QQ} H^i(X;\QQ) \cdot \dim_{\QQ} H^j(Y;\QQ)$.

::: pf-proof

Künneth theorem with field coefficients $\QQ$.

:::

:::

::: {.pf-step #s5}

Hence $\dim_{\FF_p} H^n(X \times Y;\FF_p) = \dim_{\QQ} H^n(X \times Y;\QQ)$ for all $n$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} have equal summands term-by-term by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Therefore $H^*(X \times Y;\ZZ)$ has no $p$-torsion.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s1){.pf-ref} applied to $Z = X \times Y$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
