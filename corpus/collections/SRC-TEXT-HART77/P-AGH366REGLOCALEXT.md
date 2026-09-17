---
schema: qual/card@1
id: P-AGH366REGLOCALEXT
kind: problem
title: Projective dimension over a regular local ring detected by Ext into the ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Groups
  - Regular Local Rings
  - Projective Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both projective-dimension assertions and the descending-induction hint with the retained Hartshorne III.6.6 transcription. The proof uses the finite global-dimension bound of Proposition III.6.11A, tests all finite coefficient modules by descending induction, and then splits a finite free presentation.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a regular local ring, and let $M$ be a finitely generated $A$-module.
In this case, strengthen the result (6.10A) as follows.

(a) $M$ is projective if and only if $\Ext^i(M, A)=0$ for all $i>0$.

(b) Use (a) to show that for every $n\ge0$, $\operatorname{pd} M \leq n$ if and only if $\Ext^i(M, A)=0$ for all $i>n$.
:::

::: {.hint}
For (a), use (6.11A) and descending induction on $i$ to show that $\Ext^i(M, N)=0$ for all $i>0$ and all finitely generated $A$-modules $N$.
Then show $M$ is a direct summand of a free $A$-module.
:::

::: {.solution}
All Ext groups and projective dimensions are over $A$.
The regular local ring $A$ is noetherian and has finite dimension $d$.
The regular-local global-dimension theorem gives $\operatorname{pd}_A L\le d$ for every $A$-module $L$ [@Har10a, Proposition III.6.11A].

<1>1. If $\Ext_A^i(M,A)=0$ for every $i>0$, then $\Ext_A^i(M,N)=0$ for every finite $A$-module $N$ and every $i>0$.

::: {.proof}
The bound $\operatorname{pd}_A M\le d$ gives the assertion for all $i>d$, even for arbitrary $N$.
Proceed downwards from $i=d$ to $i=1$.
Suppose the assertion has been proved in degree $i+1$ for all finite modules, and let $N$ be finite.
Choose an exact sequence
$$
0\longrightarrow K\longrightarrow A^{\oplus r}\longrightarrow N\longrightarrow0.
$$
The kernel $K$ is finite because $A$ is noetherian.
The long exact Ext sequence in the second variable contains
$$
\Ext_A^i(M,A^{\oplus r})\longrightarrow\Ext_A^i(M,N)
\longrightarrow\Ext_A^{i+1}(M,K).
$$
The first term is $\Ext_A^i(M,A)^{\oplus r}=0$; the last is zero by the induction hypothesis.
Thus the middle group is zero.
This completes the descending induction; when $d=0$, the initial bound already gives every required vanishing.
:::

<1>2. The equivalence in (a) holds.

::: {.proof}
If $M$ is projective, its length-zero projective resolution gives $\Ext_A^i(M,A)=0$ for all $i>0$.

Conversely, assume these groups vanish and choose a finite free presentation
$$
0\longrightarrow K\longrightarrow A^{\oplus r}\xrightarrow{p}M\longrightarrow0.
$$
Again $K$ is finite.
Step <1>1 gives $\Ext_A^1(M,K)=0$.
The corresponding long exact sequence therefore makes
$$
\Hom_A(M,A^{\oplus r})\longrightarrow\Hom_A(M,M)
$$
surjective.
A preimage of $\id_M$ is a section of $p$, so $M$ is a direct summand of a finite free module.
It is therefore [[D-DEFPROJO|projective]], proving (a).
:::

<1>3. The equivalence in (b) holds for every $n\ge0$.

::: {.proof}
A projective resolution of length at most $n$ makes $\Ext_A^i(M,A)=0$ for $i>n$.

For the converse, construct a finite-free resolution of $M$ successively and denote its kernels by
$$
K_0=M,\qquad
0\longrightarrow K_{j+1}\longrightarrow P_j\longrightarrow K_j\longrightarrow0,
$$
where each $P_j$ is finite free and each $K_j$ is finite.
The long exact Ext sequences in the first variable give
$$
\Ext_A^i(K_n,A)\cong\Ext_A^{i+n}(M,A)
\qquad(i>0).
$$
If the groups on the right vanish for all $i>0$, part (a), proved in step <1>2, implies that $K_n$ is projective.
For $n\ge1$, truncation then gives a projective resolution
$$
0\longrightarrow K_n\longrightarrow P_{n-1}\longrightarrow\cdots
\longrightarrow P_0\longrightarrow M\longrightarrow0
$$
of length $n$.
For $n=0$, the same argument says directly that $M=K_0$ is projective.
Hence $\operatorname{pd}_A M\le n$ in every case.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), and step <1>3 proves (b).
:::
:::
