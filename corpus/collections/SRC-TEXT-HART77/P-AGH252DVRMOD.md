---
schema: qual/card@1
id: P-AGH252DVRMOD
kind: problem
title: Modules over the spectrum of a discrete valuation ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-coherent Sheaves
  - Discrete Valuation Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.2(a)-(b).
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $R$ be a discrete valuation ring with quotient field $K$, and let $X=\Spec R$.

(a) To give an $\OO_X$-module is equivalent to giving an $R$-module $M$, a $K$-vector space $L$, and a homomorphism $\rho:M\otimes_R K\to L$.

(b) That $\OO_X$-module is quasi-coherent if and only if $\rho$ is an isomorphism.
:::

::: {.solution}
Choose a uniformizer $\pi\in R$ and write $\mathfrak m=(\pi)$.
Let $x\in X$ correspond to $\mathfrak m$, and let $\eta\in X$ correspond to $(0)$.
All homomorphisms $\rho:M\otimes_R K\to L$ are taken to be $K$-linear.

<1>1. The nonempty open sets of $X$ are $X$ and $\{\eta\}$, with section rings $R$ and $K$, respectively.

::: {.proof}
Every nonzero element of $R$ is $u\pi^n$ for a unit $u$ and an integer $n\ge0$.
A nonzero prime ideal therefore contains $\pi$, and must equal the maximal ideal $\mathfrak m$.
Thus $X$ has precisely the points $x,\eta$.
The distinguished open $D(\pi)$ is $\{\eta\}$, and its ring of sections is $R[\pi^{-1}]=K$.
Any open set containing $x$ contains a distinguished neighborhood $D(a)$ with $a\notin\mathfrak m$.
Such an $a$ is a unit, so $D(a)=X$.
Hence $X$ is the only open neighborhood of $x$.
The restriction map on the structure sheaf is the inclusion $R\hookrightarrow K$.
:::

<1>2. The correspondence in part (a) is an equivalence, including morphisms.

::: {.proof}
Given an $\OO_X$-module $\mcf$, set
$$
M=\mcf(X),\qquad L=\mcf(\{\eta\}).
$$
The restriction map $r:M\to L$ is $R$-linear for the inclusion $R\hookrightarrow K$.
It extends uniquely to a $K$-linear map
$$
\rho:M\otimes_R K\longrightarrow L,
\qquad\rho(m\otimes a)=a\,r(m).
$$

Conversely, from $(M,L,\rho)$ define the sections on $X$, $\{\eta\}$, and $\varnothing$ to be $M$, $L$, and $0$, with restriction
$$
r(m)=\rho(m\otimes1).
$$
Use the given $R$-module and $K$-module structures on the two nonempty opens.
The $K$-linearity of $\rho$ gives the required compatibility of $r$ with $R\hookrightarrow K$.
Every open cover of either nonempty open set contains that open set itself, so locality and gluing hold: a compatible family is uniquely determined by its section on that member of the cover.
The empty-set sheaf condition holds because its module of sections is zero.
Thus these data define an $\OO_X$-module.

A morphism from $(M,L,\rho)$ to $(M',L',\rho')$ is a pair consisting of an $R$-linear map $u:M\to M'$ and a $K$-linear map $v:L\to L'$ such that
$$
v\circ\rho=\rho'\circ(u\otimes\operatorname{id}_K).
$$
This equation is equivalent to compatibility with the restriction maps, so such pairs are precisely sheaf-module morphisms.
Both constructions preserve composition and identities.
They are inverse on section modules and restriction maps, proving the equivalence.
:::

<1>3. The sheaf corresponding to $(M,L,\rho)$ is quasi-coherent exactly when $\rho$ is an isomorphism.

::: {.proof}
The sheaf $\widetilde M$ associated to $M$ has sections $M$ on $X$ and $M\otimes_R K$ on $D(\pi)=\{\eta\}$, with restriction $m\mapsto m\otimes1$ [@Har10a, Proposition II.5.1].
It corresponds to $(M,M\otimes_R K,\operatorname{id}_{M\otimes_R K})$.
If $\rho$ is an isomorphism, the pair $(\operatorname{id}_M,\rho)$ therefore gives an isomorphism $\widetilde M\to\mcf$, proving that $\mcf$ is quasi-coherent.

Conversely, if $\mcf$ is quasi-coherent, its defining affine-local description supplies an affine neighborhood $U$ of $x$ and a module $N$ with $\mcf|_U\cong\widetilde N$ [@Har10a, Chapter II, §5].
Step <1>1 forces $U=X$.
The resulting isomorphism gives an $R$-linear isomorphism $u:N\to M$ and a $K$-linear isomorphism $v:N\otimes_R K\to L$.
By step <1>2 they satisfy $v=\rho\circ(u\otimes\operatorname{id}_K)$.
Hence $\rho=v\circ(u\otimes\operatorname{id}_K)^{-1}$ is an isomorphism.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), and step <1>3 proves part (b).
:::
:::
