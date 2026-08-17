---
schema: qual/card@1
id: P-4XOCE
kind: problem
title: "Let $H \\normal G$ be a normal subgroup of a finite group $G$, where the\u2026"
classification:
  areas:
  - algebra
  topics:
  - centralizers-and-normalizers
  - normal-subgroups
  - conjugacy
relations: []
review: draft
solved: false
---
Let $H \normal G$ be a normal subgroup of a finite group $G$, where the order of $H$ is the smallest prime $p$ dividing $\abs{G}$.
Prove that $H$ is contained in the center of $G$.

> Solution due to Swaroop Hegde, typed up + modifications added by DZG.

:::{.concept}
\envlist

- $x\in Z(G)$ iff $\size C_x = 1$, i.e. the size of its conjugacy class is one.
- Normal subgroups are disjoint unions of (some) conjugacy classes in $G$.
  - In fact, this is a characterization of normal subgroups (i.e. $H$ is normal iff $H$ is a union of conjugacy classes in $G$).
  - Why: if $H\normal G$ then $ghg\inv \in H$ for all $g$, so $C_h \subseteq H$ and $\Union_h C_h = H$.
  Conversely, if $H = \Union_{h\in H} C_h$, then $ghg\inv \in C_h \subseteq H$ and thus $gHg\inv = H$.
- Orbit stabilizer theorem: $\size C_g = \size G/ \size K_g$ where $C_g$ is the centralizer and $K_g$ is the conjugacy class of $g$.
  - In particular, $\size C_g$ divides $\size G$.
:::


:::{.strategy}
Show an element $x$ is central by showing $\size C_x = 1$.
:::


:::{.proof title="?"}
\envlist

- Let $p \da \size H$.
- Let \( \ts{ C_i }_{i\leq n} \) be the conjugacy classes in $G$, then $G = \disjoint_{i\leq n} C_i$
- By the first fact, there is a sub-collection \( \ts{ C_{i_j}}_{j\leq k } \)  such that 
\[
H = \disjoint_{j\leq k} C_{i_j}
.\]
- The identity is always in a single conjugacy class, so $C_e = \ts{ e }$.
- Since $e\in H$, without loss of generality, label $C_{i_1} = \ts{ e }$.
- So
\[
H 
= \Disjoint_{j\leq k} C_{i_j} 
= C_{i_1}{\textstyle  \coprod} \displaystyle\Disjoint_{\substack{ j\leq k \\ j\neq 1} } C_{i_j} 
.\]

- Take cardinality in the above equation 
\[
p = 1 + \sum_{\substack{ j\leq k \\ j\neq 1 }} \size C_{i_j}
.\]
- So $\size C_{i_j} \leq p-1$ for all $j\neq 1$.

- Every $\size C_{i_j}$ divides $\size G$, but $p$ was the *minimal* prime dividing $\size G$, forcing $\size C_{i_j} = 1$ for all $j \neq 1$.
  - This rules out $\size C_{i_j}$ being a prime less than $p$, but also rules out composites: if a prime $q\divides \size C_{i_j}$, then $q<p$ and $q\divides \size G$, a contradiction.

- By fact 3, each $x\in C_{i_j}$ satisfies $x\in Z(G)$.

- $\union C_{i_j} = H$, so $H \subseteq Z(G)$.

:::
