---
schema: qual/card@1
id: P-5PEC2
kind: problem
title: Order, centre, and $\PSL_2(\FF_3)$ as a permutation group
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let's look at $\SL_2(\FF_3)$.
How many elements are in that group?
What is its centre?
Identify $\PSL_2(\FF_3)$ as a permutation group.
:::


::: {.solution}
<1>1. The group $\operatorname{SL}_2(\FF_3)$ has order $24$.
::: {.proof}
First
\[
|\operatorname{GL}_2(\FF_3)|=(3^2-1)(3^2-3)=8\cdot6=48.
\]
The determinant map
\[
\det:\operatorname{GL}_2(\FF_3)\to\FF_3^\times
\]
is surjective, and $|\FF_3^\times|=2$. Its kernel is $\operatorname{SL}_2(\FF_3)$, so
\[
|\operatorname{SL}_2(\FF_3)|=48/2=24.
\]
:::

<1>2. The center of $\operatorname{SL}_2(\FF_3)$ is
\[
Z(\operatorname{SL}_2(\FF_3))=\{I,-I\}.
\]
::: {.proof}
Let
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]
be central. It commutes with the two elementary matrices
\[
U=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
L=\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]
in $\operatorname{SL}_2(\FF_3)$. From $AU=UA$ one gets $c=0$ and $a=d$; from $AL=LA$ one then gets $b=0$. Thus $A=aI$ is scalar. The determinant condition gives
\[
a^2=1
\]
in $\FF_3$, so $a=\pm1$. Hence the center is exactly $\{\pm I\}$.
:::

<1>3. Therefore
\[
|\operatorname{PSL}_2(\FF_3)|=12.
\]
::: {.proof}
By definition,
\[
\operatorname{PSL}_2(\FF_3)=\operatorname{SL}_2(\FF_3)/\{\pm I\}.
\]
Use <1>1 and <1>2.
:::

<1>4. The natural action on the projective line $\PP^1(\FF_3)$ gives an embedding
\[
\operatorname{PSL}_2(\FF_3)\hookrightarrow S_4.
\]
::: {.proof}
The projective line has
\[
|\PP^1(\FF_3)|=3+1=4
\]
points. The group $\operatorname{SL}_2(\FF_3)$ acts on one-dimensional subspaces of $\FF_3^2$. The kernel consists exactly of scalar matrices, hence of $\{\pm I\}$ by <1>2. Thus the induced action of $\operatorname{PSL}_2(\FF_3)$ is faithful.
:::

<1>5. Under this action,
\[
\operatorname{PSL}_2(\FF_3)\cong A_4.
\]
::: {.proof}
By <1>3--<1>4, the image is a subgroup of $S_4$ of order $12$, hence of index $2$. Any index-$2$ subgroup is the kernel of a surjective homomorphism $S_4\to C_2$; the unique such subgroup is $A_4$. Therefore the image is $A_4$.
:::
:::
