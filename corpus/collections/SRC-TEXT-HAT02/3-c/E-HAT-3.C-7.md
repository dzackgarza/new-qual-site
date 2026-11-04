---
schema: qual/card@1
id: E-HAT-3.C-7
kind: problem
title: Primitive elements of $\ZZ_p[x]$
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 7; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof, including the case split. If $p=2$ or $\deg x$ is even the two tensor summands
    of $\Delta x$ commute, and the Frobenius identity makes every $x^{p^r}$ primitive. Conversely
    an exponent $m=p^rq$ with $q>1$ gives the mixed term $x^{(q-1)p^r}\otimes x^{p^r}$ with
    coefficient $q\ne0$ in $\ZZ_p$, and distinct total powers cannot cancel it. For $p$ odd and
    $\deg x$ odd, $y=x^2$ is primitive by the Koszul sign ($\Delta(x^2)=x^2\otimes1+1\otimes x^2$
    because the two cross terms cancel), so the primitives are spanned by $x$ and the
    $y^{p^r}=x^{2p^r}$; the odd part contributes only $x$ since $\Delta(xy^m)$ has the uncancelled
    mixed term $x\otimes y^m$ for $m>0$.
---

::: {.problem}
What are the primitive elements of the Hopf algebra $\ZZ_p[x]$ for $p$ prime?
:::

::: {.solution}
The generator $x$ is primitive: $\Delta x=x\otimes1+1\otimes x$.

If $x$ has even degree, or $p=2$, the two summands commute. The Frobenius identity shows that every $x^{p^r}$ is primitive. Conversely, write a positive exponent as $m=p^r q$ with $p\nmid q$. If $q>1$, then in
$$
\Delta(x^m)=(x^{p^r}\otimes1+1\otimes x^{p^r})^q
$$
the coefficient of $x^{(q-1)p^r}\otimes x^{p^r}$ is $q\ne0$ in $\ZZ_p$. Thus $x^m$ is not primitive. Distinct total powers cannot cancel one another's mixed terms. The primitive elements in this case are exactly the finite $\ZZ_p$-linear combinations of $x,x^p,x^{p^2},\ldots$.

If $p$ is odd and $x$ has odd degree, the graded tensor-product sign makes $y=x^2$ primitive. The even subalgebra $\ZZ_p[y]$ has primitive elements spanned by $y,y^p,y^{p^2},\ldots$ by the same argument. In the odd part, $\Delta(xy^m)=\Delta(x)\Delta(y)^m$ has the mixed term $x\otimes y^m$ for every $m>0$, and no other term of that bidegree cancels it. Thus only $x$ is primitive there. The primitive elements are exactly the finite $\ZZ_p$-linear combinations of $x,x^2,x^{2p},x^{2p^2},\ldots$.
:::
