---
schema: qual/card@1
id: P-VHDZL
kind: problem
title: The graph of a measurable function $\mathbb{R}\to\mathbb{R}$ has measure zero in $\mathbb{R}^2$
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: problem
Let $f$ be a measurable function on $\mathbb{R}$.
Show that the graph of $f$ has measure zero in $\mathbb{R}^{2}$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The graph $G = \{(x, f(x)) : x \in \RR\}$ is measurable in $\RR^2$.
    <2>1. The map $h(x,y) = f(x) - y$ is measurable on $\RR^2$.
        Proof: $(x,y) \mapsto f(x)$ is measurable (composition of the measurable $f$ with the continuous coordinate projection) and $(x,y) \mapsto y$ is continuous; their difference is measurable.
    <2>2. $G = \bigcap_{k=1}^\infty \{(x,y) : |f(x) - y| < 1/k\}$.
        Proof: $(x,y) \in G \iff y = f(x) \iff |f(x) - y| = 0$, and $|f(x) - y| = 0$ iff $|f(x) - y| < 1/k$ for all $k$.
    <2>3. Q.E.D.
        Proof: each set $\{|f(x) - y| < 1/k\}$ is measurable (preimage of the open interval under the measurable map $h$, or a countable union of measurable sets via rationals), so $G$ is a countable intersection of measurable sets.
:::
<1>2. The vertical section of $G$ at $x$ is $G_x = \{y \in \RR : (x,y) \in G\} = \{f(x)\}$, a singleton, so $m_1(G_x) = 0$ for every $x$.
    Proof: by definition of the graph, exactly one $y$ pairs with each $x$.

<1>3. $m_2(G) = 0$.
    Proof: Tonelli's theorem applied to $\chi_G$ (measurable by <1>1): $m_2(G) = \int_\RR m_1(G_x)\,dx = \int_\RR 0\,dx = 0$ by <1>2.
:::
