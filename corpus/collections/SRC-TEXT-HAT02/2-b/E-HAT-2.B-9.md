---
schema: qual/card@1
id: E-HAT-2.B-9
kind: problem
title: "Transfer sequence for trivial coverings"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Make the transfer sequence explicit in the case of a trivial covering $\tilde{X} \to X$, where $\tilde{X} = X \times S^0$.
:::

::: {.solution}
Use $\ZZ_2$ coefficients, as in the transfer sequence of §2.B. Since $X\times S^0=X\amalg X$, its singular chain complex is $C_*(X;\ZZ_2)\oplus C_*(X;\ZZ_2)$. In these coordinates the transfer and projection are
$$
\tau(c)=(c,c),\qquad p_\#(a,b)=a+b.
$$
Thus the short exact sequence defining Hatcher's transfer sequence is
$$
0\longrightarrow C_*(X;\ZZ_2)
\xrightarrow{\Delta}
C_*(X;\ZZ_2)^2
\xrightarrow{+}
C_*(X;\ZZ_2)\longrightarrow0.
$$
The diagonal is injective, the sum is surjective, and its kernel is the diagonal because the coefficients have characteristic two. The sequence splits as a sequence of chain complexes: $c\mapsto(c,0)$ is a section of the sum map. Consequently every connecting homomorphism vanishes, and the transfer sequence is the split short exact sequence
$$
0\longrightarrow H_n(X;\ZZ_2)
\xrightarrow{x\mapsto(x,x)}
H_n(X;\ZZ_2)^2
\xrightarrow{(a,b)\mapsto a+b}
H_n(X;\ZZ_2)\longrightarrow0
$$
in each degree $n$.
:::
