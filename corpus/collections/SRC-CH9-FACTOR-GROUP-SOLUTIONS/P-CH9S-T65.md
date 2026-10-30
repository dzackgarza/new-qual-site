---
schema: qual/card@1
id: P-CH9S-T65
kind: problem
title: $\operatorname{Aut}(G)$ is not cyclic for non-abelian $G$
classification:
  areas:
    - algebra
  topics:
    - Normal Subgroups and Factor Groups
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: '2026-09-14'
    note: Checked against Team Problem Solutions for Ch 9, problem 65, in the deterministic MinerU Flash extraction assets/attachments/Ch9Sltns_extracted.md.
---

::: {.problem}
If $G$ is non-Abelian, show that $\Aut(G)$ is not cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $\operatorname{Aut}(G)$ were cyclic, then $\operatorname{Inn}(G)$ would be cyclic.


::: pf-proof

Every inner automorphism is an automorphism, so
$$
\operatorname{Inn}(G)\leq\operatorname{Aut}(G).
$$
Every subgroup of a cyclic group is cyclic. Hence cyclicity of
$\operatorname{Aut}(G)$ would imply cyclicity of $\operatorname{Inn}(G)$.

:::

:::

::: {.pf-step #s1-2}

There is an isomorphism
$$
G/Z(G)\cong\operatorname{Inn}(G).
$$


::: pf-proof

Define
$$
c:G\longrightarrow\operatorname{Inn}(G),
\qquad
c(g)(x)=gxg^{-1}.
$$
The map $c$ is a homomorphism and is surjective by the definition of
inner automorphisms. Moreover, $c(g)$ is the identity automorphism
exactly when $g$ commutes with every element of $G$, so
$$
\ker c=Z(G).
$$
The first isomorphism theorem therefore gives
$G/Z(G)\cong\operatorname{Inn}(G)$.

:::

:::

::: {.pf-step #s1-3}

If $G/Z(G)$ is cyclic, then $G$ is Abelian.


::: pf-proof

Suppose
$$
G/Z(G)=\langle gZ(G)\rangle.
$$
For arbitrary $x,y\in G$, there are integers $m,n$ and central
elements $z_1,z_2\in Z(G)$ such that
$$
x=g^mz_1,
\qquad
y=g^nz_2.
$$
Therefore
$$
xy=g^{m+n}z_1z_2=g^{n+m}z_2z_1=yx.
$$
Thus all elements of $G$ commute, so $G$ is Abelian.

:::

:::

::: {.pf-step #s1-4}

The group $\operatorname{Aut}(G)$ is not cyclic.


::: pf-proof

Suppose for contradiction that $\operatorname{Aut}(G)$ is cyclic.
By step [](#s1-1){.pf-ref}, $\operatorname{Inn}(G)$ is cyclic. By step [](#s1-2){.pf-ref},
$G/Z(G)$ is therefore cyclic, and step [](#s1-3){.pf-ref} then makes $G$ Abelian.
This contradicts the hypothesis that $G$ is non-Abelian. Hence
$\operatorname{Aut}(G)$ cannot be cyclic.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
