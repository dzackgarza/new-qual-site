---
schema: qual/card@1
id: P-HGRO31
kind: problem
title: Sylow theorems
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The exercise asks for a statement, so the card is structured as a decomposition of the
    three theorems with the definition they rest on, and the two consequences the statement
    claims are now proved rather than appended: that n_p = [G : N_G(P)] for a Sylow
    p-subgroup P, hence n_p divides m and n_p = 1 exactly when P is normal. Proved from the
    transitivity of conjugation on the set of Sylow subgroups and orbit-stabiliser, using the
    stated parts and nothing further; the three Sylow theorems themselves are statements here,
    not proved, since the exercise asks for exactly that. The statement was checked against the
    collection's provenance, assets/attachments/MGSA_Group_Theory_Oral_Questions.pdf, whose
    preserved extraction records the question as "state the Sylow theorems". No statement
    repair; the card's phrase "one conjugacy class" is what the conjugacy clause says.
---

::: {.problem}
State the Sylow theorems.
:::

::: {.solution}
The exercise asks for statements rather than proofs, so what follows separates the definition, the three theorems, and the two consequences the statement draws — and proves the consequences from the theorems, since those are deductions and not part of what is being stated.

Throughout, $G$ is a finite group, $p$ is a prime, $\abs G=p^{n}m$ with $p\nmid m$, and a $p$-subgroup of $G$ is a subgroup whose order is a power of $p$.

::: pf

::: {.pf-step #definition}
A Sylow $p$-subgroup of $G$ is a subgroup of order $p^{n}$, the largest power of $p$ dividing $\abs G$.

::: pf-proof
Writing $\abs G=p^{n}m$ with $p\nmid m$ fixes $n=v_{p}(\abs G)$, and by Lagrange's theorem a subgroup of order $p^{k}$ has $p^{k}\mid p^{n}m$, which forces $k\le n$. So $p^{n}$ is the largest order of a $p$-subgroup allowed by the group's order, and a $p$-subgroup of that order — a subgroup of order $p^{n}$ — is by definition a Sylow $p$-subgroup. We write $\operatorname{Syl}_{p}(G)$ for the set of them and $n_{p}=\abs{\operatorname{Syl}_{p}(G)}$.
:::

:::

::: {.pf-step #existence}
(First Sylow theorem) $G$ has a Sylow $p$-subgroup; more generally, if $p^{k}$ divides $\abs G$ then $G$ has a subgroup of order $p^{k}$.

::: pf-proof
This is the existence clause of the theorem as stated, with the standard refinement that the dividing powers $p^{k}$ of $\abs G$ are all realised by subgroups. In particular $k=n$ gives a subgroup of order $p^{n}$, that is a Sylow $p$-subgroup, so $\operatorname{Syl}_{p}(G)\neq\emptyset$ and $n_{p}\ge1$.
:::

:::

::: {.pf-step #conjugacy}
(Second Sylow theorem) Every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup, and any two Sylow $p$-subgroups are conjugate in $G$; hence $\operatorname{Syl}_{p}(G)$ is a single conjugacy class.

::: pf-proof
This is the second theorem as stated. The final clause is a restatement and not a new assertion: conjugacy of any two members says that the action of $G$ on $\operatorname{Syl}_{p}(G)$ by $g\cdot P=gPg^{-1}$ is transitive, and a transitive action has a single orbit, which is what "one conjugacy class" means.
:::

:::

::: {.pf-step #number}
(Third Sylow theorem) $n_{p}\equiv1\pmod p$ and $n_{p}\mid m$.

::: pf-proof
This is the third theorem as stated, in the notation of step [](#definition){.pf-ref}: the congruence constrains the count modulo $p$ and the divisibility constrains it against the $p'$-part $m$ of $\abs G$.
:::

:::

::: {.pf-step #index}
$n_{p}=[G:N_{G}(P)]$ for every $P\in\operatorname{Syl}_{p}(G)$, so $n_{p}\mid m$; and $n_{p}=1$ if and only if the Sylow $p$-subgroup is normal.

::: pf-proof
Conjugation gives an action of $G$ on $\operatorname{Syl}_{p}(G)$, transitive by step [](#conjugacy){.pf-ref}. The stabiliser of $P$ under this action is $\{g : gPg^{-1}=P\}=N_{G}(P)$, so by orbit-stabiliser $\abs{\operatorname{Syl}_{p}(G)}=\abs{G}/\abs{N_{G}(P)}=[G:N_{G}(P)]$. Since $\abs G=p^{n}m$, this index divides $p^{n}m$; and $n_{p}\equiv1\pmod p$ from step [](#number){.pf-ref} makes $n_{p}$ coprime to $p$, so the $p$-part $p^{n}$ of the index cannot occur and $n_{p}\mid m$. Finally $n_{p}=1$ means $\operatorname{Syl}_{p}(G)=\{P\}$, which under conjugation says $gPg^{-1}=P$ for all $g$, that is $P\trianglelefteq G$; conversely if $P$ is normal then $gPg^{-1}=P$ for all $g$ and transitivity forces $\operatorname{Syl}_{p}(G)=\{P\}$.
:::

:::

::: {.pf-step #statement}
The Sylow theorems: $G$ has a Sylow $p$-subgroup; every $p$-subgroup lies in one and any two are conjugate; and $n_{p}\equiv1\pmod p$ with $n_{p}\mid m$.

::: pf-proof
Steps [](#existence){.pf-ref}, [](#conjugacy){.pf-ref} and [](#number){.pf-ref} are the three theorems, stated for the finite group $G$, the prime $p$ and the factorisation $\abs G=p^{n}m$ with $p\nmid m$ fixed in step [](#definition){.pf-ref}; step [](#index){.pf-ref} draws the two consequences that the statement of the count carries, with their proofs. That is the complete statement the exercise asks for.
:::

:::

:::
:::
