---
schema: qual/card@1
id: P-AGSCHEMEDEF
kind: problem
title: What a scheme is
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Spec
  - Definitions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for the definition of a scheme.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What is a scheme?
:::

::: {.solution}
<1>1. A ringed space is a pair
\[
(X,\mathcal O_X)
\]
consisting of a topological space $X$ and a sheaf of rings $\mathcal O_X$ on $X$.
It is locally ringed if every stalk
\[
\mathcal O_{X,x}
\]
is a local ring.
::: {.proof}
The sheaf $\mathcal O_X$ records the functions available on every open subset, together with their restriction and gluing.  The local-ring condition singles out, at each point $x$, the functions vanishing there as the unique maximal ideal of the stalk.
:::

<1>2. For a commutative ring $A$, the affine scheme
\[
\operatorname{Spec}A
\]
is the locally ringed space whose underlying set is the set of prime ideals of $A$, with Zariski closed subsets
\[
V(I)=\{\mathfrak p\in\operatorname{Spec}A:I\subseteq\mathfrak p\},
\]
and whose structure sheaf satisfies
\[
\mathcal O_{\operatorname{Spec}A}(D(f))=A_f.
\]
::: {.proof}
The distinguished opens
\[
D(f)=\{\mathfrak p:f\notin\mathfrak p\}
\]
form a basis of the Zariski topology.  Localizing on them and sheafifying gives the structure sheaf.  Its stalk at a point $\mathfrak p$ is
\[
\mathcal O_{\operatorname{Spec}A,\mathfrak p}=A_{\mathfrak p},
\]
which is a local ring with maximal ideal $\mathfrak pA_{\mathfrak p}$.
:::

<1>3. A scheme is a locally ringed space $(X,\mathcal O_X)$ admitting an open cover
\[
X=\bigcup_i U_i
\]
such that for every $i$ there is a ring $A_i$ and an isomorphism of locally ringed spaces
\[
\boxed{
(U_i,\mathcal O_X|_{U_i})\cong
(\operatorname{Spec}A_i,\mathcal O_{\operatorname{Spec}A_i}).
}
\]
::: {.proof}
This is the definition.  The open subsets $U_i$ are the affine open charts of the scheme.  Thus a scheme is obtained by gluing affine schemes along open subschemes, with both their topologies and their rings of regular functions glued compatibly.
:::

<1>4. A morphism of schemes
\[
f:(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
is a morphism of locally ringed spaces: a continuous map $f:X\to Y$ together with a sheaf morphism
\[
f^\sharp:\mathcal O_Y\longrightarrow f_*\mathcal O_X
\]
whose maps on stalks
\[
f_x^\sharp:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]
are local homomorphisms.
::: {.proof}
The locality requirement means
\[
(f_x^\sharp)^{-1}(\mathfrak m_x)=\mathfrak m_{f(x)}.
\]
With this requirement, morphisms of affine schemes correspond contravariantly to ring homomorphisms:
\[
\operatorname{Hom}_{\mathrm{Sch}}(\operatorname{Spec}B,\operatorname{Spec}A)
\cong
\operatorname{Hom}_{\mathrm{Ring}}(A,B).
\]
:::

<1>5. In one sentence,
\[
\boxed{
\text{a scheme is a space locally modeled on spectra of rings, with the rings retained as its structure sheaf.}
}
\]
::: {.proof}
This is exactly the content of <1>1--<1>3: the topology alone would forget nilpotents and local algebra, while the structure sheaf remembers them.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>3 is the formal definition, with <1>2 specifying the affine local model.
:::
:::
