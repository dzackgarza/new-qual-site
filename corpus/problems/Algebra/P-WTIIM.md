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
The simple case of the Artin--Wedderburn theorem says:

> A ring $R$ is simple Artinian if and only if
> $$
> R\cong M_n(D)
> $$
> for some integer $n\ge1$ and some division ring $D$.

Here "simple" means that $R$ has no two-sided ideals other than $0$ and $R$, and "Artinian" means that descending chains of left ideals terminate.

The matrix ring $M_n(D)$ is simple Artinian. It is left and right Artinian because its left and right ideals are $D$-subspaces of the finite-dimensional $D$-vector space $M_n(D)$. A nonzero two-sided ideal contains a matrix $A$ with some entry $a_{kl}\ne0$, and then $E_{ij}=a_{kl}^{-1}E_{ik}AE_{lj}$ lies in the ideal for all $i,j$, so the ideal is all of $M_n(D)$.

For the forward direction, the Artinian hypothesis gives a minimal nonzero left ideal $L$. Schur's lemma implies that
$$
D=\Endo_R(L)^{\mathrm{op}}
$$
is a division ring. The sum $LR=\sum_{a\in R}La$ is a nonzero two-sided ideal, so $LR=R$ by simplicity. Each $La$ is the image of $L$ under $x\mapsto xa$, so it is $0$ or isomorphic to $L$. Hence the regular left module $R$ is a sum of simple submodules isomorphic to $L$, and therefore a direct sum of some of them; since $1$ lies in a finite subsum, finitely many suffice:
$$
{}_R R\cong L^{\oplus n}.
$$
Taking endomorphism rings gives
$$
R^{\mathrm{op}}\cong\Endo_R(R)
\cong M_n(\Endo_R(L)),
$$
and transposing gives
$$
R\cong M_n(D).
$$
:::
