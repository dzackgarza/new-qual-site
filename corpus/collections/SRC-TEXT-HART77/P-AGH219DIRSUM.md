---
schema: qual/card@1
id: P-AGH219DIRSUM
kind: problem
title: The direct sum of two sheaves is both a product and a coproduct
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Direct Sums
  - Universal Properties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise II.1.9 in Hartshorne. The proof checks the sheaf axioms componentwise and verifies both the product and coproduct universal properties in the category of sheaves of abelian groups.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $\mcf$ and $\mcg$ be sheaves on $X$.
Show that the presheaf $U \mapsto \mcf(U) \oplus \mcg(U)$ is a sheaf.
It is called the **direct sum** of $\mcf$ and $\mcg$ and is denoted $\mcf \oplus \mcg$.

Show that it plays the role of both the direct sum and the direct product in the category of sheaves of abelian groups on $X$.
:::

::: {.solution}
Define a presheaf $\mcf\oplus\mcg$ by
$$
(\mcf\oplus\mcg)(U)=\mcf(U)\oplus\mcg(U),
$$
with restriction maps taken componentwise.

<1>1. The presheaf $\mcf\oplus\mcg$ is a sheaf.

::: {.proof}
Let $U=\bigcup_iU_i$ be an open cover.
Suppose
$$
(s_i,t_i)\in\mcf(U_i)\oplus\mcg(U_i)
$$
agree on every overlap $U_i\cap U_j$.
Then the $s_i$ agree pairwise in $\mcf$, and the $t_i$ agree pairwise in $\mcg$.
Since $\mcf$ and $\mcg$ are sheaves, there are unique sections
$$
s\in\mcf(U),\qquad t\in\mcg(U)
$$
restricting to all the $s_i$ and $t_i$.
Thus $(s,t)$ is the unique section of $\mcf\oplus\mcg$ restricting to every $(s_i,t_i)$.
This proves both existence and uniqueness in the sheaf gluing axiom.
:::

<1>2. With the projection morphisms
$$
p_\mcf:\mcf\oplus\mcg\to\mcf,
\qquad
p_\mcg:\mcf\oplus\mcg\to\mcg,
$$
the sheaf $\mcf\oplus\mcg$ is a categorical product of $\mcf$ and $\mcg$.

::: {.proof}
Let $\mch$ be a sheaf with morphisms
$$
f:\mch\to\mcf,
\qquad
g:\mch\to\mcg.
$$
For every open $U$, define
$$
h(U):\mch(U)\to\mcf(U)\oplus\mcg(U),
\qquad
u\mapsto(f(U)(u),g(U)(u)).
$$
These maps commute with restrictions because $f$ and $g$ do, so they define a sheaf morphism
$$
h:\mch\to\mcf\oplus\mcg.
$$
By construction,
$$
p_\mcf h=f,
\qquad
p_\mcg h=g.
$$
Any morphism with these two properties must agree with $h$ on every section, since both components are prescribed.
Hence $h$ is unique, proving the product universal property.
:::

<1>3. With the inclusion morphisms
$$
i_\mcf:\mcf\to\mcf\oplus\mcg,
\qquad
i_\mcg:\mcg\to\mcf\oplus\mcg,
$$
the sheaf $\mcf\oplus\mcg$ is a categorical coproduct of $\mcf$ and $\mcg$.

::: {.proof}
Let $\mch$ be a sheaf with morphisms
$$
f:\mcf\to\mch,
\qquad
g:\mcg\to\mch.
$$
For each open $U$, define
$$
h(U):\mcf(U)\oplus\mcg(U)\to\mch(U),
\qquad
(s,t)\mapsto f(U)(s)+g(U)(t).
$$
Again these maps commute with restrictions, so they define a sheaf morphism
$$
h:\mcf\oplus\mcg\to\mch.
$$
By construction,
$$
hi_\mcf=f,
\qquad
hi_\mcg=g.
$$
Every section $(s,t)$ decomposes as
$$
(s,t)=(s,0)+(0,t),
$$
so any morphism satisfying those two identities must equal $h$.
Thus $h$ is unique, proving the coproduct universal property.
:::

<1>4. Hence $\mcf\oplus\mcg$ is both product and coproduct in the category of sheaves of abelian groups.

::: {.proof}
Step <1>2 proves the product universal property, and step <1>3 proves the coproduct universal property for the same sheaf.
This common object is therefore the biproduct, or direct sum, of $\mcf$ and $\mcg$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves that the sectionwise direct sum is a sheaf, and steps <1>2--<1>4 prove both required universal properties.
:::
:::
