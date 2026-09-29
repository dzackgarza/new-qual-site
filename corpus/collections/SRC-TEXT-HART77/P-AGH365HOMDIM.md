---
schema: qual/card@1
id: P-AGH365HOMDIM
kind: problem
title: Homological dimension of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Sheaves
  - Homological Dimension
  - Locally Free Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three equivalences with the retained Hartshorne III.6.5 transcription and the module projective-dimension criterion in Proposition III.6.10A. The proof splits a locally free presentation locally using sheaf Ext, performs dimension shifting on coherent kernels, and treats both finite and infinite stalkwise suprema.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and assume that $\Coh(X)$ has enough locally frees (Ex. 6.4).
For a coherent sheaf $\mcf$, define its **homological dimension** $\operatorname{hd}(\mcf)$ to be the least length of a resolution by locally free coherent sheaves, or $+\infty$ if there is no finite one.
Show:

(a) $\mcf$ is locally free $\iff \mathcal{E}xt^1(\mcf, \mcg)=0$ for all $\mcg \in \Mod(X)$;

(b) For $n\ge0$, $\operatorname{hd}(\mcf) \leq n \iff \mathcal{E}xt^i(\mcf, \mcg)=0$ for all $i>n$ and all $\mcg \in \Mod(X)$;

(c) $\operatorname{hd}(\mcf)=\sup_x \operatorname{pd}_{\mco_x} \mcf_x$.
:::

::: {.solution}
Lengths and projective dimensions take values in $\NN\cup\{+\infty\}$, with the zero sheaf or module assigned dimension zero.
For an empty $X$, take the supremum in this ordered set to be zero; all assertions are then immediate.
The hypothesis of [[P-AGH364UNIVERSALDELTA|enough locally free sheaves]] supplies finite-rank locally free epimorphisms onto every coherent sheaf.

::: pf

::: {.pf-step #s1}

The equivalence in (a) holds.

::: pf-proof

If $\mcf$ is locally free, the functor $\sheafhom_X(\mcf,-)=\mcf^\vee\otimes-$ is exact locally, so all its positive derived sheaves vanish, as proved in [[P-AGH364UNIVERSALDELTA]], step [](#s2){.pf-ref}.

Conversely, choose an exact sequence
$$
0\longrightarrow K\longrightarrow E\xrightarrow{p}\mcf\longrightarrow0
$$
with $E$ locally free of finite rank; $K$ is coherent because $X$ is noetherian.
The long exact sequence in the second variable gives
$$
\sheafhom_X(\mcf,E)\longrightarrow\sheafhom_X(\mcf,\mcf)
\longrightarrow\mathcal{E}xt_X^1(\mcf,K)=0.
$$
The germ of the identity morphism therefore lifts at every point to a local sheaf morphism $\mcf\to E$.
After shrinking its domain, its composite with $p$ is the identity.
Thus $\mcf$ is locally a direct summand of $E$.
Its stalks are finite projective modules over local rings and hence free.
Since $\mcf$ is coherent, a basis at a stalk extends to a basis on a neighborhood: extend its finitely many elements to sections and shrink until the coherent kernel and cokernel of the resulting map from a finite free sheaf vanish.
Hence $\mcf$ is locally free, proving (a).

:::

:::

::: {.pf-step #s2}

There are coherent sheaves $K_j$ and exact sequences
$$
K_0=\mcf,\qquad
0\longrightarrow K_{j+1}\longrightarrow E_j\longrightarrow K_j\longrightarrow0
\quad(j\ge0),
$$
with all $E_j$ locally free of finite rank; they satisfy
$$
\mathcal{E}xt_X^q(K_n,\mcg)
\cong\mathcal{E}xt_X^{q+n}(\mcf,\mcg)
\quad(q\ge1).
$$

::: pf-proof

Construct the sequences successively using enough locally frees.
At each stage the kernel is coherent by [@Har10a, Proposition II.5.7], so the construction can continue.
The long exact sheaf-Ext sequence in the first variable [@Har10a, Proposition III.6.4] contains
$$
\mathcal{E}xt_X^q(E_j,\mcg)\longrightarrow
\mathcal{E}xt_X^q(K_{j+1},\mcg)\longrightarrow
\mathcal{E}xt_X^{q+1}(K_j,\mcg)\longrightarrow
\mathcal{E}xt_X^{q+1}(E_j,\mcg).
$$
For $q\ge1$ the outside terms vanish by local freeness.
Iterating the middle isomorphisms proves the formula, with $n=0$ giving the identity.

:::

:::

::: {.pf-step #s3}

The equivalence in (b) holds for every $n\ge0$.

::: pf-proof

If $\mcf$ has a locally free resolution of length at most $n$, [@Har10a, Proposition III.6.5] computes $\mathcal{E}xt_X^i(\mcf,\mcg)$ as the cohomology of its sheaf-Hom complex with $\mcg$.
That complex has no terms above degree $n$, so the required groups vanish for every $i>n$ and every $\mcg$.

Conversely, assume the stated vanishing.
Step [](#s2){.pf-ref} gives $\mathcal{E}xt_X^1(K_n,\mcg)=0$ for every $\mcg$.
By step [](#s1){.pf-ref}, $K_n$ is locally free.
For $n\ge1$ the exact sequence
$$
0\longrightarrow K_n\longrightarrow E_{n-1}\longrightarrow\cdots
\longrightarrow E_0\longrightarrow\mcf\longrightarrow0
$$
is therefore a locally free resolution of length $n$.
For $n=0$, this says directly that $\mcf=K_0$ is locally free and has a length-zero resolution.
Thus $\operatorname{hd}(\mcf)\le n$.

:::

:::

::: {.pf-step #s4}

The equality in (c) is
$$
\boxed{\operatorname{hd}(\mcf)=
\sup_{x\in X}\operatorname{pd}_{\OO_{X,x}}\mcf_x.}
$$

::: pf-proof

A finite locally free resolution stays exact on stalks and becomes a finite free resolution over $\OO_{X,x}$.
Consequently every stalkwise projective dimension is at most $\operatorname{hd}(\mcf)$.

Suppose their supremum is a finite integer $n$ and use the resolution in step [](#s2){.pf-ref}.
For every $x$, dimension shifting of module Ext along its stalk sequences gives
$$
\Ext^1_{\OO_{X,x}}((K_n)_x,N)
\cong\Ext^{n+1}_{\OO_{X,x}}(\mcf_x,N)=0
$$
for every $\OO_{X,x}$-module $N$.
The module projectivity criterion [@Har10a, Proposition III.6.10A] makes $(K_n)_x$ projective, and its finite generation makes it free over the local ring.
The neighborhood argument from step [](#s1){.pf-ref} then makes the coherent sheaf $K_n$ locally free.
Truncating the resolution as in step [](#s3){.pf-ref} gives $\operatorname{hd}(\mcf)\le n$.

If the supremum is infinite, no finite locally free resolution can exist, by the first inequality.
If the homological dimension were infinite while the supremum were finite, the preceding construction would give a finite resolution, a contradiction.
These observations cover all values and prove (c).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), step [](#s3){.pf-ref} proves (b), and step [](#s4){.pf-ref} proves (c).

:::

:::

:::
