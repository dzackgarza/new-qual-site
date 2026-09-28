---
schema: qual/card@1
id: D-DEFREGSQ
kind: definition
title: Regular sequences
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Regular Sequences
  - Depth
relations:
- kind: uses
  target: D-DEFNOETH
review: draft
prompts:
- What is a regular sequence for a module $M$?
- Does the order of a regular sequence matter?
- What is the Koszul complex computing, for a regular sequence?
---

::: {.definition title="Regular sequence"}
Let $M$ be an $A$-module and $x_1,\ldots,x_r \in A$.
This is a \dfn{regular sequence for $M$} if

(i) for each $i$, $x_i$ is not a zero divisor on $M/(x_1,\ldots,x_{i-1})M$, and in particular $x_1$ is not a zero divisor on $M$;

(ii) the inclusion $(x_1,\ldots,x_r)M \subsetneq M$ is proper.
For $M=A$, this is called a regular sequence in $A$; see the [regular-sequence definition](https://stacks.math.columbia.edu/tag/00LF).
:::

::: {.proposition title="Permutation over a local ring"}
Let $(A,\mathfrak m)$ be a noetherian local ring and let $M$ be a finite $A$-module.
Every permutation of an $M$-regular sequence is again $M$-regular; see the [permutation lemma](https://stacks.math.columbia.edu/tag/0AUH).
The entries of such a sequence necessarily lie in $\mathfrak m$, since an entry that is a unit would make the final quotient zero.
:::

::: {.example title="Order can matter outside the local setting"}
In $A=k[x,y,z]$, the sequence $x,y(1-x),z(1-x)$ is regular: after quotienting by $x$, its remaining entries are $y,z$ in $k[y,z]$, and the final quotient is $k$.
The reordering $y(1-x),z(1-x),x$ is not regular.
Modulo $y(1-x)$, the second entry annihilates the nonzero class of $y$.
That class is nonzero because $y=y(1-x)h$ in the polynomial domain would imply $1=(1-x)h$, impossible for a polynomial $h$.
:::

::: {.definition title="Depth along an ideal"}
For a finite $A$-module $M$ and an ideal $I$, define $\depth_I M$ as the supremum of the lengths of $M$-regular sequences in $I$ when $IM\ne M$, and set $\depth_I M=\infty$ when $IM=M$.
This includes $\depth_I0=\infty$ and $\depth_A M=\infty$; see the [depth convention](https://stacks.math.columbia.edu/tag/00LE).
For a noetherian ring and $IM\ne M$, the supremum is a finite maximum.
For a local ring $(A,\mathfrak m)$, write $\depth M=\depth_{\mathfrak m}M$.
:::

::: {.proposition title="Dimension bound"}
For a nonzero finite module $M$ over a noetherian local ring,
$$
\depth M\le\dim\operatorname{Supp}(M).
$$
Equality defines a Cohen--Macaulay module; see the [depth dimension bound](https://stacks.math.columbia.edu/tag/00LE).
For $M=A$, this recovers the [[D-SCHCMGOR|Cohen--Macaulay ring]] condition.
:::

::: {.proposition title="Koszul coefficients"}
If $x_1,\ldots,x_r$ is $M$-regular, the Koszul complex $K_\bullet(x_1,\ldots,x_r;M)$ has zero homology in positive degrees and degree-zero homology $M/(x_1,\ldots,x_r)M$.
Its terms are finite direct sums of $M$.
In particular, an $A$-regular sequence gives a finite free resolution $K_\bullet(x_1,\ldots,x_r;A)$ of $A/(x_1,\ldots,x_r)$ [@Har10a, Proposition III.7.10A].
For the module assertion, tensor the one-element Koszul complexes successively with $M$.
At each step the mapping-cone homology sequence reduces positive homology to the kernel of the next element on the preceding quotient, which is zero by regularity; degree-zero homology is the next quotient.
:::

::: {.example title="Module regularity is not ring regularity"}
Let $A=k[x,y]/(xy)$ and $M=A/(x)\cong k[y]$.
Multiplication by $y$ on $M$ is injective and $M/yM\cong k\ne0$, so $y$ is $M$-regular.
But multiplication by $y$ on $A$ kills the nonzero class of $x$.
Thus $K_\bullet(y;A)$ has nonzero first homology and is not a free resolution of $A/(y)$, whereas $K_\bullet(y;M)$ resolves $M/yM$.
:::
