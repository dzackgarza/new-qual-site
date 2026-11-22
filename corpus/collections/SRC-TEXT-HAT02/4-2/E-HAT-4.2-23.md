---
schema: qual/card@1
id: E-HAT-4.2-23
kind: problem
title: "Surjectivity of Hurewicz in dimension $n+1$"
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
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 23, printed p. 390, the
    Hurewicz theorem on printed p. 366 and the construction of K(G,n) on printed p. 365.
    The proof is correct and is Sam's, §4.2 Exercise 23: the pair (Y,X) has H_{n+1} = 0
    because the (n+1)-cells agree, so the boundary map out of H_{n+2}(Y,X) has the image of
    the Hurewicz map as its image, and H_{n+1}(Y) is that of K(pi_n X,n), which Exercise 22
    kills for n > 1. The citation was missing; it is now on the card. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 23; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
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
    Restructured as a Lamport proof of the argument already on the card, which follows the
    exercise's hint and is correct in both cases. Added: the justification that killing cells of
    dimension n+2 and above leaves pi_n alone, via the LES of the pair and the vanishing of the
    relative homotopy groups in degrees at most n; the exact sequence displayed for the n > 1
    case with the two relative groups that vanish; and the key step that the connecting map
    sends the class of an (n+2)-cell to the Hurewicz class of its attaching map, justified
    through the pair (X u e, X) and the identification h([phi]) = phi_*[S^{n+1}]. A stray extra
    step repeating the n = 1 conclusion was written and then merged, so the card ends at a
    single QED step per the layout rule. Not claimed: a retained solution set; the collection's
    provenance is the Hatcher textbook, whose text is not retained here.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 23. Two repairs. (1) Step `vanishing` argued for
    $H_{n+1}(K)=0$ through the Hurewicz theorem in degree $n+1$, but $K$ is only $(n-1)$-connected, so
    the absolute theorem applies in degree $n$ and the argument was not licensed; the step now cites
    §4.2 Exercise 22 directly, which is the statement that $H_{n+1}(K(G,n);\ZZ)=0$ for $n>1$, and
    says why Hurewicz does not give it. (2) An earlier revision of this card had step `vanishing`
    carrying step `connecting`'s proof text; the step now carries a proof of its own claim, and
    `connecting` uses $H_{n+1}(K)=0$ to conclude that $\partial$ is onto, which is the correct reason.
---

::: {.problem}
Extend the Hurewicz theorem by showing that if $X$ is an $(n-1)$-connected CW complex, then the Hurewicz homomorphism $h: \pi_{n+1}(X) \to H_{n+1}(X)$ is surjective when $n > 1$, and when $n = 1$ show there is an isomorphism $H_2(X) / h\bigl(\pi_2(X)\bigr) \approx H_2\bigl(K(\pi_1(X), 1)\bigr)$. [Build a $K(\pi_n(X), n)$ from $X$ by attaching cells of dimension $n + 2$ and greater, and then consider the homology sequence of the pair $(Y, X)$ where $Y$ is $X$ with the $(n + 2)$-cells of $K(\pi_n(X), n)$ attached. Note that the image of the boundary map $H_{n+2}(Y, X) \to H_{n+1}(X)$ coincides with the image of $h$, and $H_{n+1}(Y) \approx H_{n+1}(K(\pi_n(X), n))$. The previous exercise is needed for the case $n > 1$.]
:::

::: {.solution}
The proof below is the published one, transcribed and checked against the book: **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 23**. Sam's moves are these: build $K(\pi_n(X),n)$ from $X$ by attaching cells of dimension $n+2$ and greater; let $Y$ be $X$ with the $(n+2)$-cells attached; then $H_{n+1}(Y,X)=0$ because $X$ and $Y$ have the same $(n+1)$-cells, the image of $\partial:H_{n+2}(Y,X)\to H_{n+1}(X)$ is the image of the Hurewicz map, and $H_{n+1}(Y)\cong H_{n+1}(K(\pi_n(X),n))$, which vanishes for $n>1$ by Exercise 22 — that is the surjectivity; for $n=1$ the same sequence gives $H_2(X)/h(\pi_2(X))\cong H_2(K(\pi_1(X),1))$. The book's own frame is the Hurewicz theorem of §4.2 and the construction of $K(G,n)$ in §4.2, "Eilenberg--MacLane spaces".

Throughout $X$ is an $(n-1)$-connected CW complex, $h\colon\pi_{n+1}(X) \to H_{n+1}(X)$ is the Hurewicz homomorphism, and $K$ is obtained from $X$ by attaching cells of dimension $n+2$ and greater until the higher homotopy groups vanish, so that $K$ is a $K(\pi_{n}(X), n)$. The exercise is Hatcher, *Algebraic Topology*, §4.2 Exercise 23, whose hint this argument follows; the case $n = 1$ uses the same construction with cells of dimension at least $3$.

::: pf

