---
schema: qual/card@1
id: E-8Q9TN
kind: problem
title: Star-fine refinements of open coverings
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Supplementary Exercise 1, printed p. 499. The two printed parts (a) and (b): a star-fine refinement exists for a metrizable space, and for a compact Hausdorff space, by the two printed hints. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: part (b) invoked "the Shrinking Lemma" as a named result of the book, which it is not; the shrinking step is now proved on the card from the Definition of normality (printed p. 195) by shrinking the members of the cover one at a time, and Theorem 32.3 (printed p. 202) supplies normality of a compact Hausdorff space. Corrected: the statement carried the closing square bracket of the printed bracketed hint inside the display mathematics, so the displayed formula for B_J ended in a stray bracket; the bracket interrupted a display and is dropped, which is recorded here. Citations added: the definition of a metric space (printed p. 119) for the triangle inequality, the definition of compactness (printed p. 164), and the definition of a refinement (printed p. 245). Also corrected in the structure: the old solution was a pf block whose inner steps had no proofs; the steps below each carry a proof, and the covering property and the star property of B are separate steps. What the certificate does not cover: part (a) as printed uses 3 epsilon(x) and no paracompactness; the proof does exactly that and nothing more.
---

::: {.exercise}

Let $X$ be a space; let $\mathcal{A}$ be an open covering of $X$.
Under what conditions does there exist an open covering $\mathcal{B}$ of $X$ refining $\mathcal{A}$ such that for each pair $B, B'$ of elements of $\mathcal{B}$ that have nonempty intersection, the union $B \cup B'$ lies in an element of $\mathcal{A}$?

(a) Show that such a covering $\mathcal{B}$ exists if $X$ is metrizable.
[Hint: Choose $\epsilon(x)$ so that $B(x, 3\epsilon(x))$ lies in an element of $\mathcal{A}$. Let $\mathcal{B}$ consist of the open sets $B(x, \epsilon(x))$.]

