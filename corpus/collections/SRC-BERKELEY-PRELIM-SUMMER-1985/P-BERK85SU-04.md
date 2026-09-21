---
schema: qual/card@1
id: P-BERK85SU-04
kind: problem
title: A subgroup of order $24$ in a group of order $120$ from one matching left and right coset
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    A matching nontrivial left and right coset gives g outside H with gH=Hg,
    so g lies in the normalizer N_G(H). Since [G:H]=5 is prime and
    H<N_G(H)<=G, multiplicativity of indices forces N_G(H)=G.
---

::: {.problem}
Let $G$ be a group of order $120$ and $H\le G$ a subgroup of order $24$. Assume that at least one left coset of $H$, other than $H$ itself, is equal to some right coset of $H$.
Prove that $H$ is normal in $G$.
:::

::: {.solution}
Let $gH$ be a left coset with $g\notin H$ that is equal to a right
coset $Hx$.

<1>1. One has
$$
gH=Hg.
$$

::: {.proof}
Since
$$
g\in gH=Hx,
$$
there is some $h\in H$ such that $g=hx$. Hence
$$
x=h^{-1}g,
$$
and therefore
$$
Hx=Hh^{-1}g=Hg.
$$
Thus the assumed equality $gH=Hx$ becomes $gH=Hg$.
:::

<1>2. The element $g$ lies in the normalizer $N_G(H)$, and
$g\notin H$.

::: {.proof}
By step <1>1,
$$
gH=Hg.
$$
Multiplying on the right by $g^{-1}$ gives
$$
gHg^{-1}=H,
$$
so $g\in N_G(H)$. The chosen left coset was not $H$ itself, so
$g\notin H$.
:::

<1>3. The normalizer satisfies
$$
H<N_G(H)\le G.
$$

::: {.proof}
Every subgroup normalizes itself, so $H\le N_G(H)$. Step <1>2 gives
an element of $N_G(H)$ outside $H$, making the first inclusion
strict. The second inclusion is part of the definition of the
normalizer.
:::

<1>4. One has
$$
N_G(H)=G.
$$

::: {.proof}
The index of $H$ in $G$ is
$$
[G:H]
=
\frac{120}{24}
=
5.
$$
By multiplicativity of indices along the subgroup chain in step
<1>3,
$$
5
=
[G:N_G(H)]\,[N_G(H):H].
$$
Since $H<N_G(H)$, the factor $[N_G(H):H]$ is greater than $1$.
Because $5$ is prime, it must equal $5$, and therefore
$[G:N_G(H)]=1$. Hence $N_G(H)=G$.
:::

<1>5. Consequently,
$$
\boxed{H\trianglelefteq G}.
$$

::: {.proof}
Step <1>4 says that every element of $G$ normalizes $H$, which is
exactly the definition that $H$ is normal in $G$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
