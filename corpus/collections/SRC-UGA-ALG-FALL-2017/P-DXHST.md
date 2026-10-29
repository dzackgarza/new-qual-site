---
schema: qual/card@1
id: P-DXHST
kind: problem
title: 'Faithful transitive actions: trivial core of a stabilizer, and abelian transitive
  subgroups of $S_n$'
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---
::: {.problem}
Suppose the group $G$ acts on the non-empty set $A$.
Assume this action is **faithful** ($\ker(G \to \operatorname{Sym}(A)) = \{1\}$) and **transitive** (for all $a, b \in A$, there exists $g \in G$ such that $g \cdot a = b$).

(a) For $a \in A$, let $G_a = \operatorname{Stab}_G(a)$ denote the stabilizer of $a$. Prove that:
$$
\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \{1\}.
$$

(b) Suppose that $G$ is **abelian**. Prove that $|G| = |A|$, and deduce that every abelian transitive subgroup of the symmetric group $S_n$ has order exactly $n$.
:::

::: {.solution}
Let $\rho:G\to\operatorname{Sym}(A)$ denote the action homomorphism and fix $a\in A$.

::: pf

::: {.pf-step #s1}

The kernel of $\rho$ is the normal core of $G_a$:
$$
\ker\rho=\bigcap_{\sigma\in G}\sigma G_a\sigma^{-1}.
$$

::: pf-proof

By definition, $\ker\rho=\bigcap_{b\in A}G_b$. Transitivity supplies, for every $b\in A$, an element $\sigma\in G$ with $b=\sigma a$. The stabilizer identity $G_{\sigma a}=\sigma G_a\sigma^{-1}$ follows because $g(\sigma a)=\sigma a$ exactly when $\sigma^{-1}g\sigma$ fixes $a$. Substitution into the intersection proves the identity.

:::

:::

::: {.pf-step #s2}

The intersection in part (a) is trivial.

::: pf-proof

Faithfulness means $\ker\rho=\{1\}$. Apply step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

If $G$ is abelian, then the orbit map
$$
\theta:G\longrightarrow A,\qquad g\longmapsto ga
$$
is a bijection.

::: pf-proof

Every subgroup of an abelian group is normal, so every conjugate of $G_a$ equals $G_a$. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $G_a=\{1\}$. Transitivity makes $\theta$ surjective. If $\theta(g)=\theta(h)$, then $h^{-1}g\in G_a=\{1\}$, and hence $g=h$. Thus $\theta$ is injective.

:::

:::

::: {.pf-step #s4}

The conclusions of part (b) are
$$
\boxed{|G|=|A|,\qquad\text{and every abelian transitive subgroup of }S_n\text{ has order }n.}
$$

::: pf-proof

Step [](#s3){.pf-ref} gives a bijection $G\cong A$, so their cardinalities agree, including when $G$ and $A$ are infinite. For an abelian transitive subgroup $H\leq S_n$, its natural action on $\{1,\ldots,n\}$ is faithful because the homomorphism $H\hookrightarrow S_n$ is injective. The same argument gives $|H|=n$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), and step [](#s4){.pf-ref} proves part (b).

:::

:::

:::
