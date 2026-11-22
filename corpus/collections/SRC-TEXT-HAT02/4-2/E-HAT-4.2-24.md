---
schema: qual/card@1
id: E-HAT-4.2-24
kind: problem
title: "Moore spaces $M(G,1)$ and $H_2(K(G,1))$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 24, printed p. 391,
    and Exercise 23 of the same section. The proof is correct in both directions.
    Necessity: attaching cells of dimension at least 3 to a Moore space M(G,1) gives a
    K(G,1) without changing pi_1, and Exercise 23 gives H_2(K) = H_2(M)/h(pi_2 M) = 0.
    Sufficiency: in a CW model of K(G,1), the 2-skeleton A has pi_1(A) = G, H_2(A) free,
    and h(pi_2 A) = H_2(A) by Exercise 23 again; attaching one 3-cell along a map
    representing each element of a basis makes d_3 injective onto ker d_2, so H_2 and H_3
    vanish and pi_1 is unchanged. What was wrong is the provenance sentence: it said the
    checkout's only §4.2 set is Proudfoot's Homework #7, whereas Sam's set is there too.
    The coverage claim about exercise 24 itself is right --- neither set reaches it --- and
    the sentence now says so correctly. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two directions, which is what Queue D asks for on this card. The necessity uses the cell-attachment killing of higher homotopy groups and Exercise 23; the sufficiency is split into the 2-skeleton (free H_2 and the surjectivity of the Hurewicz map, which is what makes a basis of H_2 representable by spheres), the cell attachment with the resulting chain computation, and the torus example. The step from a basis of H_2(A) to 3-cells now says why it is available (Exercise 23 gives h(pi_2(A)) = H_2(A)) and why d_3 is injective with image ker d_2, which the prose asserted in one sentence. No retained set covers this exercise; the card now says so. Locators: the exercise on printed p. 391; Proudfoot's Homework #7 holds §4.2 exercises 1, 2, 30, 31, 32, 39 and not this one. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 24. The proof reads correct. One provenance correction: the
    solution said that no retained set covers the exercise, and the retained sets' actual coverage is
    now recorded — Sam's §4.2 numbering is Hatcher's and Proudfoot's homework 7 covers 1, 2, 30, 31
    and 32, announcing 39 without a solution of it.
---

::: {.problem}
Show there is a Moore space $M(G, 1)$ with $\pi_1\bigl(M(G, 1)\bigr) \approx G$ iff $H_2(K(G, 1); \ZZ) = 0$. [Use the preceding problem. Build such an $M(G, 1)$ from the 2-skeleton $K^2$ of a $K(G, 1)$ by attaching 3-cells according to a basis for the free group $H_2(K^2; \ZZ)$.]
In particular, there is no $M(\ZZ^n, 1)$ with fundamental group $\ZZ^n$, free abelian of rank $n$, if $n \geq 2$.
:::

::: {.solution}
No retained solution set covers this exercise: Sam's §4.2 covers exercises 1, 4, 6, 8, 9, 10, 12, 13, 15, 16, 18, 20, 21, 22, 23, 26, 27, 28, 31, 32, 33 and 34, and Proudfoot's homework 7 covers 1, 2, 30, 31 and 32 — its coverage line announces 39, but no solution of 39 is present — so neither reaches 24. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 24, and it uses §4.2 Exercise 23, which identifies $H_2$ of a $K(G,1)$ with a quotient of $H_2$ of a complex with the same fundamental group by the image of the Hurewicz map.

Here $G$ is abelian, as in the definition of a Moore space: $H_1(M(G,1))\cong G$ and $\widetilde H_i(M(G,1))=0$ for $i\ne1$.

::: pf

::: {.pf-step #necessary}
If a Moore space $M$ has $\pi_1(M)\cong G$ then $H_2(K(G,1);\ZZ)=0$.

::: pf-proof
Attach cells of dimension at least $3$ to $M$ to kill $\pi_2,\pi_3,\dots$; this does not change $\pi_1$, so the result $K$ is a $K(G,1)$. Exercise 23 of the section, applied to $M$, gives $H_2(K)\cong H_2(M)/h(\pi_2(M))$ with $h$ the Hurewicz map; $H_2(M)=0$ because $M$ is a Moore space, so $H_2(K(G,1);\ZZ)=0$.
:::

:::

::: {.pf-step #skeleton}
Conversely let $K$ be a CW model of $K(G,1)$ with $H_2(K;\ZZ)=0$ and put $A=K^2$. Then $\pi_1(A)\cong G$, $H_2(A;\ZZ)$ is free abelian, and $h(\pi_2(A))=H_2(A)$.

::: pf-proof
The $2$-skeleton receives all $2$-cells, so $\pi_1(K^2)\to\pi_1(K)$ is an isomorphism; $H_2(A)$ is a subgroup of the free abelian group $C_2(A)$, hence free; and Exercise 23 applied to $A$ gives $H_2(A)/h(\pi_2(A))\cong H_2(K)=0$, so the Hurewicz image is all of $H_2(A)$. In particular each basis element of $H_2(A)$ is the class of a map $S^2\to A$.
:::

:::

::: {.pf-step #attach}
Attaching one $3$-cell to $A$ along a map $S^2\to A$ representing each element of a basis of $H_2(A)$ gives a complex $M$ with $\pi_1(M)\cong G$ and $\widetilde H_i(M)=0$ for $i\ne1$.

::: pf-proof
Since $A$ has no cells above dimension $2$, the cellular chain complex of $M$ has $C_4=0$, $C_3$ free on the attached cells, and $d_3:C_3\to C_2(A)$ carrying the chosen basis bijectively onto $H_2(A)=\ker d_2$ — this is the standard description of the effect of attaching a cell along a map representing a homology class. Hence $d_3$ is injective, so $H_3(M)=\ker d_3=0$, and its image is $\ker d_2$, so $H_2(M)=\ker d_2/\operatorname{im}d_3=0$. Attaching cells of dimension $\ge3$ does not change $\pi_1$ or $H_1$, so $\pi_1(M)\cong G$ and $H_1(M)\cong G$; and there are no cells in dimensions above $3$, so the higher homology vanishes. Thus $M$ is a Moore space with fundamental group $G$.
:::

:::

::: {.pf-step #torus}
There is no Moore space $M(\ZZ^n,1)$ with fundamental group $\ZZ^n$ for $n\ge2$.

::: pf-proof
The torus $T^n$ is a $K(\ZZ^n,1)$, and $H_2(T^n;\ZZ)\cong\bigwedge^2\ZZ^n$, which is $\ZZ^{n(n-1)/2}\ne0$ for $n\ge2$. By step [](#necessary){.pf-ref} a Moore space with fundamental group $\ZZ^n$ would force $H_2(K(\ZZ^n,1))=0$, so none exists in this range. This is the last assertion of the exercise.
:::

:::

:::
:::
