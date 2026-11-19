---
schema: qual/card@1
id: P-HCAX3
kind: problem
title: Mapping class group of the torus
classification:
  areas:
  - topology
  topics:
  - Mapping Class Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card. Added: the
    computation det A = 1 from A^T J A = J in both steps (the prose derived det A = 1 directly
    from A^T J A = (det A) J without noting that det A = +-1 follows first); that the linear map
    x -> Ax descends to a homeomorphism of degree det A; the identification H_1 = pi_1 for the
    abelian group Z^2 in the injectivity direction; and explicit naming of the two external
    inputs — that T^2 is a K(Z^2,1) and Baer's theorem that homotopic orientation-preserving
    homeomorphisms of a closed orientable surface are isotopic. Not claimed: a retained solution
    set; the provenance names the oral question list.
---

::: {.problem}
Show that the orientation-preserving mapping class group of the torus is $\operatorname{SL}_2(\ZZ)$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the MGSA complex-analysis oral question list, which carries no solutions, and this is a topology question in it. The argument below is the card's own and follows the card's previous prose; the two external inputs are named where used — that $T^2$ is a $K(\ZZ^2,1)$, and Baer's theorem that homotopic orientation-preserving homeomorphisms of a closed orientable surface are isotopic.

Throughout $T^2=\RR^2/\ZZ^2$, $\operatorname{Mod}^+(T^2)$ is the group of isotopy classes of orientation-preserving homeomorphisms $T^2\to T^2$, and the standard basis of $H_1(T^2;\ZZ)\cong\ZZ^2$ is that of the two circle factors.

::: pf

::: {.pf-step #homomorphism}
There is a homomorphism $\Phi:\operatorname{Mod}^+(T^2)\to GL_2(\ZZ)$, assigning to the class of $f$ the matrix of $f_*:H_1(T^2;\ZZ)\to H_1(T^2;\ZZ)$.

::: pf-proof
$H_1(T^2;\ZZ)\cong\ZZ^2$, a free abelian group, so a homomorphism $f_*:\ZZ^2\to\ZZ^2$ has an integral matrix in the standard basis. The assignment $f\mapsto f_*$ is a functor, so it respects composition and identities; it is constant on isotopy classes because homotopic maps induce equal maps on homology. Hence $\Phi$ is a well-defined homomorphism. The inverse of an orientation-preserving homeomorphism is orientation preserving, so $\operatorname{Mod}^+(T^2)$ is a group and $f_*\in GL_2(\ZZ)$.

:::

:::

::: {.pf-step #det}
$\Phi$ takes values in $SL_2(\ZZ)$: if $f$ is orientation preserving then $\det f_*=1$.

::: pf-proof
Let $\cdot$ be the algebraic intersection form on $H_1$, alternating and unimodular, whose matrix in the standard basis is $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. An orientation-preserving homeomorphism preserves intersection numbers, so $f_*a\cdot f_*b=a\cdot b$ for all $a,b$, that is $A^TJA=J$ for $A=[f_*]$. Taking determinants, $(\det A)^2\det J=\det J$, so $\det A=\pm1$; and $A^TJA=(\det A)J$ holds for every $2\times2$ matrix, so $A^TJA=J$ forces $\det A=1$.

:::

:::

::: {.pf-step #surjective}
$\Phi$ is surjective.

::: pf-proof
Let $A\in SL_2(\ZZ)$. The linear map $x\mapsto Ax$ carries $\ZZ^2$ into itself and is invertible with inverse given by $A^{-1}\in SL_2(\ZZ)$, so it induces a homeomorphism $f_A:T^2\to T^2$ of the quotient, of degree $\det A=1$, hence orientation preserving. Since $\pi_1(T^2)=\ZZ^2$ and $H_1=\pi_1^{\mathrm{ab}}=\pi_1$, the induced map on $H_1$ is the map $A$ on $\ZZ^2$. So $\Phi[f_A]=A$.

:::

:::

::: {.pf-step #injective}
$\Phi$ is injective.

::: pf-proof
Suppose $f$ is orientation preserving and $\Phi[f]=I$, i.e. $f_*=\mathrm{id}$ on $H_1(T^2;\ZZ)\cong\ZZ^2$. Since $\ZZ^2$ is abelian, $H_1=\pi_1$ and the induced map on $\pi_1$ is the identity after identifying basepoints along a path; equivalently, for every loop $\gamma$ in $T^2$ the loop $f\circ\gamma$ is freely homotopic to $\gamma$. The torus is a $K(\ZZ^2,1)$, so a map inducing the identity on $\pi_1$ is homotopic to the identity; hence $f\simeq\mathrm{id}$. By Baer's theorem, homotopic orientation-preserving homeomorphisms of a closed orientable surface are isotopic, so $f$ represents the trivial mapping class.

:::

:::

::: {.pf-step #conclusion}
$\operatorname{Mod}^+(T^2)\cong SL_2(\ZZ)$.

::: pf-proof
Steps [](#homomorphism){.pf-ref} and [](#det){.pf-ref} give a homomorphism into $SL_2(\ZZ)$, and steps [](#surjective){.pf-ref} and [](#injective){.pf-ref} make it bijective.

:::

:::

:::
:::
