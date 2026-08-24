---
schema: qual/card@1
id: E-2HSGM
kind: exercise
title: $[0,1]$ is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
---

::: exercise
Show that $[0, 1]$ is compact.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

We prove that $[0, 1]$ is compact directly using the least-upper-bound property of $\RR$.

Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ be an open cover of $[0, 1]$ by open subsets of $\RR$.
Define the set:
$$
S = \{x \in [0, 1] \mid [0, x] \text{ can be covered by finitely many sets from } \mathcal{U}\}.
$$

1. **$S$ is non-empty and bounded:**

   - Since $0 \in [0, 1]$, there is some $U_0 \in \mathcal{U}$ with $0 \in U_0$.
     Thus $[0, 0] = \{0\} \subseteq U_0$, so $0 \in S$, and $S \neq \emptyset$.

   - By definition, $S \subseteq [0, 1]$, so $S$ is bounded above by $1$.

2. **Supremum of $S$:** By the completeness (least upper bound property) of $\RR$, $c = \sup S$ exists, and $0 \leq c \leq 1$.

3. **Show $c \in S$:** Since $c \in [0, 1]$, there exists some $U_c \in \mathcal{U}$ containing $c$.
   Since $U_c$ is open in $\RR$, there exists $\varepsilon > 0$ such that $(c - \varepsilon, c + \varepsilon) \cap [0, 1] \subseteq U_c$.
   By definition of the supremum, there exists $x_0 \in S$ with $c - \varepsilon < x_0 \leq c$.
   Since $x_0 \in S$, $[0, x_0]$ is covered by a finite subcollection $\{U_{\alpha_1}, \ldots, U_{\alpha_k}\} \subseteq \mathcal{U}$.
   Then:
   $$
   [0, c] \subseteq [0, x_0] \cup [x_0, c] \subseteq \left(\bigcup_{i=1}^k U_{\alpha_i}\right) \cup U_c.
   $$
   This is a finite subcover of $[0, c]$, so $c \in S$.

4. **Show $c = 1$:** Suppose towards a contradiction that $c < 1$.
   Since $c \in U_c$ and $U_c$ is open, we can choose $x_1 \in (c, c + \varepsilon) \cap [0, 1]$ (since $c < 1$). Then $[0, x_1] = [0, c] \cup [c, x_1] \subseteq \left(\bigcup_{i=1}^k U_{\alpha_i}\right) \cup U_c$.
   Thus $[0, x_1]$ is also covered by finitely many sets from $\mathcal{U}$, meaning $x_1 \in S$.
   Since $x_1 > c$, this contradicts that $c = \sup S$.

Therefore, $c = 1$, and since $c \in S$, we have $1 \in S$.
Hence $[0, 1]$ is covered by a finite subcollection of $\mathcal{U}$, proving that $[0, 1]$ is compact.
:::
