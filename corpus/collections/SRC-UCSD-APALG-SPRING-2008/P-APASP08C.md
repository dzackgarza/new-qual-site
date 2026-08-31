---
schema: qual/card@1
id: P-APASP08C
kind: problem
title: "Character of a permutation representation, orbits, and double cosets"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Group Actions
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\Gamma$ act on a family $\mathcal{F}$, and let $\chi$ be the character of the permutation representation resulting from this action.

**(a)** Show that the multiplicity of the trivial representation in this representation is equal to the number of orbits of $\mathcal{F}$ under the action of $\Gamma$.

**(b)** Show that the integer $\langle \chi, \chi \rangle$ counts the number of orbits in the action of $\Gamma$ on the family of ordered pairs
$$
\mathcal{F} \times \mathcal{F} = \bigl\{ (f, g) : f, g \in \mathcal{F} \bigr\}.
$$

**(c)** Suppose that $\Gamma$ acts transitively on $\mathcal{F}$.
Let $f_0$ be an element of $\mathcal{F}$, $H$ be its stabilizer, and let
$$
\Gamma = H\tau_1 H + H\tau_2 H + \cdots + H\tau_k H
$$
be the double coset decomposition of $\Gamma$ resulting from the equivalence relation
$$
\gamma_1 \sim_H \gamma_2 \quad\Longleftrightarrow\quad \gamma_2 = h'\gamma_1 h'' \quad\text{(for some } h', h'' \in H\text{)}.
$$
Show that in this case $\langle \chi, \chi \rangle_\Gamma = k$.
Hint: Use part (b).
:::

::: {.solution}
<1>1. Part (a): Multiplicity of trivial representation equals number of orbits:
<2>1. For any $g \in \Gamma$, the character value $\chi(g) = \operatorname{Tr}(\rho(g))$ of the permutation representation on $\mathbb{C}[\mathcal{F}]$ equals the number of fixed points:
\[
\chi(g) = |\operatorname{Fix}(g)| = |\{f \in \mathcal{F} \mid g \cdot f = f\}|.
\]
::: {.proof}
diagonal entries in the standard permutation basis are 1 for fixed points and 0 otherwise.
:::
<2>2. The inner product with the trivial character $\mathbf{1}$ is:
\[
\langle \chi, \mathbf{1} \rangle = \frac{1}{|\Gamma|} \sum_{g \in \Gamma} \chi(g) \cdot 1 = \frac{1}{|\Gamma|} \sum_{g \in \Gamma} |\operatorname{Fix}(g)|.
\]
::: {.proof}
definition of character inner product.
:::
<2>3. By Burnside’s Lemma (Cauchy–Frobenius Lemma):
\[
\frac{1}{|\Gamma|} \sum_{g \in \Gamma} |\operatorname{Fix}(g)| = |\mathcal{F} / \Gamma| = \text{number of orbits of } \mathcal{F} \text{ under } \Gamma.
\]
Thus the multiplicity of the trivial representation is $|\mathcal{F}/\Gamma|$.
::: {.proof}
Burnside's Lemma.
:::

<1>2. Part (b): $\langle \chi, \chi \rangle$ counts orbits on $\mathcal{F} \times \mathcal{F}$:
<2>1. Consider the diagonal action of $\Gamma$ on $\mathcal{F} \times \mathcal{F}$ defined by $g \cdot (f_1, f_2) = (g \cdot f_1, g \cdot f_2)$.
The fixed points of $g$ on $\mathcal{F} \times \mathcal{F}$ are:
\[
\operatorname{Fix}_{\mathcal{F} \times \mathcal{F}}(g) = \{(f_1, f_2) \in \mathcal{F} \times \mathcal{F} \mid g \cdot f_1 = f_1, \, g \cdot f_2 = f_2\} = \operatorname{Fix}(g) \times \operatorname{Fix}(g).
\]
::: {.proof}
product of fixed point sets.
:::
<2>2. Thus the permutation character $\chi_{\mathcal{F} \times \mathcal{F}}$ satisfies:
\[
\chi_{\mathcal{F} \times \mathcal{F}}(g) = |\operatorname{Fix}_{\mathcal{F} \times \mathcal{F}}(g)| = |\operatorname{Fix}(g)|^2 = \chi(g)^2.
\]
::: {.proof}
cardinality of Cartesian product.
:::
<2>3. Since $\chi(g)$ is integer-valued (hence real), $\overline{\chi(g)} = \chi(g)$.
Applying Part (a) to the action on $\mathcal{F} \times \mathcal{F}$:
\[
|(\mathcal{F} \times \mathcal{F}) / \Gamma| = \langle \chi_{\mathcal{F} \times \mathcal{F}}, \mathbf{1} \rangle = \frac{1}{|\Gamma|} \sum_{g \in \Gamma} \chi(g)^2 = \frac{1}{|\Gamma|} \sum_{g \in \Gamma} \chi(g) \overline{\chi(g)} = \langle \chi, \chi \rangle.
\]
::: {.proof}
Part (a) applied to the set $\mathcal{F} \times \mathcal{F}$.
:::

<1>3. Part (c): Double coset decomposition and $\langle \chi, \chi \rangle = k$:
<2>1. By transitivity of $\Gamma$ on $\mathcal{F}$, every orbit of $\Gamma$ on $\mathcal{F} \times \mathcal{F}$ contains at least one pair of the form $(f_0, f)$ for some $f \in \mathcal{F}$.
::: {.proof}
for any $(f_1, f_2)$, choose $\gamma \in \Gamma$ with $\gamma f_1 = f_0$; then $\gamma(f_1, f_2) = (f_0, \gamma f_2)$.
:::
<2>2. Two pairs $(f_0, f)$ and $(f_0, f')$ lie in the same $\Gamma$-orbit if and only if there exists $\gamma \in \Gamma$ with $\gamma(f_0, f) = (f_0, f')$.
The condition $\gamma f_0 = f_0$ means $\gamma \in H = \operatorname{Stab}_\Gamma(f_0)$, so $f' = \gamma f \in H \cdot f$.
Thus the $\Gamma$-orbits on $\mathcal{F} \times \mathcal{F}$ are in bijective correspondence with the $H$-orbits on $\mathcal{F}$.
::: {.proof}
stabilizer property of $f_0$.
:::
<2>3. Using the equivariant bijection $\mathcal{F} \cong \Gamma / H$ given by $\gamma f_0 \leftrightarrow \gamma H$, the action of $H$ on $\mathcal{F}$ corresponds to left multiplication of $H$ on the left coset space $\Gamma / H$.
The $H$-orbits on $\Gamma / H$ are the double cosets $H \backslash \Gamma / H$:
\[
H \cdot (\tau_i H) = H \tau_i H / H.
\]
::: {.proof}
definition of double cosets $H \tau_i H$.
:::
<2>4. Since the double coset decomposition has $k$ distinct double cosets $\Gamma = \bigsqcup_{i=1}^k H \tau_i H$, there are exactly $k$ distinct $H$-orbits on $\mathcal{F}$.
By <2>2 and Part (b), $\langle \chi, \chi \rangle = |(\mathcal{F} \times \mathcal{F})/\Gamma| = k$.
::: {.proof}
<2>2 and <2>3.
:::

<1>4. Conclusion:
$\langle \chi, \mathbf{1} \rangle = |\mathcal{F}/\Gamma|$, $\langle \chi, \chi \rangle = |(\mathcal{F}\times\mathcal{F})/\Gamma|$, and $\langle \chi, \chi \rangle = k$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