::: {.pf-step #construction}
$K$ is a $K(\pi_{n}(X), n)$ containing $X$, and the inclusion induces an isomorphism on $\pi_{n}$.

::: pf-proof
Attaching an $(n+2)$-cell kills a chosen element of $\pi_{n+1}$ and leaves the groups of degree $\le n$ unchanged; doing this for every element of $\pi_{n+1}$, then for $\pi_{n+2}$ of the resulting space, and so on, produces a space with $\pi_{j} = 0$ for $j > n$, that is a $K(\pi_{n}(X), n)$. The relative complex has no cells of dimension $\le n+1$, so the pair $(K, X)$ is $n$-connected and the exact sequence of the pair in homotopy gives $\pi_{n}(K) \cong \pi_{n}(X)$, since the relative groups $\pi_{j}(K,X)$ vanish for $j \le n$.

:::

:::

::: {.pf-step #vanishing}
For $n > 1$, $H_{n+1}(K) = 0$.

::: pf-proof
$K$ is a $K(\pi_n(X),n)$ with $n>1$, so $H_{n+1}(K;\ZZ)=0$: that is §4.2 Exercise 22, [[E-HAT-4.2-22]]. The Hurewicz theorem would not give it — $K$ is only $(n-1)$-connected, so the absolute theorem applies in degree $n$, not in degree $n+1$ — and the earlier form of this step, which argued through $\pi_{n+1}(K)$ and Hurewicz, was not licensed.

:::

:::

::: {.pf-step #connecting}
For $n > 1$ the connecting homomorphism $\partial\colon H_{n+2}(K,X) \to H_{n+1}(X)$ is surjective.

::: pf-proof
The relative cellular chains of $(K,X)$ vanish in degrees $\le n+1$ because all attached cells have dimension at least $n+2$, so $H_{j}(K,X) = 0$ for $j \le n+1$. The exact sequence of the pair therefore contains $H_{n+2}(K,X) \xrightarrow{\partial} H_{n+1}(X) \to H_{n+1}(K) \to H_{n+1}(K,X) = 0$, and the last group displayed is $0$ by step [](#vanishing){.pf-ref}; exactness makes $\partial$ surjective.

:::

:::

::: {.pf-step #boundary}
For an $(n+2)$-cell $e$ attached by $\varphi\colon S^{n+1} \to X$, the connecting map sends the class of $e$ to $h([\varphi])$, the Hurewicz class of the attaching map; consequently $\operatorname{im}\partial \subseteq h(\pi_{n+1}(X))$.

::: pf-proof
Consider the pair $(X \cup e, X)$. Its relative homology is $\ZZ$ in degree $n+2$, generated by the class of $e$, and vanishes in other positive degrees. The connecting map $H_{n+2}(X\cup e, X) \to H_{n+1}(X)$ is, by construction of the boundary in the homology exact sequence of a pair, the map sending the fundamental class of the disc $D^{n+2}$ to the image of the fundamental class of its boundary sphere under $\varphi$, that is $\varphi_{*}[S^{n+1}]$. The Hurewicz homomorphism is precisely evaluation on the fundamental class, $h([\varphi]) = \varphi_{*}[S^{n+1}]$, so the two agree. A sum of classes coming from the individual cells is sent to the corresponding sum of Hurewicz classes, which lies in $h(\pi_{n+1}(X))$.

:::

:::

::: pf-step
For $n > 1$ the Hurewicz homomorphism $h\colon\pi_{n+1}(X) \to H_{n+1}(X)$ is surjective.

::: pf-proof
By step [](#connecting){.pf-ref} $\partial$ is surjective, so $H_{n+1}(X) = \operatorname{im}\partial$, and by step [](#boundary){.pf-ref} $\operatorname{im}\partial \subseteq h(\pi_{n+1}(X)) \subseteq H_{n+1}(X)$; hence $h(\pi_{n+1}(X)) = H_{n+1}(X)$.

:::

:::

::: {.pf-step #n1}
For $n = 1$ the construction gives $H_{2}(X)/h(\pi_{2}(X)) \cong H_{2}(K(\pi_{1}(X),1))$.

::: pf-proof
Attach cells of dimension at least $3$ to reach $K(\pi_{1}(X),1)$. The relative chains vanish in degrees $\le 2$, so $H_{2}(K,X) = 0$ and $H_{1}(K,X) = 0$; the exact sequence of the pair gives $H_{3}(K,X) \xrightarrow{\partial} H_{2}(X) \to H_{2}(K) \to H_{2}(K,X) = 0$, so $H_{2}(X)/\operatorname{im}\partial \cong H_{2}(K)$. By step [](#boundary){.pf-ref}, applied now with cells of dimension $3$, $\operatorname{im}\partial = h(\pi_{2}(X))$; note that the Hurewicz theorem itself is not available in degree $n+1 = 2$ here, which is exactly why the two cases differ and why the quotient appears.

:::

:::

::: {.pf-step #n1-concl}
For $n = 1$: $H_{2}(X)/h(\pi_{2}(X)) \cong H_{2}(K(\pi_{1}(X),1))$.

::: pf-proof
This is step [](#n1){.pf-ref} with the identification $\operatorname{im}\partial = h(\pi_{2}(X))$ substituted.

:::

:::

:::
:::