(b) Show that such a covering exists if $X$ is compact Hausdorff.
[Hint: Let $A_1, \ldots, A_n$ be a finite subcollection of $\mathcal{A}$ that covers $X$.
Choose an open covering $C_1, \ldots, C_n$ of $X$ such that $\overline{C}_i \subset A_i$ for each $i$.
For each nonempty subset $J$ of $\{1, \ldots, n\}$, consider the set

$$
B_J = \bigcap_{j \in J} A_j - \bigcup_{j \notin J} \overline{C}_j.
$$

:::

::: {.solution}

A family $\mathcal{B}$ of open sets is a refinement of $\mathcal{A}$ if each $B \in \mathcal{B}$ is contained in some element of $\mathcal{A}$ (definition of refinement, printed p. 245).

::: pf

::: {.pf-step #metric}

(a) If $X$ is metrizable with metric $d$, then
$$
\mathcal{B}=\{B(x,\varepsilon(x))\mid x\in X\}
$$
with $3\varepsilon(x)$ chosen as in the hint is an open cover refining $\mathcal{A}$, and the union of two intersecting members lies in an element of $\mathcal{A}$.

::: pf-proof

::: {.pf-step}

For each $x$ there is $A_x\in\mathcal{A}$ and $\varepsilon(x)>0$ with $B(x,3\varepsilon(x))\subseteq A_x$.

::: pf-proof

$\mathcal{A}$ is an open cover, so $x\in A_x$ for some $A_x\in\mathcal{A}$, and $A_x$ is open, so it contains a ball $B(x,r_x)$ about $x$; put $\varepsilon(x)=r_x/3>0$. A metric space has the triangle inequality as an axiom (definition of a metric, printed p. 119).

:::

:::

::: {.pf-step}

$\mathcal{B}$ is an open cover of $X$ refining $\mathcal{A}$.

::: pf-proof

Each $B(x,\varepsilon(x))$ is open, and $x$ lies in it, so the family covers $X$. It refines $\mathcal{A}$ because $B(x,\varepsilon(x))\subseteq B(x,3\varepsilon(x))\subseteq A_x\in\mathcal{A}$.

:::

:::

::: {.pf-step}

If $B(x_1,\varepsilon(x_1))\cap B(x_2,\varepsilon(x_2))\ne\varnothing$, then their union lies in $A_{x_1}$ or in $A_{x_2}$.

::: pf-proof

Let $z$ be a point of the intersection and suppose, without loss of generality, that $\varepsilon(x_1)\ge\varepsilon(x_2)$. For $y\in B(x_2,\varepsilon(x_2))$ the triangle inequality gives
$$
d(y,x_1)\le d(y,x_2)+d(x_2,z)+d(z,x_1)<\varepsilon(x_2)+\varepsilon(x_2)+\varepsilon(x_1)\le 3\varepsilon(x_1),
$$
so $B(x_2,\varepsilon(x_2))\subseteq B(x_1,3\varepsilon(x_1))\subseteq A_{x_1}$, while $B(x_1,\varepsilon(x_1))\subseteq A_{x_1}$ as well.

:::

:::

:::

:::

::: {.pf-step #shrinking}

If $X$ is normal and $A_1,\dots,A_n$ are open sets covering $X$, there are open sets $C_1,\dots,C_n$ covering $X$ with $\overline{C}_i\subseteq A_i$ for each $i$.

::: pf-proof

Proceed in $n$ stages. At stage $i$, suppose that $C_1,\dots,C_{i-1}$ have been chosen so that the family $C_1,\dots,C_{i-1},A_i,\dots,A_n$ covers $X$ and $\overline{C}_k\subseteq A_k$ for $k<i$; for $i=1$ this is the hypothesis. The set
$$
F=X-\left(C_1\cup\cdots\cup C_{i-1}\cup A_{i+1}\cup\cdots\cup A_n\right)
$$
is closed, and $F\subseteq A_i$ because the family covers $X$. The sets $F$ and $X-A_i$ are disjoint closed sets, so by the Definition of normality (printed p. 195) there are disjoint open sets $V\supseteq F$ and $W\supseteq X-A_i$; then $\overline{V}\subseteq X-W\subseteq A_i$ because $X-W$ is closed. Take $C_i=V$. The family $C_1,\dots,C_i,A_{i+1},\dots,A_n$ still covers $X$, since $F\subseteq V$. After $n$ stages the family $C_1,\dots,C_n$ has the required properties.

:::

:::

::: {.pf-step #compact}

(b) If $X$ is compact Hausdorff and $\mathcal{A}$ is an open cover, then the family of the nonempty sets $B_J$ is an open cover of $X$ refining $\mathcal{A}$, and the union of two intersecting members lies in an element of $\mathcal{A}$.

::: pf-proof

::: {.pf-step}

Extract a finite subcover $A_1,\dots,A_n$ and choose $C_1,\dots,C_n$ as in step [](#shrinking){.pf-ref}.

::: pf-proof

$X$ is compact, so the open cover $\mathcal{A}$ has a finite subcover (definition of compactness, printed p. 164). A compact Hausdorff space is normal (Theorem 32.3, printed p. 202), so step [](#shrinking){.pf-ref} applies to $A_1,\dots,A_n$.

:::

:::

::: {.pf-step}

The nonempty sets
$$
B_J=\left(\bigcap_{j\in J}A_j\right)\setminus\left(\bigcup_{k\notin J}\overline{C}_k\right)
$$
for nonempty $J\subseteq\{1,\dots,n\}$ form an open cover of $X$ refining $\mathcal{A}$.

::: pf-proof

Each $B_J$ is open, being a finite intersection of open sets minus a finite union of closed sets. Given $x\in X$, let $J=\{i\mid x\in\overline{C}_i\}$; this set is nonempty because $C_1,\dots,C_n$ cover $X$, and $x\in\overline{C}_j\subseteq A_j$ for $j\in J$, while $x\notin\overline{C}_k$ for $k\notin J$; so $x\in B_J$. Each $B_J$ is contained in $A_j$ for every $j\in J$, hence in an element of $\mathcal{A}$.

:::

:::

::: {.pf-step}

If $B_J\cap B_K\ne\varnothing$, then $B_J\cup B_K$ lies in an element of $\mathcal{A}$.

::: pf-proof

Let $x\in B_J\cap B_K$. Since $C_1,\dots,C_n$ cover $X$, there is $j_0$ with $x\in C_{j_0}\subseteq\overline{C}_{j_0}$. Then $x\in\overline{C}_{j_0}$ and $x\in B_J$ force $j_0\in J$, and $x\in B_K$ forces $j_0\in K$, so $j_0\in J\cap K$. Now $B_J\subseteq A_{j_0}$ and $B_K\subseteq A_{j_0}$ by the definition of $B_J$ and $B_K$, whence $B_J\cup B_K\subseteq A_{j_0}\in\mathcal{A}$.

:::

:::

:::

:::

:::

:::
