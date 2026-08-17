---
schema: qual/card@1
id: P-FSFMB
kind: problem
title: The commuting probability of a finite group is $c(G)/|G|$
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - class-equation
  - burnside-s-lemma
relations: []
review: draft
solved: true
---
For a finite group $G$, let $c(G)$ denote the number of conjugacy classes of $G$.

a.
Prove that if two elements of $G$ are chosen uniformly at random,then the probability they commute is precisely
$$
\frac{c(G)}{\abs G}
.$$

b.
State the class equation for a finite group.

c.
Using the class equation (or otherwise) show that the probability in part (a) is at most $$
\frac 1 2 + \frac 1 {2[G : Z(G)]}
.$$

> Here, as usual, $Z(G)$ denotes the center of $G$.

:::{.warnings}
(DZG) This is a slightly anomalous problem!
It's fun and worth doing, because it uses the major counting formulas.
Just note that the techniques used in this problem perhaps don't show up in other group theory problems.
:::

:::{.concept}
\envlist

- Notation: $X/G$ is the set of $G\dash$orbits
- Notation: $X^g = \theset{x\in X\suchthat g\cdot x = x}$
- Burnside's formula: $\#{X/G} = {1 \over \# G} \sum \# {X^g}$.
- Definition of conjugacy class: $C(g) = \ts{ hgh\inv \st h\in G }$.
:::

:::{.strategy}
Fixed points of the conjugation action are precisely commuting elements.
Apply Burnside.
Context clue: $1/[G:Z(G)]$ is weird, right? 
Use that $[G:Z(G)] = \# G/\# Z(G)$, so try to look for $\#Z(G)/\#(G)$ somewhere.
Count sizes of centralizers.
:::

:::{.solution}
\envlist

:::{.proof title="Part a"}
\envlist

- Define a sample space $\Omega = G \cross G$, so $\# {\Omega} = (\# {G})^2$.

- Identify the event we want to analyze: 
\[
A \definedas \theset{(g,h) \in G\cross G \suchthat [g,h] = 1} \subseteq \Omega
.\]
- Note that the slices are centralizers:
\[
A_g \definedas \theset{(g, h) \in \ts{ g } \cross G \suchthat [g, h] = 1} = Z(g) \implies A = \Disjoint_{g\in G} Z(g)
.\]

- Set $n$ be the number of conjugacy classes, note we want to show $P(A) = n / \abs{G}$.
 
- Let $G$ act on itself by conjugation, which partitions $G$ into conjugacy classes.

  - What are the orbits? 
  $$
  \mathcal{O}_g = \theset{hgh\inv \suchthat h\in G}
  ,$$ 
  which is the **conjugacy class** of $g$.
  In particular, the number of orbits is the number of conjugacy classes.

  - What are the fixed points? 
  $$X^g = \theset{h\in G \suchthat hgh\inv = g},$$ 
  which are the elements of $G$ that commute with $g$, which is isomorphic to $A_g$.

- Identifying centralizers with fixed points, 
  $$
  \#{A} = \#{\Disjoint_{g\in G} Z(g) } = \sum_{g\in G} \#{Z(g)} = \sum_{g\in G}\# {X^g}
  .$$

- Apply Burnside
$$
\# {X / G} = \frac { 1 } { \# G  } \sum _ { g \in G } \# X ^ { g } ,
$$
- Note $\#{X/G} = n$, i.e. the number of conjugacy classes is the number of orbits.
- Rearrange and use definition:
$$
n \cdot \#{G}
= \qty{\#{X/G} }\cdot \#{G}
= \sum _ { g \in G } \# X ^ { g } 
$$
- Compute probability:
\[
P(A)
= {\# A \over \# \Omega} 
= \Sum_{ g \in G } \frac{\# X ^ { g }}{ ( \# {G} )^2} 
= \frac{\qty{ \# {X/G}} \cdot \#{G}}{ (\#{G})^2} 
= \frac{n \cdot \#{G}}{( \#{G} )^2} 
= \frac n {\# G}
.\]

:::

:::{.proof title="Part b"}
Statement of the class equation:
\[
\abs G = Z(G) + \sum_{\substack{\text{One $x$ from each} \\ \text{conjugacy class}}}[G: Z(x)]
\]
where $Z(x) = \theset{g\in G \suchthat [g, x] = 1}$ is the centralizer of $x$ in $G$.
:::

:::{.proof title="Part c"}
\envlist

> (DZG): I couldn't convince myself that a previous proof using the class equation actually works.
> Instead, I'll borrow the proof from [this note](https://math.berkeley.edu/~tb65536/Commuting_Probability.pdf)

- Write the event as $A = \Disjoint_{g\in G} \ts{g} \cross Z(g)$, then
\[
P(A) 
= {\# A\over (\# G)^2} 
= {1\over (\# G)^2} \sum_{g\in G} \# Z(g)
.\]
- Attempt to estimate the sum: pull out central elements $g\in Z(G)$.
  - Note $Z(g) = G$ for central $g$, so $\# Z(g) = \# G$
  - Note 
  \[
  g\not\in Z(G)\implies \# Z(g) \leq {1\over 2} \# G
  ,\]
  since $Z(g) \leq G$ is a subgroup, and 
  \[
  [G:Z(g)] \neq 1 \implies [G: Z(g)] \geq 2
  .\]
- Use these facts to calculate:
\[
P(A) 
&= {1\over (\# G)^2 } \qty{ \sum_{g\in Z(g)} \# Z(g) + \sum_{g\not\in Z(g)} \# Z(g) } \\
&= {1\over (\# G)^2 } \qty{ \sum_{g\in Z(g)} \# G + \sum_{g\not\in Z(g)} \# Z(g) } \\
&= {1\over (\# G)^2 } \qty{ \# Z(G) \cdot \# G + \sum_{g\not\in Z(g)} \# Z(g) } \\
&\leq {1\over (\# G)^2 } \qty{ \# Z(G) \cdot \# G + \sum_{g\not\in Z(g)} {1\over 2} \# G } \\
&= {1\over (\# G)^2 } \qty{ \# Z(G) \cdot \# G + \qty{ \sum_{g\not\in Z(g)} {1\over 2} } \cdot \# G } \\
&= {1\over (\# G) } \qty{ \# Z(G) + \sum_{g\not\in Z(g)} {1\over 2} } \\
&= {1\over (\# G) } \qty{ \# Z(G) + {1\over 2} \sum_{g\not\in Z(g)} 1 } \\
&= {1\over (\# G) } \qty{ \# Z(G) + {1\over 2} \#(G \sm Z(G) ) } \\
&= {1\over (\# G) } \qty{ \# Z(G) + {1\over 2} \#G - {1\over 2} \# Z(G) } \\
&= {1\over (\# G) } \qty{ {1\over 2} \# Z(G) + {1\over 2} \#G  } \\
&= {1\over 2} \qty{1 + { \# Z(G) \over \# G }} \\
&= {1\over 2} \qty{1 + { 1 \over [G : Z(G)]  }}
.\]

:::

:::

