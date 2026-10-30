---
schema: qual/card@1
id: P-K2CGJ
kind: problem
title: Conjugacy class size equals the index of the centralizer; restriction to a
  subgroup of index $2$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Class Equation
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Let $G$ be a finite group.
For any $x \in G$ $$Z_G(x) = \{g \in G : gxg^{-1} = x\}$$ is the centralizer of $x$ in $G$ and $$x^G = \{gxg^{-1} : g \in G\}$$ is the conjugacy class of $x$ in $G$.

a. Show that $\cardinality{x^G} = [G : Z_G(x)]$.

b. If $H \le G$ and $x \in H$, prove that $Z_H(x) = H \cap Z_G(x)$.

c. If $H$ is a subgroup of index 2 in $G$ and $x \in H$, prove that either $\cardinality{x^H} = \cardinality{x^G}$ or $\cardinality{x^H} = \frac{1}{2}\cardinality{x^G}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a),
$$
\boxed{\cardinality{ x^G}=[G:Z_G(x)]}.
$$

::: pf-proof

Let $G$ act on itself by conjugation:
$$
g\cdot y=gyg^{-1}.
$$
The orbit of $x$ is exactly $x^G$, and its stabilizer is exactly
$Z_G(x)$. The orbit-stabilizer theorem therefore gives
$$
\cardinality{ x^G}=[G:Z_G(x)].
$$
Equivalently, the map
$$
G/Z_G(x)\longrightarrow x^G,
\qquad
gZ_G(x)\longmapsto gxg^{-1},
$$
is a bijection.

:::

:::

::: {.pf-step #s2}

For part (b),
$$
\boxed{Z_H(x)=H\cap Z_G(x)}.
$$

::: pf-proof

For $h\in H$,
$$
h\in Z_H(x)
\iff hxh^{-1}=x
\iff h\in Z_G(x).
$$
Thus the elements of $Z_H(x)$ are precisely those elements of $H$ that
also lie in $Z_G(x)$.

:::

:::

::: {.pf-step #s3}

Under the hypotheses of part (c),
$$
2\cardinality{ x^H}
=\cardinality{ x^G}[Z_G(x):Z_H(x)].
$$

::: pf-proof

By step [](#s1){.pf-ref}, applied in $G$ and in $H$,
$$
\cardinality{ x^G}=[G:Z_G(x)],
\qquad
\cardinality{ x^H}=[H:Z_H(x)].
$$
Because $Z_H(x)\le H\le G$ and $[G:H]=2$,
$$
[G:Z_H(x)]
=2[H:Z_H(x)]
=2\cardinality{ x^H}.
$$
By step [](#s2){.pf-ref}, $Z_H(x)\le Z_G(x)\le G$, so also
$$
[G:Z_H(x)]
=[G:Z_G(x)][Z_G(x):Z_H(x)]
=\cardinality{ x^G}[Z_G(x):Z_H(x)].
$$
Equating the two expressions proves the claim.

:::

:::

::: {.pf-step #s4}

One has
$$
[Z_G(x):Z_H(x)]\in\{1,2\}.
$$

::: pf-proof

Since $[G:H]=2$, the subgroup $H$ is normal in $G$. By step [](#s2){.pf-ref} and the
second isomorphism theorem,
$$
[Z_G(x):Z_H(x)]
=[Z_G(x):Z_G(x)\cap H]
=[HZ_G(x):H].
$$
The subgroup $HZ_G(x)$ lies between $H$ and $G$. Hence
$$
[HZ_G(x):H]\mid[G:H]=2,
$$
so the index is either $1$ or $2$.

:::

:::

::: {.pf-step #s5}

Therefore either
$$
\boxed{\cardinality{ x^H}=\cardinality{ x^G}}
$$
or
$$
\boxed{\cardinality{ x^H}=\frac12\cardinality{ x^G}}.
$$

::: pf-proof

Insert the two possibilities from step [](#s4){.pf-ref} into the identity of step
step [](#s3){.pf-ref}. If the centralizer index is $2$, then
$2\cardinality{ x^H}=2\cardinality{ x^G}$. If it is $1$, then
$2\cardinality{ x^H}=\cardinality{ x^G}$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s5){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
