---
schema: qual/card@1
id: E-HAT-3.F-7
kind: problem
title: "Moore spaces as quotients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that for a short exact sequence of abelian groups $0 \to A \to B \to C \to 0$, a Moore space $M(C, n)$ can be realized as a quotient $M(B, n)/M(A, n)$.
Applying the long exact sequence of cohomology for the pair $(M(B,n), M(A,n))$ with any coefficient group $G$, deduce an exact sequence

$$0 \to \operatorname{Hom}(C,G) \to \operatorname{Hom}(B,G) \to \operatorname{Hom}(A,G) \to \operatorname{Ext}(C,G) \to \operatorname{Ext}(B,G) \to \operatorname{Ext}(A,G) \to 0.$$

::: {.solution}
Choose Moore spaces functorially enough for the given short exact sequence
\[
0\to A\xrightarrow{i}B\xrightarrow{q}C\to0.
\]
For $n\ge1$, realize $i$ by a cellular map
\[
M(A,n)\longrightarrow M(B,n)
\]
inducing $i$ on the only nonzero reduced homology group. Replace it by a mapping-cylinder inclusion, so we may regard $M(A,n)$ as a subcomplex of $M(B,n)$. Let
\[
Q=M(B,n)/M(A,n).
\]
The reduced homology long exact sequence of the pair gives
\[
\widetilde H_j(Q)=0\quad(j\ne n),
\qquad
\widetilde H_n(Q)\cong B/A\cong C.
\]
Thus $Q$ is a Moore space $M(C,n)$ (up to the standard Moore-space homotopy uniqueness in this range), so
\[
M(C,n)\simeq M(B,n)/M(A,n).
\]

Apply cohomology with coefficients $G$ to the pair $(M(B,n),M(A,n))$. By the universal coefficient theorem for Moore spaces,
\[
\widetilde H^n(M(D,n);G)\cong\operatorname{Hom}(D,G),
\]
\[
\widetilde H^{n+1}(M(D,n);G)\cong\operatorname{Ext}(D,G),
\]
and all other reduced cohomology groups vanish. The long exact sequence of the pair, together with
\[
H^*(M(B,n),M(A,n);G)\cong\widetilde H^*(M(C,n);G),
\]
therefore becomes exactly
\[
0\to\operatorname{Hom}(C,G)	o\operatorname{Hom}(B,G)	o
\operatorname{Hom}(A,G)	o\operatorname{Ext}(C,G)	o
\operatorname{Ext}(B,G)	o\operatorname{Ext}(A,G)	o0.
\]
:::
