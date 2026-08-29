---
schema: qual/card@1
id: P-UWZPY
kind: problem
title: Induced representations of $G$ from a subgroup $H$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $H$ be a subgroup of a finite group $G$, and let $(\rho, W)$ be a representation of $H$ over $\mathbb{C}$.
How is the induced representation $\operatorname{Ind}_H^G(W)$ defined? State its dimension, character formula (Frobenius formula), and Frobenius Reciprocity.
:::

::: solution
**Goal:** Define the induced representation $\operatorname{Ind}_H^G(W)$ via tensor products / functions, give its character formula, and state Frobenius Reciprocity.

<1>1. Definition via Tensor Products of Modules over Group Rings:
    *Proof:*
    <2>1. Let $\mathbb{C}[G]$ and $\mathbb{C}[H]$ be the complex group algebras of $G$ and $H$.
    <2>2. The representation $(\rho, W)$ makes $W$ a left $\mathbb{C}[H]$-module.
    <2>3. Since $\mathbb{C}[H] \subseteq \mathbb{C}[G]$, the group algebra $\mathbb{C}[G]$ is naturally a $(\mathbb{C}[G], \mathbb{C}[H])$-bimodule.
    <2>4. The **induced representation** $V = \operatorname{Ind}_H^G(W)$ is defined as the extension of scalars:
        $$V = \mathbb{C}[G] \otimes_{\mathbb{C}[H]} W.$$
    <2>5. The action of $g \in G$ on $V$ is given by left multiplication: $g \cdot (x \otimes w) = (gx) \otimes w$.

<1>2. Vector Space Decomposition and Dimension:
    *Proof:*
    <2>1. Let $\{g_1, g_2, \dots, g_m\}$ be a complete set of left coset representatives of $H$ in $G$, where $m = [G : H]$.
    <2>2. As a vector space over $\mathbb{C}$:
        $$V \cong \bigoplus_{i=1}^m g_i W = g_1 W \oplus g_2 W \oplus \cdots \oplus g_m W.$$
    <2>3. The dimension of the induced representation is:
        $$\dim(\operatorname{Ind}_H^G(W)) = [G : H] \cdot \dim(W).$$

<1>3. Induced Character Formula (Frobenius Character Formula):
    *Proof:*
    <2>1. Let $\chi_W: H \to \mathbb{C}$ be the character of $W$. Extend $\chi_W$ to all of $G$ by setting $\dot{\chi}_W(x) = \chi_W(x)$ if $x \in H$ and $\dot{\chi}_W(x) = 0$ if $x \notin H$.
    <2>2. The character $\chi_{\operatorname{Ind}_H^G(W)}$ of the induced representation evaluated at $g \in G$ is:
        $$\chi_{\operatorname{Ind}_H^G(W)}(g) = \frac{1}{|H|} \sum_{x \in G} \dot{\chi}_W(x^{-1} g x) = \sum_{\substack{i=1 \\ g_i^{-1} g g_i \in H}}^{[G:H]} \chi_W(g_i^{-1} g g_i).$$

<1>4. Frobenius Reciprocity Theorem (Adjunction):
    *Proof:*
    <2>1. Induction is the left adjoint to restriction $\operatorname{Res}_H^G$:
        $$\operatorname{Hom}_G(\operatorname{Ind}_H^G(W), U) \cong \operatorname{Hom}_H(W, \operatorname{Res}_H^G(U))$$
        for any representation $U$ of $G$.
    <2>2. In terms of characters and class function inner products:
        $$\langle \chi_{\operatorname{Ind}_H^G(W)}, \psi \rangle_G = \langle \chi_W, \operatorname{Res}_H^G(\psi) \rangle_H.$$

<1>5. Conclusion:
    $\operatorname{Ind}_H^G(W) = \mathbb{C}[G] \otimes_{\mathbb{C}[H]} W$ has dimension $[G:H]\dim(W)$, satisfies Frobenius Reciprocity, and has character $\chi(g) = \frac{1}{|H|}\sum_{x \in G} \dot{\chi}_W(x^{-1}gx)$. Q.E.D.
:::
