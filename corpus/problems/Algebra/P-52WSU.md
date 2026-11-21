---
schema: qual/card@1
id: P-52WSU
kind: problem
title: Toeplitz operator
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks for three
    definitions and a description of the matrix, so there is no proof obligation and
    no pf block was added; this note is the record. What was checked, by reading
    against a fresh derivation: the Hardy space as the closed span of the
    nonnegative powers of z, equivalently the L^2 functions whose negative Fourier
    coefficients vanish, which is the standard definition; the Szego projection and
    the definition T_phi = P_+ M_phi restricted to H^2, with the bound
    ||T_phi|| <= ||phi||_infty following from ||M_phi|| = ||phi||_infty and
    ||P_+|| = 1; and the matrix entries, which were recomputed: with
    <f,g> = (1/2pi) int f conj(g) the entry <T_phi e_j, e_i> equals
    (1/2pi) int phi z^{j-i} = hat(phi)(i-j), so the matrix is the semi-infinite
    Toeplitz matrix (a_{i-j}) with a_k = hat(phi)(k), constant on diagonals, as
    displayed. All correct. What was not checked: no source solution is retained for
    this card, so no source comparison was made, and no theorem about Toeplitz
    operators (Fredholmness, essential spectrum) is stated or needed here.
---

::: {.problem}
What is a Toeplitz operator? Define the Hardy space $H^2(\circlegroup)$, the Toeplitz operator $T_\varphi$ associated with a symbol $\varphi \in L^\infty(\circlegroup)$, and describe its matrix representation.
:::

::: {.solution}

The definitions and the matrix computation are the card's own, with the Brown--Halmos theorem quoted and its easy direction proved; no retained set supplies them, and the sets searched are recorded in the audit trail.

Let $\circlegroup=\{z\in\CC:\abs{z}=1\}$ carry normalized Lebesgue measure $m$, so that $\langle f,g\rangle=\int_{\circlegroup}f\bar g\,dm$ and $\widehat\varphi(k)=\int_{\circlegroup}\varphi(z)z^{-k}\,dm(z)$. The Hardy space is
$$
H^{2}(\circlegroup)=\{f\in L^{2}(\circlegroup):\widehat f(n)=0\ \text{for}\ n<0\}=\overline{\operatorname{span}}\{z^{j}:j\ge0\},
$$
$P_{+}$ is the orthogonal projection of $L^{2}$ onto it, and for $\varphi\in L^{\infty}$ the Toeplitz operator is $T_{\varphi}=P_{+}M_{\varphi}$ on $H^{2}$, that is $T_{\varphi}f=P_{+}(\varphi f)$.

::: pf

::: {.pf-step #closed}
$H^{2}(\circlegroup)$ is a closed subspace of $L^{2}(\circlegroup)$, so $P_{+}$ is defined.

::: pf-proof
The functions $z\mapsto z^{n}$ are orthonormal in $L^{2}$, since $\int z^{n}\bar z^{m}\,dm=\int z^{n-m}\,dm$ is $1$ for $n=m$ and $0$ otherwise. Hence $\overline{\operatorname{span}}\{z^{j}:j\ge0\}$ is a closed subspace, and it consists exactly of the functions whose negative Fourier coefficients vanish, by the Riesz--Fischer theorem and the completeness of the trigonometric system: an $L^{2}$ function is the sum of its Fourier series, and with the convention $\widehat f(k)=\int_{\circlegroup}f(z)z^{-k}\,dm(z)$ its scalar product with $z^{j}$ is $\int f\bar z^{j}=\int f z^{-j}=\widehat f(j)$.
:::

:::

::: {.pf-step #bounded}
$T_{\varphi}$ is bounded with $\norm{T_{\varphi}}\le\norm{\varphi}_{\infty}$.

::: pf-proof
For $f\in H^{2}$, $\norm{T_{\varphi}f}=\norm{P_{+}(\varphi f)}\le\norm{\varphi f}_{2}\le\norm{\varphi}_{\infty}\norm{f}_{2}$, the first inequality because an orthogonal projection does not increase the norm and the second by the definition of the essential supremum. So $T_{\varphi}$ is bounded and its norm is at most $\norm{\varphi}_{\infty}$.
:::

:::

::: {.pf-step #matrix}
With $e_{j}(z)=z^{j}$ and $a_{k}=\widehat\varphi(k)$, the matrix of $T_{\varphi}$ in the orthonormal basis $(e_{j})_{j\ge0}$ is $(a_{i-j})_{i,j\ge0}$.

::: pf-proof
$\langle T_{\varphi}e_{j},e_{i}\rangle=\langle P_{+}(\varphi z^{j}),z^{i}\rangle=\langle \varphi z^{j},z^{i}\rangle$ because $z^{i}\in H^{2}$ and $P_{+}$ is self-adjoint and idempotent. Then
$$
\langle \varphi z^{j},z^{i}\rangle=\int_{\circlegroup}\varphi(z)z^{j}\bar z^{i}\,dm(z)=\int_{\circlegroup}\varphi(z)z^{-(i-j)}\,dm(z)=a_{i-j},
$$
using $\bar z^{i}=z^{-i}$ on the circle. So the $(i,j)$ entry depends only on $i-j$, which is the assertion that the matrix is constant along diagonals.
:::

:::

::: {.pf-step #adjoint}
$T_{\varphi}^{*}=T_{\bar\varphi}$, and for $\varphi(z)=z$ the operator $T_{z}$ is the unilateral shift.

::: pf-proof
For $f,g\in H^{2}$, $\langle T_{\varphi}f,g\rangle=\langle \varphi f,g\rangle_{L^{2}}=\langle f,\bar\varphi g\rangle_{L^{2}}=\langle f,P_{+}(\bar\varphi g)\rangle$, since $f\in H^{2}$ and $P_{+}$ is the projection onto $H^{2}$; so the adjoint is $T_{\bar\varphi}$. For $\varphi(z)=z$ and $f\in H^{2}$ one has $zf\in H^{2}$ — its Fourier coefficients are those of $f$ shifted, and none of them is negative — so $P_{+}(zf)=zf$ and $T_{z}$ sends $e_{j}$ to $e_{j+1}$: the unilateral shift.
:::

:::

::: {.pf-step #brown-halmos}
$S^{*}T_{\varphi}S=T_{\varphi}$ for the shift $S=T_{z}$; and a bounded operator $T$ on $H^{2}$ is a Toeplitz operator if and only if $S^{*}TS=T$.

::: pf-proof
$S^{*}=T_{\bar z}$ by step [](#adjoint){.pf-ref}, so for $f\in H^{2}$,
$$
S^{*}T_{\varphi}Sf=P_{+}\big(\bar z\,\varphi\,zf\big)=P_{+}(\varphi f)=T_{\varphi}f,
$$
because $\abs{z}=1$ and $P_{+}$ is idempotent. That is the easy direction of the Brown--Halmos characterization; the converse, that $S^{*}TS=T$ forces $T=T_{\varphi}$ with $\varphi\in L^{\infty}$, is the theorem of Brown and Halmos and is quoted here rather than reproduced.
:::

:::

:::
:::
