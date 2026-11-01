---
schema: qual/card@1
id: E-HAT-4.2-6
kind: problem
title: "Relative Hurewicz implies absolute"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 6 (AT.txt 19351-19353) and correct as it stands. The cone
    pair is the right device: pi_i(CX,X) = pi_{i-1}(X) for i>=2 with CX contractible, so X (n-2)-connected
    makes (CX,X) (n-1)-connected; relative Hurewicz then identifies pi_n(CX,X) with H_n(CX,X), which
    H_n(CX,X) = H~_{n-1}(X) computes; and naturality of the Hurewicz map makes the comparison square
    commute, so the bottom map is an isomorphism. Checked the restriction n>=3: it is correct and
    necessary, since the absolute Hurewicz theorem in dimension n-1 is stated for n-1>=2, while dimension 1
    has H_1 = pi_1^ab instead of an isomorphism, which the card does not claim. Not checked: nothing
    outside this exercise.

---

::: {.problem}
Show that the relative form of the Hurewicz theorem in dimension $n$ implies the absolute form in dimension $n-1$ by considering the pair $(CX, X)$ where $CX$ is the cone on $X$.
:::

::: {.solution}
Take $n\ge3$, so the absolute theorem in dimension $n-1$ lies in its stated range. Assume the relative Hurewicz theorem in dimension $n$. Let $X$ be $(n-2)$-connected, as in the absolute Hurewicz theorem in dimension $n-1$, and consider the cone pair $(CX,X)$. Since $CX$ is contractible, the long exact homotopy sequence gives
$$
\pi_i(CX,X)\cong \pi_{i-1}(X)\qquad(i\ge2).
$$
Hence $(CX,X)$ is $(n-1)$-connected. Relative Hurewicz therefore gives an isomorphism
$$
h:\pi_n(CX,X)\xrightarrow{\cong}H_n(CX,X).
$$
The homology long exact sequence of the pair, again using contractibility of $CX$, gives
$$
H_n(CX,X)\cong \widetilde H_{n-1}(X).
$$
Under these two boundary isomorphisms, naturality of the Hurewicz maps makes the square
$$
\begin{array}{ccc}
\pi_n(CX,X)&\xrightarrow{h}&H_n(CX,X)\\
\downarrow\partial&&\downarrow\partial\\
\pi_{n-1}(X)&\xrightarrow{h}&H_{n-1}(X)
\end{array}
$$
commute. The three other arrows are isomorphisms, so the bottom Hurewicz map is an isomorphism. This is exactly the absolute Hurewicz theorem in dimension $n-1$.
:::
