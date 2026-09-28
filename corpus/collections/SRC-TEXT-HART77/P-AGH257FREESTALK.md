---
schema: qual/card@1
id: P-AGH257FREESTALK
kind: problem
title: Local freeness from free stalks, and invertible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Invertible Sheaves
  - Coherent Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.7. Checked the localization argument and the use of Nakayama's lemma against Stacks Project sections 10.20 and 10.78; the proof kills both kernel and cokernel and proves faithfulness before concluding rank-one freeness.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and let $\mcf$ be a coherent sheaf.

(a) If the stalk $\mcf_x$ is a free $\OO_x$-module for some point $x \in X$, then there is a neighborhood $U$ of $x$ such that $\mcf|_U$ is free.

(b) $\mcf$ is locally free if and only if its stalks $\mcf_x$ are free $\OO_x$-modules for all $x \in X$.

(c) $\mcf$ is invertible, i.e. locally free of rank $1$, if and only if there is a coherent sheaf $\mcg$ such that $\mcf \tensor \mcg \cong \OO_X$.
    This justifies the terminology: it means that $\mcf$ is an invertible element of the monoid of coherent sheaves under $\tensor$.
:::

::: {.solution}
All sheaf tensor products are over $\OO_X$.

<1>1. For part (a), a free stalk of rank $r$ extends to a free sheaf of rank $r$ on a neighborhood of that point.

::: {.proof}
Choose an affine neighborhood $V=\Spec A$ of $x$, and let $\mathfrak p$ be the prime corresponding to $x$.
Since $X$ is noetherian and $\mcf$ is [[D-QNTZY|coherent]], there is a finite $A$-module $M$ with $\mcf|_V\cong\widetilde M$ [@Har10a, Proposition II.5.4].
Then $\mcf_x\cong M_{\mathfrak p}$.
Its free rank $r$ is finite because it is finitely generated over $A_{\mathfrak p}$.

Represent each member of a basis of $M_{\mathfrak p}$ as $m_i/s_i$, with $m_i\in M$ and $s_i\notin\mathfrak p$.
Multiplying the individual basis vectors by the units $s_i$ shows that $m_1/1,\ldots,m_r/1$ are also a basis.
Define
$$
u:A^r\longrightarrow M,\qquad (a_i)\longmapsto\sum_i a_im_i.
$$
The localized map $u_{\mathfrak p}$ is an isomorphism.
Let $K=\ker u$ and $C=\operatorname{coker}u$.
Both are finite: $C$ is a quotient of $M$, and $K$ is a submodule of the finite module $A^r$ over the noetherian ring $A$.
Exactness of localization gives $K_{\mathfrak p}=C_{\mathfrak p}=0$.

For every member of finite generating lists of $K$ and $C$, choose an element of $A\setminus\mathfrak p$ annihilating it.
The product $s$ of these finitely many elements lies outside $\mathfrak p$ and annihilates both modules.
Thus $K_s=C_s=0$, and $u_s:A_s^r\to M_s$ is an isomorphism.
On $U=D_V(s)$, it induces $\mcf|_U\cong\OO_U^r$.
If $r=0$, the same argument applies to $u:0\to M$ and gives $\mcf|_U=0$.
:::

<1>2. Part (b) holds.

::: {.proof}
An isomorphism $\mcf|_U\cong\OO_U^r$ induces $\mcf_x\cong\OO_{X,x}^r$ for every $x\in U$ by passing to stalks.
Consequently local freeness implies freeness of every stalk.
Conversely, if every stalk is free, step <1>1 supplies a free neighborhood at each point.
These neighborhoods cover $X$, proving local freeness.
:::

<1>3. For the forward implication of part (c), a tensor inverse of $\mcf$ is
$$
\boxed{\mcg=\dualof{\mcf}=\sheafhom_{\OO_X}(\mcf,\OO_X)}.
$$

::: {.proof}
Assume $\mcf$ is locally free of rank one.
The evaluation morphism
$$
\mcf\otimes\dualof{\mcf}\longrightarrow\OO_X,
\qquad s\otimes\lambda\longmapsto\lambda(s)
$$
is defined compatibly on local sections, as in [[P-AGH251DUALSHEAF]]. On a trivializing open set with frame $e$, the coordinate functional $\dualof{e}$ is a frame of $\dualof{\mcf}$, and evaluation sends $e\otimes \dualof{e}$ to $1$.
It is therefore an isomorphism on each such open set, hence on $X$.
The sheaf $\dualof{\mcf}$ is locally free of rank one as well, so its local modules over noetherian affine charts are finite and it is [[D-QNTZY|coherent]]. The evaluation morphism is independent of the chosen frames; the frames only verify that it is an isomorphism.
:::

<1>4. Conversely, a [[D-QNTZY|coherent]] tensor inverse forces $\mcf$ to be locally free of rank one.

::: {.proof}
Suppose $\mcf\otimes\mcg\cong\OO_X$ with $\mcg$ [[D-QNTZY|coherent]]. Fix $x\in X$, put $R=\OO_{X,x}$, and write $\mathfrak m$ for its maximal ideal and $\kappa=R/\mathfrak m$ for its residue field.
The modules $M=\mcf_x$ and $N=\mcg_x$ are finite over $R$.
Taking stalks and then tensoring with $\kappa$ gives
$$
M\otimes_R N\cong R,
\qquad
(M/\mathfrak mM)\otimes_\kappa(N/\mathfrak mN)\cong\kappa.
$$
The product of the dimensions of these finite-dimensional vector spaces is one, so each dimension is one.
By [[T-DEFNAKA|Nakayama's lemma]], $M$ is cyclic.
Every element of $\Ann_R M$ annihilates $M\otimes_R N\cong R$, so $\Ann_R M=0$.
For a generator $m\in M$, the surjection $R\to M$, $a\mapsto am$, has kernel $\Ann_R m=\Ann_R M=0$.
Hence $M\cong R$.
This holds for every $x$, and the rank-preserving construction of step <1>1 supplies rank-one trivializations around all points.
Thus $\mcf$ is invertible.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove parts (a) and (b). Steps <1>3 and <1>4 prove both implications of part (c).
:::
:::
