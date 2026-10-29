---
schema: qual/card@1
id: P-DK3J4
kind: problem
title: Galois theory of $x^{2n}-2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Describe the Galois theory of $f(x) = x^{2n} - 2$ over $\QQ$: irreducibility, splitting field, and Galois group structure.
:::

::: {.solution}
Put $m=2n$ and $\alpha=2^{1/m}$, let $\zeta_m$ be a primitive $m$th root of unity, and let $E=\QQ(\alpha)$ and $F=\QQ(\zeta_m)$.

::: pf

::: pf-step
$x^m-2$ is irreducible over $\QQ$, and $[E:\QQ]=m$.

::: pf-proof
The polynomial is Eisenstein at $2$, and $\alpha$ is one of its roots.
:::

:::

::: {.pf-step #splitting}
The splitting field of $x^m-2$ is $\boxed{K=\QQ(\alpha,\zeta_m)}$, and $[K:\QQ]=\dfrac{m\varphi(m)}{[E\cap F:\QQ]}$.

::: pf-proof
The roots are $\alpha\zeta_m^j$ for $j\in\ZZ/m\ZZ$, and they generate $\QQ(\alpha,\zeta_m)$, since $\zeta_m$ is the quotient of two of them.
Since $F/\QQ$ is Galois, $[K:\QQ]=[E:\QQ][F:\QQ]/[E\cap F:\QQ]$, with $[E:\QQ]=m$ and $[F:\QQ]=\varphi(m)$.
:::

:::

::: {.pf-step #affine}
$\Gal(K/\QQ)$ embeds in the affine group $\ZZ/m\ZZ\rtimes(\ZZ/m\ZZ)^\times$ as a subgroup of index $[E\cap F:\QQ]$.

::: pf-proof
Every $\sigma\in\Gal(K/\QQ)$ is determined by $\sigma(\alpha)=\alpha\zeta_m^b$ and $\sigma(\zeta_m)=\zeta_m^a$, with $b\in\ZZ/m\ZZ$ and $a\in(\ZZ/m\ZZ)^\times$.
The pair $(a,b)$ acts on the root index $j$ by $j\mapsto aj+b$, and composition of automorphisms corresponds to composition of these affine maps.
The affine group has order $m\varphi(m)$, so by step [](#splitting){.pf-ref} the image has index $[E\cap F:\QQ]$.
:::

:::

::: pf-step
$\Gal(K/\QQ)$ is solvable, with cyclic normal subgroup $\Gal(K/F)$ and abelian quotient $\Gal(F/\QQ)\cong(\ZZ/m\ZZ)^\times$.

::: pf-proof
$F$ contains the $m$th roots of unity and $K=F(\alpha)$ with $\alpha^m=2$, so $K/F$ is a Kummer extension, and $\Gal(K/F)$ is cyclic of order dividing $m$.
Since $F/\QQ$ is Galois, $\Gal(K/F)$ is normal in $\Gal(K/\QQ)$ with quotient $\Gal(F/\QQ)\cong(\ZZ/m\ZZ)^\times$.
:::

:::

::: pf-step
For $m=2$, $K=\QQ(\sqrt2)$ with Galois group $C_2$; for $m=4$, $K=\QQ(\sqrt[4]2,i)$ with Galois group $D_4$ of order $8$.

::: pf-proof
For $m=2$, $\zeta_2=-1\in\QQ$, so $K=E$ has degree $2$.
For $m=4$, $F=\QQ(i)$ and $E\cap F=\QQ$, since $E$ is real; so $[K:\QQ]=8$ by step [](#splitting){.pf-ref}, and step [](#affine){.pf-ref} identifies the Galois group with the full affine group $\ZZ/4\ZZ\rtimes(\ZZ/4\ZZ)^\times\cong D_4$.
:::

:::

:::

:::
