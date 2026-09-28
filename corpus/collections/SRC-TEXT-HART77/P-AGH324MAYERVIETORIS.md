---
schema: qual/card@1
id: P-AGH324MAYERVIETORIS
kind: problem
title: Mayer-Vietoris sequence for cohomology with supports
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Local Cohomology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the full exact sequence with the retained Hartshorne Chapter III section 2 transcription. The proof constructs the decomposition of a flasque section supported in a union by gluing on the complements and extending, then fixes the difference and sum maps before deriving the natural long exact sequence.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a topological space, let $\mcf$ be a sheaf of abelian groups on $X$, and let $Y_1,Y_2$ be two closed subsets of $X$.
Then there is a long exact sequence of cohomology with supports
$$
\begin{aligned}
\cdots & \to H_{Y_1 \intersect Y_2}^i(X, \mcf) \to H_{Y_1}^i(X, \mcf) \oplus H_{Y_2}^i(X, \mcf) \to H_{Y_1 \union Y_2}^i(X, \mcf) \\
& \to H_{Y_1 \intersect Y_2}^{i+1}(X, \mcf) \to \cdots
\end{aligned}
$$
:::

::: {.solution}
For a closed subset $Y$, write $\Gamma_Y(A)=\Gamma_Y(X,A)$ for the sections of an abelian sheaf $A$ with support in $Y$.
These are precisely the sections whose restriction to $X\setminus Y$ is zero, and their right derived functors are $H_Y^i(X,-)$, as in [[P-AGH323SUPPORTS]].
Put $U_i=X\setminus Y_i$ for $i=1,2$.

<1>1. For every abelian sheaf $A$, the sequence
$$
0\longrightarrow\Gamma_{Y_1\cap Y_2}(A)
\xrightarrow{a\mapsto(a,-a)}\Gamma_{Y_1}(A)\oplus\Gamma_{Y_2}(A)
\xrightarrow{(b,c)\mapsto b+c}\Gamma_{Y_1\cup Y_2}(A)
$$
is exact at the first two nonzero terms.

::: {.proof}
A section supported in the intersection is supported in each $Y_i$, so the first map is defined and injective.
A sum of sections supported respectively in $Y_1,Y_2$ vanishes outside their union, so the second map is defined.
The composite is zero.
Conversely, if $b+c=0$, then $b=-c$ is supported in both $Y_1$ and $Y_2$, and thus in their intersection.
The pair $(b,c)$ is the image of this section under the first map.
This proves exactness and specifies the signs.
:::

<1>2. If $A$ is flasque, the last map in step <1>1 is surjective.

::: {.proof}
Let $s\in\Gamma_{Y_1\cup Y_2}(A)$.
Its restriction to $U_1\cap U_2=X\setminus(Y_1\cup Y_2)$ is zero.
Consequently the section $0$ on $U_1$ and the section $s|_{U_2}$ agree on their overlap.
They glue to a section $t$ on
$$
U_1\cup U_2=X\setminus(Y_1\cap Y_2).
$$
Since $A$ is [[D-COHFLQ|flasque]], extend $t$ to a global section $b$ of $A$.
It is zero on $U_1$, so $b$ is supported in $Y_1$.
Moreover, $c=s-b$ is zero on $U_2$, so $c$ is supported in $Y_2$.
Thus $s=b+c$ is in the image of the sum map, proving surjectivity.
The choice of this decomposition need not be unique; the kernel describing that ambiguity is exactly the image of the first map in step <1>1.
:::

<1>3. Applying steps <1>1--<1>2 to an injective resolution yields the stated natural long exact sequence.

::: {.proof}
Choose an injective resolution $\mcf\to I^\bullet$ in the category of abelian sheaves on $X$.
Each $I^j$ is flasque [@Har10a, Lemma III.2.4].
Steps <1>1--<1>2 therefore give a short exact sequence of complexes
$$
0\to\Gamma_{Y_1\cap Y_2}(I^\bullet)
\to\Gamma_{Y_1}(I^\bullet)\oplus\Gamma_{Y_2}(I^\bullet)
\to\Gamma_{Y_1\cup Y_2}(I^\bullet)\to0.
$$
The difference and sum maps commute with the differentials because they are natural in the sheaf.
By the definition of supported cohomology, the cohomology of each complex is the corresponding $H_Y^i(X,\mcf)$.
The long exact sequence of cohomology of a short exact sequence of complexes consequently gives the sequence in the statement.
It begins in degree zero with the injective map of step <1>1 and continues through all nonnegative degrees.
Its first two maps in each degree are induced by the signed inclusions and sum map; the third is the connecting homomorphism.
Functoriality of the short exact sequence and comparison of injective resolutions make the resulting long exact sequence natural in $\mcf$ [@Har10a, Chapter III, §1].
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 establish exactness for flasque resolution terms, and step <1>3 derives the required Mayer--Vietoris sequence with its natural maps.
:::
:::
