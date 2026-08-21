---
schema: qual/card@1
id: E-HAT-3.F-7
kind: exercise
title: "Moore spaces as quotients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
solved: false
---

Show that for a short exact sequence of abelian groups $0 \to A \to B \to C \to 0$, a Moore space $M(C, n)$ can be realized as a quotient $M(B, n)/M(A, n)$.
Applying the long exact sequence of cohomology for the pair $(M(B,n), M(A,n))$ with any coefficient group $G$, deduce an exact sequence

$$0 \to \operatorname{Hom}(C,G) \to \operatorname{Hom}(B,G) \to \operatorname{Hom}(A,G) \to \operatorname{Ext}(C,G) \to \operatorname{Ext}(B,G) \to \operatorname{Ext}(A,G) \to 0.$$
