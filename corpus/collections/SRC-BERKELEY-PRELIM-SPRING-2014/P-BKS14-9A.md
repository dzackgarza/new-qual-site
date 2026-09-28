---
schema: qual/card@1
id: P-BKS14-9A
kind: problem
title: A finite abelian group is the additive group of a subring of its endomorphism ring
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the cyclic decomposition, componentwise scalar endomorphism subring, and its additive-group identification with A.
---

::: {.problem}
Let $A$ be a finite abelian group, written additively, and let $R=\operatorname{End}(A)$. Show that there is a subring $S\subseteq R$ such that $A$ and $S$ are isomorphic as abelian groups.
:::

::: {.solution}
<1>1. There are positive integers
$$
m_1,\ldots,m_r
$$
such that
$$
A
\cong
C_{m_1}\oplus\cdots\oplus C_{m_r},
$$
where
$$
C_m\coloneqq\ZZ/m\ZZ.
$$

::: {.proof}
This is the structure theorem for finite abelian groups.
:::

<1>2. For every positive integer $m$,
$$
\operatorname{End}(C_m)
\cong
\ZZ/m\ZZ
$$
as rings.

::: {.proof}
An endomorphism of the cyclic group $C_m$ is determined by the image of
$1$. For each residue class
$$
r\in\ZZ/m\ZZ,
$$
define
$$
\mu_r(x)=rx.
$$
Every endomorphism is of this form.

Moreover,
$$
\mu_r+\mu_s=\mu_{r+s}
$$
and
$$
\mu_r\circ\mu_s=\mu_{rs}.
$$
Thus
$$
r\longmapsto\mu_r
$$
is a ring isomorphism.
:::

<1>3. After identifying
$$
A=C_{m_1}\oplus\cdots\oplus C_{m_r},
$$
let $S$ be the set of endomorphisms
$$
\phi_{(a_1,\ldots,a_r)}
$$
defined by
$$
\phi_{(a_1,\ldots,a_r)}(x_1,\ldots,x_r)
=
(a_1x_1,\ldots,a_rx_r),
$$
where
$$
a_i\in\ZZ/m_i\ZZ.
$$
Then
$$
S\subseteq\operatorname{End}(A)
$$
is a subring.

::: {.proof}
Each displayed map is an endomorphism of the direct sum. If
$$
a=(a_1,\ldots,a_r)
$$
and
$$
b=(b_1,\ldots,b_r),
$$
then
$$
\phi_a+\phi_b=\phi_{a+b}
$$
and
$$
\phi_a\circ\phi_b=\phi_{ab},
$$
where addition and multiplication on the right are componentwise.
Also the zero endomorphism belongs to $S$, and additive inverses remain
in $S$. Hence $S$ is a subring.
:::

<1>4. The map
$$
\Phi:
\prod_{i=1}^r\ZZ/m_i\ZZ
\longrightarrow
S,
\qquad
(a_1,\ldots,a_r)
\longmapsto
\phi_{(a_1,\ldots,a_r)}
$$
is an isomorphism of rings, and in particular an isomorphism of additive
abelian groups.

::: {.proof}
Step <1>3 shows that $\Phi$ respects addition and multiplication. It is
surjective by the definition of $S$.

If
$$
\phi_{(a_1,\ldots,a_r)}=0,
$$
then evaluating on the element supported by $1$ in the $i$th coordinate
shows
$$
a_i=0
$$
in $\ZZ/m_i\ZZ$ for every $i$. Thus $\Phi$ is injective.
:::

<1>5. As additive abelian groups,
$$
\boxed{S\cong A}.
$$

::: {.proof}
By steps <1>1 and <1>4,
$$
S
\cong
\prod_{i=1}^r\ZZ/m_i\ZZ
\cong
C_{m_1}\oplus\cdots\oplus C_{m_r}
\cong
A.
$$
For a finite family, direct product and direct sum are the same underlying
abelian group.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 constructs the required subring, and step <1>5 proves the
required additive-group isomorphism.
:::
:::
