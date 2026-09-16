---
schema: qual/card@1
id: P-3A7RU
kind: problem
title: Punctured unit disk and annulus are not conformally equivalent
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Mappings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Spring 2019 Question 2.4 and the following two exam boundaries with the retained source. Removed the fourteen subsequent appearances only after reading their thirteen independently listed owning cards; preserved all owning IDs and memberships."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the removable extension, exclusion of both annulus boundary circles, and continuity of the inverse at the extended value. Source preservation includes the unrestricted smooth-kernel repair on P-JHUU67RA3."
---

::: {.problem}
Show that the punctured unit disk $\{z:0<|z|<1\}$ and the annulus $\{z:1<|z|<2\}$ cannot be conformally equivalent.
:::

::: {.solution}
Write $D=\{z:|z|<1\}$ and $A=\{w:1<|w|<2\}$.
Suppose there were a biholomorphism $f:D\setminus\{0\}\to A$
with holomorphic inverse $g:A\to D\setminus\{0\}$.

<1>1. The map $f$ extends holomorphically to $D$, with its value at zero in $A$.

::: {.proof}
The bound $|f|<2$ makes the singularity at zero removable
[@SS03]. Denote the extension by $F$. Continuity gives
$1\leq|F(0)|\leq2$. The extension is nonconstant since
its restriction $f$ is bijective onto $A$.

If $|F(0)|=2$, the holomorphic function $F$ attains
its maximum modulus at an interior point, so it is
constant by the maximum modulus principle, a contradiction.
If $|F(0)|=1$, then $F$ is nonzero on $D$, and
$1/F$ is holomorphic with modulus at most one and with
modulus one at zero. The same principle makes $1/F$,
and hence $F$, constant, again a contradiction [@SS03].
Thus $1<|F(0)|<2$, so $F(0)\in A$.
:::

<1>2. The inverse map gives a contradiction at the added point.

::: {.proof}
For every $z\in D\setminus\{0\}$, one has
$g(F(z))=g(f(z))=z$. Since $F(0)\in A$, the map
$g$ is continuous at $F(0)$. Letting $z\to0$ therefore gives
$$
g(F(0))=0.
$$
But $g$ takes all its values in $D\setminus\{0\}$.
This contradiction rules out the biholomorphism.
:::
:::
