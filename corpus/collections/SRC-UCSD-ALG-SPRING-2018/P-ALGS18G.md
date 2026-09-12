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

::: problem
Suppose $f(x) \in \mathbb{Q}[x]$ is an irreducible polynomial of degree $p+1$ where $p$ is a prime.
Let $E$ be a splitting field of $f$ over $\mathbb{Q}$.
Suppose $[E:\mathbb{Q}] = p(p+1)$.

(a) Prove that for any zero $\alpha \in E$ of $f$, $E/\mathbb{Q}[\alpha]$ is a Galois extension and $\operatorname{Gal}(E/\mathbb{Q}[\alpha]) \cong \mathbb{Z}/p\mathbb{Z}$.

(b) Prove that there is $\beta \in E$ such that $\mathbb{Q}[\beta]/\mathbb{Q}$ is a Galois extension and $\operatorname{Gal}(\mathbb{Q}[\beta]/\mathbb{Q}) \cong \mathbb{Z}/p\mathbb{Z}$.

Hint: You can use whatever has been proved about groups of order $p(p+1)$.
:::

::: {.solution}
<1>1. Let $G = \operatorname{Gal}(E/\QQ)$; then $|G| = [E:\QQ] = p(p+1)$.
::: {.proof}
$E/\QQ$ is a splitting field, hence Galois, so $|G| = [E:\QQ]$.
:::

<1>2. $G$ acts faithfully and transitively on the $p+1$ roots of $f$.
::: {.proof}
$f$ is irreducible, so $G$ acts transitively on its roots; an automorphism fixing every root is the identity, so the action is faithful.
:::

<1>3. $G$ is a Frobenius group: it has a normal subgroup $N$ of order $p+1$ (the Frobenius kernel) and a complement $H$ of order $p$ (a point stabilizer).
<2>1. The stabilizer of a root has order $|G|/(p+1) = p$.
::: {.proof}
orbit–stabilizer theorem applied to the transitive action on $p+1$ roots.
:::
<2>2. A point stabilizer $H$ (order $p$) acts freely on the other $p$ roots.
::: {.proof}
Let $1\neq h\in H$.
Since $|H|=p$, the permutation induced by $h$ has order $p$.
On a set of $p+1$ points, a nonidentity permutation of order $p$ has exactly one $p$-cycle and one fixed point.
Because $h\in H$, that fixed point is the chosen root.
Hence $h$ fixes no second root.
Thus $H$ acts freely on the other $p$ roots.
:::
<2>3. Hence $G$ is a Frobenius group with complement $H$ (order $p$) and kernel $N$ (order $p+1$), and $N$ is normal.
::: {.proof}
Frobenius' theorem (or the standard structure of a transitive group of degree $p+1$ and order $p(p+1)$).
:::

<1>4. $H \cong \ZZ/p$.
::: {.proof}
a group of prime order $p$ is cyclic.
:::

**Part (a).**

<1>1. For any root $\alpha$ of $f$, $[\QQ(\alpha):\QQ] = p+1$.
::: {.proof}
$f$ is irreducible of degree $p+1$.
:::

<1>2. $\operatorname{Gal}(E/\QQ(\alpha))$ is the stabilizer of $\alpha$, of order $p$.
::: {.proof}
the fixed field of the stabilizer of $\alpha$ is $\QQ(\alpha)$; its order is $|G|/(p+1) = p$ by <1>3.
:::

<1>3. Hence $\operatorname{Gal}(E/\QQ(\alpha)) \cong \ZZ/p$.
::: {.proof}
<1>2 and <1>4.
:::

<1>4. $E/\QQ(\alpha)$ is Galois.
::: {.proof}
The subgroup fixing $\QQ(\alpha)$ is $H$.
For a finite Galois extension $E/\QQ$, the extension $E/E^H$ is Galois with Galois group $H$ for every subgroup $H\le G$.
Since $E^H=\QQ(\alpha)$, the extension $E/\QQ(\alpha)$ is Galois.
:::

<1>5. Q.E.D. (part (a)).
::: {.proof}
<1>3 and <1>4.
:::

**Part (b).**

<1>1. Let $K = E^N$ be the fixed field of the normal subgroup $N$ (order $p+1$).
::: {.proof}
definition.
:::

<1>2. $K/\QQ$ is Galois.
::: {.proof}
$N$ is normal in $G$, so its fixed field $K$ is Galois over $\QQ$ (fundamental theorem of Galois theory).
:::

<1>3. $\operatorname{Gal}(K/\QQ) = G/N$, of order $p$.
::: {.proof}
fundamental theorem of Galois theory; $|G/N| = p(p+1)/(p+1) = p$.
:::

<1>4. Hence $\operatorname{Gal}(K/\QQ) \cong \ZZ/p$.
::: {.proof}
a group of order $p$ is cyclic.
:::

<1>5. Let $\beta$ be a primitive element of $K$ over $\QQ$; then $\QQ(\beta) = K$ and $\operatorname{Gal}(\QQ(\beta)/\QQ) \cong \ZZ/p$.
::: {.proof}
<1>4 and the primitive element theorem.
:::

<1>6. Q.E.D. (part (b)).
::: {.proof}
<1>5.
:::
:::
