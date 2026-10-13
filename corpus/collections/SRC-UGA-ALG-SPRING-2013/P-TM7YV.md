---
schema: qual/card@1
id: P-TM7YV
kind: problem
title: $\gal(E/B)$ and $\gal(E/C)$ for splitting fields of $f=gh$, $\gal(E/\QQ)\cong\gal(E/B)\times\gal(E/C)$
  when $B\cap C=\QQ$, and $\gal(\QQ[\sqrt{2}+\sqrt{3}]/\QQ)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---
::: {.problem}
Let $f(x) = g(x) h(x) \in \mathbb{Q}[x]$ and let $E, B, C / \mathbb{Q}$ be the splitting fields over $\mathbb{Q}$ of $f, g, h$ respectively (viewed inside a fixed algebraic closure $\overline{\mathbb{Q}}$).

(a) Prove that $\operatorname{Gal}(E/B)$ and $\operatorname{Gal}(E/C)$ are normal subgroups of $\operatorname{Gal}(E/\mathbb{Q})$.
(b) Prove that $\operatorname{Gal}(E/B) \cap \operatorname{Gal}(E/C) = \{1\}$.
(c) If $B \cap C = \mathbb{Q}$, show that $\operatorname{Gal}(E/B) \operatorname{Gal}(E/C) = \operatorname{Gal}(E/\mathbb{Q})$.
(d) Under the hypothesis of (c), show that $\operatorname{Gal}(E/\mathbb{Q}) \cong \operatorname{Gal}(E/B) \times \operatorname{Gal}(E/C) \cong \operatorname{Gal}(C/\mathbb{Q}) \times \operatorname{Gal}(B/\mathbb{Q})$.
(e) Use (d) to describe $\operatorname{Gal}(\mathbb{Q}[\alpha]/\mathbb{Q})$ where $\alpha = \sqrt{2} + \sqrt{3}$.
:::

::: {.solution}
Write $G=\operatorname{Gal}(E/\mathbb Q)$, $H=\operatorname{Gal}(E/B)$, and $J=\operatorname{Gal}(E/C)$. The splitting fields are finite Galois extensions and $E=BC$.

::: pf

::: {.pf-step #s1}

The subgroups $H$ and $J$ are normal in $G$.

::: pf-proof

Both $B/\mathbb Q$ and $C/\mathbb Q$ are normal since they are splitting fields. The fundamental theorem of Galois theory identifies normal intermediate extensions with normal subgroups, so $H,J\trianglelefteq G$.

:::

:::

::: {.pf-step #s2}

The intersection $H\cap J$ is trivial.

::: pf-proof

An automorphism in $H\cap J$ fixes both $B$ and $C$ pointwise. Therefore it fixes the compositum $BC=E$ and is the identity.

:::

:::

::: {.pf-step #s3}

If $B\cap C=\mathbb Q$, then $HJ=G$.

::: pf-proof

By step [](#s1){.pf-ref}, $HJ$ is a subgroup of $G$. Its fixed field is
\[
E^{HJ}=E^H\cap E^J=B\cap C=\mathbb Q.
\]
The Galois correspondence then implies $HJ=G$.

:::

:::

::: {.pf-step #s4}

Under this hypothesis,
\[
\boxed{G\cong H\times J\cong
\operatorname{Gal}(C/\mathbb Q)\times\operatorname{Gal}(B/\mathbb Q)}.
\]

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $H,J$ are normal, intersect trivially and generate $G$. They centralize each other because every commutator of an element of $H$ with an element of $J$ belongs to $H\cap J$. Multiplication therefore gives the first isomorphism. Restriction $H\to\operatorname{Gal}(C/\mathbb Q)$ is injective by step [](#s2){.pf-ref}; its surjectivity follows from extension of automorphisms of the normal extension $C/\mathbb Q$ to $E$ followed by the adjustment using the restriction to $B$, or from the degree formula $[BC:B]=[C:B\cap C]=[C:\mathbb Q]$ for finite Galois extensions. The same argument applies to $J$ and $B$.

:::

:::

::: {.pf-step #s5}

For $\alpha=\sqrt2+\sqrt3$, the extension $\mathbb Q(\alpha)/\mathbb Q$ is Galois with
\[
\boxed{\operatorname{Gal}(\mathbb Q(\alpha)/\mathbb Q)\cong C_2\times C_2}.
\]

::: pf-proof

Take $B=\mathbb Q(\sqrt2)$ and $C=\mathbb Q(\sqrt3)$. The quadratic fields are distinct, hence their intersection is $\mathbb Q$. Since
\[
\alpha^{-1}=\sqrt3-\sqrt2,\qquad
\sqrt3=\frac{\alpha+\alpha^{-1}}2,\quad
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\]
one has $\mathbb Q(\alpha)=BC$. Step [](#s4){.pf-ref} identifies its Galois group with the direct product of the two order-two Galois groups. Its four automorphisms are the independent sign changes of $\sqrt2$ and $\sqrt3$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} establish parts (a)--(e), respectively.

:::

:::

:::
