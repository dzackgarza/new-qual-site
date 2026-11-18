---
schema: qual/card@1
id: P-WTIIM
kind: problem
title: Structure theorem for simple rings
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Rings
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks to
    state the theorem, not to prove it, so no pf block was added; a structured proof
    here would answer a question the card does not ask. What was checked: the
    statement as given — R is simple Artinian iff R = M_n(D) for some n >= 1 and some
    division ring D — is the standard form of the simple case of Artin-Wedderburn,
    and the two definitions it uses (simple: no two-sided ideals other than 0 and R;
    Artinian: descending chains of left ideals terminate) are the standard ones.
    The proof sketch already on the card was also read against a fresh derivation and
    is correct, including the two steps easiest to get wrong: that a nonzero
    two-sided ideal of M_n(D) contains a matrix unit E_ij = a_kl^{-1} E_ik A E_lj and
    hence everything, and that taking endomorphism rings of _R R = L^n gives
    R^op = M_n(End_R(L)) = M_n(D^op), which transposes to R = M_n(D) since
    M_n(E)^op = M_n(E^op). What was not checked: no source solution is retained for
    this card, so no source comparison was made, and the theorem itself is not
    proved by a certificate here, the card asking only for its statement.
---

::: {.problem}
State the structure theorem for simple Artinian rings.
:::

::: {.solution}

The argument is the card's own, the standard proof of the simple case of Artin--Wedderburn, with each step justified; no retained set supplies it, and the sets searched are recorded in the audit trail.

A ring $R$ is **simple** when it has exactly two two-sided ideals, $0$ and $R$, and **left Artinian** when every descending chain of left ideals stabilises; modules are unital left modules.

::: pf

::: {.pf-step #matrix}
For every $n\ge1$ and division ring $D$, the ring $M_{n}(D)$ is simple and left and right Artinian.

::: pf-proof
Its left ideals are the $D$-subspaces of the left $D$-module $M_{n}(D)\cong D^{n^{2}}$, which is finite dimensional over the division ring $D$, so every descending chain of left ideals is a descending chain of subspaces of a finite-dimensional space and stabilises; the same holds on the right. For simplicity, let $I\ne0$ be a two-sided ideal and pick $0\ne A=(a_{kl})\in I$ with $a_{kl}\ne0$; the matrix units satisfy $E_{ik}AE_{lj}=a_{kl}E_{ij}$, so $E_{ij}=a_{kl}^{-1}E_{ik}AE_{lj}\in I$ for all $i,j$, and the $E_{ij}$ span $M_{n}(D)$. So $I=M_{n}(D)$.
:::

:::

::: {.pf-step #division}
If $R$ is simple left Artinian and $L\le R$ is a minimal nonzero left ideal, then $D=\End_{R}(L)^{\mathrm{op}}$ is a division ring.

::: pf-proof
$L$ is simple as a module, so every nonzero $R$-endomorphism of $L$ is injective (its kernel is a submodule different from $L$) and surjective (its image is a nonzero submodule), hence an automorphism; so $\End_{R}(L)$ is a division ring, and its opposite is one as well.
:::

:::

::: {.pf-step #sum}
$LR=\sum_{a\in R}La$ equals $R$, and each $La$ is $0$ or isomorphic to $L$.

::: pf-proof
$LR$ is a two-sided ideal: it is a left ideal, and $L R\cdot r=L R$ for $r\in R$. It is nonzero because $L\ne0$ and $R$ has a unit, so $LR=R$ by simplicity. For fixed $a\in R$ the map $x\mapsto xa$ is a homomorphism of left modules with domain $L$; its kernel is a submodule of the simple module $L$, so it is $0$ or $L$, and correspondingly the image $La$ is isomorphic to $L$ or is $0$.
:::

:::

::: {.pf-step #finite}
${}_{R}R\cong L^{\oplus n}$ for some $n\ge1$.

::: pf-proof
Steps [](#sum){.pf-ref} give $R=\sum_{a}La$ with each $La$ simple. A sum of simple submodules is semisimple, and a semisimple module is the direct sum of some subfamily of any generating family of simple submodules, so ${}_{R}R$ is a direct sum of copies of $L$. Since $1\in R$ lies in the sum, it lies in a finite subsum: $1=\sum_{t=1}^{n}x_{t}$ with $x_{t}\in L a_{t}$, and then every $r=1\cdot r=\sum x_{t}r$ lies in $La_{1}+\cdots+La_{n}$. So finitely many summands suffice and ${}_{R}R\cong L^{\oplus n}$.
:::

:::

::: {.pf-step #endomorphism}
$R\cong M_{n}(D)$.

::: pf-proof
Taking endomorphism rings of the isomorphism ${}_{R}R\cong L^{\oplus n}$ of step [](#finite){.pf-ref} gives $\End_{R}(R)\cong\End_{R}(L^{\oplus n})\cong M_{n}\big(\End_{R}(L)\big)$, the last because a homomorphism $L^{\oplus n}\to L^{\oplus n}$ is an $n\times n$ matrix of homomorphisms $L\to L$. And $\End_{R}(R)\cong R^{\mathrm{op}}$ via $r\mapsto(x\mapsto xr)$, with inverse $\varphi\mapsto\varphi(1)$. So $R^{\mathrm{op}}\cong M_{n}\big(\End_{R}(L)\big)$, and taking opposites, which reverses the order of multiplication in each matrix entry, gives
$$
\boxed{R\cong M_{n}(D)},\qquad D=\End_{R}(L)^{\mathrm{op}},
$$
a division ring by step [](#division){.pf-ref}.
:::

:::

:::
:::
