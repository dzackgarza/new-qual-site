---
schema: qual/card@1
id: E-HAT-4.H-2
kind: exercise
title: "Cofibrations are preserved by pushout"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Consider a pushout diagram where $B$ is $B$ with $X$ attached along $A$ via $f$.
Show that if $A \hookrightarrow X$ is a cofibration, so is $B \hookrightarrow B \sqcup_f X$.

::: solution
**Goal:** Prove that $j:B\hookrightarrow P:=B\sqcup_f X$ is a cofibration.

<1> Use the homotopy extension property.
    *Proof:*
    <2>1. Let $i:A\hookrightarrow X$ be a cofibration and $p:A\to B$ the attaching map.
    <2>2. To test $j$, take any space $Y$, map $u:P\to Y$, and homotopy
        $H:B\times I\to Y$ with $H(\cdot,0)=u\circ j$.
    <2>3. Set $u_X=u\circ q$ for the quotient map $q:X\to P$.
    <2>4. The boundary data on $A$ is
        $$
        h_0=H\circ(p\times\id_I):A\times I\to Y.
        $$
        Since $H$ is a homotopy starting at $u\circ j$, we have
        $h_0(a,0)=u_X(i(a))$.

<1> Extend over $X\times I$.
    *Proof:*
    <2>1. Because $i$ is a cofibration, $u_X$ and $h_0$ extend to
        $H_X:X\times I\to Y$ with
        $H_X(\cdot,0)=u_X$ and $H_X(i(a),t)=h_0(a,t)$.
    <2>2. On $A\times I$, we have $H_X\circ(i\times\id)=H\circ(p\times\id)$, so pasting is compatible.

<1> Paste homotopies on the pushout.
    *Proof:*
    <2>1. Define
        $$
        \widetilde H(p',t)=
        \begin{cases}
        H(b,t), & p'=b\in B,\\
        H_X(x,t),& p'=q(x)\in X.
        \end{cases}
        $$
    <2>2. The compatibility on $A$ makes this a well-defined map $\widetilde H:P\times I\to Y$.
    <2>3. $\widetilde H(\cdot,0)=u$, and $\widetilde H$ extends $H$.

<1> Therefore $j$ has the homotopy extension property and is a cofibration.

Authored by **Codex 5.3 Spark Extra High**.
:::

::: {.solution}
<1>1. $G$ group.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
