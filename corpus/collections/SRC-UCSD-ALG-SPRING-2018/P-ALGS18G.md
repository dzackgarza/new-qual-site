---
schema: qual/card@1
id: P-ALGS18G
kind: problem
title: "Galois theory of splitting fields of degree p+1 polynomials with specific Galois group structure"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $f(x) \in \mathbb{Q}[x]$ is an irreducible polynomial of degree $p+1$ where $p$ is a prime.
Let $E$ be a splitting field of $f$ over $\mathbb{Q}$.
Suppose $[E:\mathbb{Q}] = p(p+1)$.

(a) Prove that for any zero $\alpha \in E$ of $f$, $E/\mathbb{Q}[\alpha]$ is a Galois extension and $\operatorname{Gal}(E/\mathbb{Q}[\alpha]) \cong \mathbb{Z}/p\mathbb{Z}$.

(b) Prove that there is $\beta \in E$ such that $\mathbb{Q}[\beta]/\mathbb{Q}$ is a Galois extension and $\operatorname{Gal}(\mathbb{Q}[\beta]/\mathbb{Q}) \cong \mathbb{Z}/p\mathbb{Z}$.

Hint: You can use whatever has been proved about groups of order $p(p+1)$.
:::

::: {.solution}

::: pf

::: pf-step
Let $G = \operatorname{Gal}(E/\QQ)$; then $|G| = [E:\QQ] = p(p+1)$.

::: pf-proof
$E/\QQ$ is a splitting field, hence Galois, so $|G| = [E:\QQ]$.
:::

:::

::: pf-step
$G$ acts faithfully and transitively on the $p+1$ roots of $f$.

::: pf-proof
$f$ is irreducible, so $G$ acts transitively on its roots; an automorphism fixing every root is the identity, so the action is faithful.
:::

:::

::: {.pf-step #p1-s3}
$G$ is a Frobenius group: it has a normal subgroup $N$ of order $p+1$ (the Frobenius kernel) and a complement $H$ of order $p$ (a point stabilizer).

::: pf-proof

::: pf-step
The stabilizer of a root has order $|G|/(p+1) = p$.

::: pf-proof
orbit–stabilizer theorem applied to the transitive action on $p+1$ roots.
:::

:::

::: pf-step
A point stabilizer $H$ (order $p$) acts freely on the other $p$ roots.

::: pf-proof
Let $1\neq h\in H$.
Since $|H|=p$, the permutation induced by $h$ has order $p$.
On a set of $p+1$ points, a nonidentity permutation of order $p$ has exactly one $p$-cycle and one fixed point.
Because $h\in H$, that fixed point is the chosen root.
Hence $h$ fixes no second root.
Thus $H$ acts freely on the other $p$ roots.
:::

:::

::: pf-step
Hence $G$ is a Frobenius group with complement $H$ (order $p$) and kernel $N$ (order $p+1$), and $N$ is normal.

::: pf-proof
Frobenius' theorem (or the standard structure of a transitive group of degree $p+1$ and order $p(p+1)$).
:::

:::

:::

:::

::: {.pf-step #p1-s4}
$H \cong \ZZ/p$.

::: pf-proof
a group of prime order $p$ is cyclic.
:::

:::

:::

**Part (a).**

::: pf

::: pf-step
For any root $\alpha$ of $f$, $[\QQ(\alpha):\QQ] = p+1$.

::: pf-proof
$f$ is irreducible of degree $p+1$.
:::

:::

::: {.pf-step #p2-s2}
$\operatorname{Gal}(E/\QQ(\alpha))$ is the stabilizer of $\alpha$, of order $p$.

::: pf-proof
the fixed field of the stabilizer of $\alpha$ is $\QQ(\alpha)$; its order is $|G|/(p+1) = p$ by step [](#p1-s3){.pf-ref}.
:::

:::

::: {.pf-step #p2-s3}
Hence $\operatorname{Gal}(E/\QQ(\alpha)) \cong \ZZ/p$.

::: pf-proof
step [](#p2-s2){.pf-ref} and step [](#p1-s4){.pf-ref}.
:::

:::

::: {.pf-step #p2-s4}
$E/\QQ(\alpha)$ is Galois.

::: pf-proof
The subgroup fixing $\QQ(\alpha)$ is $H$.
For a finite Galois extension $E/\QQ$, the extension $E/E^H$ is Galois with Galois group $H$ for every subgroup $H\le G$.
Since $E^H=\QQ(\alpha)$, the extension $E/\QQ(\alpha)$ is Galois.
:::

:::

::: pf-qed
(part (a)).

step [](#p2-s3){.pf-ref} and step [](#p2-s4){.pf-ref}.
:::

:::

**Part (b).**

::: pf

::: pf-step
Let $K = E^N$ be the fixed field of the normal subgroup $N$ (order $p+1$).

::: pf-proof
definition.
:::

:::

::: pf-step
$K/\QQ$ is Galois.

::: pf-proof
$N$ is normal in $G$, so its fixed field $K$ is Galois over $\QQ$ (fundamental theorem of Galois theory).
:::

:::

::: pf-step
$\operatorname{Gal}(K/\QQ) = G/N$, of order $p$.

::: pf-proof
fundamental theorem of Galois theory; $|G/N| = p(p+1)/(p+1) = p$.
:::

:::

::: {.pf-step #p3-s4}
Hence $\operatorname{Gal}(K/\QQ) \cong \ZZ/p$.

::: pf-proof
a group of order $p$ is cyclic.
:::

:::

::: {.pf-step #p3-s5}
Let $\beta$ be a primitive element of $K$ over $\QQ$; then $\QQ(\beta) = K$ and $\operatorname{Gal}(\QQ(\beta)/\QQ) \cong \ZZ/p$.

::: pf-proof
step [](#p3-s4){.pf-ref} and the primitive element theorem.
:::

:::

::: pf-qed
(part (b)).

step [](#p3-s5){.pf-ref}.
:::

:::
:::
