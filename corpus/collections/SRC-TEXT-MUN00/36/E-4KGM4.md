---
schema: qual/card@1
id: E-4KGM4
kind: exercise
title: Properties of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties does a compact Hausdorff space have?
:::

::: solution
**Goal:** Evaluate which of the 17 fundamental topological properties are necessarily possessed by every compact Hausdorff space, and provide proofs or counterexamples for each.

<1>1. The seventeen standard properties and their validity for compact Hausdorff spaces:
    - **Guaranteed properties (9):**
      1. $T_1$ (Points are closed)
      2. Hausdorff ($T_2$)
      3. Regular ($T_3$)
      4. Completely regular ($T_{3\frac{1}{2}}$)
      5. Normal ($T_4$)
      6. Compact
      7. Limit point compact
      8. Locally compact
      9. Lindelöf
    - **Not necessarily possessed (8):**
      10. First-countable
      11. Second-countable
      12. Separable
      13. Metrizable
      14. Sequentially compact
      15. Connected
      16. Path-connected
      17. Locally connected

<1>2. Proofs for guaranteed properties:
    *Proof:*
    <2>1. **$T_1$ and Hausdorff:** Every Hausdorff space is $T_1$, and Hausdorffness holds by hypothesis.
    <2>2. **Regularity and Normality:** Every compact Hausdorff space is normal ($T_4$). Given disjoint closed sets $A, B \subseteq X$, compactness allows finite subcovers of point-separating open sets to separate $A$ and $B$. Normality with $T_1$ immediately implies regularity ($T_3$).
    <2>3. **Complete regularity:** By Urysohn's Lemma, every normal $T_1$ space is completely regular ($T_{3\frac{1}{2}}$).
    <2>4. **Compactness, Limit Point Compactness, Local Compactness, Lindelöf:**
        - Compactness holds by hypothesis.
        - Compactness implies limit point compactness (every infinite subset has an accumulation point).
        - Every compact space is locally compact ($X$ itself serves as a compact neighborhood for each point).
        - Every open cover has a finite subcover, which is in particular a countable subcover, so $X$ is Lindelöf.

<1>3. Counterexamples for non-guaranteed properties:
    *Proof:*
    <2>1. **Countability and Metrizability (First-countable, Second-countable, Separable, Metrizable):**
        - The one-point compactification of an uncountable discrete space is compact Hausdorff, but fails to be first-countable (and hence not second-countable, separable, or metrizable).
        - The product space $\{0, 1\}^{\mathbb{R}}$ is compact Hausdorff by Tychonoff's Theorem, but is not first-countable and not metrizable.
    <2>2. **Sequential compactness:** The space $\{0, 1\}^{\mathbb{R}}$ (or the Stone-Čech compactification $\beta\mathbb{N}$) is compact Hausdorff but not sequentially compact.
    <2>3. **Connectedness properties (Connected, Path-connected, Locally connected):**
        - The two-point discrete space $\{0, 1\}$ or the Cantor set $C$ is compact Hausdorff, but is totally disconnected (hence neither connected, path-connected, nor locally connected without isolated components). Q.E.D.
:::
