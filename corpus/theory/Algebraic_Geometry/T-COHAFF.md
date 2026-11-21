---
schema: qual/card@1
id: T-COHAFF
kind: theorem
title: Higher cohomology vanishes on an affine scheme
slogan: 'Quasicoherent cohomology on an affine scheme lives in degree $0$; higher cohomology is gluing data between affine pieces.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Affine Schemes
  - Quasicoherent Sheaves
relations:
- kind: uses
  target: D-COHFLQ
- kind: related-to
  target: T-5IOUR
review: draft
prompts:
- Compute the cohomology of a quasicoherent sheaf on an affine scheme.
- Which hypothesis in affine vanishing is load-bearing?
- Why do Čech complexes of finite affine covers compute the cohomology of quasicoherent sheaves on a separated scheme?
---

::: {.theorem}
Let $X = \Spec A$ with $A$ Noetherian and $\mcf \in \QCoh(X)$.
Then $H^0(X, \mcf) = \globsec{X;\mcf}$ and $H^i(X, \mcf) = 0$ for all $i > 0$.
:::

::: {.proof}
Put $M \coloneqq \globsec{X;\mcf}$; then $\mcf\cong\tilde M$ [@Har77, II.5.5].
Take an injective resolution $0\to M\to I^\bullet$ in $\amod$, which exists because every $A$-module embeds in an injective one [@Har77, Proposition III.2.1A].
Sheafifying gives an exact sequence of sheaves $0\to\tilde M\to\tilde I^\bullet$ on $X$, because $M\mapsto\tilde M$ is an exact functor [@Har77, II.5.5].
Each $\tilde I^j$ is flasque, $I$ being injective over the Noetherian ring $A$ [@Har77, Proposition III.3.4], hence $\globsec{X;-}$-acyclic ([[D-COHFLQ]]); so $\tilde I^\bullet$ is a $\globsec{X;-}$-acyclic resolution of $\mcf$ and computes its cohomology [@Har77, Proposition III.1.2A]:
$$
H^i(X,\mcf)\cong h^i\big(\globsec{X;\tilde I^\bullet}\big).
$$
On $X=\Spec A$ the global sections of $\tilde N$ are $N$ [@Har77, II.5.5], so the complex on the right is $I^\bullet$ again; it is exact in positive degrees and has cohomology $M$ in degree $0$ because $I^\bullet$ resolves $M$.
Hence $H^0(X,\mcf)=M=\globsec{X;\mcf}$ and $H^i(X,\mcf)=0$ for $i>0$.
:::

::: {.proposition title="Čech computation"}
Let $\mcf$ be a quasicoherent sheaf on a scheme $X$.

1. If $X$ is affine and $\mathfrak{U} = \{U_1, \ldots, U_r\}$ is a finite cover of $X$ by affine opens whose finite intersections are affine, the augmented Čech complex $0 \to \mcf(X) \to C^0(\mathfrak{U}, \mcf) \to C^1(\mathfrak{U}, \mcf) \to \cdots$ is exact; so $\check{H}^i(\mathfrak{U}, \mcf) = 0$ for $i > 0$.

2. If $X$ is quasicompact and separated, any two finite affine covers $\mathfrak{U}$, $\mathfrak{V}$ give the same Čech cohomology: $\check{H}^i(\mathfrak{U}, \mcf) \cong \check{H}^i(\mathfrak{V}, \mcf)$; for $X$ Noetherian both equal $H^i(X, \mcf)$ [@Har77, Theorem III.4.5].
:::

::: {.remark title="Hypotheses"}
Quasicoherence is the essential hypothesis: the theorem is false for general sheaves of abelian groups, which see the topology of $X$ rather than the module $M$.
Noetherianness is only used to know that $\tilde I$ is flasque for $I$ injective; the statement is true for any affine scheme, but that version is harder.

This is one direction of Serre's criterion: an affine scheme has vanishing higher cohomology for quasicoherent sheaves. The converse, that a noetherian scheme with this vanishing is affine, is the criterion proper.
It is also the reason every computation is done on an affine cover: on the pieces of the cover there is nothing above degree $0$, so all the cohomology comes from the gluing, which is exactly what the Čech complex records.
:::
