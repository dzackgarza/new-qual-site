---
schema: qual/card@1
id: P-6VBZV
kind: problem
title: "Suppose the group $G$ acts on the set $X$ . Show that the stabilizers\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
a.
Suppose the group $G$ acts on the set $X$ . Show that the stabilizers of elements in the same orbit are conjugate.

b.
Let $G$ be a finite group and let $H$ be a proper subgroup. Show that the union of the conjugates of $H$ is strictly smaller than $G$, i.e.
\[
\Union_{g\in G} gHg\inv \subsetneq G
\]

c.
Suppose $G$ is a finite group acting transitively on a set $S$ with at least 2 elements. Show that there is an element of $G$ with no fixed points in $S$.

:::{.concept}
\envlist

- Orbit: $G\cdot x \definedas \theset{g\cdot x \suchthat g\in G} \subseteq X$
- Stabilizer: $G_x \definedas \theset{g\in G\suchthat g\cdot x = x} \leq G$
- Orbit-Stabilizer: $G\cdot x \simeq G/G_x$.
- $abc\in H \iff b\in a\inv H c\inv$
- Set of orbits for $G\actson X$, notated $X/G$.
- Set of fixed points for $G\actson X$, notated $X^g$.
- Burnside's Lemma: $\abs{X/G} \cdot \abs{G} = \sum_{g\in G} \abs{X^g}$ 
  - Number of orbits equals average number of fixed points.

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Fix $x$, then $y\in \Orb(x) \implies g\cdot x = y$ for some $g$, and $x = g\inv \cdot y$.
- Then
\[
h \in \Stab(x)
&\iff h\cdot x = x && \text{by being in the stabilizer} \\
&\iff h\cdot (g\inv \cdot y) = g\inv \cdot y \\
&\iff (g h g\inv) \cdot y = y \\
&\iff ghg\inv \in G_y && \text{by definition}\\
&\iff h\in g ^{-1}  \Stab(y) g
,\]
so $\Stab(x) = g\inv \Stab(y) g$.

:::

:::{.proof title="of b"}
Let $G$ act on its subgroups by conjugation, 

- The orbit $G\cdot H$ is the set of all subgroups conjugate to $H$, and

- The stabilizer of $H$ is $G_H = N_G(H)$.

- By orbit-stabilizer,
\[
G\cdot H = [G: G_H] = [G: N_G(H)]
.\]

- Since $\abs H = n$, and all of its conjugate also have order $n$.

- Note that 
\[
H\leq N_G(H) \implies \abs{H} \leq \abs{N_G(H)} \implies {1\over \abs{N_G(H)}} \leq {1\over \abs{H}}
,\]

- Now *strictly* bound the size of the union by overcounting their intersections at the identity:
\[
\abs{\Union_{g\in G}gHg\inv} 
&< (\text{Number of Conjugates of } H) \cdot (\text{Size of each conjugate}) \\ 
& \text{strictly overcounts since they intersect in at least the identity} \\
&= [G: N_G(H)] \abs{H} \\
&= {\abs{G} \over \abs{N_G(H)}} \abs{H} \\
& \text{since $G$ is finite} \\
&\leq {\abs G \over \abs H} \abs H \\
&= \abs{G}
.\]

:::

:::{.proof title="of c"}
\envlist

- Let $G\actson X$ transitively where $\abs{X} \geq 2$.
- An action is transitive iff there is only one orbit, so $\abs{X/G} = 1$.
- Apply Burnside's Lemma
\[
1 = \abs{X/G} = \frac{1}{\abs G} \sum_{g\in G} \abs{\Fix(g)} \implies \abs{G} = \sum_{g\in G} \abs{\Fix(g)} = \Fix(e) + \sum_{\substack{g\in G \\ g\neq e}} \abs{\Fix(g)}
\]
- Note that $\Fix(e) = X$, since the identity must fix every element, so $\abs{\Fix(e)} \geq 2$.
- If $\abs{\Fix(g)} > 0$ for all $g\neq e$, the remaining term is at least $\abs{G} -1$.
  But then the right-hand side yields is at least $2 + (\abs{G} -1) = \abs{G} + 1$, contradicting the equality.
- So not every $\abs{\Fix(g)} > 0$, and $\abs{ \Fix(g) } = 0$ for some $g$, which says $g$ has no fixed points in $X$.

:::

:::

