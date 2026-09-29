---
schema: qual/card@1
id: E-SMI-8000E-SY6
kind: problem
title: Symmetric groups on five or more letters are not solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Symmetric Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Checked the PDF text directly. The packet says S(5)≅Icos here but later explicitly identifies Icos with A(5), so the source has a one-letter group-name error."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Corrected the intended hypothesis to A5≅Icos, proved a nonabelian simple group is not solvable, proved subgroups of solvable groups are solvable, and embedded A5 in every S_n for n≥5."
---

::: {.exercise}
Prove that $S(n)$ is not solvable if $n > 4$, assuming $A(5) \cong Icos$ (the icosahedral rotation group) and the simplicity of $Icos$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A nonabelian simple group is not solvable.

::: pf-proof

Let $H$ be nonabelian and simple. Suppose, for contradiction, that $H$ has an
abelian normal tower
$$
H=H_1\trianglerighteq H_2\trianglerighteq\cdots\trianglerighteq H_m=1.
$$
Since $H\ne1$, there is a first index $j$ with $H_{j+1}\ne H_j$. Then
$H_j=H$, and $H_{j+1}$ is a proper normal subgroup of $H$, so
$H_{j+1}=1$ by simplicity. Thus one of the abelian quotients of the tower is
$$
H_j/H_{j+1}=H/1\cong H,
$$
which would make $H$ abelian, a contradiction. Hence every nonabelian simple
group is nonsolvable.

In particular, the assumed simple group
$$
A_5\cong Icos
$$
is not solvable.

:::

:::

::: {.pf-step #s2}

Every subgroup of a solvable group is solvable.

::: pf-proof

Let
$$
G=G_1\trianglerighteq G_2\trianglerighteq\cdots\trianglerighteq G_m=1
$$
be an abelian normal tower for a solvable group $G$, and let $H\le G$.
Intersect the tower with $H$:
$$
H=H\cap G_1\trianglerighteq H\cap G_2\trianglerighteq\cdots\trianglerighteq
H\cap G_m=1.
$$
Because $G_{i+1}\trianglelefteq G_i$, one has
$$
H\cap G_{i+1}\trianglelefteq H\cap G_i.
$$
Moreover, the map
$$
H\cap G_i\longrightarrow G_i/G_{i+1}
$$
has kernel $H\cap G_{i+1}$. Therefore
$$
(H\cap G_i)/(H\cap G_{i+1})
$$
is isomorphic to a subgroup of the abelian group $G_i/G_{i+1}$, and is hence
abelian. Thus the intersected tower proves that $H$ is solvable.

:::

:::

::: pf-step

Embed $A_5$ in every $S_n$ for $n\ge5$ and conclude.

::: pf-proof

For $n\ge5$, let $A_5$ act on the first five letters and fix the remaining
$n-5$ letters. This gives an injective homomorphism
$$
A_5\hookrightarrow S_n.
$$
If $S_n$ were solvable, step [](#s2){.pf-ref} would imply that its subgroup $A_5$ is
solvable. This contradicts step [](#s1){.pf-ref}. Therefore
$$
\boxed{S_n\text{ is not solvable for every }n>4.}
$$

:::

:::

:::

:::

::: {.remark}
The source prints the hypothesis as $S(5)\cong Icos$ and later identifies
"Icos (or $A(5)$)". The rotation group of the icosahedron has order $60$ and
is isomorphic to $A_5$, not to $S_5$, which has order $120$; the statement
uses $A(5)\cong Icos$.
:::
