---
schema: qual/card@1
id: E-HAT-4.2-25
kind: problem
title: "Hurewicz cokernel for spaces with few nonzero $\\pi_i$"
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
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continued §4.2 read. Read against Hatcher, Exercise 25 of §4.2, printed p. 391, and
    the printed page is added, the card having had none. Checked: a $K(G,1)$ is built from $X$ by
    attaching $(n+1)$-cells along representatives of $\pi_n(X)$ — legitimate because
    $\pi_i(X)=0$ for $1<i<n$ — and then cells of dimension at least $n+2$; the relative chain complex
    has nothing below degree $n+1$, so the exact sequence of the pair ends
    $H_{n+1}(K,X)\to H_n(X)\to H_n(K)\to0$; the connecting map sends a relative $(n+1)$-cell to the
    homology class of its attaching map, which is exactly the Hurewicz image of the corresponding
    class; hence the quotient is $H_n(K)\cong H_n(K(\pi_1X,1))$. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Structured the prose into six steps with their justifications. Checked against Hatcher: the
    construction of a $K(G,1)$ from $X$ by attaching $(n+1)$-cells along representatives of
    $\pi_n(X)$ and then cells of dimension at least $n+2$; the relative cellular complex of
    $(K,X)$ vanishing below degree $n+1$ with $H_{n+1}(K,X)$ free on the attached cells (Theorem
    2.35); the exact sequence $H_{n+1}(K,X)\to H_n(X)\to H_n(K)\to0$; and the identification of the
    image of the boundary with the Hurewicz image, which is the one place the old prose was terse —
    the boundary of a relative $(n+1)$-cell is the homology class of its attaching map, and that
    class is by definition the Hurewicz image of the corresponding element of $\pi_n(X)$. The
    mathematics is unchanged; the solution is now a structured proof. No statement changed. Not
    checked: no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 25. One repair in step `relative-complex`: it claimed that
    $H_{n+1}(K,X)$ is free on the classes of the $(n+1)$-cells. The relative chain group
    $C_{n+1}(K,X)$ is free on those cells, but the homology is
    $C_{n+1}(K,X)/\operatorname{im}\partial_{n+2}$, a quotient of it, since the $(n+2)$-cells
    contribute relations; the step now says quotient, and notes that the argument below uses only the
    vanishing in degrees $\le n$ and the identification with the quotient.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Item 8 of the current #163 repair split. Repaired the $K(G,1)$ construction in step
    `construction`: attaching cells of dimension at least $n+1\ge3$ preserves $\pi_1=G$;
    it cannot kill loops. The previous proof incorrectly said $\pi_i(X')=0$ for
    $1\le i\le n$. At each inductive stage the revised proof attaches cells along based
    representatives of every element of the relevant $\pi_k$, so no finite-generation or
    countability assumption is used, and compactness identifies the homotopy groups of the
    union. This follows Hatcher's Example 4.16 and the Eilenberg--MacLane construction in
    §4.2. Step `image` now also notes why relations from $(n+2)$-cells die in $H_n(X)$.
    No retained solution set covers Exercise 25, so this repair remains the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Verification of the preceding two events against the body, and one closure repair in
    step `conclusion`: it compared $H_n(K)$ with $H_n(K(G,1))$ from "$K$ is a $K(G,1)$"
    alone, which is not an argument until uniqueness of the homotopy type is named. The
    step now records $\pi_1(K)=G$ and $\pi_i(K)=0$ for $i>1$ from step `construction` and
    cites Proposition 4.30, and the preamble lists that proposition among the inputs.
    Re-read and unchanged: the cell attachment at each stage with no finiteness or
    countability assumption, the compact-image passage to the union, the vanishing of
    $C_*(K,X)$ in degrees at most $n$ with $H_{n+1}(K,X)$ a quotient of the free group on
    the $(n+1)$-cells, the exact sequence of the pair, and the identification of
    $\operatorname{im}\partial$ with the Hurewicz image.
- event: solution-reviewed
  by: kimi
  date: 2026-11-23
  note: >-
    Residue repair for issue #163. Corrected the pair sequence in step `les` to end
    $H_n(X)\to H_n(K)\to H_n(K,X)$. Rebuilt the relation argument in step `image`
    from the short exact sequence of singular chain complexes of $(K,X)$: relative
    boundaries die under the connecting homomorphism by $\partial^2=0$. This removes
    the invalid triple $(K^{n+2},K^{n+1},X)$ and uses no containment of $X$ in a
    skeleton, so cells of $X$ above dimension $n+1$ are allowed. The natural
    cellular--singular comparison on the attached $(n+1)$-cells was also made explicit.
---

::: {.problem}
For $X$ a connected CW complex with $\pi_i(X) = 0$ for $1 < i < n$ for some $n \geq 2$, show that $H_n(X) / h\bigl(\pi_n(X)\bigr) \approx H_n\bigl(K(\pi_1(X), 1)\bigr)$, where $h$ is the Hurewicz map.
:::

::: {.solution}
No retained solution set covers this exercise: Guanyu Li's set ends with §3.3, DeMason's M382C problem set covers §4.2 Exercises 1, 2, 14 and 27 only, the Stanford 215C sets cover §3.B and §3.3 exercises, and the retained Casassas, Putman and Bredon material is not a set of Hatcher solutions. So the argument is the card's own, from Example 4.16 and the construction of Eilenberg--MacLane spaces in §4.2, the cellular chain complex of a CW pair (Theorem 2.35), the Hurewicz theorem (Theorem 4.32), the long exact sequence of homology groups of a pair (§2.1) and the uniqueness of the homotopy type of a $K(G,1)$ (Proposition 4.30).

::: pf

::: {.pf-step #construction}
Let $G=\pi_1(X)$. Since $\pi_i(X)=0$ for $1<i<n$, a $K(G,1)$ can be obtained from $X$ by attaching $(n+1)$-cells along maps $S^n\to X$ representing the elements of $\pi_n(X)$, then cells of dimension at least $n+2$.

::: pf-proof
Attaching an $(n+1)$-cell along $\varphi:S^n\to X$ kills $[\varphi]$ in $\pi_n$ and, since $n+1\ge3$, leaves $\pi_i$ unchanged for $i<n$ and surjective for $i=n$, by cellular approximation. Attach one cell for each based representative of an element of $\pi_n(X)$. The resulting $X'$ has $\pi_1(X')=G$ and $\pi_i(X')=0$ for $1<i\le n$: every class in $\pi_n(X')$ comes from $\pi_n(X)$, and every such class has been killed. In particular, the cells do not affect the fundamental group; they cannot kill loops.

Now suppose, for $k\ge n+1$, that a complex $Z$ has $\pi_1(Z)=G$ and $\pi_i(Z)=0$ for $1<i<k$. Attach $(k+1)$-cells along based representatives of every element of $\pi_k(Z)$. The same cellular-approximation argument preserves $\pi_i$ for $i<k$, including $\pi_1=G$, and kills all of $\pi_k$. Iterate over $k=n+1,n+2,\ldots$. Maps of spheres, and homotopies between them, have compact images and hence lie in a finite stage, so the union $K$ has $\pi_1(K)=G$ and $\pi_i(K)=0$ for $i>1$. This is the cell-attachment procedure of Example 4.16, and $K$ is a $K(G,1)$.
:::
:::

::: {.pf-step #relative-complex}
$H_i(K,X)=0$ for $i\le n$, and $H_{n+1}(K,X)$ is a quotient of the free abelian group on the classes of the $(n+1)$-cells attached.

::: pf-proof
The cells of $K$ not in $X$ have dimension at least $n+1$, so the relative cellular chain complex $C_*(K,X)$ of the CW pair $(K,X)$ vanishes in degrees at most $n$ and is free on the attached $(n+1)$-cells in degree $n+1$. By Theorem 2.35 the cellular homology of the pair is the singular homology, so $H_i(K,X)=0$ for $i\le n$ and $H_{n+1}(K,X)=C_{n+1}(K,X)/\operatorname{im}\partial_{n+2}$, a quotient of that free group — not free in general, the $(n+2)$-cells contributing relations — which is all that the argument below uses.
:::
:::

::: {.pf-step #les}
There is an exact sequence $H_{n+1}(K,X)\xrightarrow{\partial}H_n(X)\to H_n(K)\to 0$.

::: pf-proof
The long exact sequence of the pair $(K,X)$ reads $\cdots\to H_{n+1}(K,X)\xrightarrow{\partial}H_n(X)\to H_n(K)\to H_n(K,X)\to\cdots$, and $H_n(K,X)=0$ by step [](#relative-complex){.pf-ref}.
:::
:::

::: {.pf-step #image}
$\operatorname{im}\partial=h\bigl(\pi_n(X)\bigr)$, the Hurewicz image of $\pi_n(X)$ in $H_n(X)$.

::: pf-proof
Under the natural cellular--singular comparison of Theorem 2.35, the boundary $\partial$ sends the class of a relative $(n+1)$-cell to the homology class in $X$ of its attaching map. The attaching maps are exactly the maps $S^n\to X$ used in step [](#construction){.pf-ref} to represent all elements of $\pi_n(X)$, and the class in $H_n(X)$ of a map $S^n\to X$ is by definition its image under the Hurewicz map $h:\pi_n(X)\to H_n(X)$ of Theorem 4.32.

The relations coming from $\operatorname{im}\partial_{n+2}$ in step [](#relative-complex){.pf-ref} die under $\partial$ without any skeletal containment hypothesis on $X$. To see this, use the short exact sequence of singular chain complexes $0\to C_*(X)\to C_*(K)\to C_*(K,X)\to0$: the connecting homomorphism is computed by lifting a relative cycle $c$ to $\widetilde c\in C_{n+1}(K)$ and taking the boundary of $\widetilde c$ in $C_n(X)$. If the relative cycle is a boundary, a lift can be chosen of the form $\widetilde c=\partial\widetilde d$ for $\widetilde d\in C_{n+2}(K)$, and then $\partial\widetilde c=\partial^2\widetilde d=0$. Hence the image of $\partial$ is precisely $h(\pi_n(X))$, whether or not $X$ has cells above dimension $n+1$.
:::
:::

::: {.pf-step #conclusion}
$H_n(X)/h\bigl(\pi_n(X)\bigr)\cong H_n\bigl(K(\pi_1(X),1)\bigr)$.

::: pf-proof
By steps [](#les){.pf-ref} and [](#image){.pf-ref}, exactness gives $H_n(K)\cong H_n(X)/h\bigl(\pi_n(X)\bigr)$. Step [](#construction){.pf-ref} gives $\pi_1(K)=G$ and $\pi_i(K)=0$ for $i>1$, so $K$ is a $K(G,1)$; Proposition 4.30 gives that any two such spaces are homotopy equivalent, hence $H_n(K)\cong H_n(K(G,1))$.
:::
:::

:::
:::
