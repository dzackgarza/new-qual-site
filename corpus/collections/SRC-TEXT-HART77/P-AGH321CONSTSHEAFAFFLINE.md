---
schema: qual/card@1
id: P-AGH321CONSTSHEAFAFFLINE
kind: problem
title: Nonvanishing top cohomology of extensions by zero on affine space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Sheaf Cohomology
  - Affine Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts with the retained Hartshorne Chapter III section 2 transcription. The proof specifies Zariski extension by zero, computes the affine-line group, and builds an explicit flasque resolution on all proper hyperplane intersections. Its global complex computes the top group over the integers without assuming comparison with analytic topology.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Let $X=\AA_k^1$ be the affine line over an infinite field $k$.
Let $P, Q$ be distinct closed points of $X$, and let $U=X-\ts{P, Q}$.
Show that $H^1(X, \ZZ_U) \neq 0$.

(b) More generally, for $n\ge1$, let $Y \subseteq X=\AA_k^n$ be the union of $n+1$ hyperplanes in suitably general position, and let $U=X-Y$.
Show that $H^n(X, \ZZ_U) \neq 0$.
Thus the result of (2.7) is the best possible.
:::

::: {.solution}
All sheaves and cohomology are for the Zariski topology.
For an open inclusion $j:U\hookrightarrow X$, the notation $\ZZ_U$ on $X$ means the [[D-SHFSIX|extension by zero]] $j_!\underline{\ZZ}_U$ of the constant sheaf, not the constant sheaf on $X$ or the direct image $j_*\underline{\ZZ}_U$.
For a closed subset $D\subseteq X$, write $\underline{\ZZ}_D$ for its constant sheaf pushed forward to $X$; its stalk is $\ZZ$ at points of $D$ and zero elsewhere.

<1>1. A constant sheaf on an irreducible space is flasque, and its direct image under a closed inclusion remains flasque.

::: {.proof}
Every nonempty open subset of an irreducible space is irreducible and therefore connected.
A section of the constant sheaf $\underline{\ZZ}$ is a locally constant integer-valued function, so on such an open it is a single constant.
The section group is consequently $\ZZ$ on a nonempty open and zero on the empty open.
Restriction maps are identities or maps onto zero, and are surjective.
This is [[D-COHFLQ|flasqueness]].
For a closed inclusion $i:D\hookrightarrow X$, the sections of $i_*\underline{\ZZ}$ on an open $V$ are the sections on $V\cap D$.
Thus their restrictions are also surjective when $D$ is irreducible.
Finite direct sums of these sheaves are flasque as well, since their restrictions are finite direct sums of surjections.
:::

<1>2. In (a), $\boxed{H^1(X,\ZZ_U)\cong\ZZ}$.

::: {.proof}
The constant-sheaf restriction maps give an exact sequence
$$
0\longrightarrow\ZZ_U\longrightarrow\underline{\ZZ}_X
\longrightarrow\underline{\ZZ}_{\{P\}}\oplus\underline{\ZZ}_{\{Q\}}
\longrightarrow0.
$$
Indeed, outside $P,Q$ the first map is an isomorphism on stalks; at either omitted point the second map is an isomorphism from $\ZZ$ onto its one nonzero skyscraper stalk.
This proves exactness at every point.
The two terms after $\ZZ_U$ are flasque by step <1>1, since $X$ is irreducible and each closed point is an irreducible space.
They form a flasque resolution, which computes sheaf cohomology [@Har10a, Proposition III.2.5 and Remark III.2.5.1].
On global sections its differential is the diagonal map
$$
\ZZ\longrightarrow\ZZ\oplus\ZZ,\qquad a\longmapsto(a,a).
$$
Its cokernel is $\ZZ$ via $(b,c)\mapsto c-b$.
This proves (a), whether or not the two closed points are $k$-rational.
:::

<1>3. In (b), choose affine hyperplanes $H_0,\ldots,H_n$ so that each intersection of $s\le n$ of them is an affine space of dimension $n-s$, and their total intersection is empty.
Such a choice exists.

