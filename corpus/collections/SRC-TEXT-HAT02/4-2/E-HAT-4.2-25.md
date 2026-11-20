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
---

::: {.problem}
For $X$ a connected CW complex with $\pi_i(X) = 0$ for $1 < i < n$ for some $n \geq 2$, show that $H_n(X) / h\bigl(\pi_n(X)\bigr) \approx H_n\bigl(K(\pi_1(X), 1)\bigr)$, where $h$ is the Hurewicz map.
:::

::: {.solution}
No retained solution set covers this exercise: Guanyu Li's set ends with §3.3, DeMason's M382C problem set covers sections up to part of §4.1, the Stanford 215C sets cover §3.B and §3.3 exercises, and the retained Casassas, Putman and Bredon material is not a set of Hatcher solutions. So the argument is the card own, from the construction of Moore and Eilenberg–MacLane spaces by attaching cells (§4.2), the cellular chain complex of a CW pair (Theorem 2.35), the Hurewicz theorem (Theorem 4.32) and the long exact sequence of homology groups of a pair (§2.1).

::: pf

::: {.pf-step #construction}
Let $G=\pi_1(X)$. Since $\pi_i(X)=0$ for $1<i<n$, a $K(G,1)$ can be obtained from $X$ by attaching $(n+1)$-cells along maps $S^n\to X$ representing the elements of $\pi_n(X)$, then cells of dimension at least $n+2$.

::: pf-proof
Attaching an $(n+1)$-cell along a map $\varphi:S^n\to X$ kills the class of $\varphi$ in $\pi_n$ and leaves $\pi_i$ for $i<n$ unchanged, by cellular approximation and the exact sequence of the pair; doing this for a set of generators of $\pi_n(X)$ gives a complex $X'$ with $\pi_i(X')=0$ for $1\le i\le n$. For a connected CW complex $Y$ with $\pi_i(Y)=0$ for $1\le i<m$ with $m\ge2$, attaching $(m+1)$-cells along representatives of $\pi_m(Y)$ kills $\pi_m$ and leaves the lower groups unchanged, so iterating over $m=n+1,n+2,\dots$ produces a CW complex $K$ with $\pi_1(K)=G$ and $\pi_i(K)=0$ for $i>1$, that is, a $K(G,1)$.
:::
:::

::: {.pf-step #relative-complex}
$H_i(K,X)=0$ for $i\le n$, and $H_{n+1}(K,X)$ is free on the classes of the $(n+1)$-cells attached.

::: pf-proof
The cells of $K$ not in $X$ have dimension at least $n+1$, so the relative cellular chain complex $C_*(K,X)$ of the CW pair $(K,X)$ vanishes in degrees at most $n$ and is free on the attached $(n+1)$-cells in degree $n+1$. By Theorem 2.35 the cellular homology of the pair is the singular homology, so $H_i(K,X)=0$ for $i\le n$ and $H_{n+1}(K,X)\cong C_{n+1}(K,X)$.
:::
:::

::: {.pf-step #les}
There is an exact sequence $H_{n+1}(K,X)\xrightarrow{\partial}H_n(X)\to H_n(K)\to 0$.

::: pf-proof
The long exact sequence of the pair $(K,X)$ reads $\cdots\to H_{n+1}(K,X)\xrightarrow{\partial}H_n(X)\to H_n(K)\to H_{n-1}(K,X)\to\cdots$, and $H_{n-1}(K,X)=0$ by step [](#relative-complex){.pf-ref}.
:::
:::

::: {.pf-step #image}
$\operatorname{im}\partial=h\bigl(\pi_n(X)\bigr)$, the Hurewicz image of $\pi_n(X)$ in $H_n(X)$.

::: pf-proof
The boundary $\partial$ sends the class of a relative $(n+1)$-cell to the homology class in $X$ of its attaching map, which is the cellular boundary formula of §2.2 read in the relative complex. The attaching maps are exactly the maps $S^n\to X$ used in step [](#construction){.pf-ref} to represent the elements of $\pi_n(X)$, and the class in $H_n(X)$ of a map $S^n\to X$ is by definition its image under the Hurewicz map $h:\pi_n(X)\to H_n(X)$ of Theorem 4.32. Hence the image of $\partial$ is $h(\pi_n(X))$.
:::
:::

::: {.pf-step #conclusion}
$H_n(X)/h\bigl(\pi_n(X)\bigr)\cong H_n\bigl(K(\pi_1(X),1)\bigr)$.

::: pf-proof
By steps [](#les){.pf-ref} and [](#image){.pf-ref}, exactness gives $H_n(K)\cong H_n(X)/h(\pi_n(X))$, and $H_n(K)\cong H_n(K(G,1))$ because $K$ is a $K(G,1)$ and homotopy equivalent spaces have isomorphic homology.
:::
:::

:::
:::
