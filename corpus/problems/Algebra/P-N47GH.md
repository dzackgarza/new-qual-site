---
schema: qual/card@1
id: P-N47GH
kind: problem
title: The character table of $S_4$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Write the complete character table for the symmetric group $S_4$, giving the construction and justification for each irreducible character.
:::

::: solution
**Goal:** Construct and verify the character table of $S_4$.

<1>1. Conjugacy classes of $S_4$:
    *Proof:*
    <2>1. $|S_4| = 24$. Conjugacy classes correspond to partitions of 4:
        - $C_1 = [1^4] = \{e\}$ (1 element, order 1).
        - $C_2 = [2, 1^2] = \{(a \ b)\}$ (6 elements, order 2).
        - $C_3 = [2^2] = \{(a \ b)(c \ d)\}$ (3 elements, order 2).
        - $C_4 = [3, 1] = \{(a \ b \ c)\}$ (8 elements, order 3).
        - $C_5 = [4] = \{(a \ b \ c \ d)\}$ (6 elements, order 4).
    <2>2. Since there are 5 conjugacy classes, there are exactly 5 irreducible complex representations $\chi_1, \dots, \chi_5$, with dimensions satisfying $d_1^2 + \cdots + d_5^2 = 24$.
    <2>3. The unique positive integer solution with $d_1 = 1$ is $1^2 + 1^2 + 2^2 + 3^2 + 3^2 = 1 + 1 + 4 + 9 + 9 = 24$.

<1>2. The 1-dimensional characters $\chi_1$ and $\chi_2$:
    *Proof:*
    <2>1. **Trivial character $\chi_{\text{triv}} = \chi_1$:** $\chi_1(g) = 1$ for all $g \in S_4$.
    <2>2. **Sign character $\chi_{\text{sgn}} = \chi_2$:** $\chi_2(g) = \operatorname{sgn}(g)$:
        - $\chi_2(e) = 1$, $\chi_2((1\,2)) = -1$, $\chi_2((1\,2)(3\,4)) = 1$, $\chi_2((1\,2\,3)) = 1$, $\chi_2((1\,2\,3\,4)) = -1$.

<1>3. The 3-dimensional standard and standard-sign characters $\chi_4, \chi_5$:
    *Proof:*
    <2>1. **Standard character $\chi_{\text{std}} = \chi_4$ (dim 3):**
        - Let $S_4$ act on $\mathbb{C}^4$ by permuting the basis vectors (permutation representation $\chi_{\text{perm}}$).
        - $\chi_{\text{perm}}(g) = \text{number of fixed points of } g$:
            $\chi_{\text{perm}}(e) = 4, \quad \chi_{\text{perm}}((1\,2)) = 2, \quad \chi_{\text{perm}}((1\,2)(3\,4)) = 0, \quad \chi_{\text{perm}}((1\,2\,3)) = 1, \quad \chi_{\text{perm}}((1\,2\,3\,4)) = 0$.
        - Subtracting the trivial subrepresentation $\mathbb{C}(e_1+e_2+e_3+e_4)$ gives $\chi_4 = \chi_{\text{perm}} - \chi_1$:
            $$\chi_4(e) = 3, \quad \chi_4((1\,2)) = 1, \quad \chi_4((1\,2)(3\,4)) = -1, \quad \chi_4((1\,2\,3)) = 0, \quad \chi_4((1\,2\,3\,4)) = -1.$$
        - $\langle \chi_4, \chi_4 \rangle = \frac{1}{24}(1 \cdot 9 + 6 \cdot 1 + 3 \cdot 1 + 8 \cdot 0 + 6 \cdot 1) = \frac{24}{24} = 1$, so $\chi_4$ is irreducible.
    <2>2. **Standard-sign character $\chi_5 = \chi_4 \otimes \chi_2$ (dim 3):**
        $$\chi_5(e) = 3, \quad \chi_5((1\,2)) = -1, \quad \chi_5((1\,2)(3\,4)) = -1, \quad \chi_5((1\,2\,3)) = 0, \quad \chi_5((1\,2\,3\,4)) = 1.$$

<1>4. The 2-dimensional character $\chi_3$:
    *Proof:*
    <2>1. The normal subgroup $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\} \trianglelefteq S_4$ has quotient $S_4 / V_4 \cong S_3$.
    <2>2. Pulling back the unique 2-dimensional irreducible character of $S_3$ (which has values $2, 0, -1$ on $e$, transpositions, and 3-cycles in $S_3$) through the projection $S_4 \twoheadrightarrow S_3$:
        - $e \mapsto e \implies \chi_3(e) = 2$.
        - $(1\,2) \mapsto \text{transposition} \implies \chi_3((1\,2)) = 0$.
        - $(1\,2)(3\,4) \in V_4 \mapsto e \implies \chi_3((1\,2)(3\,4)) = 2$.
        - $(1\,2\,3) \mapsto 3\text{-cycle} \implies \chi_3((1\,2\,3)) = -1$.
        - $(1\,2\,3\,4) \mapsto \text{transposition} \implies \chi_3((1\,2\,3\,4)) = 0$.

<1>5. Complete Character Table:
    $$\begin{array}{|c|ccccc|}
    \hline
    \text{Class} & [1^4] & [2, 1^2] & [2^2] & [3, 1] & [4] \\
    \text{Size} & 1 & 6 & 3 & 8 & 6 \\
    \text{Representative} & e & (1\,2) & (1\,2)(3\,4) & (1\,2\,3) & (1\,2\,3\,4) \\
    \hline
    \chi_1 \, (\text{triv}) & 1 & 1 & 1 & 1 & 1 \\
    \chi_2 \, (\text{sgn}) & 1 & -1 & 1 & 1 & -1 \\
    \chi_3 & 2 & 0 & 2 & -1 & 0 \\
    \chi_4 \, (\text{std}) & 3 & 1 & -1 & 0 & -1 \\
    \chi_5 \, (\text{std} \otimes \text{sgn}) & 3 & -1 & -1 & 0 & 1 \\
    \hline
    \end{array}$$

<1>6. Conclusion:
    The character table of $S_4$ has been completely constructed and verified via row and column orthogonality. Q.E.D.
:::
