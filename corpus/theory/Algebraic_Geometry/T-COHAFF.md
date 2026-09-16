---
schema: qual/card@1
id: T-COHAFF
kind: theorem
title: Higher cohomology vanishes on an affine scheme
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
- Prove affine vanishing and independence of the affine cover with Čech complexes.
---

::: {.theorem}
Let $X = \Spec A$ with $A$ Noetherian and $\mcf \in \QCoh(X)$.
Then $H^0(X, \mcf) = \globsec{X;\mcf}$ and $H^i(X, \mcf) = 0$ for all $i > 0$.
:::

::: {.remark title="The proof in one line"}
Put $M = \globsec{X;\mcf}$, so $\mcf \cong \tilde M$.
Take an injective resolution $M \injects I^\bullet$ in $\amod$ and sheafify: each $\tilde{I^j}$ is flasque, hence acyclic, so $\tilde{I^\bullet}$ computes the cohomology.
Applying $\globsec{X;\wait}$ returns the original exact complex $M \injects I^\bullet$, and its higher cohomology is zero.
:::

::: {.proposition title="Čech computation"}
Let $\mcf$ be a quasicoherent sheaf on a scheme $X$.

1. If $X$ is affine and $\mathfrak{U} = \{U_1, \ldots, U_r\}$ is a finite cover of $X$ by affine opens whose finite intersections are affine, the augmented Čech complex $0 \to \mcf(X) \to C^0(\mathfrak{U}, \mcf) \to C^1(\mathfrak{U}, \mcf) \to \cdots$ is exact; so $\check{H}^i(\mathfrak{U}, \mcf) = 0$ for $i > 0$.

2. If $X$ is quasicompact and separated, any two finite affine covers $\mathfrak{U}$, $\mathfrak{V}$ give the same Čech cohomology: $\check{H}^i(\mathfrak{U}, \mcf) \cong \check{H}^i(\mathfrak{V}, \mcf)$.
:::

<1>1. If some member of $\mathfrak{U}$ equals $X$, the augmented complex is exact.

::: {.proof}
Say $U_1 = X$. Define $h \colon C^{p}(\mathfrak{U}, \mcf) \to C^{p-1}(\mathfrak{U}, \mcf)$ for $p \geq 0$ by $(h c)_{i_0 \cdots i_{p-1}} = c_{1\, i_0 \cdots i_{p-1}}$, using $U_1 \cap U_{i_0 \cdots i_{p-1}} = U_{i_0 \cdots i_{p-1}}$, with $C^{-1} = \mcf(X)$ and $(hc) = c_1$ for $p = 0$. The alternating Čech differential $d$ satisfies $dh + hd = \id$ in every degree, so the augmented complex is contractible.
:::

<1>2. Part 1 holds for every finite affine cover of an affine scheme with affine intersections.

::: {.proof}
Let $X = \Spec A$ and $M = \mcf(X)$, so each term of the augmented complex is a product of modules $\mcf(U_I)$. Every point of $X$ lies in a distinguished open $D(f)$ contained in some $U_i$, and finitely many such $f$ generate the unit ideal, so the augmented complex is exact if its localization at each such $f$ is exact. Localization at $f$ commutes with sections over affine opens of the quasicoherent sheaf $\mcf$, since $\mcf(U_I)_f = \mcf(U_I \cap D(f))$, so the localized complex is the augmented Čech complex of the cover $\{U_i \cap D(f)\}$ of $D(f)$. That cover contains $U_i \cap D(f) = D(f)$, so it is exact by step <1>1.
:::

<1>3. Part 2.

::: {.proof}
Form the double complex $K^{p,q} = \prod_{\abs{I} = p+1, \abs{J} = q+1} \mcf(U_I \cap V_J)$ with the two Čech differentials. For fixed $I$, the column $q \mapsto K^{p,q}$ augmented by $\mcf(U_I)$ is the augmented Čech complex of the finite affine cover $\{U_I \cap V_j\}_j$ of the affine scheme $U_I$, with affine intersections because $X$ is separated; by step <1>2 it is exact. So the total complex of $K$ has the same cohomology as $C^\bullet(\mathfrak{U}, \mcf)$, and by symmetry as $C^\bullet(\mathfrak{V}, \mcf)$.
:::

::: {.remark title="Hypotheses"}
Quasicoherence is the load-bearing hypothesis, and it is where the whole argument lives: the theorem is false for general sheaves of abelian groups, which see the topology of $X$ rather than the module $M$.
Noetherianness is only used to know that $\tilde I$ is flasque for $I$ injective; the statement is true for any affine scheme, but that version is harder.

This is the direction of Serre's criterion that is a theorem about affines, and the other direction is the criterion proper.
It is also the reason every computation is done on an affine cover: on the pieces of the cover there is nothing above degree $0$, so all the cohomology comes from the gluing, which is exactly what the Čech complex records.
:::
