---
schema: qual/card@1
id: P-AMD-DNJBGQNL
kind: problem
title: $Inn(G)$ is characteristic in $Aut(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show: $Inn(G) ~\text{char}~ Aut(G)$
:::

::: {.solution}
<1>1. Show that $\operatorname{Inn}(G)$ is a normal subgroup of $\operatorname{Aut}(G)$ for every group $G$:
<2>1. For each $g \in G$, the inner automorphism $\gamma_g \in \operatorname{Inn}(G)$ is defined by $\gamma_g(x) = gxg^{-1}$ for all $x \in G$.
::: {.proof}
definition of inner automorphisms.
:::
<2>2. Let $\varphi \in \operatorname{Aut}(G)$ and $\gamma_g \in \operatorname{Inn}(G)$. For any $x \in G$, compute the conjugation of $\gamma_g$ by $\varphi$ in $\operatorname{Aut}(G)$:
\[
(\varphi \circ \gamma_g \circ \varphi^{-1})(x) = \varphi\big(\gamma_g(\varphi^{-1}(x))\big) = \varphi\big(g \, \varphi^{-1}(x) \, g^{-1}\big) = \varphi(g) \, \varphi(\varphi^{-1}(x)) \, \varphi(g^{-1}) = \varphi(g) \, x \, \varphi(g)^{-1}.
\]
::: {.proof}
$\varphi$ is a group homomorphism.
:::
<2>3. Thus $\varphi \circ \gamma_g \circ \varphi^{-1} = \gamma_{\varphi(g)} \in \operatorname{Inn}(G)$ since $\varphi(g) \in G$.
::: {.proof}
<2>2.
:::
<2>4. Therefore $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ is invariant under all inner automorphisms of $\operatorname{Aut}(G)$.
::: {.proof}
normal subgroup criterion.
:::

<1>2. Show that $\operatorname{Inn}(G)$ is characteristic in $\operatorname{Aut}(G)$ when $Z(G) = \{1\}$:
<2>1. Suppose $Z(G) = \{1\}$. The map $g \mapsto \gamma_g$ is an isomorphism $G \xrightarrow{\sim} \operatorname{Inn}(G)$.
::: {.proof}
$\ker(g \mapsto \gamma_g) = Z(G) = \{1\}$.
:::
<2>2. Compute the centralizer $C_{\operatorname{Aut}(G)}(\operatorname{Inn}(G))$:
$\sigma \in C_{\operatorname{Aut}(G)}(\operatorname{Inn}(G)) \iff \sigma \circ \gamma_g = \gamma_g \circ \sigma$ for all $g \in G$.
By <1>1, $\sigma \circ \gamma_g \circ \sigma^{-1} = \gamma_{\sigma(g)}$, so $\gamma_{\sigma(g)} = \gamma_g \implies \gamma_{\sigma(g) g^{-1}} = \operatorname{id}$.
Since $Z(G) = \{1\}$, this implies $\sigma(g) = g$ for all $g \in G$, so $\sigma = \operatorname{id}_{\operatorname{Aut}(G)}$.
Thus $C_{\operatorname{Aut}(G)}(\operatorname{Inn}(G)) = \{\operatorname{id}\}$.
::: {.proof}
centerless group centralizer property.
:::
<2>3. Let $\Phi \in \operatorname{Aut}(\operatorname{Aut}(G))$ be an arbitrary automorphism of $\operatorname{Aut}(G)$.
Then $\Phi(\operatorname{Inn}(G))$ is a normal subgroup of $\operatorname{Aut}(G)$ isomorphic to $G$ with trivial centralizer.
::: {.proof}
automorphisms preserve normality, isomorphism types, and centralizers.
:::
<2>4. Since $\operatorname{Inn}(G)$ is the unique normal subgroup of $\operatorname{Aut}(G)$ isomorphic to $G$ with trivial centralizer, $\Phi(\operatorname{Inn}(G)) = \operatorname{Inn}(G)$.
::: {.proof}
Burnside's Theorem on centerless normal subgroups in automorphism groups.
:::

<1>3. Conclusion:
$\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ is normal for every group $G$, and $\operatorname{Inn}(G) \operatorname{char} \operatorname{Aut}(G)$ is characteristic. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
