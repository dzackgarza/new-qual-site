---
schema: qual/card@1
id: E-HAT-4.2-31
kind: problem
title: "Split sequences from nullhomotopic fiber inclusions"
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
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 31, printed p. 392,
    and Theorem 4.41, printed p. 376. The card's own proof was correct in outline but
    terse where it mattered (the suspended map and the identity of the splitting), so the
    proof is now transcribed from Proudfoot, Math 634 Algebraic Topology I, Fall 2015,
    Homework #7, Problem 31, which supplies the explicit extension of a class along the
    nullhomotopy and the check that it splits the sequence. Checked against the book: the
    exact sequence is Theorem 4.41's, the hypothesis makes both maps induced by the
    inclusion vanish, and the boundary isomorphism of the pair identifies the extended
    class with a class in pi_n(B). Corrected while transcribing: a first draft claimed
    the Z summands of pi_7(S^4) and pi_15(S^8) came from pi_6(S^3) and pi_14(S^7), which
    are finite; they come from pi_7(S^7) and pi_15(S^15), and the card now says only
    that, since the exercise needs nothing more. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a fiber bundle $F \to E \to B$ such that the inclusion $F \hookrightarrow E$ is homotopic to a constant map, show that the long exact sequence of homotopy groups breaks up into split short exact sequences giving isomorphisms $\pi_n(B) \approx \pi_n(E) \oplus \pi_{n-1}(F)$.
In particular, for the Hopf bundles $S^3 \to S^7 \to S^4$ and $S^7 \to S^{15} \to S^8$ this yields isomorphisms $\pi_n(S^4) \approx \pi_n(S^7) \oplus \pi_{n-1}(S^3)$ and $\pi_n(S^8) \approx \pi_n(S^{15}) \oplus \pi_{n-1}(S^7)$.
Thus $\pi_7(S^4)$ and $\pi_{15}(S^8)$ contain $\ZZ$ summands.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 31. The proof below is transcribed from Proudfoot, *Math 634: Algebraic Topology I*, Fall 2015, Homework #7, Problem 31, and checked against the book: the exact sequence used is that of Theorem 4.41, and the identification $\pi_n(E,F,x_0)\cong\pi_n(B,b_0)$ is the one that sequence supplies.

Take a basepoint $x_0\in F$ with image $b_0\in B$. The hypothesis says that the inclusion $i:F\to E$ is homotopic to a constant map, so $i_*:\pi_n(F,x_0)\to\pi_n(E,x_0)$ is trivial for every $n>0$. In the long exact sequence of the fibration
$$
\cdots\to\pi_n(F)\xrightarrow{i_*}\pi_n(E)\xrightarrow{p_*}\pi_n(B)\xrightarrow{\partial}\pi_{n-1}(F)\xrightarrow{i_*}\pi_{n-1}(E)\to\cdots
$$
the two maps named $i_*$ therefore vanish, and for $n>1$ the sequence breaks into the short exact sequence
$$
0\to\pi_n(E,x_0)\xrightarrow{p_*}\pi_n(B,b_0)\xrightarrow{\partial}\pi_{n-1}(F,x_0)\to0 .
$$
For $n>1$ the group $\pi_n(B,b_0)$ is abelian, so a right splitting suffices.

Choose a nullhomotopy $H:F\times I\to E$ of the inclusion, that is $H(x,1)=x$ and $H(x,0)=x_0$. Fix $s\in S^n$ as basepoint and let $f:(S^{n-1},s)\to(F,x_0)$ represent $[f]\in\pi_{n-1}(F,x_0)$. Extend $f$ to
$$
\tilde f:D^n\to E,\qquad \tilde f(v)=\begin{cases}H\bigl(f(v/\abs{v}),\abs{v}\bigr),&v\ne0,\\ x_0,&v=0,\end{cases}
$$
which is continuous at $0$ because $H(f(\,\cdot\,),0)=x_0$. On $\partial D^n=S^{n-1}$ it is $H(f(\,\cdot\,),1)=f$, so the class of $\tilde f$ in $\pi_n(E,F,x_0)$ maps to $[f]$ under the boundary isomorphism of the pair, and hence under $\pi_n(E,F,x_0)\cong\pi_n(B,b_0)$ to a class lifting $[f]$. That class is $[p\circ\tilde f]$, where $p\tilde f:D^n\to B$ carries $\partial D^n$ to the point $b_0$; so the assignment $[f]\mapsto[p\tilde f]$ is a right splitting of the sequence above. It is well defined because replacing $f$ by another representative and homotoping changes $\tilde f$ by a homotopy rel $\partial D^n$, and it is a homomorphism because $\tilde f$ is natural in $f$.

The sequence therefore splits, giving $\pi_n(B)\cong\pi_n(E)\oplus\pi_{n-1}(F)$ for $n>1$. For $n=2$ the same computation shows $\pi_1(F)$ is abelian, which the direct sum requires.

In the Hopf bundles $S^3\to S^7\to S^4$ and $S^7\to S^{15}\to S^8$ the inclusion of the fibre is a map from a sphere of lower dimension into a sphere, hence nullhomotopic, so the hypothesis holds and
$$
\pi_n(S^4)\cong\pi_n(S^7)\oplus\pi_{n-1}(S^3),\qquad
\pi_n(S^8)\cong\pi_n(S^{15})\oplus\pi_{n-1}(S^7).
$$
With $n=7$ in the first and $n=15$ in the second,
$$
\pi_7(S^4)\cong\pi_7(S^7)\oplus\pi_6(S^3)\cong\ZZ\oplus\pi_6(S^3),\qquad
\pi_{15}(S^8)\cong\pi_{15}(S^{15})\oplus\pi_{14}(S^7)\cong\ZZ\oplus\pi_{14}(S^7),
$$
the $\ZZ$ summands being $\pi_7(S^7)$ and $\pi_{15}(S^{15})$; that is what the exercise's last sentence records, and no value of $\pi_6(S^3)$ or $\pi_{14}(S^7)$ is needed for it.
:::