::: {.proof}
For example, in coordinates $x_1,\ldots,x_n$, take
$$
H_i=V(x_i)\quad(1\le i\le n),\qquad
H_0=V(x_1+\cdots+x_n-1).
$$
An intersection involving only coordinate hyperplanes sets the corresponding coordinates to zero and has the stated dimension.
If an intersection of at most $n$ hyperplanes involves $H_0$, at least one coordinate is not prescribed to be zero.
The equation of $H_0$ solves uniquely for that coordinate in terms of the remaining ones, again giving the stated affine space.
All $n+1$ equations would imply $0=1$, so their intersection is empty.
These are the intersection properties of suitably general affine hyperplanes, and the rest of the proof applies to any hyperplanes with these properties.
:::

<1>4. For $H_J=\bigcap_{j\in J}H_j$, there is a flasque resolution
$$
0\longrightarrow\ZZ_U\longrightarrow C^0\longrightarrow C^1
\longrightarrow\cdots\longrightarrow C^n\longrightarrow0,
\qquad
C^0=\underline{\ZZ}_X,\quad
C^p=\bigoplus_{\#J=p}\underline{\ZZ}_{H_J}\ (1\le p\le n).
$$

::: {.proof}
Order the hyperplanes by their indices.
The differential is alternating restriction: for $J=\{j_0<\cdots<j_p\}$, its component is
$$
(dc)_J=\sum_{a=0}^p(-1)^a c_{J\setminus\{j_a\}}|_{H_J}.
$$
In degree zero, the empty-index component is the constant sheaf on $X$.
Every pair of omitted indices occurs with opposite signs in the next differential, so $d^2=0$.

To verify exactness, fix $x\in X$ and let $T=\{i:x\in H_i\}$.
If $T$ is empty, then $x\in U$ and the stalk complex is the identity $\ZZ\to\ZZ$ followed by zeros.
If $T$ is nonempty, its cardinality is at most $n$ by step <1>3.
The stalk of $\ZZ_U$ is zero, and the remaining stalk complex has one copy of $\ZZ$ for every subset of $T$, including the empty subset, with the displayed alternating maps.
This is the augmented cochain complex of a simplex and is exact.
For an explicit contraction, choose $v\in T$ and extend cochains to alternating functions on ordered tuples, setting them to zero on tuples with a repeated index.
The operator $h$ which sends a cochain $c$ to $hc(j_1,\ldots,j_{p-1})=c(v,j_1,\ldots,j_{p-1})$ satisfies $dh+hd=\id$; expanding both alternating sums cancels all terms except $c$.
The same formula in the augmented degree evaluates a one-index cochain at $v$.
Thus every stalk complex is exact.

Each nonempty $H_J$ is an affine space and hence irreducible by step <1>3.
Step <1>1 makes every $C^p$ flasque, proving the resolution assertion.
:::

<1>5. In (b), $\boxed{H^n(X,\ZZ_U)\cong\ZZ}$.

::: {.proof}
Take global sections of the flasque resolution in step <1>4.
Each proper intersection contributes exactly one copy of $\ZZ$.
Consequently the resulting complex is
$$
\ZZ\longrightarrow\ZZ^{\binom{n+1}{1}}
\longrightarrow\cdots\longrightarrow\ZZ^{\binom{n+1}{n}},
$$
in degrees $0,\ldots,n$, with alternating subset maps.
Adjoin one further copy of $\ZZ$ in degree $n+1$, corresponding to the full index set, and define
$$
\varepsilon(c)=\sum_{i=0}^n(-1)^i c_{\{0,\ldots,n\}\setminus\{i\}}.
$$
The extended complex is the augmented simplex complex on $n+1$ vertices.
The contraction in step <1>4 proves that it is exact.
In particular, $\ker\varepsilon$ is the image of the preceding differential, and $\varepsilon$ is surjective; one component with coefficient $1$ maps to $1$ or $-1$.
The original complex has no outgoing differential in degree $n$, because the total hyperplane intersection is empty.
Its degree-$n$ cohomology is therefore
$$
\ZZ^{\binom{n+1}{n}}/\im d^{n-1}
\cong\ZZ^{\binom{n+1}{n}}/\ker\varepsilon
\cong\ZZ.
$$
The flasque-resolution computation identifies this with $H^n(X,\ZZ_U)$, proving (b).
Since $\dim\AA_k^n=n$, this also shows that the vanishing in degrees greater than $n$ in [@Har10a, Theorem III.2.7] cannot be extended to degree $n$ for all abelian sheaves.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves (a), and steps <1>3--<1>5 prove (b) and the sharpness assertion.
:::
:::
