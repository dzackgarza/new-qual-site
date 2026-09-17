---
schema: qual/card@1
id: P-AGH2712SEPSTRICT
kind: problem
title: Strict transforms after blowing up an intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Strict Transforms
  - Closed Subschemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement with the retained Hartshorne II.7.12 transcription and the scheme-theoretic strict-transform definition in Stacks Project Tag 080C. The affine-chart proof retains arbitrary closed subschemes and removes exceptional torsion, rather than identifying strict transforms with total inverse images.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and let $Y, Z$ be two closed subschemes, neither one containing the other.
Let $\tilde X$ be obtained by blowing up $Y \intersect Z$, defined by the ideal sheaf $\mci_Y + \mci_Z$.
Show that the strict transforms $\tilde Y$ and $\tilde Z$ of $Y$ and $Z$ in $\tilde X$ do not meet.
:::

::: {.solution}
Put $W=Y\cap Z$ and let $b:\tilde X\to X$ be its [[D-SCHBLOWUP|blowup]], with exceptional divisor $E=b^{-1}(W)$.
The strict transform of a closed subscheme is the scheme-theoretic closure of its inverse image outside $W$; equivalently, remove from its total inverse image the sections supported on $E$.

<1>1. Locally over $X$, the blowup is covered by charts indexed by generators of the ideal of $Y$ and generators of the ideal of $Z$.

::: {.proof}
On an affine open $\Spec A\subseteq X$, let $I=(a_1,\ldots,a_r)$ and $J=(b_1,\ldots,b_s)$ define $Y$ and $Z$ there.
Then $K=I+J$ defines $W$.
In the Rees algebra $R=\bigoplus_{q\ge0}K^q$, the degree-one elements corresponding to the $a_i$ and $b_j$ generate the algebra over $A$.
Their distinguished opens therefore cover $\operatorname{Proj}R$.

For any one of these generators $c\in K$, denote its degree-one copy by $c^{(1)}$ and put
$$
C_c=(R[1/c^{(1)}])_0.
$$
The corresponding chart is $\Spec C_c$.
The identity $h=c(h/c)$ for $h\in K$ shows that $KC_c=cC_c$, so the exceptional divisor on this chart is cut out by $c$ and its complement is $D(c)$.
These statements use homogeneous localization and remain valid when $A$ has zero divisors; a chart may be empty.
:::

<1>2. On a chart indexed by $a_i\in I$, the strict transform $\tilde Y$ is empty; on a chart indexed by $b_j\in J$, the strict transform $\tilde Z$ is empty.

::: {.proof}
On $\Spec C_c$, the total inverse image of $Y$ has coordinate ring $C_c/IC_c$.
Its part outside the exceptional divisor has coordinate ring $(C_c/IC_c)[1/c]$.
The scheme-theoretic closure in this affine chart is therefore defined by the kernel of
$$
C_c\longrightarrow(C_c/IC_c)[1/c].
$$
This kernel consists of the elements whose image modulo $IC_c$ is killed by a power of $c$, which is precisely the removal of exceptional torsion in the strict-transform definition.

When $c=a_i\in I$, its image in $C_c/IC_c$ is zero.
Inverting it gives the zero ring, so the kernel is all of $C_c$ and the strict transform is empty on the chart.
Interchanging $I$ and $J$ proves the assertion for the $b_j$ charts and $\tilde Z$.
:::

<1>3. Q.E.D.

::: {.proof}
The charts in step <1>1 cover the blowup over every affine open of $X$, hence cover $\tilde X$.
By step <1>2, at least one of $\tilde Y$ and $\tilde Z$ is empty on each chart.
Their scheme-theoretic intersection is consequently empty, and in particular their underlying sets do not meet.
:::
:::
