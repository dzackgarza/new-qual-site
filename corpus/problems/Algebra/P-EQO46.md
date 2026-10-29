---
schema: qual/card@1
id: P-EQO46
kind: problem
title: Groups of order 12, and two nonisomorphic subgroups of the same order
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
(a) What are all the groups of order 12 up to isomorphism?

(b) Can a group of order 12 have two non-isomorphic subgroups of the same order?
:::

::: {.solution}
Write $D_{12}=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle$ for the dihedral group of order $12$ and $\operatorname{Dic}_3=\langle a,b\mid a^6=1,\ b^2=a^3,\ bab^{-1}=a^{-1}\rangle$.

::: pf

::: pf-step
(a) The groups of order $12$ up to isomorphism are $\boxed{C_{12},\ C_6\times C_2,\ A_4,\ D_{12},\ \operatorname{Dic}_3}$.

::: pf-proof

::: {.pf-step #sylow}
Let $G$ have order $12=2^2\cdot3$. Then $n_3\in\{1,4\}$ and $n_2\in\{1,3\}$.

::: pf-proof
By the Sylow theorems, $n_3\equiv1\pmod 3$ and $n_3\mid4$, and $n_2$ is odd and divides $3$.
:::

:::

::: {.pf-step #a4}
If $n_3=4$, then $G\cong A_4$.

::: pf-proof
Conjugation on the four Sylow $3$-subgroups gives a homomorphism $G\to S_4$.
Since $[G:N_G(Q)]=n_3=4$ for each Sylow $3$-subgroup $Q$, $\abs{N_G(Q)}=3$ and $N_G(Q)=Q$; the kernel is the intersection of these normalizers, hence of the four Sylow $3$-subgroups.
Distinct subgroups of prime order intersect trivially, so the kernel is trivial and $G$ embeds in $S_4$ as a subgroup of order $12$.
The only subgroup of order $12$ in $S_4$ is $A_4$, since a subgroup of index $2$ contains all squares, hence all $3$-cycles, which generate $A_4$.
:::

:::

::: {.pf-step #semidirect}
If $n_3=1$, then $G\cong C_3\rtimes P$ with $P\cong C_4$ or $P\cong V_4$, and $G$ is one of $C_{12}$, $\operatorname{Dic}_3$, $C_6\times C_2$, $D_{12}$.

::: pf-proof
The Sylow $3$-subgroup $Q\cong C_3$ is normal, and a Sylow $2$-subgroup $P$ meets it trivially and has order $4$, so $G\cong Q\rtimes P$.
Since $\Aut(C_3)\cong C_2$, the action is trivial or acts through a quotient of $P$ of order $2$ by inversion.
For $P=C_4$ there is one nontrivial action, and the two actions give $C_{12}$ and $\operatorname{Dic}_3$.
For $P=V_4$ the three nontrivial actions differ by automorphisms of $V_4$, so they give isomorphic groups, and the two cases give $C_6\times C_2$ and $D_{12}\cong C_2\times S_3$.
:::

:::

::: pf-qed
By step [](#sylow){.pf-ref}, either $n_3=4$ or $n_3=1$, and steps [](#a4){.pf-ref} and [](#semidirect){.pf-ref} list the groups in each case.
The five groups are pairwise nonisomorphic: $C_{12}$ and $C_6\times C_2$ are the abelian ones, distinguished by an element of order $12$; $A_4$ has no element of order $6$; and $\operatorname{Dic}_3$ has a unique element of order $2$, while $D_{12}$ has seven.
:::

:::

:::

::: pf-step
(b) $\boxed{\text{Yes}}$: in $D_{12}$, the subgroups $\langle r\rangle\cong C_6$ and $\langle r^2,s\rangle\cong S_3$ both have order $6$ and are not isomorphic.

::: pf-proof
$\langle r\rangle$ is cyclic of order $6$.
$\langle r^2,s\rangle$ has order $6$, since $r^2$ has order $3$ and $s$ inverts it, so it is nonabelian and isomorphic to $S_3$.
One subgroup is abelian and the other is not.
:::

:::

:::

:::
