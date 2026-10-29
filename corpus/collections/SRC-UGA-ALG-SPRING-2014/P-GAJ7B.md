---
schema: qual/card@1
id: P-GAJ7B
kind: problem
title: Structure of a Sylow $3$-subgroup of $S_9$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Permutations
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G\subset S_9$ be a Sylow-3 subgroup of the symmetric group on 9 letters.

a. Show that $G$ contains a subgroup $H$ isomorphic to $\ZZ_3 \cross \ZZ_3 \cross \ZZ_3$ by exhibiting an appropriate set of cycles.

b. Show that $H$ is normal in $G$.

c. Give generators and relations for $G$ as an abstract group, such that all generators have order 3. Also exhibit elements of $S_9$ in cycle notation corresponding to these generators.

d. Without appealing to the previous parts of the problem, show that $G$ contains an element of order 9.
:::

::: {.solution}

Write $a=(123)$, $b=(456)$, $c=(789)$, and $d=(147)(258)(369)$. By Sylow conjugacy it suffices to construct the asserted structure in the subgroup they generate.

::: pf

::: {.pf-step #s1-1}

The subgroup $H=\langle a,b,c\rangle$ is isomorphic to $C_3^3$.


::: pf-proof

The three displayed $3$-cycles have disjoint supports, hence commute, have order three, and have independent powers. Therefore $H$ is their internal direct product, of order $27$.

:::

:::

::: {.pf-step #s1-2}

The subgroup $H$ is normal in the Sylow $3$-subgroup $G_0=\langle a,b,c,d\rangle$.


::: pf-proof

Conjugation by $d$ cyclically permutes $a,b,c$: $dad^{-1}=b$, $dbd^{-1}=c$, and $dcd^{-1}=a$. Thus $d$ normalizes $H$, and so do the elements of $H$. Since $d$ has order three and $d\notin H$, the semidirect product $G_0=H\rtimes\langle d\rangle$ has order $81$. Legendre's formula gives $v_3(9!)=\lfloor9/3\rfloor+\lfloor9/9\rfloor=4$, so $G_0$ is Sylow. All other Sylow $3$-subgroups are conjugate to $G_0$, carrying $H$ to a normal subgroup with the same structure.

:::

:::

::: {.pf-step #s1-3}

The group $G$ has a presentation, with all generators of order three,
$$
\boxed{\begin{aligned}
\langle a,b,c,d\mid\;&a^3=b^3=c^3=d^3=1,\\
&[a,b]=[a,c]=[b,c]=1,\\
&dad^{-1}=b,\ dbd^{-1}=c,\ dcd^{-1}=a\rangle.
\end{aligned}}
$$


::: pf-proof

The permutations $a,b,c,d$ satisfy the displayed relations. Conversely, these relations move every word into $a^ib^jc^kd^\ell$ with $0\leq i,j,k,\ell<3$, so the presented group has at most $3^4=81$ elements. The corresponding subgroup $G_0$ has exactly $81$ elements by step [](#s1-2){.pf-ref}, so the presentation describes $G_0$ and therefore any Sylow $3$-subgroup up to isomorphism.

:::

:::

::: {.pf-step #s1-4}

The Sylow $3$-subgroup $G$ contains an element of order nine, independently of steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.


::: pf-proof

The cycle $(1\,2\,3\,4\,5\,6\,7\,8\,9)$ has order nine, so its cyclic subgroup is contained in a Sylow $3$-subgroup $P$ of $S_9$. By Sylow conjugacy, $P$ is conjugate to $G$. The conjugate of this $9$-cycle belongs to $G$ and retains order nine.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish parts (a)--(d), respectively.

:::

:::

:::
