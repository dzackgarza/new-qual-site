---
schema: qual/card@1
id: E-HAT-4.1-13
kind: problem
title: "CW complexes retract onto contractible subcomplexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    The card cited "Hatcher, Lemma 4.15 / Extension Lemma" for the homotopy extension property.
    Hatcher's Section 4.1 has no Lemma 4.15: a search of the text for Lemmas 4.11 through 4.19
    returns only Lemma 4.10. The citation is replaced by a reference to the property as Hatcher
    states it for CW pairs in §4.1, with Proposition 0.16 named for the HEP itself.

- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    Second correction to this card's citation, superseding the gloss left by the preceding event. The
    preceding note correctly established that Section 4.1 has no Lemma 4.15, but the wording it put in
    the statement, "the extension lemma (homotopy extension property for CW pairs)", still misidentified
    the book's lemma: Hatcher's extension lemma is Lemma 4.7 (AT.txt:17363-17367, indexed at 27215 as
    "extension lemma 348"), a criterion for extending a map A -> Y when the target's homotopy groups
    vanish in the degrees of the relative cells, and the homotopy extension property is a different
    result, Proposition 0.16 (AT.txt:926-928). The statement now quotes Lemma 4.7's content, and the
    solution is that lemma applied once: A contractible makes every pi_k(A) vanish and A path-connected,
    so id_A extends to r: X -> A, which is a retraction. The previous solution proved the same conclusion
    by the homotopy extension property. That argument was correct -- target A, initial map the constant
    map, hypothesis of Proposition 0.16 satisfied -- but it is a different tool from the one the exercise
    names, and it was an expanded derivation of a standard consequence, so it is replaced rather than
    kept alongside. It remains in the file's history at commit 78363c50b0. Not checked: nothing further
    in the book; the two cited spans are the whole source basis of this correction.

---

::: {.exercise}
Use the **extension lemma** (Lemma 4.7: for a CW pair $(X,A)$, a map $f\colon A\to Y$ with $Y$ path-connected extends to a map $X\to Y$ provided $\pi_{n-1}(Y)=0$ for every $n$ such that $X-A$ has cells of dimension $n$) to show that a CW complex $X$ **retracts** onto any contractible subcomplex $A \subseteq X$.

:::

::: {.solution}

::: pf

::: {.pf-step #vanishes}
Every homotopy group of $A$ vanishes, and $A$ is path-connected.

::: pf-proof
Contractibility of $A$ gives a point $a_0\in A$ and a homotopy $h\colon A\times I\to A$ from $\operatorname{id}_A$ to the constant map at $a_0$. For a map $\alpha\colon S^k\to A$, the composite $h(\alpha(-),t)$ is a homotopy from $\alpha$ to the constant map at $a_0$, so every element of $\pi_k(A,a_0)$ is trivial, for every $k\ge0$. At $k=0$ this says that $A$ has one path component, that is, that $A$ is path-connected.

:::

:::

::: {.pf-step #extends}
$\operatorname{id}_A$ extends to a map $r\colon X\to A$.

::: pf-proof
Take the CW pair $(X,A)$, the map $f=\operatorname{id}_A\colon A\to A$ and the target $Y=A$ in Lemma 4.7. The target is path-connected by step [](#vanishes){.pf-ref}, and for every $n$ such that $X-A$ has cells of dimension $n$ one has $\pi_{n-1}(A)=0$ by the same step. The lemma's induction begins at the $0$-cells of $X-A$, where the hypothesis needed is exactly that $A\neq\emptyset$ be path-connected, so the hypothesis is met in every degree and $f$ extends.

:::

:::

::: {.pf-step #retract}
$r$ is a retraction of $X$ onto $A$.

::: pf-proof
The map $r$ is continuous and extends $\operatorname{id}_A$, so $r(a)=a$ for every $a\in A$. A continuous map $X\to A$ whose restriction to $A$ is the identity of $A$ is by definition a retraction of $X$ onto $A$.

:::

:::

:::

:::
